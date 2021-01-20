
# importing the necessary dependencies
from flask import Flask, render_template, request
from flask_cors import cross_origin
from sklearn.linear_model import LinearRegression
import pickle

app = Flask(__name__) # initializing a flask app

@app.route('/',methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")

@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            crim =float(request.json['crim'])
            zn = float(request.json['zn'])
            indus = float(request.json['indus'])
            chas = request.json['chas']
            nox = float(request.json['nox'])
            rm = float(request.json['rm'])
            age = request.json['age']
            dis = float(request.json['dis'])
            rad = float(request.json['rad'])
            tax = float(request.json['tax'])
            ptratio = float(request.json['ptratio'])
            b = float(request.json['b'])
            lstat = float(request.json['lstat'])

            filename = 'lr_model.pickle'
            loaded_model = pickle.load(open(filename, 'rb')) # loading the model file from the storage
            # predictions using the loaded model file
            prediction=loaded_model.predict([[crim, zn, indus, chas, nox, rm, age, dis, rad, tax, ptratio,b,lstat]])
            print('Prediction is', prediction)
            # showing the prediction results in a UI
            return render_template('results.html', prediction = 100*prediction)
        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'
    # return render_template('results.html')
    else:
        return render_template('index.html')

if __name__ == "__main__":
    #app.run(host='127.0.0.1', port=8001, debug=True)
	app.run(debug=True) # running the app