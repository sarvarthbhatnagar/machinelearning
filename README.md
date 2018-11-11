# machinelearning
Contains packages for various machine learning concepts

Regression Dummy Variables -
> Multicollinearity - when there are more than 1 collinear variables then ignore 1 of them.
> OneHotEncoder - this is different frrom label encoder. Latter gives numerical denotion to a label like ocmpany name for putting them in a model.
  Onehotencoder on the other hand splits 1 column into multiple and assigns 0100 so that no encoding changes weight of variables
  
  
  
Goto learning docs
Theory -
STATS : https://onlinecourses.science.psu.edu/stat501/node/344/

Standard Deviation : Circle area theory 

Building a model
---------------------
A. Backward elimination
1. select the significance level
2. select all predicates
3. if p > sl, remove predicate and repeat, else finish
    
B. 