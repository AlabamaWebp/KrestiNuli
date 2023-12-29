from fastapi import FastAPI

game = FastAPI()


@game.get("/get_full_data")
def get_full_data():
    return "Твоя функция"
