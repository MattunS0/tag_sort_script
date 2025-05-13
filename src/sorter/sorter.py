import os
import shutil

from utils.history_manager import recode_JSONfile
from utils.logger import write_errorlog


''' ファイル抽出系メソッド '''

def load_valid_tags(TAGSPATH):
    tags_cash = []
    seen = set()
    TAGSPATH = TAGSPATH + '/tags.txt'
    with open(TAGSPATH,encoding="utf-8") as tags:
        for line in tags:
            tag = line.strip()
            if tag and tag not in seen:
                tags_cash.append(tag)
                seen.add(tag)
    return tags_cash



def filename_extracted(WATCHPATH):
    files = os.listdir(WATCHPATH)
    return files



def tag_extracting_from_filename(filename):
    name,_ = os.path.splitext(filename)
    file_tags = str(name).split('_')[1:]
    return file_tags




''' メイン機能1 メソッド '''

def sorted_script(PATHS):
    file_tags = []
    tags = set()

    SORTEPATH = PATHS['SORTEPATH']
    LOGPATH = PATHS['LOGPATH']
    JSONPATH = PATHS['JSONPATH']
    WATCHPATH = PATHS['WATCHPATH']
    TAGSPATH = PATHS['TAGSPATH']
    tags = load_valid_tags(TAGSPATH)

    for curDir,_,files in os.walk(WATCHPATH):
        for filename in files:
            filepath = os.path.join(curDir,filename)
            file_tags = tag_extracting_from_filename(filename)
            
            if all(tag in tags for tag in file_tags):
                targetdir = os.path.join(SORTEPATH,*file_tags)
                os.makedirs(targetdir,exist_ok = True)
                afterpath = os.path.join(targetdir,filename)
                shutil.move(filepath,afterpath)
                print(f"移動しています : {filepath} → {afterpath}")
                recode_JSONfile(JSONPATH,LOGPATH,filepath,afterpath)

            else:
                print("エラーログに追記が発生しました。")
                write_errorlog('unmatch_tags',f"{filename} : タグが不一致です → {tags}",LOGPATH)
