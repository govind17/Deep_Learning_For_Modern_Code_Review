import sqlite3
import pickle
from strudata import get_adjacent2, get_adjacent, parse_program

con = sqlite3.connect('/Users/GovindShukla/Desktop/dlmcr/etcr_backup11_postprocessing.db')
cur = con.cursor()
write_code_path_train = '/Users/GovindShukla/Desktop/GSCS-master/java2/train/code2'
write_code_path_dev = '/Users/GovindShukla/Desktop/GSCS-master/java2/dev/code2'
write_code_path_test = '/Users/GovindShukla/Desktop/GSCS-master/java2/test/code2'

def getSyntacticallyCorrectCode(row):
    ss = None
    while ss is None:
        try:
            a = 1
            codelst = list(map(str.strip, row[-1].decode("utf-8").split('\n')[row[0] - 1:row[1] + a]))
            codelistwihtoutcomment = [x for x in codelst if not x.startswith('//')]
            codewithoutcomment = ' '.join(codelistwihtoutcomment)
            ss = parse_program(codewithoutcomment)
        except:
            a = a + 1
            continue
    return codewithoutcomment

def getCode(row):
    codelst = list(map(str.strip, row[-1].decode("utf-8").split('\n')[row[0] - 1:row[1]]))
    codelistwihtoutcomment = [x for x in codelst if not x.startswith('//')]
    codewithoutcomment = ' '.join(codelistwihtoutcomment)
    return codewithoutcomment

count = 0
t_cnt = 0
d_cnt = 0
tt_cnt = 0
with open(write_code_path_train, 'w') as fp_t:
    with open(write_code_path_dev, 'w') as fp_d:
        with open(write_code_path_test, 'w') as fp_tt:
            print('Start.......')
            for row in cur.execute('''SELECT  data.ast_fromline,
                                             data.ast_toline,
                                              data.commit_id,
                                               data.file_path,
                                              data.comment ,
                                              data.pr_merge_order,
                                              file.content
                                        FROM DATASET  data
                                        JOIN file
                                        ON file.commit_id = data.commit_id
                                        AND file.path = data.file_path
                                        where data.comment  is not  null
                                        order by data.pr_merge_order'''):
                # print(row[3], row[2],row[0], row[1])
                # code = ''.join(row[-1].decode("utf-8").split('\n')[row[0]:row[1]]).replace("\t","")
                # print(code)

                if count <= 10780:
                    fp_t.write(getCode(row))
                    fp_t.write('\n')
                    count = count + 1
                    t_cnt = t_cnt + 1
                if 10780 < count <= 12130:
                    fp_d.write(getCode(row))
                    fp_d.write('\n')
                    count = count + 1
                    d_cnt = d_cnt + 1
                if 12130 < count <= 13475:
                    fp_tt.write(getCode(row))
                    fp_tt.write('\n')
                    count = count + 1
                    tt_cnt = tt_cnt + 1
                # print(' '.join(codelstwithoutcomment))
                # print('-----------------------------------------------------------------------------------------------')
print('Code Done: ', count)
print('Code Train count: ', t_cnt)
print('Code Dev count: ', d_cnt)
print('Code test count: ', tt_cnt)

# Review files
write_review_path_train = '/Users/GovindShukla/Desktop/GSCS-master/java2/train/review'
write_review_path_dev = '/Users/GovindShukla/Desktop/GSCS-master/java2/dev/review'
write_review_path_test = '/Users/GovindShukla/Desktop/GSCS-master/java2/test/review'
count = 0
t_cnt = 0
d_cnt = 0
tt_cnt = 0
with open(write_review_path_train, 'w') as fp_t:
    with open(write_review_path_dev, 'w') as fp_d:
        with open(write_review_path_test, 'w') as fp_tt:
            for row in cur.execute('''SELECT
                                            REPLACE(REPLACE(comment, CHAR(13), ''), CHAR(10), '') comment,
                                            pr_merge_order
                                        FROM DATASET
                                        where comment  is not  null
                                        order by pr_merge_order'''):
                if count <= 10780:
                    fp_t.write(row[0])
                    fp_t.write('\n')
                    count = count + 1
                    t_cnt = t_cnt + 1
                if count > 10780 and count <= 12130:
                    fp_d.write(row[0])
                    fp_d.write('\n')
                    count = count + 1
                    d_cnt = d_cnt + 1
                if count > 12130 and count <= 13475:
                    fp_tt.write(row[0])
                    fp_tt.write('\n')
                    count = count + 1
                    tt_cnt = tt_cnt + 1

            print('Review Done: ', count)
            print('Review Train count: ', t_cnt)
            print('Review Dev count: ', d_cnt)
            print('Review test count: ', tt_cnt)

