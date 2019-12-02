import pandas as pd
import pickle

from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

pima_df = pd.read_csv('data/diabetes.csv')
feature_cols = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction',
                'Age']
X = pima_df[feature_cols]
y = pima_df.Outcome

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

log_reg_model = LogisticRegression()
log_reg_model.fit(X_train, y_train)

y_pred = log_reg_model.predict(X_test)

accuracy = accuracy_score(y_true=y_test, y_pred=y_pred)

#exporting my model
pickle.dump(log_reg_model,open("log_reg_model.pkl","wb"))

# Loading model to compare the results
model = pickle.load( open('log_reg_model.pkl','rb'))
print(model.predict([[5, 148, 75, 30, 8, 44.2, 0.43, 45]]))


