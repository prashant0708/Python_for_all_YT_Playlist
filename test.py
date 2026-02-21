
from logger import logging
def calculator(a,b):
    try:
        logging.info("received paramater a and b")
        if a<b:
            logging.warning("passed b parameter is smaller than a so divison can't be possible")
        else:
            result= a/b
            logging.info("Division is done")
            return result
    except Exception as e:
        logging.error(f"There is error {e}")
        
        
result = calculator(a=15,b=30)