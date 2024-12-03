from fastapi import FastAPI
from fastapi.responses import FileResponse
from routes.password_resets import password_reset
from routes.role_user import role_users
from routes.usuario_real import usuarios_real
from routes.user import user
app = FastAPI()
app.include_router(password_reset)
app.include_router(role_users)
app.include_router(user)
app.include_router(usuarios_real)
@app.get("/actualizar", response_class=FileResponse)
async def get_form():
    return FileResponse("static/index.html") 
@app.get("/login", response_class=FileResponse)
async def get_form():
    return FileResponse("static/login.html") 
@app.get("/crear", response_class=FileResponse)
async def get_form():
    return FileResponse("static/update.html") 
@app.get("/listar", response_class=FileResponse)
async def get_form():
    return FileResponse("static/lista.html") 