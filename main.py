from fastapi import FastAPI
import joblib
import pandas as pd

names_app = FastAPI()

def encode_prenom(prenom: str) -> pd.Series:
    """
        This function encode a given name into a pd.Series.
        
        For instance alain is encoded [1, 0, 0, 0, 0 ... 1, 0 ...].
    """
    alphabet = "abcdefghijklmnopqrstuvwxyzé-'"
    prenom = prenom.lower()
    
    return pd.Series([letter in prenom for letter in alphabet]).astype(int)

@names_app.get("/predict")
async def predict(name:str):
    regr_loaded = joblib.load("model.v1.bin")
    sexe = regr_loaded.predict([encode_prenom(name)])
    sexe = ("M" if sexe[0]==0 else "F")

    return {"name":name, "predicted_sex":sexe}

