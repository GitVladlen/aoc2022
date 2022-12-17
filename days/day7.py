import utils

lines = utils.get_file_lines("../inputs/input_day7.txt")
lines = utils.get_file_lines("../inputs/test_1_day7.txt")

#print(lines)

TOTAL_SPACE = 70000000
NEEDED_SPACE = 30000000

class MyTree:
    def __init__(self, tag, data):
        self.nodes = []
        self.tag = tag
        self.data = data

    def has_node(self, in_node):
        for node in self.nodes:
            if node.tag == in_node.tag and node.data == in_node.data:
                return True
        return False

    def visit(self, visitor, data):
        data = visitor(self, data)
        for node in self.nodes:
            data = node.visit(visitor, data)
        return data

    def apply(self, visitor, data):
        data = visitor(self, data)
        for node in self.nodes:
            node.apply(visitor, data)
        return data


class MyFileSystem:
    def __init__(self):
        self.tree = None

    def get_node_by_path(self, path):
        cur_node = self.tree
        for path_node in path:
            for tree_node in cur_node.nodes:
                if tree_node.tag == 'dir' and tree_node.data == path_node:
                    cur_node = tree_node
                    break
        return cur_node

    def add_node(self, path, node):
        if self.tree is None:
            self.tree = node
        else:
            cur_node = self.get_node_by_path(path)
            
            if not cur_node.has_node(node):
                cur_node.nodes.append(node)
    
    def add_dir(self, path, dir_name):
        #print("  add dir: path '{}' dir '{}'".format(path, dir_name))

        self.add_node(path, MyTree('dir', dir_name))
    
    def add_file(self, path, file_name, size):
        #print("  add file: path '{}' name '{}' size '{}'".format(path, file_name, size))

        self.add_node(path, MyTree('file', (file_name, size)))

    def get_dir_size(self, node):
        # todo: impl
        
        def node_visitor(_node, _data):
            if _node.tag == 'file':
                _data += int(_node.data[1])
            return _data
        
        dir_size = node.visit(node_visitor, 0)
        
        return (node.data, dir_size)

    def get_dir_sizes(self):
        dir_sizes = []
        if not self.tree:
            return dir_sizes

        def tree_visitor(node, data):
            if node.tag == 'dir':
                dir_size = self.get_dir_size(node)
                data.append(dir_size)
            return data

        dir_sizes = self.tree.visit(tree_visitor, dir_sizes)

        return dir_sizes


    def print_tree(self):
        if self.tree is None:
            print("Tree is empty")
            return
        
        print("Tree:")

        def tree_visitor(node, data):
            print("{indent}{data} ({tag})".format(
                indent='  ' * data,
                tag=node.tag,
                data=node.data,
                nodes=[(n.tag, n.data, len(n.nodes)) for n in node.nodes]))
            return data + 1

        self.tree.apply(tree_visitor, 0)

        
def parse_commands(lines):
    commands = []
    cur_command_id = None
    cur_command_nodes = None
    cur_command_output = []
    for line in lines:
        nodes = line.split(' ')
        if cur_command_id == None:
            cur_command_id = nodes[1]
            cur_command_nodes = nodes
            continue
            
        if nodes[0] == '$':
            commands.append((cur_command_id, cur_command_nodes, cur_command_output))
            cur_command_id = nodes[1]
            cur_command_nodes = nodes
            cur_command_output = []
        else:
            cur_command_output.append(nodes)
    
    commands.append((cur_command_id, cur_command_nodes, cur_command_output))
    cur_command_id = nodes[1]
    cur_command_nodes = nodes
    cur_command_output = []
    return commands


def parse_filesystem(commands):
    fs = MyFileSystem()

    path = []
    for command in commands:
        c_id, c_nodes, c_output = command
        #print(command)
        if c_id == 'cd':
            dir_name = c_nodes[2]
            if dir_name == '..':
                path.pop()
            else:
                fs.add_dir(path, c_nodes[2])
                path.append(c_nodes[2])

            #print(" path:", path)
        elif c_id == 'ls':
            for output_nodes in c_output:
                a, b = output_nodes
                if a == 'dir':
                    fs.add_dir(path, b)
                else:
                    fs.add_file(path, b, a)
    return fs

def part_one(lines):
    commands = parse_commands(lines)

    fs = parse_filesystem(commands)

    #fs.print_tree()

    dir_sizes = fs.get_dir_sizes()

    #print(dir_sizes)

    result = 0
    for dir_name, dir_size in dir_sizes:
        if dir_size <= 100000:
            result += dir_size

    return result
    
	
def part_two(lines):
    commands = parse_commands(lines)

    fs = parse_filesystem(commands)

    dir_sizes = fs.get_dir_sizes()

    root_dir_size = 0
    if dir_sizes:
        root_dir_size = dir_sizes[0][1]
    print("root dir size is", root_dir_size)

    unused_space = TOTAL_SPACE - root_dir_size
    print("unused space is", unused_space)

    if unused_space < NEEDED_SPACE:
        print("FAIL")
        need_to_free = NEEDED_SPACE - unused_space
        print("need to free space", need_to_free)
    else:
        print("SUCCESS")



    result = 0

    # todo: imple solution

    return result
    

result_part_one = part_one(lines)
result_part_two = part_two(lines)

print("Part 1 result:", result_part_one)
print("Part 2 result:", result_part_two)
