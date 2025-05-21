from fastapi import FastAPI, UploadFile, File, Form

from app.routers import usuarios, alumnos


app = FastAPI() # Intanciamos FastAPI

app.include_router(usuarios.router, prefix="/usuarios", tags=["usuarios"])
app.include_router(alumnos.router, prefix="/alumnos", tags=["alumnos"])


@app.get("/")
async def hola_mundo():
    return {"mensaje":"Hola mundo!"}


@app.post("/subir_imagen")
async def subir_imagen(nombre: str = Form(...), imagen: UploadFile = File(...)):
    contenido = await imagen.read()
    
    with open(f"{nombre}_{imagen.filename}", "wb") as f:
        # Lo que quiera con el archivo abierto
        f.write(contenido)
    # Se cierra el archivo.
    
    return {"mensaje": "Imagen subida exitosamente"}
