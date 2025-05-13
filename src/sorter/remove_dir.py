import os
import shutil

from utils.logger import write_errorlog


def remove_dir(SORTEPATH,LOGPATH,flag,src):

    if flag == 0:
        remove_dirs(SORTEPATH,LOGPATH,src)



def remove_dirs(SORTEPATH,LOGPATH,src):
    if not os.path.exists(SORTEPATH):
        print("エラーログに追記が発生しました。")
        write_errorlog('notfound_folder', f"指定されたフォルダが存在しません → {SORTEPATH}", LOGPATH)
        return
    
    for root,dirs,_ in os.walk(SORTEPATH,topdown=False):
         for dir in dirs:
            dirPath = os.path.join(root,dir)
            if not os.listdir(dirPath):
                os.rmdir(dirPath)
                print(f'空のディレクトリを削除しています...:{dirPath}')
            else:
                print("エラーログに追記が発生しました。")
                write_errorlog('undelete_folder',f"削除できませんでした → {dirPath}",LOGPATH)
                return

    if not os.listdir(SORTEPATH):
        shutil.rmtree(SORTEPATH)
        print(f'整理ルートフォルダを削除しています...{SORTEPATH}')
    else:
        print("エラーログに追記が発生しました。")
        write_errorlog('undelete_rootfolder',f"削除できませんでした → {SORTEPATH}",LOGPATH)
        return
    


def one_remove_dir(SORTEPATH,LOGPATH,src):
    restore_dir = os.path.dirname(src)
    if os.path.exists(restore_dir) and not os.listdir(restore_dir):
        shutil.rmtree(restore_dir)
        print(f'復元元の空ディレクトリを削除しました: {restore_dir}')
        return

    else:
        print("エラーログに追記が発生しました。")
        write_errorlog('undelete_folder',f"削除できませんでした → {restore_dir}",LOGPATH)
        return