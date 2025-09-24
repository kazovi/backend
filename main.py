from fastapi import FastAPI

app = FastAPI()  # create the app

@app.get("/")
def hello():
    return {"msg": "hello hi"}  # return a dictionary (JSON response)
