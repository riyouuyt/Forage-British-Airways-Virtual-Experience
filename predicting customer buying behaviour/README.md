# Predictive Customer Booking Project 📈🤖

## **Introduction to the Project** 🚀

The goal of this project is to predict customer bookings by leveraging historical data encompassing 50,000 passenger rows across 14 columns. We aim to use this dataset to create a machine learning model that can foresee future bookings. This model will be invaluable in understanding passenger behaviors, preferences, and potential trends in booking patterns.

## **Objectives and Goals**
- Develop a predictive model to forecast future customer bookings based on historical data.
- Uncover patterns, behaviors, and preferences of passengers to aid in strategic decision-making.
- Utilize various machine learning algorithms to determine the most effective model for prediction.

## **Libraries Utilized** 📚
- Pandas
``` python 
pip install pandas
```
- NumPy
``` python 
pip install numpy
``` 
- Matplotlib
``` python 
pip install matplotlib
``` 
- Seaborn
``` python 
pip install seaborn
``` 
- Scikit-learn
``` python 
pip install sklearn
```
## Dataset Information
The dataset utilized for predicting customer buying behavior is accessible via this [link](https://github.com/riyouuyt/Forage-British-Airways-Virtual-Experience/tree/master/predicting%20customer%20buying%20behaviour/Dataset). It encompasses various features encompassing booking details such as the number of passengers, sales channel, trip type, purchase lead time, length of stay, flight details, booking origin, and more. 

The dataset is structured with 50,000 rows and 14 columns, housing information that provides insights into customer behavior and preferences related to flight bookings. This dataset serves as the foundation for predictive modeling to anticipate and understand customer buying behavior.


## **Data Preparation/Understanding** 📊
The dataset consists of 14 columns covering passenger-related information, such as:

1. `num_passengers`: Represents the number of passengers associated with a booking.
2. `sales_channel`: Indicates the channel through which the sales occurred—internet or mobile platforms.
3. `trip_type`: Describes the type of trip—RoundTrip, CircleTrip, or OneWay.
4. `purchase_lead`: Time duration between purchase and travel date.
5. `length_of_stay`: Duration of stay associated with the booking.
6. `flight_hour`: Hour of the flight departure.
7. `flight_day`: Day of the week for the flight departure.
8. `route`: Flight itinerary or sequence of destinations.
9. `booking_origin`: Location or country from where the booking originated.
10. `wants_extra_baggage`: Indicates if a passenger wants extra baggage (1 for yes, 0 for no).
11. `wants_preferred_seat`: Specifies if a passenger prefers a particular seat (1 for yes, 0 for no).
12. `wants_in_flight_meals`: Indicates if a passenger desires in-flight meals (1 for yes, 0 for no).
13. `flight_duration`: Duration of the flight.
14. `booking_complete`: Denotes booking completion status (1 for complete, 0 for incomplete).

## Exploratory Data Analysis (EDA) 📊

The EDA focuses on comprehensively examining the dataset to gain insights into its structure, relationships, and underlying patterns. It involves both numerical and categorical analysis, enabling a better understanding of the dataset's characteristics.

### Numeric Columns Analysis 🧮

![image](https://github.com/riyouuyt/Forage-British-Airways-Virtual-Experience/assets/122600889/022d8644-69de-4978-9289-b4395280b024)


The skewness measurement reveals the distribution of numerical features:
1. `purchase_lead`: Highly skewed with a skewness value of 1.65, indicating a significant skew.
2. `length_of_stay`: Highly skewed with a skewness value of 5.27, suggesting a substantial skewness in this feature.
3. `flight_hour`: Moderately skewed with a skewness value of 0.40, indicating a moderate skew.
4. `flight_duration`: Moderately skewed with a skewness value of -0.36, implying a moderate skewness in the distribution.

### Outlier Analysis 📈

![image](https://github.com/riyouuyt/Forage-British-Airways-Virtual-Experience/assets/122600889/aca02be7-cf1f-40bc-b2c0-46deb62234ee)

Outlier detection and severity:
- `purchase_lead`: Contains 3456 severe outliers.
- `length_of_stay`: Shows 3807 severe outliers.
- `flight_hour` and `flight_duration`: No severe outliers detected in these columns.

### Categorical Columns Analysis 📊

![image](https://github.com/riyouuyt/Forage-British-Airways-Virtual-Experience/assets/122600889/f11a447b-57b2-41f2-9169-e7ae39818a89)

Categorical columns with unique values:
- `sales_channel`: Internet, Mobile.
- `trip_type`: RoundTrip, CircleTrip, OneWay.
- `flight_day`: Sat, Wed, Thu, Mon, Sun, Tue, Fri.
- `booking_origin`: Countries and locations of booking origins.
- `wants_extra_baggage`, `wants_preferred_seat`, `wants_in_flight_meals`: Binary features (0 or 1).


## **Data Preprocessing Steps:** 
- **Duplicate Data Check:**

  Ensured the removal of any duplicate entries.

- **Log Transformation**

  * **np.log(df['purchase_lead'] + 1)**: This function applies the natural logarithm to the 'purchase_lead' column values after adding 1 to handle instances where the data contains zeros. Log transformation is often used to reduce right-skewedness in data distributions, compressing larger values and expanding smaller ones.

  * **np.log(df['length_of_stay'] + 1)**: Similar to 'purchase_lead', the 'length_of_stay' column undergoes a log transformation by adding 1 to the values. This transformation can help mitigate skewness and normalize the data distribution, making it more conducive for analysis and modeling.

  The addition of 1 to the values is crucial to handle situations where the data contains zeros because the logarithm of zero is undefined. By adding 1, it ensures that zeros do not cause issues during the transformation process, allowing the transformation to be applied to the entire dataset effectively.

- **Feature Engineering:**

  Created new features by generating an interaction term between 'purchase_lead' and 'length_of_stay,' and binning 'flight_hour' into morning, afternoon, and evening categories.

- **Scaling and Encoding:**

  Normalized data using MinMaxScaler and encoded categorical columns using one-hot encoding. Additionally, mapped 'flight_day' to numerical values.

## **Modeling and Model Comparison** 🤖
We built three models: Random Forest, Logistic Regression, and Gradient Boosting. Upon comparing their performances, the Gradient Boosting model stood out due to its accuracy in predicting customer bookings. It achieved an accuracy of 85%, although its precision and recall varied for each class, showcasing higher performance for predicting non-bookings ('0') than bookings ('1'). Despite its lower recall for bookings, the model's accuracy makes it the preferred choice for this predictive task.

This choice was primarily made due to the model's overall accuracy and the balance it strikes between predicting both booking and non-booking instances.

### **Feature Importance**

![image](https://github.com/riyouuyt/Forage-British-Airways-Virtual-Experience/assets/122600889/90b5f5ff-710f-4871-beed-8cd635931d95)


The top three influential features in our analysis are 'booking_origin' for Malaysia, 'booking_origin' for Australia, and 'length_of_stay.' These features played a significant role in the predictive capacity of our model, contributing notably to the outcomes and insights drawn from our analysis.
