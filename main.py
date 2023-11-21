# # import 
# from flask import Flask, render_template , request
# import joblib


# # load the model
# model = joblib.load('predict_79.pkl')

# # initilaise the app
# app = Flask(__name__)

# @app.route('/')
# def homepage():
#     return render_template("home.html")


# @app.route('/form')
# def contact():
#     return render_template("forms.html")

# @app.route('/predict', methods = ['post'])
# def predict():
#     number =  request.form.get('phone')
#     mail =  request.form.get('email')
#     name =  request.form.get('name')
    
    
#     data = model.predict([[1,1,1,1,1,1,1,1]])

#     if data[0]==0:
#         resp = "not diabetic"
#     else:
#         resp ="diabetic"    
    
#     print(number)
#     print(mail)
#     print(name)
    
#     return resp


# @app.route('/dsa')
# def dsa():
#     return "welcome to dsa page"




# # Running the app
# app.run(debug=True)



# import 
from flask import Flask, render_template, request
import joblib

# load the model
model = joblib.load('predict_79.pkl')

# initialize the app
app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("home.html")

@app.route('/form')
def contact():
    return render_template("forms.html")

@app.route('/predict', methods=['POST'])
def predict():
    preg = float(request.form.get('preg'))
    glas = float(request.form.get('glas'))
    pres = float(request.form.get('pres'))
    skin = float(request.form.get('skin'))
    test = float(request.form.get('test'))
    mass = float(request.form.get('mass'))
    pedi = float(request.form.get('pedi'))
    age = float(request.form.get('age'))

    data = model.predict([[preg, glas, pres, skin, test, mass, pedi, age]])

    if data[0] == 0:
        resp = "not diabetic"
    else:
        resp = "diabetic"

    print("Input values:")
    print(f"Pregnancies: {preg}")
    print(f"Glucose: {glas}")
    print(f"Blood Pressure: {pres}")
    print(f"Skin Thickness: {skin}")
    print(f"Insulin Test: {test}")
    print(f"BMI: {mass}")
    print(f"Pedigree: {pedi}")
    print(f"Age: {age}")

    return render_template("forms.html" , data = resp)

    

@app.route('/dsa')
def dsa():
    return "Welcome to dsa page"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)



