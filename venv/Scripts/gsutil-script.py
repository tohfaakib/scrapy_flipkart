#!C:\Users\H311812Z3R\PersonalProjects\work\flipmart\scarper\scrapy_flipkart\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'gsutil==4.46','console_scripts','gsutil'
__requires__ = 'gsutil==4.46'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('gsutil==4.46', 'console_scripts', 'gsutil')()
    )
