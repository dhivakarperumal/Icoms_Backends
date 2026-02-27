from fastapi import FastAPI

# create the FastAPI application instance
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome all to the FastAPI backend!"}