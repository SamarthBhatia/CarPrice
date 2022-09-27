from flask import Flask,render_template,request
import pandas as pd
import pickle
app=Flask(__name__)
car=pd.read_csv("Cleanedcar.csv")
model=pickle.load(open("LinearRegressionModel.pkl",'rb'))
@app.route('/')
def index():

    companies=sorted(car['full_name'].str.split(' ').str.slice(0,1).str.join(' ').unique())
    car_models=sorted(car['full_name'].str.split(' ').str.slice(0,3).str.join(' ').unique())
    year=sorted(car['year'].unique(),reverse=True)
    fuel_type=car['fuel_type'].unique()
    km_driven=car['km_driven'].unique()
    transmission_type=car['transmission_type'].unique()
    mileage=car['mileage'].unique()
    engine=car['engine'].unique
    return render_template('index.html',companies=companies,car_models=car_models,years=year,fuel_type=fuel_type,transmission_type=transmission_type,mileage=mileage,engine=engine)


@app.route('/predict',methods=['POST'])
def predict():
    company=request.form.get('company')
    car_models=request.form.get('car_models')
    years=(request.form.get('year'))
    fuel=request.form.get('fuel')
    transmission=request.form.get('transmission')
    kmdriven=request.form.get('kmdriven')
    mileage=request.form.get('mileage')
    engine=request.form.get('engine')
    print(company,car_models,years,kmdriven,fuel,transmission,mileage,engine)
    prediction=model.predict(pd.DataFrame([[car_models,years,kmdriven,fuel,transmission,mileage,engine]],columns=['full_name','year','km_driven','fuel_type','transmission_type','mileage','engine']))
    return str(prediction[0])


if __name__=="__main__":
    app.run(debug=True)