from fastapi import APIRouter, Depends, Form, HTTPException, Path
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app1.core.config import DBConfigurer
from app1.api.v1.users import crud as users_crud
from app1.api.v1.users.schemas import UserRead, UserCreate
from app1.core import errors

router = APIRouter()


@router.get("/")
async def users_root():
    return {
        f"Users root"
    }


@router.get(
    "/users/",
    response_model=list[UserRead],
)
async def get_users(
    session: AsyncSession = Depends(DBConfigurer.session_getter)
):
    return await users_crud.get_users(
        session=session
    )


@router.get(
    "/users/user_by_name/",
    response_model=UserRead,
)
async def get_user_by_name(
    username: str,
    session: AsyncSession = Depends(DBConfigurer.session_getter),
):
    return await users_crud.get_user_by_name(
        session=session,
        username=username,
    )


@router.get(
    "/users/{user_id}/",
    response_model=UserRead,
)
async def get_user_by_id(
    user_id: int,
    session: AsyncSession = Depends(DBConfigurer.session_getter),
):
    return await users_crud.get_user_by_id(
        session=session,
        user_id=user_id,
    )


@router.post(
    "/users/",
    response_model=UserRead,
    status_code=status.HTTP_201_CREATED
)
async def create_user(
    user: UserCreate = Form(),
    session: AsyncSession = Depends(DBConfigurer.session_getter),
):
    # try:
    return await users_crud.create_user(
        session=session,
        instance=user,
    )
    # except errors.Validation as error:
    #     raise HTTPException(
    #         status_code=status.HTTP_400_BAD_REQUEST,
    #         detail=error.msg
    #     )
