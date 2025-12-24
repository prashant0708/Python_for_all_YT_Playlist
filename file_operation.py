## example 1 , create txt file and write something

# file_name = 'content.txt'

# with open(file_name, 'w') as f:
#     f.write("Hello I am learning file read and write operation")
#     f.close()

## example 2 create content.txt in the folder in same dir 

import os 
from pathlib import Path

# dir_name  = 'data'
# file_name = 'log.txt'
# ## data/log.txt

# file_path  = Path(dir_name,file_name )

# print(file_path)

# txt = "This is the second file under that data folder"
# os.makedirs(dir_name, exist_ok =True)

# with open(file_path,'w') as f:
#     f.write(txt)
#     f.close()


    
## example 3 create file in download /data  folder and write some content

# download_dir = Path.home()/'Downloads' #C:\Users\prash\Downloads

# print(download_dir) 

# folder_name  = 'data'

# file_name = 'test.txt'

# file_path = Path(download_dir,folder_name,file_name)

# print(f"File path {file_path}") # C:\Users\prash\Downloads\data\test.txt

# ## create folder data inside the downloads dir

# print(f"file_path parent{ file_path.parent}") ## C:\Users\prash\Downloads\data

# os.makedirs(file_path.parent,exist_ok =True)

# text = " This is the third file created in download dir"

# with open(file_path,'w') as f:
#     f.write(text)
#     f.close()
    
## example 4 perform write operation in exisitng file 

# file_path = r"C:\Users\prash\Downloads\data\test.txt"


# text = "This is the second line in the same file of download"
# text2 = "This is the third line in same file under same write operation"
# print(file_path)
# with open(file_path,'w') as file:
#     file.write(text + "\n")
#     file.write(text2+ "\n")
    
#     file.close()

## example 5 perform append operation into the existing file
# file_path = r"C:\Users\prash\Downloads\data\test.txt"
# text = """Artificial Intelligence (AI) is the ability of computer systems to perform tasks that 
# typically need human intelligence, like learning, reasoning, problem-solving, understanding language,
# and recognizing patterns, by analyzing data to make decisions and predictions, 
# enabling automation and smart applications from virtual assistants to self-driving cars. 
# It's a branch of computer science that creates algorithms to simulate these cognitive functions,
# allowing machines to adapt and improve over time without explicit programming for every scenario."""

# with open(file_path , 'a') as f:
#     f.write(text)
#     f.close()
    


# example 6

# lines = ['This is first line.' , 'This is second line.' ,'This is third line.' ]

# file_path = r"C:\Users\prash\Downloads\data\test.txt"

# with open(file_path,'w') as f:
#     for line in lines:
#         print(line)
#         f.write(line + "\n")
#     f.close()

# example 7

# *****read - file must be available and content must be available

# file_path = r"C:\Users\prash\Downloads\data\test.txt"

# with open(file_path,'r') as f:
#     content= f.read()  ## read all the data from the file at a time
#     f.close()
# print(content)
# print(type(content))

# ****** readlines

# file_path = r"C:\Users\prash\Downloads\data\test.txt"

# with open(file_path,'r') as f:
#     content= f.readlines()  ## readlines will read all the data and make one list
#     f.close()
# print(content)

# print(type(content))

# *******readline
# file_path = r"C:\Users\prash\Downloads\data\test.txt"

# with open(file_path,'r') as f:
#     while True:
#         content= f.readline()## readline , read sigle line at a time
#         if not content:
#             break
#         print(content)
#     f.close()


# print(type(content))

# example 8

## copy content from source file and paste to new file at new destination

# file_path = r"C:\Users\prash\Downloads\data\test.txt"
# dest_path = "example.txt"

# with open(file_path, 'r') as f:
#     content = f.read()
    
# print(f"Data from source file {content}")

# with open(dest_path,'w') as f:
#     f.write(content)
#     f.close()

# ***example 9
## *** Binary read and write >>> used for non txt data

## ** Binary read and write >> used for image , video , pdf
## read image data using binary read 

# img_file_path = r"C:\Users\prash\Downloads\img_thumb.png"

# with open(img_file_path, 'rb') as f:
#     img_data = f.read()
    
# #print(img_data)

# dest_img_path = "img_thumb.jpg"

# with open(dest_img_path, 'wb') as f:
#     f.write(img_data)
# print('Image saved to the dest_img_path ')


# ** Example 10 

## read and write json file 

## write a json file

import json

# user_data = {
#     "name": "John Doe",
#     "age": 30,
#     "email": "john@example.com",
#     "is_active": True,
#     "hobbies": ["coding", "reading", "gaming"]
# }

# file_path_json = "test.json"
# with open(file_path_json, 'w') as f:
#     json.dump(user_data,f,indent=True)
    
# print("file created")


# Example 11

## read a json file

file_path_json = "test.json"
with open(file_path_json, 'r') as f:
    content= json.load(f)
    

print(content)

print(f"Only key of the content {content.keys()}")





    




    











    

    

    





    
