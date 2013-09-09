from fte.settings import *

import os

BASE_DIR = '/XXXX/fte/fasta_title_editor/fte/fte_main/'
TMP_DIR = '/tmp/'


TEMPLATE_DIRS = (
   os.path.join(BASE_DIR,'templates'),
)

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR, "static"),
)