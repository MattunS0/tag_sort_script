from utils.history_manager import make_JSONfile,del_JSONfile

def JSON_manegement_CLI(PATHS):

    LOGPATH = PATHS['LOGPATH']
    JSONPATH = PATHS['JSONPATH']

    print('--- JSON管理画面 ---')
    print('1. JSONファイルを生成')
    print('2. JSONファイルの削除')
    choice = input("選択してください: ").strip()
    
    if choice == '1':
        make_JSONfile(JSONPATH,LOGPATH)
    elif choice == '2':
        del_JSONfile(JSONPATH,LOGPATH)
    else:
        print("無効な入力です。")