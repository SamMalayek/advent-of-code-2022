from collections import defaultdict, deque
file_input = open("input-day7.txt",'r')
cli = [l.strip() for l in file_input.readlines()]

class TreeNode:
    def __init__(self, dirName, parent=None, children=None):
        self.dirName = dirName
        self.parent = parent
        self.children = children or []  # if dir, then TreeNode. if file, then int

def main():
    cur = TreeNode('/')
    root = cur

    for out in cli[1:]:
        tokens = out.split()
        if tokens[0] == '$':
            if tokens[1] == 'cd':
                if tokens[2] == '..':
                    cur = cur.parent
                else:
                    cd = TreeNode(tokens[2], cur)
                    cur.children.append(cd)
                    cur = cd
        elif tokens[0].isnumeric():
            cur.children.append(int(tokens[0]))

    resp = 9999999999999999999999

    def dfs(node):
        nonlocal resp
        curTotal = 0
        for child in node.children:
            if type(child) == TreeNode:
                curTotal += dfs(child)
            else:
                curTotal += child
        if curTotal < resp and curTotal >= 1111105:
            resp = curTotal
        return curTotal

    dfs(root)
    print(resp)

main()
