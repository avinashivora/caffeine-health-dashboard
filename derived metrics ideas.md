ID,Age,Gender,Country,Coffee_Intake,Caffeine_mg,Sleep_Hours,Sleep_Quality,BMI,Heart_Rate,Stress_Level,Physical_Activity_Hours,Health_Issues,Occupation,Smoking,Alcohol_Consumption
1,40,Male,Germany,3.5,328.1,7.5,Good,24.9,78,Low,14.5,None,Other,0,0
2,33,Male,Germany,1.0,94.1,6.2,Good,20.0,67,Low,11.0,None,Service,0,0
3,42,Male,Brazil,5.3,503.7,5.9,Fair,22.7,59,Medium,11.2,Mild,Office,0,0
4,53,Male,Germany,2.6,249.2,7.3,Good,24.7,71,Low,6.6,Mild,Other,0,0

# Data
This dataset captures health and lifestyle factors potentially linked to coffee consumption and sleep quality across individuals.
The data has the following features:
- *ID*: Unique identifier (integer).
- *Age*: Age in years (integer).
- *Gender*: Sex category (string: "Male", "Female", "Other").
- *Country*: Residence country (string, e.g., "Germany", "Spain").
- *Coffee_Intake*: Daily coffee cups (float).
- *Coffee_Caffeine_mg*: Caffeine from coffee (mg, float).
- *Sleep_Hours*: Nightly sleep duration (hours, float).
- *Sleep_Quality*: Rating (string: "Poor", "Fair", "Good", "Excellent").
- *BMI*: Body Mass Index (float).
- *Heart_Rate*: Resting BPM (integer).
- *Stress_Level*: Level (string: "Low", "Medium", "High").
- *Physical_Activity_Hours*: Weekly activity (hours, float).
- *Health_Issues*: Severity (string: None, "Mild", "Moderate", "Severe").
- *Occupation*: Category (string: "Healthcare", "Service", "Office", "Student", "Other").
- *Smoking*: Status (integer: 0=non-smoker, 1=smoker).
- *Alcohol_Consumption*: Status (integer: 0=non-consumer, 1=consumer).
- *Screen_Time_Hours*: Daily screen time (hours, float).
- *Work_Hours_Per_Week*: Weekly work hours (integer).
- *Tea_Intake*: Daily tea cups (float).
- *Tea_Caffeine_mg*: Caffeine from tea (mg, float).
- *EnergyDrink_Intake*: Daily energy drinks (float).
- *Energy_Caffeine_mg*: Caffeine from energy drinks (mg, float).
- *Sugar_mg*: Daily sugar intake (mg, float).
- *Mood*: Category (string: "Positive", "Neutral", "Negative").
- *Hydration_Quantity*: Daily water liters (float).

1. `Focus_Adjusted = [Focus_Level] + ([Mood]="Positive")*1 - ([Stress_Level]="High")*1`
2. `Focus_to_ScreenRatio = [Focus_Level]/[Screen_Time_Hours]`
3. `Caffeine_to_SleepIndex = [Total_Caffeine]/SWITCH([Sleep_Quality],"Poor",4,"Fair",6,"Good",8,"Excellent",9,6)`
