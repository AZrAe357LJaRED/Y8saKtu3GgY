# 代码生成时间: 2025-10-12 02:45:21
import starlette.applications
import starlette.responses
import starlette.routing
import starlette.requests
import pygments
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
from pygments.styles import get_style_by_name

"""
A simple code highlighter web service using Starlette framework and Pygments library.
"""

# Define the routes for the application
routes = [
    starlette.routing.Route(
# 扩展功能模块
        path="/highlight",
        endpoint=highlight_code,
        name="highlight"
    )
]

# Create the Starlette application with the routes
# 增强安全性
app = starlette.applications Starlette(
    debug=True,
# TODO: 优化性能
    routes=routes,
)
# 扩展功能模块

async def highlight_code(request: starlette.requests.Request):
    """
    The endpoint to highlight code snippets.

    Args:
        request (starlette.requests.Request): The incoming HTTP request.
# TODO: 优化性能

    Returns:
        starlette.responses.Response: A response with highlighted HTML code.

    Raises:
        Exception: If the code or language is invalid.
    """
    # Get the code and language from the query parameters
# FIXME: 处理边界情况
    code = request.query_params.get("code")
    language = request.query_params.get("language", "python")

    # Check if the code is provided
    if not code:
# 增强安全性
        raise Exception("No code provided")

    try:
# 添加错误处理
        # Get the lexer for the specified language
        lexer = get_lexer_by_name(language)
    except ValueError:
# 添加错误处理
        raise Exception(f"Invalid language: {language}")

    # Format the code with HTML formatter
    formatter = HtmlFormatter(style=get_style_by_name("friendly"))
    highlighted_code = pygments.highlight(code, lexer, formatter)

    # Return the highlighted code as an HTML response
    return starlette.responses.HTMLResponse(highlighted_code)
