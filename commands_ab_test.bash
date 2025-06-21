# local

docker build -t bike_app_model:v2 .

docker tag bike_app_model:v2 gcr.io/mlops-cicd-example-463613/bike_app_model:v2

docker push gcr.io/mlops-cicd-example-463613/bike_app_model:v2

# online

gcloud run deploy bike_app_model --image gcr.io/mlops-cicd-example-463613/bike_app_model:v2 --region southamerica-east1

gcloud run revisions list --service bike_app_model --region southamerica-east1

glcoud run services update-traffic bike_app_model --to-revisions=version1=90,version2=10 --region southamerica-east1