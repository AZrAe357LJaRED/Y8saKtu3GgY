# 代码生成时间: 2025-10-07 02:12:23
import starlette.app
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route
from starlette.exceptions import HTTPException as StarletteHTTPException
import logging

# 药物相互作用检查器类
class DrugInteractionChecker:
    def __init__(self):
        # 这里可以初始化一些数据，比如药物数据库
        self.drug_database = {"Aspirin": ["Warfarin"], "Ibuprofen": ["Aspirin"]}

    def check_interaction(self, drug1, drug2):
        """
        检查两种药物是否具有相互作用。
        :param drug1: 第一种药物
        :param drug2: 第二种药物
        :return: 包含相互作用信息的字典或者错误信息
        """
        if drug1 in self.drug_database and drug2 in self.drug_database.get(drug1, []):
            return {"message": f"{drug1} and {drug2} have an interaction."}
        elif drug2 in self.drug_database and drug1 in self.drug_database.get(drug2, []):
            return {"message": f"{drug2} and {drug1} have an interaction."}
        else:
            return {"message": f"No interaction found between {drug1} and {drug2}."}

# 药物相互作用检查API的路由处理器
async def drug_interaction_route(request):
    # 获取请求参数
    params = await request.json()
    drug1 = params.get("drug1")
    drug2 = params.get("drug2")
    if not drug1 or not drug2:
        raise StarletteHTTPException(status_code=400, detail="Drug names are required")

    checker = DrugInteractionChecker()
    result = checker.check_interaction(drug1, drug2)
    return JSONResponse(result)

# 创建Starlette应用
app = Starlette(debug=True)

# 添加路由
app.add_route("/check_interaction", drug_interaction_route, methods=["POST"])

if __name__ == '__main__':
    # 运行应用
    uvicorn.run(app, host="0.0.0.0", port=8000)