# Node File
write_node_path_train = '/Users/GovindShukla/Desktop/GSCS-master/java2/train/node'
write_node_path_dev = '/Users/GovindShukla/Desktop/GSCS-master/java2/dev/node'
write_node_path_test = '/Users/GovindShukla/Desktop/GSCS-master/java2/test/node'
count = 0
t_cnt = 0
d_cnt = 0
tt_cnt = 0
code_dataset_path = "/Users/GovindShukla/Desktop/GSCS-master/java2/ast.csv"
with open(code_dataset_path, 'r', encoding='utf-8') as file:
    with open(write_node_path_train, 'w', encoding='utf-8') as fp_t:
        with open(write_node_path_dev, 'w', encoding='utf-8') as fp_d:
            with open(write_node_path_test, 'w', encoding='utf-8') as fp_tt:
                for line in file.readlines():
                    ast = pickle.loads(bytes.fromhex(line))
                    seqc = get_adjacent2(ast)
                    if count <= 10780:
                        fp_t.write(str(seqc))
                        fp_t.write('\n')
                        count = count + 1
                        t_cnt = t_cnt + 1
                    if count > 10780 and count <= 12130:
                        fp_d.write(str(seqc))
                        fp_d.write('\n')
                        count = count + 1
                        d_cnt = d_cnt + 1
                    if count > 12130 and count <= 13475:
                        fp_tt.write(str(seqc))
                        fp_tt.write('\n')
                        count = count + 1
                        tt_cnt = tt_cnt + 1

print('Node Done: ', count)
print('Node Train count: ', t_cnt)
print('Node Dev count: ', d_cnt)
print('Node test count: ', tt_cnt)

# Edge File
write_edge_path_train = '/Users/GovindShukla/Desktop/GSCS-master/java2/train/edge.pkl'
write_edge_path_dev = '/Users/GovindShukla/Desktop/GSCS-master/java2/dev/edge.pkl'
write_edge_path_test = '/Users/GovindShukla/Desktop/GSCS-master/java2/test/edge.pkl'
count = 0
t_cnt = 0
d_cnt = 0
tt_cnt = 0
code_dataset_path = "/Users/GovindShukla/Desktop/GSCS-master/java2/ast.csv"
with open(code_dataset_path, 'r', encoding='utf-8') as file:
    with open(write_edge_path_train, 'wb') as fp_t:
        with open(write_edge_path_dev, 'wb') as fp_d:
            with open(write_edge_path_test, 'wb') as fp_tt:
                for line in file.readlines():
                    ast = pickle.loads(bytes.fromhex(line))
                    ss = get_adjacent(ast)
                    if count <= 10780:
                        pickle.dump(ss, fp_t)
                        count = count + 1
                        t_cnt = t_cnt + 1
                    if 10780 < count <= 12130:
                        pickle.dump(ss, fp_d)
                        count = count + 1
                        d_cnt = d_cnt + 1
                    if 12130 < count <= 13475:
                        pickle.dump(ss, fp_tt)
                        count = count + 1
                        tt_cnt = tt_cnt + 1

print('Edge Done: ', count)
print('Edge Train count: ', t_cnt)
print('Edge Dev count: ', d_cnt)
print('Edge test count: ', tt_cnt)
