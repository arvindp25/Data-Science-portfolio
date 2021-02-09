
<centre><h2>Action Recoginiton System</centre></h2>
In this project we have to build a model which can classify five human action gestures. <br>
Let’s understand different actions <br>
Thumbs up: Increase the volume <br>
Thumbs down: Decrease the volume <br>
Left swipe: 'Jump' backwards 10 seconds <br>
Right swipe: 'Jump' forward 10 seconds <br>
Stop: Pause the movie<br>
Data<br>
2 csv and 2 folder of data is provided,<br>
Val csv<br>
Train csv<br>
Train folder <br>
Val folder <br>
Inside the train folder we have 663 folders each folder contains 30 sequential images. <br>
Inside the val folder we have 100 folders, each folder contains 30 sequential images.<br>
Train csv and val csv contain name of folders without action<br>

<h5>Approach and Steps</h5>
This problem can be solved by <h7>conv3d or,CNN+LSTM,CNN+GRU,tf+LSTM,tf+GRU</h7>.
We have tried different model architecture and moved accordingly, In final model we are
able to achieve <b>90 in training and 82</b> in validation, in 35 epochs.
We have tried a different number of frames,i.e 15,18,20,24,30.Higher number leads t
<b>OOM error </b>
We have tried different number of batch,i.e 663,256,128,64,32
For above 32 batch , We got an OOM error. Then we decided to stick under 32. <br>
Image size chosen 120x120 and 96x96
96x96 is chosen because in transfer learning we used MobileNetV2 and generally, any
state of art model performs well when we feed images of size on which they are trained
on. <br>
For other models we have chosen 120x120 or160x160, we got 2 sizes of images
360x360 and 120x160, hence we decided to go with either 120x120 or 160x160,.
 <br>
In the training dataset we cropped and then resized it to 120x120 or 160x160. If transfer
learning is used then according to the model on which it was trained. <br>
For the val dataset we resize all images to 120x120,160x160 and according to the
transfer learning model. <br>
For normalisation,
We tried 2 type of normalization
Mean normalisation and dividing by 255. We didn’t see much difference in base model
performance. So we chose dividing by 255. To keep simple. <br>
Optimizer we have chosen Adam. <br>
Total of 3 of callbacks are used <br>
Model checkpoint <br>
ReduceLROnPlateau with patience 3 and monitor val loss <br>
EarlyStopping with patience 8 and monitor val loss. <br>

Then we tried all sort of architecture CNN+LSTM,CNN+GRU,conv3d,TF+LSTM,TF+GRU. <br>
Note:- In notebook we kept only final model architecture  <br>
For more detail u can check write.pdf, you will find all sort experiment done by us. <br>

this project is done by 
Arvind kumar patel and Subhasis Pattanayak
