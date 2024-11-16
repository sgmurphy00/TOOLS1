import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from sklearn.model_selection import train_test_split
from datetime import datetime
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPool2D, Flatten
from tensorflow.keras.layers import Dense, Dropout, BatchNormalization

def train_and_test(id, model, x_train, y_train, x_test, y_test, epochs=10): 
    global best_model, best_accuracy

    start_time = datetime.now()
    model.fit(x_train, y_train, epochs=epochs)

    end_time = datetime.now()
    duration = (end_time - start_time).total_seconds()

    print("Training took %.1f seconds" % duration)
    
    print(f"Model eval:")
    accuracy = model.evaluate(x_test, y_test)

    #benchmark[id] = (accuracy[1], accuracy[0], duration)

    #if accuracy[1] > best_accuracy:
    #    best_model = model
    #    best_accuracy = accuracy[1]

    return accuracy

def create_modelv1(class_count, print_summary=False):

    model = Sequential([
        Conv2D(32, (4,4), activation='relu', input_shape=(28,28,4)),
        MaxPool2D((3,3)),
        Flatten(),
        Dense(class_count, activation='softmax'),
    ])

    model.compile('adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    if print_summary:
        model.summary()

    return model

def fgsm_attack(model, images, labels, epsilon):
    # Enable gradient tape for automatic differentiation
    with tf.GradientTape() as tape:
        # Cast images to float32 if they are not already
        images = tf.convert_to_tensor(images, dtype=tf.float32)
        # Make the model predictions
        tape.watch(images)
        predictions = model(images, training=True)
        # print(predictions)
        # Calculate the loss
        loss = tf.keras.losses.sparse_categorical_crossentropy(labels, predictions)
        loss = tf.reduce_mean(loss)
        print(loss)

    # Calculate gradients of the loss with respect to the input image
    gradients = tape.gradient(loss, images)

    if gradients is None:
        raise ValueError('NO GRAD')
    # print(gradients)
    # Get the sign of the gradients
    signed_gradients = tf.sign(gradients)
    # Create the adversarial images
    adversarial_images = images + epsilon * signed_gradients
    # Clip the values to maintain valid pixel range
    # adversarial_images = tf.clip_by_value(adversarial_images, 0, 1)  # Adjust based on normalization

    return adversarial_images