from fastapi import FastAPI
from routes import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Permitir peticiones desde el frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Permite solicitudes desde tu frontend
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos HTTP (GET, POST, DELETE, etc.)
    allow_headers=["*"],  # Permite todos los encabezados
)
@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API de gestión de tareas"}

app.include_router(router)
