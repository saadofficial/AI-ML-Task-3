# 🏠 Task 3 - House Price Prediction Using Machine Learning

## 👨‍💻 Author
**Saad Khanzada**  
AI/ML Remote Internship

---

# 📌 Project Overview

This project focuses on predicting house prices using Machine Learning techniques based on different property features such as:

- House Size (Square Footage)
- Number of Bedrooms
- Location

The project demonstrates the complete Machine Learning workflow including:

- Data Collection
- Data Preprocessing
- Feature Encoding
- Feature Scaling
- Model Training
- Prediction
- Model Evaluation
- Data Visualization

The main goal of this project is to build a regression model capable of estimating house prices using historical housing data.

---

# 🎯 Objective

The objective of this task is to:

- Understand regression-based Machine Learning
- Learn how property features affect house prices
- Preprocess and prepare housing datasets
- Train a Machine Learning model
- Predict house prices
- Evaluate model performance using MAE and RMSE
- Visualize predicted vs actual prices

---

# 📊 Dataset Information

## Dataset Name
Housing Data Dataset

The dataset contains information about houses and their prices.

---

## Dataset Features

| Feature | Description |
|---|---|
| Size | House size in square feet |
| Bedrooms | Number of bedrooms |
| Location | City where the house is located |
| Price | Actual price of the house |

---

# 🛠 Technologies & Libraries Used

| Technology | Purpose |
|---|---|
| Python | Programming Language |
| Pandas | Data handling and preprocessing |
| Scikit-learn | Machine Learning modeling |
| Matplotlib | Data visualization |
| NumPy | Numerical calculations |

---

# 🧠 Machine Learning Concept Used

## Regression

Regression is a Machine Learning technique used for predicting continuous numerical values.

Examples include:
- House prices
- Temperature prediction
- Stock prices

In this project, regression is used to predict house prices.

---

# 🤖 Model Used

## Linear Regression

Linear Regression is one of the simplest supervised Machine Learning algorithms.

It learns relationships between:
- Input features
- Output target value

The model predicts house prices based on:
- House size
- Bedrooms
- Location

---

# 🔄 Project Workflow

The project was completed in the following steps:

---

# 1️⃣ Data Collection

The dataset was stored in a CSV file:

```plaintext
housing_data.csv
```

The CSV file was loaded using Pandas.

```python
pd.read_csv()
```

---

# 2️⃣ Data Inspection

The dataset was inspected using:

- `.head()`
- `.info()`
- `.describe()`

This helped in understanding:
- Dataset structure
- Feature names
- Data types
- Statistical information

---

# 3️⃣ Data Preprocessing

## Location Encoding

Machine Learning models cannot understand text values directly.

Example:
- Karachi
- Lahore
- Islamabad

These values were converted into numerical form using:

```python
LabelEncoder()
```

Example:

| Location | Encoded Value |
|---|---|
| Karachi | 0 |
| Lahore | 1 |
| Islamabad | 2 |

---

# 4️⃣ Feature Selection

The following features were selected as inputs:

```python
Size
Bedrooms
Location
```

These features were stored in:

```python
X
```

The target variable selected was:

```python
Price
```

Stored in:

```python
y
```

---

# 5️⃣ Feature Scaling

Feature scaling was performed using:

```python
StandardScaler()
```

### Purpose of Feature Scaling

Feature scaling normalizes data into similar ranges so that the Machine Learning model performs better and faster.

---

# 6️⃣ Data Splitting

The dataset was divided into:
- Training Data (80%)
- Testing Data (20%)

Using:

```python
train_test_split()
```

### Purpose

- Training data teaches the model
- Testing data evaluates performance

---

# 7️⃣ Model Training

The Linear Regression model was trained using:

```python
model.fit(X_train, y_train)
```

The model learned patterns between:
- House features
- House prices

---

# 8️⃣ Prediction

Predictions were generated using:

```python
model.predict(X_test)
```

The model predicted prices for unseen houses.

---

# 9️⃣ Model Evaluation

The model performance was evaluated using:

## Mean Absolute Error (MAE)

Measures average prediction error.

### Formula

```plaintext
MAE = Average of absolute errors
```

Lower MAE indicates better performance.

---

## Root Mean Squared Error (RMSE)

Measures prediction accuracy.

### Formula

```plaintext
RMSE = Square root of mean squared errors
```

Lower RMSE indicates better predictions.

---

# 📈 Data Visualization

A graph was created to compare:

- Actual House Prices
- Predicted House Prices

### Visualization Used

- Line Plot

The graph helps in visually analyzing the prediction performance of the model.

---

# 📉 Graph Explanation

| Line | Description |
|---|---|
| Actual Prices | Real prices from dataset |
| Predicted Prices | Prices predicted by AI model |

If both lines are close together, it means the model is performing well.

---

# 📚 Skills Learned

Through this project, the following skills were learned:

- Regression Modeling
- Data Preprocessing
- Feature Encoding
- Feature Scaling
- Model Training
- Model Evaluation
- Data Visualization
- Working with CSV datasets

---

# 🧾 Key Concepts Explained

## 🔹 Machine Learning
A field of Artificial Intelligence where systems learn patterns from data.

---

## 🔹 Regression
Predicting continuous numerical values.

---

## 🔹 Features
Input variables used for prediction.

Examples:
- Size
- Bedrooms
- Location

---

## 🔹 Target Variable
The output value the model predicts.

Example:
- House Price

---

## 🔹 Training
The process where the model learns from historical data.

---

## 🔹 Prediction
Using learned patterns to estimate future values.

---

# 📂 Project Structure

```plaintext
Task-3-House-Price-Prediction/
│
├── housing_data.csv
├── task3_house_prediction.py
├── README.md
└── graph.png
```

---

# ▶️ How to Run the Project

## Step 1 — Install Required Libraries

```bash
pip install pandas
pip install matplotlib
pip install scikit-learn
pip install numpy
```

---

## Step 2 — Run the Python File

```bash
python task3_house_prediction.py
```

---

# ✅ Results

The Linear Regression model successfully predicted house prices based on property features.

The predicted prices were close to actual prices, demonstrating the effectiveness of the regression model.

The project also demonstrated how preprocessing and feature scaling improve Machine Learning performance.

---

# 🚀 Future Improvements

This project can be improved by:

- Using larger real-world datasets
- Adding more features
- Using advanced regression models
- Deploying the model as a web application
- Using Deep Learning models

---

# 📌 Conclusion

This project provided practical experience in Machine Learning regression techniques and real estate data analysis.

The project strengthened understanding of:
- Data preprocessing
- Regression models
- Feature scaling
- Model evaluation
- Prediction systems

It also demonstrated how AI can be used in real-world real estate price estimation systems.

---

# 🙌 Acknowledgement

This project was completed as part of an AI/ML Remote Internship to gain practical knowledge and hands-on experience in Machine Learning and data analysis.
