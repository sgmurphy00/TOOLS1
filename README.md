# TOOLS1
Final Project for Data Science Tools 1; University of Denver

## Problem Space
Image classification as a modeling technique has seen an explosion in both application
and sophistication in recent years. Increasingly accurate, lightweight, and fast-performing
image classifiers are used in traffic monitoring, remote sensing, commercial spaces,
threat detection, driving automation, and more. As we become increasingly familiar and integrated
with these technologies, we must be aware of the ability of threat actors to taint results using 
'adversarial', or intentionally obscured, data.

Popular image classification models like convolutional neural networks (CNNs) function by 
understanding patterns within image arrays which can be correlated to output class prediction.
Adversarial actors, or individuals/groups intending to degrade general model performance, or affect
classification frequency of specific classes, often utilize adversarial input images. These 'poisoned' input images
are often indistinguishable from 'clean' input images to the human eye, but have been perturbed in 
some way in order to be intentionally misclassified by the model.

One popular method of data poisoning for image classifiers is called the Fast Gradient Sign Method, 
or FGSM. FGSM calculates the gradient of the loss function, and 'adjusts' the input image 
such that the loss function is maximized by applying a mathematical filter to the input array.
The result is an input image that may look perfectly normal to the human eye, but makes
a classification model perform with much less accuracy than a typical input image.

This capstone project to COMP 4447 aims to demonstrate the effect of this poisoned data- first by building a simple, yet
>90% accurate convolutional neural network to classify DEEPSAT6 terrain imagery, then generating adversarial inputs
using FGSM, demonstrating the effect of adversarial inputs on model performance, and exploring statistical differences
between the adversarial and clean samples.

## Data Requirements
As this project has been carried out primarily on personal computers, input data must be both:
A) sufficiently coarse for acceptable processing times, and
B) sufficiently ample to build a robust classifier.
Due to a collective interest and background in remote sensing, we selected the DEEPSAT-6 satellite imagery dataset.
This dataset includes ~400,000 image arrays and labels of dimension (28,28,4). Data fall into one of six terrain 
categories: Barren land, road, construction, treecover, grassland, and water. Data takes roughly 6gB storage altogether.

## Analysis or Modeling?
This project investigates a problem involving both analysis and modeling - leveraging model outputs to generate adversarial arrays, determining optimal epsilon values by observing model performance at different perturbation levels, and using summary statistics to understand differences in adversarial vs clean image samples. From a defensive standpoint, model owners mustbe prepared either to detect and reject adversarial inputs, or to build robust models which can thwart potential attacks, often by integrating generated adversarial data into the training loop.

## Key Insights
Initial analysis of adversarial samples (~35% of total dataset size) with an epsilon value of 1 degraded model performance from ~98% accuracy to ~<ACCURACY DEGRAD>, while arrays of adversarial images vs clean images were not significantly different via t-test, anova, and held very similar summary statistics (array means, standard deviation). Future efforts should broaden statistical methods used to detect differences in adversarial vs clean array populations. FGSM is a fairly simple, yet still powerful attack method. As in many "red-team, blue-team" problems, a developmental loop exists wherein threat actors develop effective attack methods, and model owners develop models which are more robust to those attack methods. When threat actors develop new methods, model owners must meet those threats by continuing to expose models to nefarious data during training. In this way, model owners are often on the 'back foot', i.e. responding to novel threats as opposed to predicting and subverting future ones. It is clear that traditional statistical methods may struggle to detect adversarial FGSM-generated arrays, but a more standard statistical marker to flag adversarial data may prove an effective exit condition to the aforementioned loop.

## Stack

Models were designed, trained and tested using TensorFlow 2.18.0, on both local machine (Intel i7 8700k, RTX 3060) and within a Google Colab environment. Data ingestion, preprocessing, FGSM method, and visualizations are custom code using pandas, numpy, matplotlib and seaborn. Standard TensorFlow memory overflow issues occurred - solved by decreasing the FGSM load from 100% of the initial dataset size to 35%, as increasing resource allotment was not viable.

## Model Design
\\simple cnn, break initial_dataexploration.ipynb into assoc. .py or .ipynb for specified functionality
    \\data prep, model training, fgsm generation, visualization notebooks, helper functions`

# Contributors
@sgmurphy00
@psacuh
