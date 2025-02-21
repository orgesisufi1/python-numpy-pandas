from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from pydantic import BaseModel

app = FastAPI()


@app.exception_handler(404)
async def not_found_handler(request: Request, exception):
    return JSONResponse(status_code=404, content={"message": "Error 404! Does not exist!."},)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(status_code=422, content={"error": "Unprocessable Entity"},)

@app.get("/hello")
def hello():
    return {"Hello World"}

@app.get("/greet")
def greeting(name: str):
    return {"message": f"Hello {name}! It is nice to have you here!"}

@app.get("/people")
def check_adult(name: str, age: int):
    if age < 18:
        return {"result": name + " is not an adult!"}
    elif age >= 18:
        return {"result": name + " is an adult!"}

class Calculation(BaseModel):
    first_number: float
    second_number: float
    operation: str

@app.post("/calculation")
def calculate(calc: Calculation):
    if calc.operation not in ['+', '-', '*', '/']:
        raise HTTPException(status_code=400, detail="Invalid Operation! Please use only '+', '-', '*', or '/'.")
    try:
        if calc.operation == '+':
            result = calc.first_number + calc.second_number
        elif calc.operation == '-':
            result = calc.first_number - calc.second_number
        elif calc.operation == '*':
            result = calc.first_number * calc.second_number
        elif calc.operation == '/':
            if calc.second_number == 0:
                raise HTTPException(status_code=500, detail="Division by zero is not allowed!")
            result = calc.first_number / calc.second_number
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)
