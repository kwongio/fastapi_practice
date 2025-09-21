import logging

from fastapi import FastAPI, Depends
from app.web import explorer, creature
from elasticapm.contrib.starlette import make_apm_client, ElasticAPM

from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("fastapi")

app = FastAPI()
basic = HTTPBasic()

app.include_router(explorer.router)
app.include_router(creature.router)

apm_config = {
    "SERVICE_NAME": "fastapi-app",
    "SERVER_URL": "http://localhost:8200",
}
apm = make_apm_client(apm_config)
app.add_middleware(ElasticAPM, client=apm)


@app.get("/who")
def get_user(credentials: HTTPBasicCredentials = Depends(basic)):
    logger.info("username: %s", credentials.username)
    return {"username": credentials.username, "password": credentials.password}


@app.get("/")
def main() -> dict[str, str]:
    return {"msg": "Hello World"}
