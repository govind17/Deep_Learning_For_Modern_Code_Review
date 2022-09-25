import pandas as pd
import os
import pickle
from strudata import get_adjacent2, get_adjacent, parse_program

def create_data_files(dataset_type):
    dataset_dir = '/project/gshukla/GSCS/java3/'
    original_dataset_dir = '/project/gshukla/GSCS/java3/train/'
    df = pd.read_csv(os.path.join(original_dataset_dir, '{}.tsv'.format(dataset_type)),
                     sep='\t',
                     header=None,
                     skiprows=1,
                     names=['code', 'review'],
                     error_bad_lines=False)
    df = df[df.review.str.len() > 0]
    with open(os.path.join(dataset_dir, '{}/code'.format(dataset_type)), 'w') as fp_c:
        with open(os.path.join(dataset_dir, '{}/node'.format(dataset_type)), 'w') as fp_n:
            with open(os.path.join(dataset_dir, dataset_type + '/edge.pkl'), 'wb') as fp_e:
                with open(os.path.join(dataset_dir, dataset_type + '/review'), 'w') as fp_r:
                    print('Start writing {} datafiles.....'.format(dataset_type))
                    count = 0
                    for index, row in df.iterrows():
                        try:
                            # Node File
                            ns = get_adjacent2(parse_program(row['code']))
                            fp_n.write(str(ns))
                            fp_n.write('\n')
                            # Edge File
                            pickle.dump(get_adjacent(parse_program(row['code'])), fp_e)
                            # Code File
                            fp_c.write(row['code'])
                            fp_c.write('\n')
                            # Review File
                            fp_r.write(row['review'])
                            fp_r.write('\n')
                            count = count + 1
                            if count == 10000:
                                break
                        except:
                            continue
                    print('Finished writing {} datafiles!!!'.format(dataset_type))
                    print("#{} records :".format(dataset_type), count)
# Train Files
create_data_files('train')

