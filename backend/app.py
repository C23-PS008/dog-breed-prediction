from flask import Flask, request, jsonify
import tensorflow as tf
import os
import requests
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from dotenv import load_dotenv

# Load the model
model = tf.keras.models.load_model('./model')

# Load the label encoder
label_encoder = LabelEncoder()
label_encoder.classes_ = np.load('./model/label_encoder.npy', allow_pickle=True)


# Load environment variables from .env file
load_dotenv()

# Get the API key from the environment variable
api_key = os.getenv('API_KEY')

app = Flask(__name__)

@app.route('/')
def index():
    try:
        hello_json = {
            'status_code': 200,
            'message': 'Success testing the API!',
            'data': [],
        }
        return jsonify(hello_json)
    except Exception as e:
        error_json = {
            'status_code': 500,
            'message': 'Error occurred.',
            'error_details': str(e),
        }
        return jsonify(error_json), 500

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()  # Get the input data from the request
        dataframe = pd.read_csv('./data/akc-data-latest-final.csv')

        new_data_dict = {}
        for key, value in data.items():
            if key != "predictions":
                new_data_dict[key] = tf.constant(value, dtype=tf.string)

        # Make predictions
        predictions = model.predict(new_data_dict)
        predicted_labels = np.argmax(predictions, axis=1)
        predicted_labels = label_encoder.inverse_transform(predicted_labels)
        predicted_labels = predicted_labels.tolist()

        result = {'predictions': []}
        for label in predicted_labels:
            breeds = dataframe.loc[dataframe['group'] == label]
            breeds = breeds.sort_values('popularity', ascending=False)
            top_breeds = breeds.head(5)

            # Retrieve breed images from api-ninjas
            top_breeds['breed_image'] = top_breeds['breed'].apply(retrieve_breed_image)

            result['predictions'].append({
                'label': label,
                'top_breeds': top_breeds.to_dict(orient='records')
            })

        return jsonify(result)

    except Exception as e:
        error_json = {
            'status_code': 500,
            'message': 'Error occurred during prediction.',
            'error_details': str(e),
        }
        return jsonify(error_json), 500

def retrieve_breed_image(breed_name):
    api_url = 'https://api.api-ninjas.com/v1/dogs?name={}'.format(breed_name)
    response = requests.get(api_url, headers={'X-Api-Key': api_key})
    breed_data = response.json()
    if breed_data:
        breed_image_url = breed_data[0]['image_link']  # Use index [0] to access the first item in the list
        return breed_image_url
    return ''


if __name__ == '__main__':
    app.run(debug=True)

