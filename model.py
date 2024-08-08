import joblib
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

iris = load_iris()

x, y = iris.data, iris.target

model = RandomForestClassifier()
model.fit(x,y)

joblib.dump(model, 'model.joblib')