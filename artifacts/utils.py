import numpy as np
import pickle
from artifacts.config import MODEL_PATH

class icp():
    def __init__(self,data):
        self.data = data

    def load_model(self):
        with open(MODEL_PATH,'rb') as file:
            self.model= pickle.load(file)     




    def predict(self):
        self.load_model()
        SL =float(self.data['SL'])
        SW = float(self.data['SW'])
        PL=float(self.data['PL'])
        PW=float(self.data['PW'])
        array = np.array([[SL,SW,PL,PW]])   
        print(array)
        print("*"*50)
        
        result= self.model.predict(array)
        

        if result == 0:
            spacies="Iris - Setosa"
        if result == 1:
            spacies="Iris - Veriscolor"
        if result== 2:
            spacies="Iris - Virgininca"

       
        
        return spacies