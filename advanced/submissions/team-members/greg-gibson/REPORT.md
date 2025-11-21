🩺 CardioSentinel – Advanced Track

✅ Week 1: Exploratory Data Analysis (EDA)

📦 1. Data Integrity & Structure  
Q: Are there any missing, duplicate, or inconsistent entries in the dataset?  
A:  None that I found.

Q: Are all feature data types appropriate (e.g., numeric, categorical)?  
A:  Yes, but I will separate the blood pressure text into two numerical columns.

Q: Did you detect any irrelevant, constant, or low-variance features that might be removed?  
A: No constant or low-variance features - but none of the numerical features correlate with the target and will be kept for domain knowledge. 

🎯 2. Target Variable Assessment  
Q: What is the distribution of the Heart_Attack_Risk target variable (0 = Not at Risk, 1 = At Risk)?  
A:  64% are not at risk, 36% at risk.

Q: Is there a class imbalance between the two target classes? If so, how severe is it?  
A:  70/30 or better is a minor imbalance, though an FFNN is sensitive to it, I may use class weighting.

Q: How might this imbalance affect your model choice or evaluation metrics later on?  
A:  If Recall, Precision and AUC remain similar for both classes, and validation keeps the same ratio, then I could skip balancing.

📊 3. Feature Distribution & Quality  
Q: Which numerical features (e.g., Age, Cholesterol, BloodPressure, HeartRate) are skewed or contain outliers?  
A:  Checks for skewness and outliers confirmed the data is very clean already.

Q: Did any features contain unrealistic or problematic values that may require capping or removal?  
A: Not capping, but I did remove Patient ID as well as Blood Pressure after splitting it between Systolic and Diastolic.

Q: What transformation or normalization techniques might improve these distributions?  
A: Standard Scalar should suffice, as the original author of the data did extensive preparation. 

📈 4. Feature Relationships & Patterns  
Q: Which categorical features (e.g., Smoking, AlcoholConsumption, Diet, PhysicalActivity) show patterns in relation to heart-attack risk?  
A:  There is very little.  Countries can have some order.  The extremes of PhysicalActivity are slightly higher risk, and lots of sleep is slightly lower risk.  90% of all records are smokers and not indicative.

Q: Are there any strong pairwise relationships or multicollinearity among clinical variables (e.g., Cholesterol, BloodPressure, BMI)?  
A: There are no pairwise relationships, but I have strong VIF scores for blood pressure components and BMI, followed by Heart Rate and Cholesterol.

Q: What trends or correlations stood out most clearly during your EDA?  
A: That there are no obvious trends! You would assume the bad habits would pop, but not per this dataset.

🧰 5. EDA Summary & Preprocessing Plan  
Q: What are your 3–5 key insights from the EDA about heart-attack risk factors?  
A: No one feature is a clear driver.  It must be a subtle combination of factors that the machine must find.  You can rank heart attack risk by country, indicating cultural or genetic influence.

Q: Which features will you scale, encode, or exclude during preprocessing?  
A:  Patient ID and Blood Pressure are out, nine features are already binary and I would scale the remaining numericals.
    Male/Female to binary, and the blood pressure components could be categorized by medical definitions of normal to severe ranges then ordinally encoded.
    Diet can also be ordinally encoded, but location columns will have to be target encoded as they have no order of rank.


✅ Week 2: Feature Engineering & Preprocessing  

🏷️ 1. Feature Encoding  
Q: Identify binary categorical features (e.g., Smoking, AlcoholConsumption) and apply simple encoding. Which features did you encode?  
A: Diabetes, Family History, Smoking, Obesity, Alcohol Consumption, Previous Heart Problems, Medication Use, Sex and Hemisphere.  Most are already in 0/1 format, except Sex which I encoded and Hemisphere which I dropped as redundant to Country.

Q: Apply ordinal encoding to lifestyle variables with ranked categories (e.g., Diet quality or PhysicalActivity frequency). What order did you assign, and why?  
A: I did not ordinally encode any variables.  Stress Level, Physical Activity, and Sleep Hours are already ordinal, and Diet was one hot encoded as I do not know whether it is a linear progression.

Q: For remaining nominal categorical features, apply one-hot encoding. Why is one-hot encoding preferable for non-ordinal categories?  
A: I applied OHE to Diet and Country, as their are limited choices and you cannot calculate "how much better".  I dropped Continent and Hemisphere as over-representative.

✨ 2. Feature Creation  
Q: Create a new feature `BMI_Category` (Underweight, Normal, Overweight, Obese) based on BMI ranges. Display its value counts.  
A:              count  percent
BMI_Category                
Obese          3881    44.29
Normal         2619    29.89
Overweight     2059    23.50
Underweight     204     2.33  

Q: Create a `Risk_Index` feature using the formula `(Cholesterol + BloodPressure) / ExerciseHours`. Explain the rationale behind this derived metric.  
A: This combines health, strain and lifestyle, and can compare high cholesterol and blood pressure in a healthy person who offsets the risk with plenty of exercise vs someone who does not. 

Q: Did either of the engineered features show a visible relationship with heart-attack risk?  
A: Not clearly.  Risk_Index for 0 or 1 indicators of heart attack risk were very similar, and while Underweight BMI showed lowest risk, Normal BMI, surprisingly, was higher than Obese or Overweight.

✂️ 3. Data Splitting  
Q: Split your dataset into training and testing sets (80/20 recommended). Use stratification on the Heart_Attack_Risk target.  
A: (Turning into a question) Stratification is used to ensure the target column is represented in the same proportions when randomly separated into training and test.

Q: Why must the dataset be split before applying SMOTE or scaling techniques?  
A: To prevent data leakage - you must scale or SMOTE (create synthetic records) using only on the training dataset, so that the test data is truly unseen to evaluate model performance. 

Q: Show the shape of your X_train, X_test, y_train, and y_test arrays to confirm the split.  
A:  X_train.shape, X_test.shape, y_train.shape, y_test.shape, y_train.mean(), y_test.mean()
((7010, 63),
 (1753, 63),
 (7010,),
 (1753,),
 np.float64(0.358),
 np.float64(0.358))

⚖️ 4. Imbalance Handling & Final Preprocessing  
Q: Apply the SMOTE technique (or class weighting) on the training set to handle imbalance. Show the class distribution before and after resampling.  
A: Class distribution BEFORE weighting:
Training set:
Heart Attack Risk
0    0.642
1    0.358

Test set:
Heart Attack Risk
0    0.642
1    0.358

Computed class weights (used during training):
{np.int64(0): np.float64(0.7790620137808402), np.int64(1): np.float64(1.395858223815213)}

Q: Normalize numerical features using StandardScaler (fit on training data only). Why must you not fit the scaler on the test set?  
A: To avoid data leakage and keep the test set truly unseen, the test set cannot impact how data is scaled.

Q: Display the final shape of your preprocessed training (X_train_processed) and testing (X_test_processed) feature matrices.  
A: Class weighting does not rebalance the dataset, it rebalances the loss function during training.
