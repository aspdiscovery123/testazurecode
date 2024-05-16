
from flask import Flask, request



import joblib

model=joblib.load(r"ccpp_model.pkl")

app=Flask(__name__)

@app.route('/',methods=["POST"])

def predict():
    data=request.get_json(force=True)
    print(data)
    data=data["data"]
    print(data)
    out=model.predict([data])
    print(out)
    return str(out)

app.run(host='0.0.0.0',port=5002)
