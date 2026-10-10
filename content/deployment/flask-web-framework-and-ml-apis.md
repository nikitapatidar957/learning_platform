# Flask Web Framework & Machine Learning API Serving

Master deploying trained machine learning models as production REST APIs and web applications using Python Flask: application lifecycle, routing, handling HTTP requests, Jinja2 templating, and real-time model inference.

---

## 1. Introduction to Flask for Machine Learning

### Slide 1: Introduction to Flask



---

### Slide 2: Flask Introduction

• Flask is a web framework for the Python language. This means it provides tools, libraries and technologies that allow us to build a web application.

• Some times we need to serve the model we have build as end points, so flask allow us to access the model we have build and showing the results of the model.

• It provides us to create a UI based web application that allow us to provide the input data required by the models we have build.

• For an example of object detection task, we can create a web application using flask that let us capture the video and by calling the end points we can call our model for the object detection task and can show back the results of the model in the UI.

---

### Slide 3: Flask API

• Flask is a widely used micro web framework for creating APIs in Python. It is a simple yet powerful web framework that is designed to get started quickly and easily, with the ability to scale up to complex applications.

• It is designed as a web framework for RESTful API development where flask allow us to directly call the end points without creating any UI and result back the output of the model to the server from where the API was called.

• To read more visit below links:

• https://towardsdatascience.com/building-a-machine-learning-web-application-using-flask-29fa9ea11dac

• https://medium.com/@alanbanks229/part-1-of-2-introduction-to-python-flask-20286f37d2e0

• https://towardsdatascience.com/deploy-a-machine-learning-model-using-flask-da580f84e60c

---

## 2. Production Flask Application (`app.py`)

Below is the production application script loading the serialized churn prediction model pipeline and serving both HTML GUI and prediction endpoints:

```python
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

X = ['Tenure', 'WarehouseToHome', 'NumberOfDeviceRegistered',
       'NumberOfAddress', 'DaySinceLastOrder', 'CashbackAmount',
       'PreferredLoginDevice_Computer', 'PreferredLoginDevice_Mobile',
       'CityTier_1', 'CityTier_2', 'CityTier_3', 'PreferredPaymentMode_CC',
       'PreferredPaymentMode_COD', 'PreferredPaymentMode_DC',
       'PreferredPaymentMode_E wallet', 'PreferredPaymentMode_UPI',
       'PreferedOrderCat_Fashion', 'PreferedOrderCat_Grocery',
       'PreferedOrderCat_Laptop', 'PreferedOrderCat_Mobile',
       'PreferedOrderCat_Others', 'SatisfactionScore_1', 'SatisfactionScore_2',
       'SatisfactionScore_3', 'SatisfactionScore_4', 'SatisfactionScore_5',
       'MaritalStatus_Divorced', 'MaritalStatus_Married',
       'MaritalStatus_Single', 'Gender_Female', 'Gender_Male', 'Complain_0',
       'Complain_1']
len(X)

def predict_price(tenure, warehouse, numdevice, numaddress, lastorder, cashback, logindevice, citytier, paymentmode, ordercat, score, maritalstatus, gender, complain):    
    logindevice_index = X.index('PreferredLoginDevice_' + logindevice)
    citytier_index = X.index('CityTier_' + citytier)
    paymentmode_index = X.index('PreferredPaymentMode_' + paymentmode)
    ordercat_index = X.index('PreferedOrderCat_' + ordercat)
    score_index = X.index('SatisfactionScore_' + score)
    maritalstatus_index = X.index('MaritalStatus_' + maritalstatus)
    gender_index = X.index('Gender_' + gender)
    complain_index = X.index('Complain_' + complain)

    index_list = [logindevice_index, citytier_index, paymentmode_index, ordercat_index, score_index, maritalstatus_index, gender_index, complain_index]

    x = np.zeros(len(X))
    x[0] = tenure
    x[1] = warehouse
    x[2] = numdevice
    x[3] = numaddress
    x[4] = lastorder
    x[5] = cashback

    for ind in index_list:
      if ind >= 0:
          x[ind] = 1

    #for media in media_type_list:
    #  media_index = X.columns.get_loc('media_type_' + media)
    #  if media_index >= 0:
    #    x[media_index] = 1

    return model.predict([x])[0]


app = Flask(__name__)

model = pickle.load(open('churn.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    if request.method == 'POST':
        tenure = float(request.form['tenure'])
        warehouse = float(request.form['warehousetohome'])
        numdevice = float(request.form['numdevices'])
        numaddress = float(request.form['numaddress'])
        lastorder = float(request.form['lastorder'])
        cashback = float(request.form['cashbackamount'])
        logindevice = request.form['logindevice']
        citytier = request.form['citytier']
        paymentmode = request.form['paymentmode']
        ordercat = request.form['ordercat']
        score = request.form['satisfactionscore']
        maritalstatus =request.form['maritalstatus']
        gender = request.form['gender']
        complain = request.form['complain']
  

    prediction = predict_price(tenure, warehouse, numdevice, numaddress, lastorder, cashback, logindevice, citytier, paymentmode, ordercat, score, maritalstatus, gender, complain)    
  
    return render_template('index.html', prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
```

