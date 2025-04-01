from fastapi import APIRouter, HTTPException
from models import Tarea
from database import tareas_collection
from bson import ObjectId

router = APIRouter()

@router.get("/tareas")
async def obtener_tareas():
    tareas = await tareas_collection.find().to_list(100)
    for tarea in tareas:
        tarea["_id"] = str(tarea["_id"])
    return tareas

@router.post("/tareas")
async def crear_tarea(tarea: Tarea):
    nueva_tarea = await tareas_collection.insert_one(tarea.dict())
    return {"id": str(nueva_tarea.inserted_id)}

@router.put("/tareas/{tarea_id}")
async def actualizar_tarea(tarea_id: str, tarea: Tarea):
    resultado = await tareas_collection.update_one({"_id": ObjectId(tarea_id)}, {"$set": tarea.dict()})
    if resultado.matched_count == 0:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return {"mensaje": "Tarea actualizada"}

@router.delete("/tareas/{tarea_id}")
async def eliminar_tarea(tarea_id: str):
    resultado = await tareas_collection.delete_one({"_id": ObjectId(tarea_id)})
    if resultado.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return {"mensaje": "Tarea eliminada"}
