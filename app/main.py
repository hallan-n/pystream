import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from infra.routes.login_route import login
from infra.routes.plan_route import plan

load_dotenv()
app = FastAPI()

app.include_router(login)
app.include_router(plan)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
