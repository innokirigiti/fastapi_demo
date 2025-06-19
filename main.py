from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def ujumbe():
    return {"Ujumbe":"Habari Dunia!"}
