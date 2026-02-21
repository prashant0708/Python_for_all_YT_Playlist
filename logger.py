import logging
import os
from from_root import from_root
from datetime import datetime

now = datetime.now().strftime("%Y_%m_%d_%H_%m_%S")

log_file_name= f"{now}.log"

folder= "log_artifact"

os.makedirs(folder, exist_ok=True)

print(from_root()) #C:\Users\prash\Desktop\Python_for_all_YT_Playlist

log_file_path= os.path.join(from_root(),folder,log_file_name)
#C:\Users\prash\Desktop\Python_for_all_YT_Playlist\log_artifact\2026_02_09_23_02_48.log



logging.basicConfig(
    level = logging.INFO, 
    force = True,
    format = "%(asctime)s - level name: %(levelname)s  - file_name: %(filename)s - line_no: %(lineno)s - Message: %(message)s",
    filename=log_file_path,
    filemode ='w'
)