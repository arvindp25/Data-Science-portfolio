Problem statement
A bike-sharing system is a service in which bikes are made available for shared use to individuals on a short term basis for a price or free.
Many bike share systems allow people to borrow a bike from a "dock" which is usually computer-controlled wherein the user enters the payment 
information, and the system unlocks it. This bike can then be returned to another dock belonging to the same system.
A US bike-sharing provider BoomBikes has recently suffered considerable dips in their revenues due to the ongoing Corona pandemic. 
The company is finding it very difficult to sustain in the current market scenario. So, it has decided to come up with a mindful business
plan to be able to accelerate its revenue as soon as the ongoing lockdown comes to an end, and the economy restores to a healthy state. 

In such an attempt, BoomBikes aspires to understand the demand for shared bikes among the people after this ongoing quarantine situation ends across the nation due to Covid-19. They have planned this to prepare themselves to cater to the people's needs once the situation gets better all around and stand out from other service providers and make huge profits.
<hr>

Steps follwed:-
<h6>data preparation with the help of numpy and pandas </h6> <br>

     checking For null value.
     Changing dtype of categorical columns from numerical to object.
     Dropping unrelavant columns.
     Mapping categorical column
     
<h7>Exploratory data analysis with the help of matplotlib ans seaborn </h7> <br>
 
     Some insight:-
     i.When weather is clear, demand for bike is high
     ii.holiday demand of bike is low
     iii. Demand of bike is high in second quarter and third quarter i.e april-september
  
<h7> model building with the help statsmodel.api so we can have detail of model</h7> <br>

     Algorithm used Linear Regression.
     R2 Score on test data:82
     R2 Score on train data:81
     
Model validation and making sure none of assumption is contradicted <br>

     We used Vif and p-value to make sure coefficient and constant can be accepted.
     sum of residual is equal to 0
     error is normally distributed
<h7>Conclusion for company.</h7> <br>
