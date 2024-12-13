import pytest
from httpx import AsyncClient, ASGITransport
from books_library.main import app

import asyncio


@pytest.fixture(scope="session")
def event_loop(request):
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.mark.anyio
async def test_get_authors():
    async with AsyncClient(
            transport=ASGITransport(app=app), base_url="http://test"
    ) as client:
        response = await client.get("/authors")
    assert response.status_code == 200


@pytest.mark.anyio
async def test_get_books():
    async with AsyncClient(
            transport=ASGITransport(app=app), base_url="http://test"
    ) as client:
        response = await client.get("/books")
    assert response.status_code == 200


@pytest.mark.anyio
@pytest.mark.parametrize("id, status_code", [
    (1, 200),
    (0, 404),
    (-1, 404),
], )
async def test_get_authors_id(id, status_code):
    async with AsyncClient(
            transport=ASGITransport(app=app), base_url="http://test"
    ) as client:
        response = await client.get(f"/authors/{id}")
        assert response.status_code == status_code


@pytest.mark.anyio
async def test_get_books():
    async with AsyncClient(
            transport=ASGITransport(app=app), base_url="http://test"
    ) as client:
        response = await client.get("/books")
    assert response.status_code == 200


@pytest.mark.anyio
@pytest.mark.parametrize("id, status_code", [
    (1, 200),
    (0, 404),
    (-1, 404),

], )
async def test_get_books_id(id, status_code):
    async with AsyncClient(
            transport=ASGITransport(app=app), base_url="http://test"
    ) as client:
        response = await client.get(f"/books/{id}")
        assert response.status_code == status_code


@pytest.mark.anyio
async def test_get_borrows():
    async with AsyncClient(
            transport=ASGITransport(app=app), base_url="http://test"
    ) as client:
        response = await client.get("/borrows")
    assert response.status_code == 200


@pytest.mark.anyio
@pytest.mark.parametrize("id, status_code", [
    (1, 200),
    (0, 409),
    (-1, 409),

], )
async def test_get_borrows_id(id, status_code):
    async with AsyncClient(
            transport=ASGITransport(app=app), base_url="http://test"
    ) as client:
        response = await client.get(f"/borrows/{id}")
        assert response.status_code == status_code
