from fastapi import APIRouter
from models.user import User
from config.db import conn 
from schemas.user import userEntity, usersEntity

user=APIRouter()

@user.get('/')
async def find_all_users():
    return usersEntity(conn.user.user_details.find())

@user.post('/')
async def create_users(user: User):
    conn.user.user_details.insert_one(dict(user))
    return usersEntity(conn.user.user_details.find())
