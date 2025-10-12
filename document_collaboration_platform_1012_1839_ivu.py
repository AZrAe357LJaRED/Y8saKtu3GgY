# 代码生成时间: 2025-10-12 18:39:40
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route
from starlette.exceptions import HTTPException as StarletteHTTPException
def error_handler(exc, request):
    # Error handler for Starlette exceptions
    return JSONResponse(
        {
            'errors': [
                {
                    'message': exc.detail['message'],
                    'type': exc.detail['type'],
                    'status': str(exc.status_code)
                }
            ]
        },
        status_code=exc.status_code
    )

async def index(request):
    # The main endpoint for the document collaboration platform
    return JSONResponse({'message': 'Welcome to the Document Collaboration Platform'})

# Define routes for the application
routes = [
    Route('/', index),
]

# Create the application instance with the defined routes and error handler
app = Starlette(
    routes=routes,
    exception_handlers={404: error_handler},
    # Enable JSON responses by default
    debug=True
)

# Run the application with Uvicorn, the ASGI server
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
