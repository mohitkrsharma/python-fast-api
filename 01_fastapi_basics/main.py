from fastapi import FastAPI

# create app instance
app = FastAPI()

# Home Route
@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI, Mohit!"}

@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello {name}!"}