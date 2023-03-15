import os
import subprocess
import sys
import time


def extract_file(file_path):

    sys.stderr.write('\nextracting ' + file_path + '\n')
    folder_path = os.path.dirname(file_path)
    command = ['cmd', '/c', '7z', 'x', '-y', file_path, '-o' + folder_path]
    sys.stderr.write('running command: ' + command.__str__() + '\n')
    subprocess.run(command)


start_time = time.time()
sys.stdout.write('\nstarting extract all script\n')

if sys.argv.__len__() < 2:
    sys.stderr.write('insufficient arguments\n\n')
    exit(-1)

i = 0
first_arg = os.path.abspath(sys.argv[1])
if os.path.isdir(first_arg):

    folder_path = first_arg
    sys.stderr.write('\nextracting all archives inside folder ' + folder_path + '\n')

    for file_path in os.listdir(folder_path):
        if file_path.endswith(('.7z', '.zip', '.rar')):
            file_path = os.path.join(folder_path, file_path)
            extract_file(file_path)

else:
    i = 1
    while i < sys.argv.__len__():

        arg = sys.argv[i]
        file_path = os.path.abspath(arg)
        extract_file(file_path)
        i = i + 1

exec_time = str(round(time.time() - start_time, 2))
sys.stdout.write('\ndone; execution time: ' + exec_time + ' seconds\n')
