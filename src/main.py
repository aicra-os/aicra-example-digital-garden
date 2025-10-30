from fastapi import FastAPI

app = FastAPI(
    title="Dijital Bahçe API",
    description="AICRA standardı ile geliştirilen örnek proje.",
    version="1.0.0",
)

@app.get("/")
def read_root():
    """
    API'nin çalıştığını doğrulayan basit bir 'Merhaba Dünya' endpoint'i.
    """
    return {"mesaj": "Merhaba AICRA!"}
