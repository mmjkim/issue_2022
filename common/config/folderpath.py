
import os
from pathlib import Path

ROOT_DIR = os.path.dirname(os.path.abspath(__file__)).split('\\')
ROOT_PATH = ROOT_DIR[0] + '\\issue_2022'

DATA_PATH = 'data'
LOG_PATH = 'LOG'

DATA_COLL_PATH = '01_수집데이터'
DATA_USE_PATH = '02_분석데이터'
DATA_RESULT_PATH = '03_결과데이터'
DATA_API_PATH = '99_API'

PRE_DATA_PATH = 'PREPROCESSING'

ANLA_RESULT_PATH = 'ANLA_RESULT'
QGIS_RESULT_PATH = 'QGIS_RESULT'
PRED_RESULT_PATH = 'PRED_RESULT'


