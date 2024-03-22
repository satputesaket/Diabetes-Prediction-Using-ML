from diabetes.logger import logging 
from diabetes.exception import DiabetesDataException
import sys
try:
    a = 14/"dfg"
except Exception as e:
    logging.error(e)
    raise DiabetesDataException(e,sys) from e