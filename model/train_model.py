import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# simple dataset
data = {
    "hours": [1,2,3,4,5],
    "score": [50,55,65,70,80]
}

df = pd.DataFrame(data)

X = df[["hours"]]
y = df["score"]

model = LinearRegression()
model.fit(X, y)

# save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved")