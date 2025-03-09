import pickle
import pandas as pd
import warnings 
warnings.filterwarnings('ignore')

#load the trained model 
def load_model(model_path):
    with open(model_path,'rb') as f:
        return pickle.load(f)
    
model = load_model('pipeline.pk1')

#input_features = [[2637,0.00073,0.127,17.22]]

#lets make it more user friendly 
star_temp = input("Enter the temparature of the star :")
star_Luminosity = input("Enter the Luminosity of the star :")
star_Radius = input("Enter the star Radius :")
star_Absolute_magnitude = input("Enter the absolute magnitude : ")

test_data = pd.DataFrame([[star_temp,star_Luminosity,star_Radius,star_Absolute_magnitude]])
#make predictions based on this loaded model
def make_prediction(model,test_data):
    predict_class = model.predict(test_data)

    return predict_class

print(make_prediction(model,test_data))




