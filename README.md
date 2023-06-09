# Dog Breed Prediction

This is a repository for machine learning models of dog breed prediction based on features selected by the user. For dataset sources we use csv type datasets obtained from https://github.com/tmfilho/akcdata/blob/master/data/akc-data-latest.csv
We use the dataset and make modifications according to what we need.

This is a machine learning model and simple API for predicting the breed of a dog based on its characteristics. It uses a CNN to make predictions.

## Requirements

Make sure you have the following dependencies installed:

- Python (version >= 3.6)

- Flask (version >= 2.0.1)

- TensorFlow (version >= 2.6.0)

- pandas (version >= 1.3.3)

- numpy (version >= 1.21.2)

- scikit-learn (version >= 0.24.2)

You can install the dependencies by running the following command:

```shell

pip install -r requirements.txt

```

## Usage

1\. Clone the repository:

   ```shell

   git clone https://github.com/your-username/dog-breed-prediction-api.git

   cd dog-breed-prediction

   ```
   
2\. Start the API server:

   ```shell

   python app.py

   ```

3\. Make a POST request to the API endpoint with the dog's characteristics:

   ```shell

   curl -X POST -H "Content-Type: application/json" -d '{"trainability_category": ["Reserved with Strangers"], "energy_level_category": ["Needs Lots of Activity"], "shedding_category": ["Occasional"], "grooming_frequency_category": ["Weekly"], "temperament_category": ["Active"], "weight_category": ["Medium"], "height_category": ["Medium"], "demeanor_category": ["Eager to Please"]}' http://localhost:5000/predict

   ```

   Adjust the characteristics in the request payload to match the dog's attributes.

4\. The API will respond with a JSON object containing the predicted breed and additional information if available.

## API Endpoint

- **URL**: `/predict`

- **Method**: POST

- **Request Body**: JSON object containing the dog's characteristics

- **Response**: JSON object containing the predicted breed and additional information

## Project Structure

- `app.py`: The main Flask application file that defines the API endpoints and handles the prediction logic.

- `model/model.h5`: The pre-trained machine learning model for breed prediction.

- `data/akc-data-latest-final.csv`: The CSV file containing the dog breed data.

- `requirements.txt`: The list of Python dependencies required for the project.

- `README.md`: This README file providing information about the project.

Feel free to modify and customize the project according to your needs.
