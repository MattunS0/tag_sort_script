from sorter.restore import files_restore,remove_dir,restore_prev_onestep


def restore_prev_CLI (PATHS):

    SORTEPATH = PATHS['SORTEPATH']
    LOGPATH = PATHS['LOGPATH']
    JSONPATH = PATHS['JSONPATH']
    WATCHPATH = PATHS['WATCHPATH']

    print('--- リストアモード選択画面 ---')
    print("1. 1ソート分戻す")
    print("2. 1ステップ戻す")
    print("3. 準備中")
    choice = input("選択してください: ").strip()
    
    if choice == '1':
        files_restore(SORTEPATH,WATCHPATH,JSONPATH,LOGPATH)
    elif choice == '2':
        restore_prev_onestep(SORTEPATH,JSONPATH,LOGPATH)
    elif choice == '3':
        return
    else:
        print("無効な入力です。")
