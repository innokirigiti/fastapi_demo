from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def ujumbe():
    return {"Ujumbe":"Habari Dunia!"}

@app.get("/habari")
def ujumbe(jina:str):
    return {"Ujumbe":f"Habari {jina}!"}
