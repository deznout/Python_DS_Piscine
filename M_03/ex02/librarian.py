#!/usr/bin/env python

import os
import shutil

if __name__ == '__main__':
    print(os.environ['VIRTUAL_ENV'])
    try:
        if not os.environ['VIRTUAL_ENV'].endswith('hbrent'):
            raise Exception('Incorrect env')
    except Exception as ex:
        print(ex)
    else:
        os.system('pip install beautifulsoup4 PyTest')
        os.system('pip freeze')
        os.system('pip freeze > requirements.txt')
        shutil.make_archive("hbrent", "tar", '../ex00/hbrent')