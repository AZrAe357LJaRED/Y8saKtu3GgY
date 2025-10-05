# 代码生成时间: 2025-10-06 02:03:26
import json
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND


class TreeNode:
    """
    A simple tree node class representing an item in the tree structure.
    """
    def __init__(self, id, name, children=None):
        self.id = id  # Unique identifier for the node
        self.name = name  # Name of the node
        self.children = children if children else []  # List of child nodes


    def add_child(self, child):
        """
        Add a child node to the current node.
        """
        self.children.append(child)



class TreeStructure:
    """
    A class to manage the tree structure and provide operations on it.
    """
    def __init__(self):
        self.root = None

    def add_node(self, node, parent_id=None):
        """
        Add a new node to the tree. If parent_id is provided, adds it as a child of that parent.
        """
        if not self.root:
            self.root = node
            return

        if parent_id is None:
            raise ValueError('Parent ID is required when the tree is not empty.')

        parent = self.find_node(self.root, parent_id)
        if parent is None:
            raise ValueError(f'Parent with ID {parent_id} not found.')

        parent.add_child(node)

    def find_node(self, current_node, target_id):
        """
        Helper function to find a node by its ID.
        """
        if current_node.id == target_id:
            return current_node

        for child in current_node.children:
            result = self.find_node(child, target_id)
            if result:
                return result

        return None

    def get_tree(self):
        """
        Returns the entire tree as a nested dictionary.
        """
        return self._get_tree_recursive(self.root)

    def _get_tree_recursive(self, node):
        """
        Helper function to recursively build the tree structure.
        """
        tree_dict = {"id": node.id, "name": node.name, "children": []}
        for child in node.children:
            tree_dict['children'].append(self._get_tree_recursive(child))
        return tree_dict



# Instantiate the tree structure
tree_structure = TreeStructure()

# Add nodes to the tree
tree_structure.add_node(TreeNode(1, 'Root'))
tree_structure.add_node(TreeNode(2, 'Child 1', parent_id=1))
tree_structure.add_node(TreeNode(3, 'Child 2', parent_id=1))
tree_structure.add_node(TreeNode(4, 'Grandchild 1', parent_id=2))

# Create a Starlette application
app = Starlette(routes=[
    Route('/', lambda request: JSONResponse(tree_structure.get_tree())),
])

# Define exception handlers
@app.exception_handler(ValueError)
async def value_error_handler(request, exc):
    return JSONResponse(
        {'error': str(exc)}, status_code=HTTP_400_BAD_REQUEST
    )

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        {'error': str(exc)}, status_code=exc.status_code
    )

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)