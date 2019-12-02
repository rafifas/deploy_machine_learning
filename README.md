# deploy_machine_learning


machine-learning-flask-example
This project demonstrates how to train and deploy a simple model. I use a model that can predict whether or not a patient has diabetes, based on certain diagnostic measurements included in the dataset from https://github.com/karanmurthy7/machine-learning-flask-example. This project is composed of 5 python files: dataset, model, server, request and flask_app.

# model
diabetes-classification-model.py trains and saves the model to the disk.

# server
server.py contains all the requiered for flask and to manage APIs.

# request
request.py contains the python code to process POST request to server.

# Flask_app
flask_app.py contains the python code as modified server in pythonanywhere.com

# deploy model in pythonanywhere.com
I the deployed machine learning model into pythonanywhere.com and test it using postman.
To deploy the model, run the diabetes-classification-model.py first in local to get the model (log_reg_model.pkl). upload the model along with flask_app.pkl into /home/user/mysite  

![picture](https://github.com/rafifas/deploy_machine_learning/blob/master/directory_in_pythonanywhere.PNG)
![picture](https://github.com/rafifas/deploy_machine_learning/blob/master/pythonanywhere_files.PNG)

Try the deployed model with postman. Open postman and insert your pythonanywhere URL and test your model by inputing data as following example

!![picture](https://github.com/rafifas/deploy_machine_learning/blob/master/postman_input_example.PNG)
