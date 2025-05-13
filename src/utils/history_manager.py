import os
import json
from datetime import datetime

from utils.logger import write_errorlog


''' JSON管理メソッド '''

def make_JSONfile(JSONPATH,LOGPATH):
    mkph = os.path.join(JSONPATH,'history')

    if os.path.exists(mkph):
        print(f"すでに{mkph}にバックアップ用管理ファイルが存在しています！")
        write_errorlog('unmake_directory','ディレクトリ作成ができませんでした',LOGPATH)
        return
    else:
        os.makedirs(mkph,exist_ok=True)
        with open(os.path.join(mkph,'history.json'),"w",encoding='utf-8') as initJSONfile:
            json.dump([],initJSONfile,ensure_ascii=False,indent=2)




def del_JSONfile(JSONPATH,LOGPATH):
    c_fi = os.path.join(JSONPATH,'history','history.json')
    if not os.path.exists(c_fi):
        print("エラーログに追加が発生しました。")
        write_errorlog('notfound_file','ファイルが見つかりませんでした',LOGPATH)
        return

    flag = input("本当にリセットしてもよろしいでしょうか？ yes : y  no : それ以外の入力    :")
    if flag != 'y':
        print('キャンセルしました')
        return
    try:
        rmJSON = os.path.join(JSONPATH,'history/history.json')
        rmHistroyDir = os.path.join(JSONPATH,'history')
        os.remove(rmJSON)
        os.rmdir(rmHistroyDir)
    except Exception as e :
        write_errorlog('ExceptionError',f'{e}',LOGPATH)



def recode_JSONfile(JSONPATH,LOGPATH,src,dst):
    history = []
    JSONFILEPATH = os.path.join(JSONPATH,'history','history.json')
    if os.path.exists(JSONFILEPATH):
        try:
            with open(JSONFILEPATH,"r+",encoding='utf-8') as jsonfile:
                
                history = json.load(jsonfile)
                history.append({
                "src": src,
                "dst": dst,
                "timestamp": datetime.now().isoformat()
                })
                jsonfile.seek(0)
                json.dump(history,jsonfile,indent=2,ensure_ascii=False)
                jsonfile.truncate()

        except json.JSONDecodeError:
            print("エラーログに追記が発生しました。")
            write_errorlog('ExceptionError','不正な形式です',LOGPATH)
            history = []
    else:
        print("エラーログに追記が発生しました。")
        write_errorlog('notfound_file','ファイルが見つかりませんでした',LOGPATH)