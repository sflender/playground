
'''
You’re given an array of nodes, each with an id and a parentId:
nodes = [
    {"id": 1, "parentId": None, "name": "root"},
    {"id": 2, "parentId": 1, "name": "child1"},
    {"id": 3, "parentId": 1, "name": "child2"},
    {"id": 4, "parentId": 2, "name": "grandchild"},
]
Build a tree where each node has a children field:
{
  "id": 1, "parentId": None, "name": "root", "children": [
    {"id": 2, "parentId": 1, "name": "child1", "children": [
      {"id": 4, "parentId": 2, "name": "grandchild", "children": []}
    ]},
    {"id": 3, "parentId": 1, "name": "child2", "children": []}
  ]
}
'''

def build_tree(nodes):
    id_map = {node['id']: {**node, 'children': []} for node in nodes}
    root = None
    for node in id_map.values():
        if node['parentId'] is None:
            root = node
        else:
            id_map[node['parentId']]['children'].append(node)
    return root

if __name__ == '__main__':
    nodes = [
        {"id": 1, "parentId": None, "name": "root"},
        {"id": 2, "parentId": 1, "name": "child1"},
        {"id": 3, "parentId": 1, "name": "child2"},
        {"id": 4, "parentId": 2, "name": "grandchild1"},
        {"id": 5, "parentId": 2, "name": "grandchild2"},
        {"id": 6, "parentId": 3, "name": "grandchild3"},
        {"id": 7, "parentId": 4, "name": "greatgrandchild"},
    ]

    def print_tree(node, level=0):
        print("  " * level + f"{node['name']} (id={node['id']})")
        for child in node['children']:
            print_tree(child, level + 1)

    tree = build_tree(nodes)
    print_tree(tree)
    