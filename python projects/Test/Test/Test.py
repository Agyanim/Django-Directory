import os, shutil
from datetime import datetime

base_dir = os.getcwd()
sub_dir =('Test/files')
new_folder = 'test'


file = ('name.txt')
file_path = os.path.join(base_dir,sub_dir,file)
with open(file_path, 'a') as f:
    f.write('\n We cannot be left out bro!')

with open(file_path, 'r') as f:
    content = f.read()
    print(content)
  
 

# #print(datetime.now().strftime('%d-%m-%Y'))