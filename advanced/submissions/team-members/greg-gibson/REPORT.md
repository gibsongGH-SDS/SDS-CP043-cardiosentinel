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
A:  

Q: Apply ordinal encoding to lifestyle variables with ranked categories (e.g., Diet quality or PhysicalActivity frequency). What order did you assign, and why?  
A:  

Q: For remaining nominal categorical features, apply one-hot encoding. Why is one-hot encoding preferable for non-ordinal categories?  
A:  

✨ 2. Feature Creation  
Q: Create a new feature `BMI_Category` (Underweight, Normal, Overweight, Obese) based on BMI ranges. Display its value counts.  
A:  

Q: Create a `Risk_Index` feature using the formula `(Cholesterol + BloodPressure) / ExerciseHours`. Explain the rationale behind this derived metric.  
A:  

Q: Did either of the engineered features show a visible relationship with heart-attack risk?  
A:  

✂️ 3. Data Splitting  
Q: Split your dataset into training and testing sets (80/20 recommended). Use stratification on the Heart_Attack_Risk target.  
A:  

Q: Why must the dataset be split before applying SMOTE or scaling techniques?  
A:  

Q: Show the shape of your X_train, X_test, y_train, and y_test arrays to confirm the split.  
A:  

⚖️ 4. Imbalance Handling & Final Preprocessing  
Q: Apply the SMOTE technique (or class weighting) on the training set to handle imbalance. Show the class distribution before and after resampling.  
A:  

Q: Normalize numerical features using StandardScaler (fit on training data only). Why must you not fit the scaler on the test set?  
A:  

Q: Display the final shape of your preprocessed training (X_train_processed) and testing (X_test_processed) feature matrices.  
A:  
