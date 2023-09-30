import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from  flask import Flask

#app
app = Flask(__name__,  template_folder = 'templates')

@app.route('/', methods = ['POST', 'GET'])
def main():
    
    return 'hello flask'

if __name__ == '__main__':
    app.run(debug=True)