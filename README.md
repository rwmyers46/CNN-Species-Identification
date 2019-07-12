# CNN-Species-Identification
Capstone project for the Metis Data Science Bootcamp: Species Identification with Convolutional Neural Networks

## Objective:

To build a model with sufficient accuracy to automate processing trail camera images with the capability to push notifications when a target animal is identified.

## What are Trail Cameras?

Trail cameras, also known as game cameras, automatically take photos when motion is detected. They have a variety of applications and 
their popularity has driven the market size to $60B worldwide - a number expected to double over the next decade. 

<p align="center">
<img src="https://github.com/rwmyers46/CNN-species-identification/blob/master/images/game_cams.jpeg" width="325" height="400"/>
</p>

While these cameras are automatic, they are not yet intelligent. When the SD card is retrieved, the user is typically met with 1,000s of photographs. These images are often low quality or redundant, creating a labor intensive process to locate animals of interest.

## Machine Learning Workstation:

Microsoft Cognitive Services’ Bing Images API to download over 5000 training images to AWS S3. AWS Recognition was used to verify image labels (details available on blog), which correctly eliminated about 20% repository. All processing was done with an EC2 m8.large GPU on Ubuntu, also supporting Jupiter Labs running my model, which built on Keras with a Tensor Flow backend. All visuals were produced with Tableau.

![alt text](https://github.com/rwmyers46/CNN-species-identification/blob/master/images/dl-workstation.jpg)

## Model:

After iterating through some Sequential variants, I settled on a CNN model with VGG-16 and ImageNet as a base. I applied transfer learning by adding 2 dense layers and used 7 degrees of augmentation to compensate for a relatively small dataset to achieve an accuracy of 81%.

## Case Study: "Animalytics"

I applied this model to 8,000 images taken from my personal game cameras taken over all of 3 months - you see the problem? Combining the model's species identification with an image's EXIF data (the information embedded when a photograph is taken) yields time series analytics by species type, which I refer to as "animalytics."

Below is the distribution by hour of day of when deer identified in photos came to a feeder.

![alt text](https://github.com/rwmyers46/CNN-species-identification/blob/master/images/exp-hour.png)

Overlaying historic weather data reveals an inverse relationship between rain and feeding patterns. This could possibly be due to lack of grass in the dryer summer months or a hydrophobic ranch hand letting the feeder go empty.

![alt text](https://github.com/rwmyers46/CNN-species-identification/blob/master/images/rain-exp2.png)

Conventional wisdom says animals are more active during full moons; this dataset tells a different story. Activity was highest during the waning gibbous phase.

![alt text](https://github.com/rwmyers46/CNN-species-identification/blob/master/images/lunar2.png)
