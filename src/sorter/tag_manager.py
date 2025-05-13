import os
import sys

from utils.logger import write_errorlog

''' .tags.txt操作系メソッド '''

def view_tags(TAGSPATH,LOGPATH):

    tagsfile_path = discover_tagsfile(TAGSPATH,LOGPATH)

    with open(tagsfile_path, 'r' , encoding='utf-8') as tags_txt:
        print('-- 現在の.tags.txtの中身 --')
        for i ,line in enumerate(tags_txt,1):
            tag = line.strip()
            if tag:
                print(f'{i}:{tag}')



def add_tags(TAGSPATH,LOGPATH,add_tag):


    tags = []

    if add_tag == "":
        return
    
    tagsfile_path = discover_tagsfile(TAGSPATH,LOGPATH)
    
    with open(tagsfile_path,'r',encoding='utf-8') as f:
        tags = [line.strip() for line in f if line.strip()]

    if add_tag in tags:
        print(f"'タグ',{add_tag}'は既に存在しています！'")
        return
        
    tags.append(add_tag)
    with open(tagsfile_path,'w',encoding='utf-8') as f:
        f.write('\n'.join(tags) + '\n')
    print(f"タグを追加しました！:{add_tag}")



def remove_tags(TAGSPATH,LOGPATH,remove_tag):
    tags = []

    if remove_tag == "":
        return
    
    tagsfile_path = discover_tagsfile(TAGSPATH,LOGPATH)

    with open(tagsfile_path,'r',encoding='utf-8') as f:
        tags = [line.strip() for line in f if line.strip()]
    
    if remove_tag not in tags:
        print(f"タグ{remove_tag}は存在しませんでした！")
        return
    
    tags.remove(remove_tag)

    with open(tagsfile_path,'w',encoding='utf-8') as f:
        f.write('\n'.join(tags) + '\n')
    print(f"タグを削除しました！:{remove_tag}")


def discover_tagsfile(TAGSPATH,LOGPATH):
    files = os.listdir(TAGSPATH)
    tagsfile_path = None

    for file in files:
        if 'tags.txt' in files:
            tagsfile_path = os.path.join(TAGSPATH,file)

    if tagsfile_path == None:
        write_errorlog('FIleNotFoundError',"tags.txtが見つかりませんでした。",LOGPATH)
        sys.exit(1)

    return tagsfile_path