---

## 3. Frontend Web Form Template (`templates/index.html`)

Below is the HTML5 Jinja2 form template capturing customer attributes and rendering model predictions:

```html
<!DOCTYPE html>
<html >
<!--From https://codepen.io/frytyler/pen/EGdtg-->
<head>
  <meta charset="UTF-8">
  <title>Customer Churn Prediction</title>
  <link href='https://fonts.googleapis.com/css?family=Pacifico' rel='stylesheet' type='text/css'>
<link href='https://fonts.googleapis.com/css?family=Arimo' rel='stylesheet' type='text/css'>
<link href='https://fonts.googleapis.com/css?family=Hind:300' rel='stylesheet' type='text/css'>
<link href='https://fonts.googleapis.com/css?family=Open+Sans+Condensed:300' rel='stylesheet' type='text/css'>
  
</head>
<style>
    
body  {
  margin-top : 0px;
  background-color : black;
  color : #ff9933;
  width : 100%;
  transform : scale(90%);
  font-family : arial, helvatica, sans-serif;
}

.row{
	margin-top : 0px;
	padding : 0px;
	margin-bottom : 20px;
}

.result {
    margin: auto;
    width: 75%;
}

.column {
	float : left;
	width : 50%;
}

.button{
	text-align : center;
}

.button-submit {
	background-color:#ff9933;
	padding : 15px 3px;
	margin-top : 20px;
	border : none;
	color : black;
}

.button-submit:hover {
	background-color : #008cba;
	color : white;
}

.button-submit:active {
	background-color : #4caf55;
	color : white;
}

</style>


<body>
 <div class="row">
	<h1 style="margin: auto; width: 35%; padding: 0.1%; text-align: center;">Customer Churn Prediction</h1>

     <!-- Main Input For Receiving Query to our ML -->
    <form action="{{ url_for('predict')}}"method="post">
		<div class="column">
		<fieldset style="float:center; height:500px; margin-right:10px;">
			<legend><b></b></legend>
			<p><b>Tenure :</b><br>
			<input type="number" name="tenure" placeholder="tenure with the organization" required="required" /></p>
			
			
			<p><b>City Tier:</b><br>
			<select name="citytier" id="citytier" required>
				<option value="1">Tier 1</option>
				<option value="2">Tier 2</option>
				<option value="3">Tier 3</option>
			</select></p>
				
			
			<p><b>Distance to the warehouse from the residence :</b><br>
			<input type="number" name="warehousetohome" placeholder="distance in km" required="required" /></p>
			
			
			<b>Gender of the customer :</b><br>
			<div style="float:left; margin-right: 1.5em;">
			<input type="radio" id="male" name="gender" value="Male" required="required"/>
			<label for="male">Male</label>
			</div>
			<div style="float:left; margin-right: 1.5em;">
			<input type="radio" id="female" name="gender" value="Female" required="required"/>
			<label for="female">Female</label>
			</div>
			<br>
									
			
			<p><b>Marital Status :</b><br>
			<select name="maritalstatus" id="maritalstatus" required>
				<option value="Single">Single</option>
				<option value="Married">Married</option>
				<option value="Divorced">Divorced</option>
			</select></p>
			
			
			<b>Any complaints in the last month> :</b><br>
			<div style="float:left; margin-right: 1.5em;">
			<input type="radio" id="yes" name="complain" value="1" required="required"/>
			<label for="Yes">Yes</label>
			</div>
			<div style="float:left; margin-right: 1.5em;">
			<input type="radio" id="no" name="complain" value="0" required="required"/>
			<label for="No">No</label>
			</div>
			<br>
			
			
			<p><b>Number of coupons used in the last month :</b><br>
			<input type="number" name="couponused" placeholder=" " required="required" /></p>

			
			<p><b>Number of orders made in the last month :</b><br>
			<input type="number" name="ordercount" placeholder=" " required="required" /></p>
			
			<p><b>Cashback Amount :</b><br>
			<input type="number" name="cashbackamount" placeholder=" " required="required" /></p>
			
		</fieldset>
		</div>
		
		<div class="column">
		<fieldset style="height:500px; margin-right:10px;">
				<legend><b></b></legend>
				<p><b>Number of days since last order placedv :</b><br>
				<input type="number" name="lastorder" placeholder="" required="required" /></p>
				
				
				<p><b>Preferred login device:</b><br>
				<select name="logindevice" id="logindevice" required>
					<option value="Mobile">Mobile Phone</option>
					<option value="Computer">Computer</option>
				</select></p>
				
				
				<p><b>Number of devices registered with the app :</b><br>
				<input type="number" name="numdevices" placeholder="" required="required" /></p>
			
	
				<p><b>Preferred Payment Mode: </b><br>
				<select name="paymentmode" id="paymentmode" required>
					<option value="DC">Debit Card</option>
					<option value="CC">Credit Card</option>
					<option value="UPI">UPI</option>
					<option value="COD">Cash On Delivery</option>
					<option value="E wallet">E-wallet</option>
				</select></p>
				
				
				<p><b>Preferred Order Category: </b><br>
				<select name="ordercat" id="ordercat" required>
					<option value="Laptop">Laptop</option>
					<option value="Mobile">Mobile</option>
					<option value="Fashion">Fashion</option>
					<option value="Grocery">Grocery</option>
					<option value="Others">Others</option>
				</select></p>

				
				<p><b>Approx. number of hours customer spends on app :</b><br>
				<input type="number" name="hourspend" placeholder="" required="required" /></p>
				
				
				<p><b>Satisfaction score : </b><br>
				<select name="satisfactionscore" id="satisfactionscore" required>
					<option value="1">1</option>
					<option value="2">2</option>
					<option value="3">3</option>
					<option value="4">4</option>
					<option value="5">5</option>
				</select></p>


				<p><b>Number of addresses registered with the app :</b><br>
				<input type="number" name="numaddress" placeholder="" required="required" /></p>
				
				
				<p><b>Percentage increases in order from last year :</b><br>
				<input type="number" name="orderhike" placeholder="" required="required" /></p>

		</fieldset>
		</div>
		
		
		
		<div class="button" >
			<button type="submit" class="button-submit" style="cursor:pointer;" hover="background-color:blue;"><b>SUBMIT</b></button>
		</div>
    </form>
	<br>
	<div class="result" align="center">
		<div class="result" align="center">
		{% if prediction==1 %}
			<h2><p style="padding: 0.3%; color:red;"><b>CUSTOMER WILL CHURN OUT!</b></p></h2>
		{% elif prediction==0 %}
			<h2><p style="padding: 0.3%; color:green;"><b>CUSTOMER WILL NOT CHURN OUT!</b></p></h2>
		{% endif %}	
	</div>	
	</div>
 </div>


</body>
</html>
```

---

## Key Interview Concepts: Flask & Model Serving

1. **Why Flask for ML Model Serving?**:
   - Lightweight micro-framework with zero boilerplate or database dependencies.
   - Gives complete flexibility over routing, middleware, and request validation.
   - Native Python runtime allows direct loading of scikit-learn, PyTorch, and TensorFlow models via `pickle` or `joblib`.
2. **Model Persistence & Deserialization**:
   - Models must be loaded **once** at application initialization (`model = pickle.load(open('churn.pkl', 'rb'))`), never inside request handlers. Loading on every request introduces severe latency and memory leaks.
3. **Handling Categorical Encoding at Serving Time**:
   - In production, form submissions must match the exact feature columns and one-hot encoding layout expected by the trained model (as shown in the `predict_price` function index mapping).
4. **REST API Best Practices**:
   - Support both `application/x-www-form-urlencoded` (web forms) and `application/json` (microservice clients).
   - Use proper HTTP response status codes: `200 OK`, `400 Bad Request` for invalid input parameters, `500 Internal Server Error` for model execution failures.
