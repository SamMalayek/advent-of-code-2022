from collections import defaultdict, deque
file_input = open("input-day7.txt",'r')
cli = [l.strip() for l in file_input.readlines()]

class TreeNode:  # if dir, then string. if file, then int
    def __init__(self, dirName, parent=None, files=None, childDirs=None):
        self.dirName = dirName
        self.parent = parent
        self.files = files or []
        self.childDirs = childDirs or []

def main():
    prev = None
    cur = TreeNode(None)
    root = cur

    for out in cli[1:]:
        tokens = out.split()
        if tokens[0] == '$':
            if tokens[1] == 'cd':
                if tokens[2] == '..':
                    cur = cur.parent
                else:
                    cd = TreeNode(tokens[2], cur)
                    cur.childDirs.append(cd)
                    cur = cd
        elif tokens[0].isnumeric():
            cur.childDirs.append(int(tokens[0]))

    resp = 9999999999999999999999

    def dfs(node):
        nonlocal resp
        curTotal = 0
        for child in node.childDirs:
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
