import httpx
from fastapi import APIRouter, HTTPException

from backend.config import settings

github_router = APIRouter(prefix='/github', tags=['Github'])


@github_router.get("/{username}")
async def get_followers(username: str):
    """
    Получает список фолловеров пользователя с помощью GitHub API.
    """
    token = settings.GITHUB_API_TOKEN
    headers = {
        "authorization": f"token {token}"
    } if token else {}

    url = f"https://api.github.com/users/{username}/followers"

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=headers)

        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            raise HTTPException(status_code=404, detail="User not found")
        elif response.status_code == 401:
            raise HTTPException(status_code=401, detail="Invalid authorization token")
        else:
            raise HTTPException(status_code=response.status_code, detail=response.json())
    except httpx.RequestError as e:
        raise HTTPException(status_code=500, detail=f"An error occurred while connecting to GitHub: {str(e)}")


@github_router.get("/social_graph/{username}")
async def get_social_graph(username: str, depth: int = 1):
    """
    Построение социального графа фолловеров GitHub.
    :param username: Имя пользователя на GitHub.
    :param depth: Глубина построения графа (по умолчанию 1 уровень).
    """
    token = settings.GITHUB_API_TOKEN
    headers = {
        "authorization": f"token {token}"
    } if token else {}

    async def fetch_followers(user: str, current_depth: int):
        if current_depth > depth:
            return []

        url = f"https://api.github.com/users/{user}/followers"
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=headers)

        if response.status_code == 200:
            followers = response.json()
            result = []

            for follower in followers:
                follower_data = {
                    "login": follower["login"],
                    "avatar_url": follower["avatar_url"],
                    "followers": await fetch_followers(follower["login"], current_depth + 1)
                }
                result.append(follower_data)

            return result
        elif response.status_code == 404:
            raise HTTPException(status_code=404, detail=f"User '{user}' not found")
        elif response.status_code == 401:
            raise HTTPException(status_code=401, detail="Invalid authorization token")
        else:
            raise HTTPException(status_code=response.status_code, detail=response.json())

    return await fetch_followers(username, 1)


@github_router.get("/hello/{name}")
async def say_hello(name: str):
    """
    Эндпоинт для проверки сервера.
    """
    return {"message": f"Hello {name}"}
