# Create API of ML model using flask

'''
This code takes the JSON data while POST request an performs the prediction using loaded model and returns
the results in JSON format.
'''
import pandas as pd
from flask import Flask, jsonify, request
import pickle

# load model
model = pickle.load(open('log_reg_model.pkl','rb'))

# app
app = Flask(__name__)

# routes
@app.route('/api', methods=['POST'])

def predict():
    # get data
    data = request.get_json(force=True)

    # convert data into dataframe
    data.update((x, [y]) for x, y in data.items())
    data_df = pd.DataFrame.from_dict(data)

    # predictions
    result = model.predict(data_df)

    # send back to browser
    output = int(result[0])

    # return data
    return jsonify(diabetes=output)

if __name__ == '__main__':
    app.run(port = 5001, debug=True)
