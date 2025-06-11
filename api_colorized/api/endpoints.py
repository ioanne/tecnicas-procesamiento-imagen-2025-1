import numpy as np
import io

from fastapi import APIRouter, UploadFile, File, Form
from fastapi.responses import StreamingResponse

from PIL import Image
from sklearn.cluster import KMeans

from api.schemas import ReplacementRequest
from api.utils import rgb_to_hex


router = APIRouter()

@router.post("/colors")
async def extract_colors(image: UploadFile = File(...), n_colors: int = 10):
    img = Image.open(image.file).convert("RGB")
    pixels = np.array(img).reshape(-1, 3)

    # KMeans clustering to find dominant colors
    kmeans = KMeans(n_clusters=n_colors, random_state=0, n_init="auto")
    kmeans.fit(pixels)
    centroids = kmeans.cluster_centers_.astype(int)

    hex_colors = [rgb_to_hex(tuple(c)) for c in centroids]
    return {"detected_colors": hex_colors}


@router.post("/replace_colors")
async def replace_colors(
    image: UploadFile = File(...),
    replacements_json: str = Form(...)
):
    import json
    request_data = ReplacementRequest(**json.loads(replacements_json))

    img = Image.open(image.file).convert("RGB")
    array = np.array(img)

    for replacement in request_data.replacements:
        orig = np.array(replacement.original_color)
        new = np.array(replacement.new_color)

        if request_data.tolerance == 0:
            mask = np.all(array == orig, axis=-1)
        else:
            diff = np.abs(array - orig)
            mask = np.sum(diff, axis=-1) <= request_data.tolerance

        array[mask] = new

    modified_image = Image.fromarray(array)
    buffer = io.BytesIO()
    modified_image.save(buffer, format="PNG")
    buffer.seek(0)

    return StreamingResponse(buffer, media_type="image/png", headers={
        "Content-Disposition": f"attachment; filename={request_data.filename}"
    })
