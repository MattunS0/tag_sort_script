from sorter.tag_manager import view_tags,add_tags,remove_tags

def tag_manegement_CLI(PATHS):

    TAGSPATH = PATHS['TAGSPATH']
    LOGPATH = PATHS['LOGPATH']

    while True:
        print("\n--- タグ管理メニュー ---")
        print("1. タグ一覧を見る")
        print("2. タグを追加する")
        print("3. タグを削除する")
        print("4. 終了")
        
        choice = input("番号を入力してください >>> ").strip()

        if choice == "1":
            view_tags(TAGSPATH,LOGPATH)
        elif choice == "2":
            new_tag = input("追加するタグ名（空でキャンセル）: ").strip()
            if new_tag:
                add_tags(TAGSPATH,LOGPATH,new_tag)
            else:
                print("キャンセルしました。")
        elif choice == "3":
            remove_tag = input("削除するタグ名（空でキャンセル）: ").strip()
            if remove_tag:
                remove_tags(TAGSPATH,LOGPATH,remove_tag)
            else:
                print("キャンセルしました。")
        elif choice == "4":
            print("タグ管理メニューを終了します。")
            break
        else:
            print("1〜4 の番号で選択してください。")