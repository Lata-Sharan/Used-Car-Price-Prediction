import pandas as pd
from fastapi import FastAPI
from schemas import CarPrice, CarPriceResponse
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = [
    "http://usedcarprice-predictor.herokuapp.com"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def index():
    return {"detail":"please make a post request to /predict"}


@app.post('/predict/', response_model=CarPriceResponse)
def predict(request: CarPrice):
    data = dict(request)
    Year = request.Year 
    Present_Price = request.Present_Price
    Kms_Driven = request.Kms_Driven
    Owner = request.Owner
    Seller_Type_Individual = request.Seller_Type_Individual
    Transmission_Manual = request.Transmission_Manual
    Fuel_Type_Diesel = request.Fuel_Type_Diesel
    Fuel_Type_Petrol = request.Fuel_Type_Petrol
    
    # for python 3.6
    #with open("model/model.pkl", "rb") as fh:
        #model = pickle.load(fh)

    # for python 3.8
    model = pd.read_pickle("model/model.pkl")
    
    Selling_Price = model.predict([[Year,Present_Price,Kms_Driven,Owner,Seller_Type_Individual,Transmission_Manual,Fuel_Type_Diesel,Fuel_Type_Petrol]])
    reg = Selling_Price[0]
    data['Selling_Price'] = reg
    return data
    # return data

if __name__=="__main__":
    uvicorn.run(app,host="127.0.0.1",port=9000)