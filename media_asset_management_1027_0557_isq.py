# 代码生成时间: 2025-10-27 05:57:46
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route
from starlette.status import HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR
import uvicorn
from typing import Dict, Any


# This is a class representing a Media Asset
class MediaAsset:
    def __init__(self, id: str, name: str, file_path: str):
        self.id = id
        self.name = name
        self.file_path = file_path

    def to_dict(self) -> Dict[str, Any]:
        return {"id": self.id, "name": self.name, "file_path": self.file_path}


# This is a simple in-memory storage for media assets
class MediaAssetStorage:
    def __init__(self):
        self.assets = {}

    def add(self, asset: MediaAsset):
        self.assets[asset.id] = asset

    def get(self, asset_id: str) -> MediaAsset:
        if asset_id in self.assets:
            return self.assets[asset_id]
        else:
            raise ValueError(f"Asset with ID {asset_id} not found")

    def remove(self, asset_id: str):
        if asset_id in self.assets:
            del self.assets[asset_id]
        else:
            raise ValueError(f"Asset with ID {asset_id} not found")


# Define the routes for the media asset management API
def get_asset(request):
    asset_id = request.path_params['id']
    try:
        asset = media_asset_storage.get(asset_id)
        return JSONResponse(status_code=200, content=asset.to_dict())
    except ValueError as e:
        return JSONResponse(status_code=404, content={"error": str(e)})


def create_asset(request):
    data = request.json()
    try:
        asset = MediaAsset(data['id'], data['name'], data['file_path'])
        media_asset_storage.add(asset)
        return JSONResponse(status_code=201, content=asset.to_dict())
    except KeyError as e:
        return JSONResponse(status_code=400, content={"error": f"Missing data: {str(e)}"})


def delete_asset(request):
    asset_id = request.path_params['id']
    try:
        media_asset_storage.remove(asset_id)
        return JSONResponse(status_code=204)
    except ValueError as e:
        return JSONResponse(status_code=404, content={"error": str(e)})


# Initialize the media asset storage
media_asset_storage = MediaAssetStorage()

# Create the Starlette application
app = Starlette(debug=True, routes=[
    Route("/assets/{id}", get_asset, methods=["GET"]),
    Route("/assets", create_asset, methods=["POST"]),
    Route("/assets/{id}", delete_asset, methods=["DELETE"]),
])

# Run the application using Uvicorn
if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)

# Documentation for the Media Asset Management API:
# - GET    /assets/{id}     Retrieve a specific media asset
# - POST   /assets         Create a new media asset
# - DELETE /assets/{id}    Delete a specific media asset
