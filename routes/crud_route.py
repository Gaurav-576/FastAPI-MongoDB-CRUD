from fastapi import APIRouter
from models.questions import Question
from config.database import collection_name
from schema.schemas import list_serial
from models.questions import Question
from bson import ObjectId

router=APIRouter()

@router.post("/")
async def create(question: Question):
  collection_name.insert_one(dict(question))
  return "Question added successfully"

@router.get("/")
async def read():
  questions=collection_name.find()
  return list_serial(questions)

@router.put("/{id}")
async def update(id: str,question: Question):
  collection_name.find_one_and_update({"_id": question(id)}, {"$set": dict(question)})
  
@router.delete("/{id}")
async def delete(id: str):
  collection_name.find_one_and_delete({"_id": ObjectId(id)})