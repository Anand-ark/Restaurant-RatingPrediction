import numpy as np
from sklearn.tree import DecisionTreeClassifier
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('sm_model.pkl', 'rb'))
file1 = open("city.obj",'rb')
city = pickle.load(file1)
file1.close()
file2 = open("price.obj",'rb')
price = pickle.load(file2)
file2.close()
file3 = open("cuisine.obj",'rb')
cuisine = pickle.load(file3)
file3.close()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    #int_features = [float(x) for x in request.form.values()]
    
    
    features=[]
    c=request.form["City"]
    features.append(city['City'][c])
    p=request.form["Price Range"]
    features.append(price['Price'][p])
    r=(int(request.form["Number of Reviews"]))
    features.append(r)
    d=request.form["Cuisine_Style"]
    features.append(cuisine['Cuisine_Style'][d])
    
    final_features = [np.array(features)]
    prediction = model.predict(final_features)
    if(prediction==0):
        prediction='1 STAR'
    elif(prediction==1):
        prediction='1.5 STAR'
    elif(prediction==2):
        prediction='2 STAR'
    elif(prediction==3):
        prediction='2.5 STAR'
    elif(prediction==4):
        prediction='3 STAR'
    elif(prediction==5):
        prediction='3.5 STAR'
    elif(prediction==6):
        prediction='4 STAR'
    elif(prediction==7):
        prediction='4.5 STAR'
    else:
        prediction='5 STAR'

    #output =prediction[0]

    return render_template('index.html', prediction_text='Prediction : {}'.format(prediction))


if __name__ == "__main__":
    app.run(debug=True)
