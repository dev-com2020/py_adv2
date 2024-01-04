import ast

tree = ast.parse('def hello():print("WItaj!")')

print(ast.dump(tree, indent=4))
