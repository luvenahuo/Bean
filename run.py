import os

os.system('export GOOGLE_APPLICATION_CREDENTIALS="service.json"')
project_id = 'pennapps-252204'
compute_region = 'us-central1'
model_id = 'untitled_1567868172858'
file_path = 'test.png'
score_threshold = u'0.4'

from google.cloud import automl_v1beta1 as automl

automl_client = automl.AutoMlClient()

# Get the full path of the model.
model_full_id = automl_client.model_path(project_id, compute_region, model_id)

# Create client for prediction service.
prediction_client = automl.PredictionServiceClient()

# Read the image and assign to payload.
with open(file_path, "rb") as image_file:
    content = image_file.read()
payload = {"image": {"image_bytes": content}}

params = {}
if score_threshold:
    params = {"score_threshold": score_threshold}

print(model_full_id)
print(params)
response = prediction_client.predict(model_full_id, payload, params)
print("Prediction results:")
for result in response.payload:
    print("Predicted class name: {}".format(result.display_name))
    print("Predicted class score: {}".format(result.classification.score))

