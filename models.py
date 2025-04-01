from pydantic import BaseModel
from typing import Optional

class Tarea(BaseModel):
    titulo: str
    descripcion: str
    estado: str  # "por hacer", "en progreso", "completada"
