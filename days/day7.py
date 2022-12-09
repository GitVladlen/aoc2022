import utils

lines = utils.get_file_lines("../inputs/input_day7.txt")
lines = utils.get_file_lines("../inputs/test_1_day7.txt")

#print(lines)

class MyTree:
    def __init__(self):
        self.nodes = []
        self.tag = None
        self.data = None
        
    def print(self):
        print(self.tag, self.data)
        for node in self.nodes:
            print("inside", self.data)
            node.print()

class MyFileSystem:
    def __init__(self):
        self.tree = None
    
    def add_dir(self, path, dir_name):
        print("add dir: path '{}' dir '{}'".format(path, dir_name))
        if self.tree is None:
            new_tree = MyTree()
            new_tree.tag = 'dir'
            new_tree.data = dir_name
            self.tree = new_tree
        else:
            cur_node = self.tree
            for path_node in path:
                # search Tree node with cur path node
                for tree_node in cur_node.nodes:
                    if tree_node.tag == 'dir' and tree_node.data == path_node:
                        cur_node = tree_node
                        break
                        
            new_tree = MyTree()
            new_tree.tag = 'dir'
            new_tree.data = dir_name
            
            cur_node.nodes.append(new_tree)
                
        
    def print_tree(self):
        if self.tree is None:
            print("Tree is empty")
            return
        
        print("Tree:")
        self.tree.print()
        
    
    def add_file(self, path, file_name, size):
        print("add file: path '{}' name '{}' size '{}'".format(path, file_name, size))
        pass
        
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


def part_one(lines):
    fs = MyFileSystem()
    
    commands = parse_commands(lines)
    
    path = []
    for command in commands:
        c_id, c_nodes, c_output = command
        print(command)
        if c_id == 'cd':
            dir_name = c_nodes[2]
            if dir_name == '..':
                path.pop()
            else:
                path.append(c_nodes[2])
            print("path:", path)
        elif c_id == 'ls':
            for output_nodes in c_output:
                a, b = output_nodes
                if a == 'dir':
                    fs.add_dir(path, b)
                else:
                    fs.add_file(path, b, a)
    
    fs.print_tree()
    
    return 0
    
	
def part_two(lines):
	return 0
    

result_part_one = part_one(lines)
result_part_two = part_two(lines)

print("Part 1 result:", result_part_one)
print("Part 2 result:", result_part_two)