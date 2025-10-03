# 代码生成时间: 2025-10-04 02:46:24
import starlette.applications
import starlette.requests
import starlette.responses
import starlette.routing
import starlette.status
from starlette.exceptions import HTTPException as StarletteHTTPException

"""
Physics Engine API using Starlette framework.
This application creates a simple physics engine that
responds to HTTP requests with physical calculations.
"""

# Define a basic physics engine class
class PhysicsEngine:
    def __init__(self):
        self.data = {}

    def calculate_force(self, mass, acceleration):
        """Calculate the force based on mass and acceleration."""
        if mass <= 0 or acceleration <= 0:
            raise ValueError("Mass and acceleration must be positive.")
        return mass * acceleration

    def calculate_distance(self, initial_velocity, time, acceleration):
        """Calculate the distance based on initial velocity, time, and acceleration."""
        if initial_velocity < 0 or time <= 0 or acceleration <= 0:
            raise ValueError("Initial velocity, time, and acceleration must be positive.")
        return initial_velocity * time + 0.5 * acceleration * time ** 2

# Create a Starlette application with routes
class PhysicsApp(starlette.applications.Starlette):
    def __init__(self, debug: bool = False):
        super().__init__(debug)
        self.engine = PhysicsEngine()
        routes = [
            starlette.routing.Route(
                handler=self.calculate_force_handler,
                path="/force",
                methods=["POST"],
            ),
            starlette.routing.Route(
                handler=self.calculate_distance_handler,
                path="/distance",
                methods=["POST"],
            ),
        ]
        self.routes = routes

    def calculate_force_handler(self, request: starlette.requests.Request):
        """Handle POST requests to calculate force."""
        try:
            data = request.json()
            mass = data.get("mass", 0)
            acceleration = data.get("acceleration", 0)
            force = self.engine.calculate_force(mass, acceleration)
            return starlette.responses.JSONResponse({"force": force})
        except ValueError as e:
            raise StarletteHTTPException(status_code=starlette.status.HTTP_400_BAD_REQUEST, detail=str(e))
        except Exception as e:
            raise StarletteHTTPException(status_code=starlette.status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    def calculate_distance_handler(self, request: starlette.requests.Request):
        """Handle POST requests to calculate distance."""
        try:
            data = request.json()
            initial_velocity = data.get("initial_velocity", 0)
            time = data.get("time", 0)
            acceleration = data.get("acceleration", 0)
            distance = self.engine.calculate_distance(initial_velocity, time, acceleration)
            return starlette.responses.JSONResponse({"distance": distance})
        except ValueError as e:
            raise StarletteHTTPException(status_code=starlette.status.HTTP_400_BAD_REQUEST, detail=str(e))
        except Exception as e:
            raise StarletteHTTPException(status_code=starlette.status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

# Entry point for the application
def main():
    app = PhysicsApp(debug=True)
    app.run(port=8000)

if __name__ == "__main__":
    main()