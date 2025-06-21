curl -X POST https://bike-app-model-558367849711.southamerica-east1.run.app/predict \
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