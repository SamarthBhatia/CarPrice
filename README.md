# CarPrice

The data required for the project was imported from Kaggle. The data had some issues-

Selling Price had Lakh*.
Selling Price was of type object.
Seller type was not required as all were first owner in the list.
Full name had to be reduced to 3 words.
Km driven had commas and kms and were of type object.
Milegae had kmpl/kmph/kmkg and was of type object.
Seats was not required.
Engine had cc and was of type object.
All the data in CarDekho.updated was cleaned and saved in another csv file CleanedCar.csv

The data was then split in train and test parts in 4:1 ratio. OneHotEncoder and Linear Regression were used to train the model.

The best r2_score was found by iterating on each element and calculating r2_score after using linear regression to train.
