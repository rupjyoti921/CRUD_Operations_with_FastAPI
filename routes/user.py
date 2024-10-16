from fastapi import APIRouter
from models.user import User
from config.db import conn 
from schemas.user import userEntity, usersEntity

user=APIRouter()

@user.get('/')
async def find_all_users():
    print(conn.user.user_details.find())
    print(usersEntity(conn.user.user_details.find()))
    return usersEntity(conn.user.user_details.find())
