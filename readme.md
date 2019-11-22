```
vagrant up
vagrant ssh
```
Ставим нужные пакеты на виртуальную машину.
```
sudo apt install python3-pip
sudo apt install gunicorn
sudo pip3 install mlflow
git clone https://github.com/mlflow/mlflow.git
sudo mlflow server --host 192.168.33.11 
```
Результат будет доступен по адресу 192.168.33.11:5000.

В другой консоли запускаем наши эксперименты:
```
sudo python3 mlflow/examples/quickstart/mlflow_tracking.py
sudo pip3 install scikit-learn
sudo python3 mlflow/examples/sklearn_elasticnet_wine/train.py
```
Можно прямо в командной строке указывать параметры:
```
sudo python3 mlflow/examples/sklearn_elasticnet_wine/train.py <alpha> <l1_ratio>
sudo python3 example/main.py <test_size> <random_state>
```
