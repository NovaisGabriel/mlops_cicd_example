# docker build -t bike_app_model
# gsutil iam ch "user:gabrieel.novais@gmail.com:roles/storage.admin" gs://data-bikes-uci-example/
# gsutil acl ch -u allUsers:R gs://data-bikes-uci-example
curl -X POST http://127.0.0.1:5051/predict \
-H "Content-Type: application/json" \
-d '{
     "holiday": 0,
     "weekday": 6,
     "workingday": 0,
     "weathersit": 2,
     "temp": 0.344167,
     "atemp": 0.363625,
     "hum": 0.805833,
     "windspeed": 0.160446,
     "casual": 331,
     "registered": 654
}'