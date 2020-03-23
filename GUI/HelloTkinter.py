import os

abs_file = __file__

print(abs_file)
print(abs_file[:abs_file.rfind('/')])

print('current Director: ' + os.curdir)
