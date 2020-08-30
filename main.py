from typing import Optional

from fastapi import FastAPI, HTTPException, Response
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from db.EmployeeRepository import EmployeeRepository
from models.Employee import EmployeeRepository

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None


class Message(BaseModel):
    message: str


@app.get("/")
def read_root():
    return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
#     if item_id not in [1, 2, 3, 4, 5]:
#         raise HTTPException(status_code=400, detail="item_id invalid")
#     return {"item_id": item_id, "q": q}
#
#
# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item, response_model=Item, responses={404: {"model": Message}}):
#     if item_id not in [1, 2, 3, 4, 5]:
#         return JSONResponse(status_code=404, content={"message": "Item not found"})
#     return {"item_name": item.name, "item_id": item_id,
#             "item_price": item.price * 100, "is_offer": item.is_offer}


@app.get("/items/{item_id}", response_model=Item, responses={404: {"model": Message,
                                                                   "description": "he resource was not found"},
                                                             400: {"model": Message}})
async def read_item(item_id: str):
    if item_id == "foo":
        return {"name": "foo", "value": "there goes my hero", "price": 13.2}
    elif item_id == "bar":
        return JSONResponse(status_code=400, content={"message": "Invalid itemId in request"})
    else:
        return JSONResponse(status_code=404, content={"message": "Item not found"})


@app.post("/employee/", response_model=EmployeeRepository)
async def add_employee(employee: EmployeeRepository):
    EmployeeRepository.create(employee)
    return employee
