# 代码生成时间: 2025-10-14 21:39:33
import starlette.requests
import starlette.responses
import starlette.routing
from starlette import status
from starlette.endpoints import HTTPEndpoint
from starlette.types import Receive, Scope, Send
import requests
import json

# 微服务通信中间件
class MicroserviceMiddleware(HTTPEndpoint):
    def __init__(self, services):
        """
        :param services: 一个字典，包含服务名称和URL
        """
        self.services = services

    async def post(self, request: starlette.requests.Request) -> starlette.responses.Response:
        """
        处理入站请求，将请求转发到指定的微服务
        :param request: 入站请求对象
        :return: 微服务响应
        """
        try:
            service_name = request.headers.get('X-SERVICE-NAME')
            if not service_name:
                return starlette.responses.Response(
                    "Missing 'X-SERVICE-NAME' header",
                    status_code=status.HTTP_400_BAD_REQUEST
                )
            service_url = self.services.get(service_name)
            if not service_url:
                return starlette.responses.Response(
                    f"Service '{service_name}' not found",
                    status_code=status.HTTP_404_NOT_FOUND
                )

            # 转发请求到微服务
            response = await self.forward_request(service_url, request)
            return response
        except Exception as e:
            return starlette.responses.Response(
                f"Error: {str(e)}",
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    async def forward_request(self, service_url, request):
        "