# CNN-species-identification
Capstone project for the Metis Data Science Bootcamp: Species Identification with Convolutional Neural Networks

## Objective:

To build a model with sufficient accuracy to automate processing trail camera images with the capability to push notifications when a target animal is identified.


## What are Trail Cameras?

Trail cameras, also known as game cameras, automatically take photos when motion is detected. They have a variety of applications and 
their popularity has driven the market size to $60B worldwide - a number expected to double over the next decade.

While these cameras are automatic, they are not yet intelligent. When the SD card is retrieved, the user is typically met with 1,000s of photographs. These images are often low quality or redundant, creating a labor intensive process to locate animals of interest.

## Machine Learning Workstation:

For training imagery, I used Microsoft Cognitive Services’ Bing Images API to download over 5000 photos to AWS S3. AWS Recognition was used to verify image labels, which correctly eliminated about 20% repository. All processing was done with an EC2 m8.large GPU on Ubuntu, also supporting Jupiter Labs running my model, which built on Keras with a Tensor Flow backend. All visuals were produced with Tableau.

![alt text](https://github.com/rwmyers46/CNN-species-identification/blob/master/images/dl-workstation.jpg "Logo Title Text 1")
