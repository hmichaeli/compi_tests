import pathlib
import sys
import os

os.system('ls -l')

part1_path = sys.argv[1]
cur_file_path = pathlib.Path(__file__).parent.absolute()
#dirs
files_dir = os.path.join(cur_file_path, 'files')
res_dir = os.path.join(cur_file_path, 'results')
tokens_dir = os.path.join(cur_file_path, 'tokens')

# make
os.system('make -C ' + part1_path)

os.mkdir(res_dir)

files = os.listdir(files_dir)

for test_file in files:
    test_file = os.path.join(files_dir, test_file)
    tokens_file = os.path.join(tokens_dir, test_file + '.tokens')
    res_file = os.path.join(res_dir, test_file)

    command = part1_path + '/part1 < ' + test_file + ' > ' + res_file
    print(command)
    os.system(command)
    diff_command = 'diff ' + test_file + ' ' + tokens_file
    os.system(diff_command)