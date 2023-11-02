import sys
import pandas as pd
import requests
import json

# Data readout
if len(sys.argv) != 5:
    raise TypeError(
        "Syntax should be:\n"
        "dplot_client.py file.csv regions_col feature_col port"
        )
file, regions, feature, port = sys.argv[1:]
df = pd.read_csv(file)
data = json.dumps(
    {'region': df[regions].to_list(), str(feature): df[feature].to_list()})
   
# POST request to the local server, the endpoint 'plot'
url = 'http://localhost:' + str(port) + '/plot'
r = requests.post(url, json=data)
    
# Response processing
print('Status code: {}'.format(r.status_code))
if r.status_code == 200:
    print('Data have been sent')
else:
    print(r.text)
    
import requests
import json

 

if __name__ == '__main__':
    
    # выполняем POST-запрос на сервер по эндпоинту add с параметром json
    r = requests.post('http://localhost:5000/predict', json=['168811', '28222.4' ,'0.000044', '1.73', '678764', '5.68', '11.74', '216128.2', 
     '19.050', '8.175', '17.775', '483.14', '16.28', '0.0003', '0.010295', '2.19', '41.2', '3895.8', 
     '799.6', '71637.4', '16.4'])
    # выводим статус запроса
    print('Status code: {}'.format(r.status_code))
    # реализуем обработку результата
    if r.status_code == 200:
        # если запрос выполнен успешно (код обработки=200),
        # выводим результат на экран
        print('Prediction: {}'.format(r.json()['prediction']))
    else:
        # если запрос завершён с кодом, отличным от 200,
        # выводим содержимое ответа
        print(r.text)