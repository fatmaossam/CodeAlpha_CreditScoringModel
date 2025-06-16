import pandas as pd
from sklearn.ensemble import RandomForestClassifier 
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score
)
from sklearn.preprocessing import LabelEncoder

data = pd.read_csv(r'C:\Users\hossam fathy\Documents\csv project\credit score dataset.csv')
print(data)
print('-------------------------------------------------------------------------------------------------------------------')
# filtering the data
data_cleaned = data.filter(['income', 'debt', 'payment history','credit score' ])
print(data_cleaned)

# Encoding categorical variables

le = LabelEncoder()
data_cleaned['credit score'] = le.fit_transform(data_cleaned['credit score']) #poor = 3, fair = 1, good = 2, excellent = 0
print('____________________________________________________________________________________________________________________')
print(data_cleaned)

x = data_cleaned[['income', 'debt', 'payment history']]
y = data_cleaned['credit score']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(random_state=42)
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
actual = y_test.values
print('the actual values are =', le.inverse_transform(actual))
print('the predicted values are =', le.inverse_transform(y_pred))
y_pred_proba = model.predict_proba(x_test)

accuracy= accuracy_score(y_test, y_pred)*100
precision = precision_score(y_test, y_pred, average='weighted')*100
recall = recall_score(y_test, y_pred, average='weighted')*100
f1 = f1_score(y_test, y_pred, average='weighted')*100
roc_auc = roc_auc_score(y_test, y_pred_proba, multi_class='ovr')*100
# Displaying the results
print('the results of accuracy model is =', accuracy)
print('the results of precision model is =', precision)
print('the results of recall model is =', recall)
print('the results of f1 model is =', f1)
print('the results of roc_auc model is =', roc_auc)

#new data to predict
new_data = [[4500, 2000, 1]]
the_prediction = model.predict(new_data)
print('the prediction of the new data is =', le.inverse_transform(the_prediction))
