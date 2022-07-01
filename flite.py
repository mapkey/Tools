#!/usr/bin/python
# -*- coding: UTF-8 -*- 
import os
import shutil

def cp_tree_ext(exts,src,dest):
    """
    Rebuild the director tree like src below dest and copy all files like XXX.exts to dest 
    exts:exetens seperate by blank like "jpg png gif"
    """
    fp={}
    extss=exts.lower().split() 
    for dn,dns,fns  in os.walk(src):
           for fl in fns:
               if os.path.splitext(fl.lower())[1][1:] in extss:
                  if dn not in fp.keys():
                      fp[dn]=[]
                      fp[dn].append(fl)
         
    for k,v in fp.items():
            newpath=dest
            for f in v:
                oldfile=os.path.join(k,f)
                print("拷贝 ["+oldfile+"] 至 ["+newpath+"]")
                if not os.path.exists(newpath):
                    os.makedirs(newpath)
                shutil.copy(oldfile,newpath)

#用法如下：
#
#cp_tree_ext(exts,src,dest)
#
#exts:以空格分隔的字符串，可多个拓展名，如"bat txt"
#src:原目录
#dest:目标目录，如果不存在，则建立
cp_tree_ext('png','C:\\maqiang\\INDU\\ORG_3DLANDMARK','E:\\test')
