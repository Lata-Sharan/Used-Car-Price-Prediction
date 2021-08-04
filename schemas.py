from pydantic import BaseModel
from typing import Optional

class CarPrice(BaseModel):
    Year : int
    Present_Price : float
    Kms_Driven : float
    Owner : int
    Seller_Type_Individual : int
    Transmission_Manual : int
    Fuel_Type_Diesel : int
    Fuel_Type_Petrol : int
  
    

class CarPriceResponse(BaseModel):
    Selling_Price : float
   
    