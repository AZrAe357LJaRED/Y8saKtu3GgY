# 代码生成时间: 2025-10-20 00:54:54
import psutil
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route

"""
CPU Usage Analyzer using Starlette framework.
This application retrieves the current CPU usage and provides it as a JSON response.
"""

class CPUUsageAnalyzer:
    def __init__(self):
        self.cpu_usage = psutil.cpu_percent(interval=1)

    def get_cpu_usage(self):
        """
        Returns the current CPU usage as a percentage.
        """
        try:
            # Get the current CPU usage
            return psutil.cpu_percent()
        except Exception as e:
            # Handle any exceptions that may occur and return an error message
            return {"error": str(e)}

    def get(self, request):
        """
        Handle GET request to retrieve CPU usage.
        """
        return JSONResponse(content=self.get_cpu_usage(), media_type='application/json')

# Create an instance of the CPUUsageAnalyzer class
cpu_usage_analyzer = CPUUsageAnalyzer()

# Define the routes for the Starlette application
routes = [
    Route("/cpu_usage", endpoint=cpu_usage_analyzer.get, methods=["GET"]),
]

# Create the Starlette application
app = Starlette(debug=True, routes=routes)

if __name__ == "__main__":
    # Run the application
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)