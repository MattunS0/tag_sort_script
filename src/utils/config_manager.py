import os
import re
import sys
import json

from utils.logger import write_errorlog
from utils.history_manager import make_JSONfile

''' 初期設定 '''

def init():
    INVALID_CHARS = r'[<>"/|?*\x00-\x1F]'

    try:
        BASEPATH = input("ベースとなるPathを入力してください>>>")
        if not BASEPATH:
            raise ValueError("空の入力は許可されていません。")
        if re.search(INVALID_CHARS,BASEPATH):
            raise OSError("ファイル名やディレクトリ名に無効な文字が含まれています。")
        
    except OSError as osE:
        print(f"OSエラー：{osE}")
        sys.exit(1)
    except ValueError as vaE:
        print(f"入力エラー：{vaE}")
        sys.exit(1)
    except Exception:
        print("予期せぬエラーが発生しました")
        sys.exit(1)
    

    PATHS = {
        "WATCHPATH": os.path.join(BASEPATH, 'watch'),
        "TAGSPATH": os.path.join(BASEPATH, 'tagsdir'),
        "SORTEPATH": os.path.join(BASEPATH, 'sort'),
        "LOGPATH": os.path.join(BASEPATH, 'Errorlogdir'),
        "JSONPATH": BASEPATH,
    }

    if not BASEPATH:
        print("ベースパスが無効です")
        sys.exit(1)

    else:
        CONFIG_FILE = make_base(BASEPATH)

    init_settings(CONFIG_FILE,PATHS)

    return CONFIG_FILE



def make_base(BASEPATH):

    CONFIG_FILE = make_config_file(BASEPATH)
    if os.path.exists(CONFIG_FILE):
        print('すでに初期設定が存在しています。')
        used = input('このまま使用しますか？[y/n]').strip().lower()
        if used == 'y':
            return CONFIG_FILE
        elif used == 'n':
            return CONFIG_FILE
        
        else:
            print('無効な入力です。プログラムを終了します。')
            sys.exit(1)
            
    return CONFIG_FILE



def make_config_file(BASEPATH):

    CONFIGPATH = os.path.join(BASEPATH,'config')
    os.makedirs(CONFIGPATH,exist_ok=True)
    CONFIG_FILE = os.path.join(CONFIGPATH,'cache_path.json')
    return CONFIG_FILE



def init_settings(CONFIG_FILE,PATHS):
    print("\n=== Path設定を始めます ===")
    print("1. 規定値を使用する（初心者向け）")
    print("2. 自分で設定する（上級者向け）")
    try:
        mode = int(input("モードを選択してください [1/2] >>> ").strip())
    except ValueError as vaE:
        print(f"入力エラー:{vaE} 規定値を使用しますか？\n")
        select = input("y/n").strip().lower()
        if select == 'y':
            mode = 1
        elif select == 'n':
            mode = 2
        else:
            print("入力エラーです。プログラムを終了します。")
            sys.exit(1)
    except OSError as osE:
        print(f"OSエラー:{osE}")

    if mode == 1:
        for path in PATHS.values():
            os.makedirs(path,exist_ok=True)
            os.chmod(path,755)
            
        create_tags_file(PATHS["TAGSPATH"],PATHS["LOGPATH"])
        paths = PATHS.copy()

    elif mode == 2:
        paths = {
            "WATCHPATH": input("検索対象までのPATHを入力 >>> ").strip(),
            "TAGSPATH": input("登録したtags.txtファイルまでのPATHを入力 >>> ").strip(),
            "SORTEPATH": input('ソート先のPATHを入力 >>> ').strip(),
            "LOGPATH": input('エラーログを保存したいディレクトリまでのPATHを入力 >>> ').strip(),
            "JSONPATH": input('history.jsonを含むディレクトリのPathを入力').strip(),
        }
        for path in paths.values():
            os.makedirs(path,exist_ok=True)

    else:
        print('無効な入力です。規定値を使用します。')
        for path in PATHS.values():
            os.makedirs(path,exist_ok=True)
            os.chmod(path,755)

    make_JSONfile(paths['JSONPATH'],paths['LOGPATH'])

    with open(CONFIG_FILE,'w',encoding='utf-8') as config_file:
        json.dump(paths,config_file,ensure_ascii=False,indent=2)



def create_tags_file(tagspath, logpath):
    tagspath = os.path.join(tagspath,'tags.txt')
    if not os.path.exists(tagspath):
        try:
            with open(tagspath, 'w', encoding='utf-8') as f:
                f.write("")  # 空のファイルを作成
                os.chmod(tagspath,755)
            print(f"TAGSファイルを作成しました: {tagspath}")
        except Exception as e:
            write_errorlog("create_tags_file_failed", f"{tagspath} の作成に失敗しました: {e}", logpath)
    else:
        print(f"TAGSファイルは既に存在しています: {tagspath}")