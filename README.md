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

    git clone https://github.com/your-username/dog-breed-prediction-api.git
    cd dog-breed-prediction
   
2\. Start the API server:
    
    
    python app.py
    

3\. Make a POST request to the API endpoint with the dog's characteristics:
   ```
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

Machine Learning Architecture
=============================

The Dog Breed Prediction API project utilizes a machine learning model to predict the breed of a dog based on its characteristics. Here is an overview of the machine learning architecture used in the project:

Model Architecture
------------------

The machine learning model employed in this project is a deep learning model built using TensorFlow. The model architecture consists of the following layers:

-   Input Layer: This layer takes in the input features of the dog, including characteristics such as trainability, energy level, shedding, grooming frequency, temperament, weight, height, and demeanor.

-   Embedding Layer: The categorical features are passed through embedding layers to convert them into continuous numerical representations. This process helps the model learn meaningful representations of the categorical variables.

-   Dense Layers: The embedded features are then passed through multiple dense layers. These layers consist of neurons that perform mathematical operations to learn patterns and relationships in the data.

-   Output Layer: The final dense layer produces the predictions. In this case, the output layer predicts the probability distribution over different dog breed categories.

-   Activation Function: The activation function used in the intermediate dense layers is the Rectified Linear Unit (ReLU), which introduces non-linearity into the model. The output layer uses the Softmax activation function to convert the model's raw outputs into probability values.

-   Loss Function: The model is trained using the categorical cross-entropy loss function, which measures the difference between the predicted probability distribution and the true distribution of the dog breeds.

-   Optimization Algorithm: The Adam optimizer is used to optimize the model's weights and biases during the training process. It adapts the learning rate dynamically based on the gradients computed during training.

Data Preparation
----------------

The training data for the model consists of a dataset of dog characteristics and their corresponding breed labels. The data is preprocessed before training the model. The preprocessing steps include:

-   Categorical Encoding: The categorical features are encoded using one-hot encoding or label encoding techniques. This process converts the categorical variables into a numerical representation that can be understood by the model.

-   Data Split: The dataset is split into training and validation sets. The training set is used to train the model, while the validation set is used to evaluate the model's performance during training and make adjustments if needed.

Training and Evaluation
-----------------------

The model is trained using the training dataset and evaluated on the validation dataset. The training process involves iterating over the dataset multiple times (epochs) and updating the model's parameters based on the computed gradients and the optimization algorithm. The model's performance is evaluated based on metrics such as accuracy, precision, recall, and F1 score. The training process continues until the model converges or reaches a specified number of epochs.

Prediction
----------

Once the model is trained, it can be used to make predictions on new, unseen dog characteristics. The API takes in the dog's characteristics as input and passes them through the trained model to obtain the predicted breed probabilities. The breed with the highest probability is then selected as the predicted breed.


- `model/model.h5`: The pre-trained machine learning model for breed prediction.

- `data/akc-data-latest-final.csv`: The CSV file containing the dog breed data.

- `requirements.txt`: The list of Python dependencies required for the project.

- `README.md`: This README file providing information about the project.

Feel free to modify and customize the project according to your needs.
