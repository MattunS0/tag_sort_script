import sys
import os
sys.path.append(os.path.dirname(__file__))

from clis.rootCLI import root_CLI
from utils.config_manager import init

if __name__ == '__main__':
    CACHE_PATH_FILE = init()
    
    root_CLI(CACHE_PATH_FILE)