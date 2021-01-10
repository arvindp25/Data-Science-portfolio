Steps Followed:-
Data Loading and Data understanding
preprocessing 
Data augmentation
Model build
prediction on test data
analysing model in wrong classified image


1. We manually build CNN architecture with 2 convolutional 1 maxpooling layer , 3 fully connected layers and to stop model to overfit we have used Batchnormalization and dropout of .50 . <br> 
2.We got 86% accuracy in test data.<br>
3.In analysing wrong classified image what we have found that mostly model failed in classifing gender of child. <br>
5. Data used in this is focussed in only faces and grayscale in realworld we have images with background, hence if our model is used to classify them chances of classifying wrong is high. <br>

4.What we can do, for more accuracy we can use transfer learning with some state of art model like vgg16,googlenet resnet. <br>