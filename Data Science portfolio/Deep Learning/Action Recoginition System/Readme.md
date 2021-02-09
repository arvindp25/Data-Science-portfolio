
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

<b>Approach and Steps</b>
This problem can be solved by conv3d or,CNN+LSTM,CNN+GRU,tf+LSTM,tf+GRU.
We have tried different model architecture and moved accordingly, In final model we are
able to achieve 90 in training and 82 in validation, in 35 epochs.
We have tried a different number of frames,i.e 15,18,20,24,30.Higher number leads t
OOM error
We have tried different number of batch,i.e 663,256,128,64,32
For above 32 batch , We got an OOM error. Then we decided to stick under 32.
Image size chosen 120x120 and 96x96
96x96 is chosen because in transfer learning we used MobileNetV2 and generally, any
state of art model performs well when we feed images of size on which they are trained
on.
For other models we have chosen 120x120 or160x160, we got 2 sizes of images
360x360 and 120x160, hence we decided to go with either 120x120 or 160x160,.
 
