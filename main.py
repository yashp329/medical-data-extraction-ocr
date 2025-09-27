from fastapi import FastAPI
from enum import Enum

app = FastAPI()

# Our mock database
food_items = {
    "indian": ["Samosa", "Dosa"],
    "american": ["Hot Dog", "Apple Pie"],
    "italian": ["Pizza", "Burger"]
}

@app.get("/hello/{name}")
async def hello(name: str):
    return {"message": f"Welcome to FastAPI Tutorial, {name}!!"}


# Use Enum to restrict cuisine values
class AvailableCuisine(str, Enum):
    indian = "indian"
    american = "american"
    italian = "italian"

@app.get("/get_items/{cuisine}")
async def get_items(cuisine: AvailableCuisine):
    return {"cuisine": cuisine, "items": food_items[cuisine]}
