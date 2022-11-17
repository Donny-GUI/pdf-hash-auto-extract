#  extract.py
#
#  [description]:
#
#       Downloads dependencies. git john the
#       ripper. Unzip john.
#
#       Then, For every pdf file in this directory,
#       a hash will be extracted and saved as
#       <filename>.hash 
#
#   [usage]:
#   
#       python3 extract.py
#
#   [author]: Donny-GUI
#   [ date ]: Nov 17, 2022   

import os
import sys
import shutil

def determine_operating_system():
    
    print("\t Determining Operating System")
    osx = sys.platform
    files = os.listdir()
    match osx:
        case 'linux':
            if '._installed_' in files:
                linux_extract()
            else:
                linux_install()
                linux_extract()
        case 'darwin':
            if '._installed_' in files:
                linux_extract()
            else:
                darwin_install()
                linux_extract()
        case 'windows':
            if '._installed_' in files:
                windows_extract()
            else:
                windows_install()
                windows_extract()
        case _:
            print("unknown operating system")

def linux_install():
    cwd = os.getcwd()
    
    print('[+] Running Linux Install')
    apt_dependencies = ['wget', 'perl', 'unzip']
    
    for x in apt_dependencies:
        os.system(f"sudo apt-get install -y {x}")
    
    os.system(f'cd {cwd} && wget https://github.com/magnumripper/JohnTheRipper/archive/bleeding-jumbo.zip')

    os.system('unzip bleeding-jumbo.zip')
    
    with open('._installed_', 'w') as check:
        check.close()
    
    os.system(f"rm -r {cwd}/bleeding-jumbo.zip")
    
def darwin_install():
    cwd = os.getcwd()
    
    print('[+] Running Darwin Install')
    
    apt_dependencies = ['wget', 'perl', 'unzip']
    
    for x in apt_dependencies:
        os.system(f"brew install {x}")
    
    
    os.chdir(cwd)
    
    x = os.system(f'cd {cwd} && wget https://github.com/magnumripper/JohnTheRipper/archive/bleeding-jumbo.zip')

    os.chdir(cwd)

    os.system('unzip bleeding-jumbo')
    
    with open('._installed_', 'w') as check:
        check.close()
    
    os.system(f"rm -r {cwd}/bleeding-jumbo.zip")
    
def windows_install():
    
    cwd = os.getcwd()
    
    print('[+] Running Windows Install')
    
    apt_dependencies = ['wget', 'perl', 'unzip']
    
    for x in apt_dependencies:
        os.system(f"winget install {x}")
    
    x = os.system('wget https://github.com/magnumripper/JohnTheRipper/archive/bleeding-jumbo.zip')

    os.system(f'unzip {cwd}\\bleeding-jumbo')
    
    with open('._installed_', 'w') as check:
        check.close()
    
def linux_extract():
    
    print('[+] Running Linux Extract')
        
    def get_pdfs():
        
        print('\t\tAcquiring PDFs')
        
        pdfs = []
        
        files = os.listdir()
        
        cwd = os.getcwd()
        
        for file in files:
            
            if file.endswith(".pdf"):
                
                path = f"{cwd}/{file}"
                
                pdfs.append((path, file))
        
        if pdfs == []:
            print("no pdfs found in folder")
            exit()
        
        return pdfs


    def extract_hash(target, filename):
        
        print('\t\t\tExtracting Hash')
        
        xfilename = str(filename).split(".")
        
        fn = xfilename[0]
        
        cwd  = os.getcwd()
        
        fn_hash = f"{cwd}/{fn}.hash"
        
        command = f"perl john-bleeding-jumbo/run/pdf2john.pl {target} > {fn_hash}"
        
        os.system(command)
        
        with open(fn_hash, 'rb') as rfile:
            lines = rfile.readlines()
        
        retstrings = []
        
        for x in lines:
            rs = x.decode('utf-8')
            retstrings.append(rs)
        
        return retstrings 
        
    def main():
        
        files_hashes = {}
        
        pdfs_path_file = get_pdfs()
        
        for pobj in pdfs_path_file:
            
            path = pobj[0]
            
            file = pobj[1]
            
            hash_file = extract_hash(path, file)
            
            start_index = len(path)+1
            
            myhash = hash_file[0][start_index:-1]
            
            print(myhash)
            
            files_hashes[path] = myhash
            
        print(files_hashes)
        
    main()
        
def windows_extract():
    
    print('\tRunning Windows Extract')
    
    def get_pdfs():
        
        print('\t\tAcquiring PDFs')
        
        pdfs = []
        
        files = os.listdir()
        
        cwd = os.getcwd()
        
        for file in files:
            
            if file.endswith(".pdf"):
                
                path = f"{cwd}\\{file}"
                
                pdfs.append((path, file))
        
        return pdfs

    def extract_hash(target, filename):
        
        print('\t\t\tExtracting Hash')
        
        xfilename = str(filename).split(".")
        
        fn = xfilename[0]
        
        cwd  = os.getcwd()
        
        fn_hash = f"{cwd}\\{fn}.hash"
        
        command = f"perl john-bleeding-jumbo/run/pdf2john.pl {target} > {fn_hash}"
        
        os.system(command)
        
        with open(fn_hash, 'rb') as rfile:
            lines = rfile.readlines()
        
        retstrings = []
        
        for x in lines:
            rs = x.decode('utf-8')
            retstrings.append(rs)
        
        return retstrings 
        
    def main():
        
        files_hashes = {}
        
        pdfs_path_file = get_pdfs()
        
        for pobj in pdfs_path_file:
            
            path = pobj[0]
            
            file = pobj[1]
            
            hash_file = extract_hash(path, file)
            
            start_index = len(path)+1
            
            myhash = hash_file[0][start_index:-1]
            
            print(myhash)
            
            files_hashes[path] = myhash
            
        print(files_hashes)
            
    main()
        

print("\t\t\t\t[ PDF Auto Extractor v1.1 ]")

determine_operating_system()

print("\n For each pdf in this folder there is a corresponding hash file. \n Within this file is the target (line 0), and the actual hash value (line 1) ")

