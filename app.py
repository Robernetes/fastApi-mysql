from fastapi import FastAPI
from routes.user import user

# QUEDE EN EL MINUTO 38 EN ROUT USER FUNCION CREAR

app = FastAPI()

app.include_router(user)




