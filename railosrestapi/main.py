import fastapi
import railosrestapi.database

app = fastapi.FastAPI()

@app.get("/")
async def api_root():
    pass


@app.get("/trainset")
async def query_trainset_database(name_string: str, country_code: str):
    with railosrestapi.database.RailOSDatabase() as trainset:
        return trainset.get_train(name_string, country_code)

