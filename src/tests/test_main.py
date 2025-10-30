import pytest
from httpx import AsyncClient
from .main import app  # src klasöründeki app'i import ediyoruz

@pytest.mark.asyncio
async def test_read_root():
    """
    Kök endpoint'in doğru mesajı ve 200 OK durum kodunu döndürdüğünü test eder.
    """
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/")
    
    assert response.status_code == 200
    assert response.json() == {"mesaj": "Merhaba AICRA!"}
