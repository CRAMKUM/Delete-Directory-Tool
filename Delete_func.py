# -*- coding: utf-8 -*-
"""
Spyder Editor

To delete all files older than a particular number of days
"""
import os 
import datetime
import shutil


def Delete_func(path,filetype,date):
    

    #today = datetime.datetime.today()#gets current time
    os.chdir(path) #changing path to current path(same as cd command)
    
    #we are taking current folder, directory and files 
    #separetly using os.walk function
    for root,directories,files in os.walk(path,topdown=False): 
        for name in files:
            #this is the last modified time
            t = os.stat(os.path.join(root, name))[8] 
            filetime = (datetime.datetime.fromtimestamp(t) - date).days #checking if file is more than 7 days old 
            #or not if yes then remove them
            extension = ['']*16
            
            
            if (filetype[0] == 1):
                extension[0] = 'gtm'
            else:
                extension[0] = 'null'
                
            
            if (filetype[1] == 1):
                extension[1] = 'gdx'
            else:
                extension[1] = 'null'
            
            if(filetype[2] == 1):
                extension[2] = 'sim'
            else:
                extension[2] = 'null'
                
            
            if(filetype[3] == 1):
                extension[3] = 'trn'
            else:
                extension[3] = 'null'
                
            
            if(filetype[4] == 1):
                extension[4] = 'xlsx'
            else:
                extension[4] = 'null'
                
                
            if(filetype[5] == 1):
                extension[5] = 'pptx'
            else:
                extension[5] = 'null'
                
                
            if(filetype[6] == 1):
                extension[6] = 'docx'
            else:
                extension[6] = 'null'
                
            
            if(filetype[7] == 1):
                extension[7] = 'sim~'
            else:
                extension[7] = 'null'
                
            
            if(filetype[8] == 1):
                extension[8] = 'csv'
            else:
                extension[8] = 'null'
                
            
            if(filetype[9] == 1):
                extension[9] = 'x_b'
            else:
                extension[9] = 'null'
                
            if(filetype[10] == 1):
                extension[10] = 'x_t'
            else:
                extension[10] = 'null'
                
                
            if(filetype[11] == 1):
                extension[11] = 'prt'
            else:
                extension[11] = 'null'
                
                
            if(filetype[12] == 1):
                extension[12] = 'png'
            else:
                extension[12] = 'null'
                
                
            if(filetype[13] == 1):
                extension[13] = 'avi'
            else:
                extension[13] = 'null'
                
                
            if(filetype[14] == 1):
                extension[14] = 'mpeg'
            else:
                extension[14] = 'null'
                
                
                
            if filetype[15]:
                extension[15] = filetype[15]
            else:
                extension[15] = 'null'
            
            
    
            
            if (filetime <0 and (name.endswith(extension[0]) or name.endswith(extension[1]) or name.endswith(extension[2]) or name.endswith(extension[3]) or name.endswith(extension[4]) or name.endswith(extension[5]) or name.endswith(extension[6]) or name.endswith(extension[7]) or name.endswith(extension[8])or name.endswith(extension[9])or name.endswith(extension[10])or name.endswith(extension[11])or name.endswith(extension[12]) or name.endswith(extension[13]) or name.endswith(extension[14]) or name.endswith(extension[15]))):
                print(os.path.join(root, name), filetime)
                destination = os.path.join(path,'recycle_bin')
                if(not (os.path.isdir(destination))):
                    os.mkdir(os.path.join(path,'recycle_bin'))
                source = os.path.join(root,name)   
                if(not(os.path.exists(os.path.join(destination,name)))):
                    shutil.move(source,destination)
                #os.remove(os.path.join(root, name))
                
    return None

def Permanent_del(path,status):
    destination = os.path.join(path,'recycle_bin')
    if(status==True):               
        shutil.rmtree(destination)