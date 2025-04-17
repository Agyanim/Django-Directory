import os


folder_path =('python projects/day one/file')
files= os.listdir(folder_path)


for count, file in enumerate(files,start=1):
    ext = os.path.splitext(file)[1]
    new_name = f'boat{count}{ext}'
    
    src = os.path.join(folder_path,file)
    dst = os.path.join(folder_path,new_name)
    
    os.rename(src,dst)
    
    print(dst)
    
    