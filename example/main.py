# make predictions
from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
from mlflow import log_metric, log_param, log_artifacts, start_run
import os
import sys

# Load dataset
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = read_csv(url, names=names)

with start_run():
	# Split-out validation dataset
	array = dataset.values
	X = array[:,0:4]
	y = array[:,4]
	test_s = float(sys.argv[1]) if len(sys.argv) > 1 else 0.20
	random_s = int(sys.argv[2]) if len(sys.argv) > 2 else 1
	log_param("test_size", test_s)
	log_param("random_state", random_s)
	X_train, X_validation, Y_train, Y_validation = train_test_split(X, y, test_size=test_s, random_state=random_s)

	# Make predictions on validation dataset
	model = SVC(gamma='auto')
	model.fit(X_train, Y_train)
	predictions = model.predict(X_validation)

	# Evaluate predictions
	score = accuracy_score(Y_validation, predictions)
	print(score)
	log_metric("accuracy_score", score)

	c_report = classification_report(Y_validation, predictions)
	print(c_report)

	if not os.path.exists("iris_outputs"):
		os.makedirs("iris_outputs")

	with open("iris_outputs/classification_report.txt", "w") as f:
		f.write(c_report)

	log_artifacts("iris_outputs")


