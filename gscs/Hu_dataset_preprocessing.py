from pandas.io import pickle

from gscs.strudata import parse_program, get_adjacent, get_adjacent2

code_dataset_path = "/project/gshukla/GSCS/java/test/code.original"

# For tokenized AST file
with open(code_dataset_path, 'r', encoding='utf-8') as file:
    with open(r'/project/gshukla/GSCS/java/test/node_sequence', 'w') as fp:
        for line in file.readlines():
            tree = parse_program(line)
            ss = get_adjacent2(tree)
            fp.write(ss)
            fp.write('\n')
    print('Done')

# For Edge files (Adjacency matrix)
with open(code_dataset_path, 'r', encoding='utf-8') as file:
     with open(r'/project/gshukla/GSCS/java/test/edge.pkl', 'wb') as fp:
         for line in file.readlines():
             tree = parse_program(line)
             segc = get_adjacent(tree)
             pickle.dump(segc, fp)
     print('Done')

