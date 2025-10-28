# 代码生成时间: 2025-10-28 20:08:17
import starlette.requests
from starlette.responses import JSONResponse
# FIXME: 处理边界情况
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from typing import List, Dict
# NOTE: 重要实现细节

# DragAndDropService 类负责处理拖拽排序的逻辑
class DragAndDropService:
    def __init__(self, items: List[Dict]):
        self.items = items
# 改进用户体验

    def sort_items(self, item_id: int, new_index: int) -> List[Dict]:
        """根据给定的item_id和new_index重新排序items列表。

        Args:
            item_id (int): 要移动的项目的ID。
            new_index (int): 项目的新索引位置。
# 优化算法效率

        Returns:
            List[Dict]: 重新排序后的项目列表。

        Raises:
            ValueError: 如果item_id或new_index无效。"""
        if item_id < 0 or new_index < 0 or item_id >= len(self.items) or new_index >= len(self.items):
            raise ValueError(