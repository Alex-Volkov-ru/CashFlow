from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

class MonopolyGame:
    def __init__(self):
        self.players = []
        self.properties = {
            "Park Place": {"owner": None, "price": 200},
            "Boardwalk": {"owner": None, "price": 400}
        }

monopoly_game = MonopolyGame()

@app.post("/join_game/{player_name}")
def join_game(player_name: str):
    monopoly_game.players.append(player_name)
    return {"message": f"{player_name} joined the game"}

@app.get("/roll_dice/{player_name}")
def roll_dice(player_name: str):

    return {"message": f"{player_name} rolled the dice"}

@app.post("/buy_property/{player_name}/{property_name}")
def buy_property(player_name: str, property_name: str):
    if monopoly_game.properties[property_name]["owner"] is None:
        monopoly_game.properties[property_name]["owner"] = player_name
        return {"message": f"{player_name} bought {property_name}"}
    else:
        return {"message": f"{property_name} is already owned by {monopoly_game.properties[property_name]['owner']}"}

@app.get("/")
async def read_root():
    return FileResponse("static/monopoly_board.png")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)