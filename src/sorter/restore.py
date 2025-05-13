import os
import sys
import json
import shutil

from utils.logger import write_errorlog
from utils.history_manager import recode_JSONfile
from sorter.remove_dir import remove_dir


def restore_prev_onestep(SORTEPATH,JSONPATH,LOGPATH):

    JSONFILEPATH = os.path.join(JSONPATH,'history/history.json')
    with open(JSONFILEPATH,'r+',encoding='utf-8') as jsonfile:
        try:
            history = json.load(jsonfile)
        except json.jsonDecodeError:
            write_errorlog('decode_error','history.jsonの読み取りに失敗しました。',LOGPATH)
            sys.exit(1)

        if not history:
            print("エラーログに追記が発生しました。")
            write_errorlog('notfound_file','ロールバックできる履歴がありませんでした',LOGPATH)
            sys.exit(1)
        
        last = history.pop()
        src = last['dst']
        dst = last['src']

        if not os.path.exists(src):
            print("エラーログに追記が発生しました。")
            write_errorlog('notfound_file','戻すファイルが見つかりませんでした',LOGPATH)
            sys.exit(1)
        
        else:
            shutil.move(src,dst)
            print(f'復元が完了しました:{src} → {dst}')                
            jsonfile.seek(0)
            json.dump(history,jsonfile,ensure_ascii=False,indent=2)
            jsonfile.truncate()
            removedirMode_ONE = 1
            remove_dir(SORTEPATH,LOGPATH,removedirMode_ONE,src)



def files_restore(SORTEPATH,WATCHPATH,JSONPATH,LOGPATH):

    JSONFILEPATH = os.path.join(JSONPATH,'history/history.json')
    
    if not os.path.exists(JSONFILEPATH):
        write_errorlog('notfound_file','history.jsonが見つかりませんでした。',LOGPATH)
        sys.exit(1)

    with open(JSONFILEPATH,'r+',encoding='utf-8') as jsonfile:
        try:
            history = json.load(jsonfile)
        except json.JSONDecodeError:
            write_errorlog('decode_error','history.jsonの読み取りに失敗しました')
            sys.exit(1)
    
    if not history:
        write_errorlog('notfound_file','ロールバックできる履歴がありません。',LOGPATH)
        sys.exit(1)
    
    new_history = []

    for recode in history:
        src = recode['dst']
        dst = recode['src']

        if not os.path.exists(src):
            new_history.append(recode)
            continue

        print(f"戻しています: {src} → {dst}")
        shutil.move(src,dst)
        recode_JSONfile(JSONPATH,LOGPATH,src,dst)


    with open(JSONFILEPATH,'r+',encoding='utf-8') as jsonfile:
        try:
            history = json.load(jsonfile)
            jsonfile.seek(0)
            json.dump(new_history, jsonfile, ensure_ascii=False, indent=2)
            jsonfile.truncate()
        except json.JSONDecodeError:
            write_errorlog('decode_error','history.jsonの読み取りに失敗しました')
            sys.exit(1)
    
    
    removedirMode_ALL = 0
    remove_dir(SORTEPATH,LOGPATH,removedirMode_ALL,None)