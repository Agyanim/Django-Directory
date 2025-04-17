import os,shutil

base_dir = os.getcwd()
sub_folder = os.path.join('python projects','day one')
full_path = os.path.join(base_dir,sub_folder)

# os.mkdir(os.path.join(full_path,'names','department'))

# path = (os.path.join(full_path,'name.txt'))
shutil.rmtree(os.path.join(full_path,'names','department'))
