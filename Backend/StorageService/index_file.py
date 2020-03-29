from StorageService.DBExecutor import *
import os
from StorageService.helpers import *

def index_file():
    for dir, subdir, files in os.walk('../FILES'):
        for f in files:
            print(f)
            filepath = os.path.abspath(os.path.join(dir, f))
            md5_sum = read_hash(filepath)
            add_file(f, filepath, 'IVANCHUTCHEV', f.split('.')[-1], md5_sum)


index_file()