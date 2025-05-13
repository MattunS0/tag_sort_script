import os

from datetime import datetime

''' エラー管理メソッド '''

def write_errorlog(errortype,message,LOGPATH):
    print('エラーが発生しました。ログをご確認ください。')
    log_path = get_log_path(LOGPATH)
    with open(log_path,'a',encoding="utf-8") as log:
        log.write(f"[{errortype}] [{datetime.now()}] : {message}\n")



def get_log_path(LOGPATH):
    today = datetime.now().strftime('%Y%m%d'); 
    os.makedirs(LOGPATH,exist_ok=True)
    log_path = os.path.join(LOGPATH,f"{today}_Errorlog.txt")
    return log_path