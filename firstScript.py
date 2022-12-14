# -*- coding: utf-8 -*-

#import panda as pd 
import os
from datetime import datetime

setup_path = "Setup.Lst"
setup_temp_path = "Setup2.Lst"
aaDDManager_path = "aaDDManager.DDF"
version =  "7.15.3"#os.getenv("GITHUB_REF_NAME")
search_cab_file = "DD_V600b.CAB" #use last version 
replace_TmpDir = "GSTMP_" + version.replace('.', '_') + ".pwd"
replace_Spawn = "SETUP" + version.replace('.', '_') + ".EXE"
replace_cab_file =  "DD_" + version.replace('.', '_') + ".CAB"
replace_date = datetime.today().strftime('%d/%m/%Y %H:%M:%S') + ' AM'
replace_date_version = version + '.' + datetime.today().strftime('%Y%m%d')
search_date = ""
search_date_version = ""

print("stating to read ...")
    
# =============================================================================
# Replace de CabFile in Setup.lst
# =============================================================================
with open(setup_path, 'r') as f :

    # Reading the content of the file
    # using the read() function and storing
    # them in a new variable
    data = f.read()
   
    # Searching and replacing the text
    # using the replace() function
    data = data.replace(search_cab_file, replace_cab_file)
f.close()
 
with open(setup_path, 'w') as fi :
   
     # Writing the replaced data in our
     fi.write(data)
fi.close()

# =============================================================================
# Replace DD files's date in Setup.lst
# =============================================================================
fp = open(setup_temp_path, 'w')
with open(setup_path) as file:
    line = file.readline()
    
    while line :
        if line.startswith("Spawn"):
            spawn_param = line.strip().split("=")[1]
            if spawn_param != replace_Spawn:
                line = line.replace(spawn_param, replace_Spawn)
                print(line)
                fp.write(line)
                line = file.readline()
        if line.startswith("TmpDir"):
            tmpDir_param = line.strip().split("=")[1]
            if tmpDir_param != replace_TmpDir:
                line = line.replace(tmpDir_param, replace_TmpDir)
                print(line)
                fp.write(line)
                line = file.readline()
        if line.startswith("File"):
            file_params = line.strip().split("=")[1].split(",")
            for p in file_params :
                if p == file_params[0] and p.startswith('@dd') or p.startswith('@DD'):
                    search_date = file_params[4]
                    line = line.replace(search_date, replace_date)
                    print(line)
                    fp.write(line)
                    line = file.readline()
                else:
                    print(line)
                    fp.write(line)
                    line = file.readline()
        else :
            print(line)
            fp.write(line)
            line = file.readline()
file.close()
fp.close()

if os.path.exists(setup_path):
    os.remove(setup_path)
os.rename(setup_temp_path, setup_path)
 
# =============================================================================
# Replace de CabFile in aaDDManager
# =============================================================================
with open(aaDDManager_path, 'r') as f :

    # Reading the content of the file
    # using the read() function and storing
    # them in a new variable
    data = f.read()
   
    # Searching and replacing the text
    # using the replace() function
    data = data.replace(search_cab_file, replace_cab_file)
f.close()

with open(aaDDManager_path, 'w') as fi :
   
     # Writing the replaced data in our
     fi.write(data)
fi.close()


