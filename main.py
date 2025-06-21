import pandas as pd
from flask import Flask, request, jsonify
import pickle
import os
from google.cloud import storage

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
model = None

def preprocess_data(df):
    df = df.fillna(df.mode().iloc[0])
    df = df.drop_duplicates()
    return df

def load_model():
    storage_client = storage.Client()
    bucket_name = "data-bikes-uci-example"
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob("artifacts/trained_model_2.pkl")
    blob.download_to_filename("trained_model_2.pkl")
    with open("trained_model.pkl", 'rb') as file:
        model = pickle.load(file)
    return model

def preprocess(input_json):
    try:
        df = pd.DataFrame(input_json, index=[0])
        x = preprocess_data(df)
        return x
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/predict', methods=['POST'])
def predict():
    model = load_model()
    try : 
        input_json = request.get_json()
        df_preprocessed = preprocess(input_json)
        y_predictions = model.predict(df_preprocessed)
        response = {'predictions': y_predictions.tolist()}
        return jsonify(response), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 5051)))