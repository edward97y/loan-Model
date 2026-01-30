from fastapi import FastAPI
from pydantic import BaseModel,field_validator
from contextlib import asynccontextmanager
import pandas as pd
import joblib


class Features(BaseModel):
    no_of_dependents:int
    education:str
    self_employed:str
    income_annum:int
    loan_amount:int
    loan_term:int
    cibil_score:int
    residential_assets_value:int
    commercial_assets_value:int
    luxury_assets_value:int
    bank_asset_value:int

    
    @field_validator('education')
    def check_education(cls,v):
        if v.lower() not in ("graduate","not graduate"):
            raise ValueError("education must be Graduate or Not Graduate")
        return v.lower()
    
    @field_validator('self_employed')
    def check_employed(cls,v):
        if v.lower() not in ("yes","no"):
            raise ValueError("this field must be yes or no")
        return v.lower()

@asynccontextmanager
async def load_model(app:FastAPI):
    app.state.model=joblib.load('pipeline_model.pkl')
    yield
      
app=FastAPI(lifespan=load_model)
@app.post('/')
def predict_loan(features:Features):
    try:
       model=app.state.model
       data=pd.DataFrame([features.dict()])
       predict=model.predict(data)[0]
       return {"prediction":predict.strip()}
    except Exception as e:
        return {"error": str(e)}

