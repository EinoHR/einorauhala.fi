import os

uf = 'temp_unfinisheds'
content = 'content/unfinisheds/'

biggest_cont_index = 0
for file in os.listdir(content):
    try:
        if int(file) > biggest_cont_index:
            biggest_cont_index = int(file)
    except:
        pass

for file in os.listdir(uf):
    file_path = os.path.join(uf, file)
    time = os.path.getmtime(file_path)
    
    biggest_cont_index += 1
    newdir = content + str(biggest_cont_index)
    os.mkdir(newdir)
    
    _, file_ext = os.path.splitext(file)
    
    newfile_name = 'media' + file_ext 
    newfile_path = newdir + '/' + newfile_name
    os.rename(file_path, newfile_path)
    
    
    indexfile_path = newdir + '/index.md'
    indexfile = open(indexfile_path, 'w+')
    indexfile.write(f"""\
---
cover: '/unfinisheds/{biggest_cont_index}/{newfile_name}'
title: '{biggest_cont_index}'
date: {time}
categories:
    - Unfinisheds
draft: false
---

![]({newfile_name})

\
                """)