import json


from sorter.sorter import sorted_script
from clis.restoreCLI import restore_prev_CLI
from clis.tagCLI import tag_manegement_CLI
from clis.jsonCLI import JSON_manegement_CLI


def root_CLI(CACHE_PATH_FILE):
    with open (CACHE_PATH_FILE,'r+',encoding='utf-8') as f:
        PATHS = json.load(f)
    print('--- モード選択画面 ---')
    print('1. ファイル整理（sort）')
    print('2. 元に戻す（restore）')
    print('3. タグの管理(tags_management)')
    print('4. JSON管理 (JSON_management)')
    print('5. 準備中')
    choice = input("選択してください: ").strip()

    if choice == '1':
        sorted_script(PATHS)
    elif choice == '2':
        restore_prev_CLI(PATHS)
    elif choice == '3':
        tag_manegement_CLI(PATHS)
    elif choice == '4':
        JSON_manegement_CLI(PATHS)
    elif choice == '5':
        print('現在準備中です')
    else:
        print("無効な入力です。")