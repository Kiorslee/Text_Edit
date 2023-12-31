import os

role_definition = "01和02都是土生土长的生活在美国的本地人。"

"""

"""

testpath = "./Result"
for root, dirs, files in os.walk(testpath):
    print("root:", root)
    print("dirs:", dirs)
    print("files:", files)
import os
root_path = os.getcwd()
count=0
for inner_path, dirlist, filmlist in os.walk(os.path.join(root_path, 'Result')):
    for filmname in filmlist:
        filmpath = inner_path + "/" + filmname
        count=count+1
        print(filmpath)
print(count)

import os
root_path = os.getcwd()

inner_path, dirlist, php,filmlist = os.walk(os.path.join(root_path, 'Result'))
print(filmlist)

