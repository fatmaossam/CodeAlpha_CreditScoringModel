# CodeAlpha Credit Scoring Project

## Project Description
The CodeAlpha Credit Scoring Project is a machine learning application designed to predict credit scores based on user financial data. Using a Random Forest Classifier, this project demonstrates data preprocessing, model training, evaluation, and prediction capabilities. The project uses Python libraries such as pandas, scikit-learn, and a pre-defined credit scoring dataset.

---

## Features
1. **Data Preprocessing**:
   - Filters relevant financial features (income, debt, payment history, credit score).
   - Encodes categorical variables for credit score classification (poor, fair, good, excellent).

2. **Model Training**:
   - Trains a Random Forest Classifier on the cleaned data.
   - Splits the dataset into training (80%) and testing (20%) sets for robust evaluation.

3. **Evaluation Metrics**:
   - Accuracy
   - Precision
   - Recall
   - F1 Score
   - ROC-AUC Score

4. **Prediction**:
   - Predicts credit scores for new financial data inputs.

---

## Installation
To set up and run the project locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/fatmaossam/codeAlpha_creditscoring.git
   cd codeAlpha_creditscoring
   ```

2. **Install Dependencies**:
   Ensure you have Python 3.8+ installed. Install the required libraries using pip:
   ```bash
   pip install pandas scikit-learn
   ```

## How to Run
1. Open the project directory in your terminal.
2. Run the script:
   ```bash
   python credit_scoring.py
   ```

---

## Output
The script will:
1. Display the cleaned and encoded dataset.
2. Show the actual and predicted credit scores for the test data.
3. Provide model evaluation metrics (accuracy, precision, recall, F1 score, and ROC-AUC).
4. Predict the credit score for a sample new data input.

---

## Example Output
```
The actual values are: [excellent good fair poor]
The predicted values are: [excellent good fair fair]

The results of accuracy model are: 92.5%
The results of precision model are: 90.3%
The results of recall model are: 89.7%
The results of F1 model are: 91.0%
The results of ROC-AUC model are: 93.2%

The prediction of the new data is: ['good']
```

---

## Contributing
Contributions are welcome! Feel free to fork the repository and submit a pull request with your enhancements or bug fixes.


## Contact
For any inquiries or suggestions, feel free to reach out at: [fvtma22@gmail.com]
# CodeAlpha_CreditScoringModel
CodeAlpha_Credit Scoring Model | ML model to predict creditworthiness using financial data. Built with Python &amp; Scikit-learn.
