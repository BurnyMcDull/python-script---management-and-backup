import optparse
import os
import time
def isParserLegal(remarks,filename):
    if not remarks:
        print("Error: parser -r remarks is required.")
        return False
    elif not filename:
        print("Error: parser -i filename is required.")
        return False
    return True

def isDir(filename):
    filename_now=filename+'版本管理控制文件夹'
    if not os.path.exists(filename_now):
        os.makedirs(filename_now)
        return 0
    else:
        #print(len(os.listdir(filename_now)))
        print ('文件夹已存在')
        return len(os.listdir(filename_now))
def isEdition(filename):
    f=open(filename,encoding='utf-8')
    content = f.read()
    f.close()
    content_new=content.split('\n')
    if content_new[0]!="# -*- coding: utf-8 -*-":
        return 0
    else:
        if content_new[1]!="'''":
            return 1
        else:
            return 2
usage="[-a <author>] [-r <remarks>][-i <filename>]"
parser = optparse.OptionParser(usage)
parser.add_option('-a', dest='author',type='string',help="eg:author's name",default='BurnyMcDull')
#parser.add_option('-e', dest='edition',type='string', help='v1.0')
parser.add_option('-r', dest='remarks', type='string', help='remarks EN',default='')
parser.add_option('-i',  dest='filename',type='string', help='eg:test.py')
(options, args) = parser.parse_args()
author=options.author
#edition=options.edition
remarks=options.remarks
filename=options.filename
localtime = time.localtime(time.time())
times=str(localtime.tm_year)+'.'+str(localtime.tm_mon)+'.'+str(localtime.tm_mday)+' '+str(localtime.tm_hour)+':'+str(localtime.tm_min)
if not isParserLegal(remarks,filename):
    quit()
bool_v=isDir(filename)
bool_e=isEdition(filename)
if(bool_v==0):
    version='V 1.0'
else:
    version='V '+str(bool_v)+'.0'
if(bool_e==0):
    f = open(filename,encoding='utf-8')
    s = f.read()
    f.close()
    a = s.split('\n')
    a.insert(0, '# -*- coding: utf-8 -*-')
    a.insert(1,"'''")
    a.insert(2,'author: ' + author)
    a.insert(3,'remrks: ' + remarks)
    a.insert(4,'version: ' + version)
    a.insert(5,'time: '+times)
    a.insert(6,"'''")
    s = '\n'.join(a)
if(bool_e==1):
    f = open(filename,encoding='utf-8')
    s = f.read()
    f.close()
    a = s.split('\n')
    a.insert(1,"'''")
    a.insert(2,'author: ' + author)
    a.insert(3,'remrks: ' + remarks)
    a.insert(4,'version: ' + version)
    a.insert(5,'time: '+times)
    a.insert(6,"'''")
    s = '\n'.join(a)
filename_new=filename.split('.')
path=filename+'版本管理控制文件夹/'+filename_new[0]+'_'+version+'.py'
print(path)
if(bool_e!=2):
    fp = open(path,'w',encoding='utf-8')
    fp.write(s)
    fp.close()
if(bool_e==2):
        print('检查文件版本信息')