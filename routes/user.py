from fastapi import APIRouter
from models.user import User
from config.db import conn 
from schemas.user import userEntity, usersEntity
from bson import ObjectId

user=APIRouter()

#Read Data
@user.get('/')
async def find_all_users():
    return usersEntity(conn.user.user_details.find())

#Read by ID
@user.get('/{id}')
async def find_user_by_id(id):
    return userEntity(conn.user.user_details.find_one({"_id":ObjectId(id)}))

#Create Data
@user.post('/')
async def create_users(user: User):
    conn.user.user_details.insert_one(dict(user))
    return usersEntity(conn.user.user_details.find())

#Update Data
@user.put('/{id}') 
async def update_users(id,user: User):
    conn.user.user_details.find_one_and_update({"_id":ObjectId(id)},{"$set":dict(user)})
    return userEntity(conn.user.user_details.find_one({"_id":ObjectId(id)}))

#Delete Data
@user.delete('/{id}') 
async def delete_users(id):
    # conn.user.user_details.find_one_and_delete({"_id":ObjectId(id)})
    # return {"msg":"Success Deletion"}
    return userEntity(conn.user.user_details.find_one_and_delete({"_id":ObjectId(id)}))
    