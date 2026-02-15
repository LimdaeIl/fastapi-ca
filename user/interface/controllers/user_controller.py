from fastapi import APIRouter
from pydantic import BaseModel

from user.application.user_service import UserService

router = APIRouter(prefix="/users")


class CreateUserBody(BaseModel):
  name: str
  email: str
  password: str


@router.post("", status_code=201)
def crate_user(user: CreateUserBody):
  user_service = UserService()
  crated_user = user_service.create_user(
      name=user.name,
      email=user.email,
      password=user.password
  )

  return crated_user
