__winc_id__ = 'ae539110d03e49ea8738fd413ac44ba8'
__human_name__ = 'files'



import os
from zipfile import ZipFile
from pathlib import Path



def clean_cache():
    MYDIR = ("cache")
    CHECK_FOLDER = os.path.isdir(MYDIR)

    # If folder doesn't exist, then create it.
    if not CHECK_FOLDER:
        os.makedirs(MYDIR)
        print("created folder : ", MYDIR)

    else:
        dir = os.getcwd()
        for f in os.listdir(dir + "/cache"):
            os.remove(os.path.join(dir + "/cache", f))
            print("file removed: " + f)

 #function 2 zip
def cache_zip(zip_file, folder_cache):
    with ZipFile(zip_file, 'r',) as zip:        
        zip.extractall(folder_cache)
        print('extraction complete')
    return


 #function 3 zip

def cached_files(): 
    dir = os.getcwd()
    list_of_file = []
    file_list = os.listdir(dir + "/cache")
    for file in file_list:        
        p = Path(file).absolute()
        s = str(p).rsplit("\\",)[-1]
        index_line = str(p).find(s)
        output_line = str(p)[:index_line] + 'cache\\' + str(p)[index_line:]        
        list_of_file.append(output_line)                    
    return list_of_file

#print(cached_files())

#function 4 password
def find_password(file_list):
    dir = os.getcwd()
    for f in file_list: 
        #print(f)       
        open_file = open(f,'r')
        #read_file = open_file.read()
        for line in open_file.readlines():               
            password_find = line.find('password')
            if password_find != -1:
                print('password found at position: ' + str(password_find) + ' in file ' + f)
                password = line.strip('password: ').strip()
                print(password)
                return password
        
        










#clean_cache()

#cache_zip('data.zip','cache')

#print(find_password(cached_files()))


