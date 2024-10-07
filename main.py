from fastapi import FastAPI, Response, HTTPException, Depends
from fastapi.security import HTTPBearer

from config import settings
from status import status as status

app = FastAPI()
current_status = 200
security = HTTPBearer()


def checktokendependencies(token: HTTPBearer = Depends(security)):
    if token.credentials != settings.SECRET_KEY:
        raise HTTPException(status_code=403, detail="Forbidden")
    return


@app.get("/healthcheck")
def healthcheck(response: Response):
    response.status_code = current_status
    return {"status": current_status,
            "description": status[current_status]}


@app.post("/healthcheck")
def set_healthcheck_status(status_code: int, token=Depends(checktokendependencies)):
    global current_status
    current_status = status_code
    return {"status": current_status,
            "description": status[current_status]}
