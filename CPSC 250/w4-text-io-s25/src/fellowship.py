"""
Demo some reading of fellowship.txt

Modify your Run-Edit Configuration to point to the project folder, not src!
"""

import os
file_path = os.path.join("..","data","fellowship.txt")
print(file_path)


file = open(file_path)
lines = file.readlines()
file.close() # If you open, better close
print(lines)


# Phase 2 - practice with the "with-as" pattern
# with open(file_path) as file:
#     lines = file.readlines()
# # Close is automatic with "with"

# print(lines) # end='') # lines still include newline, so we skip lines; can set the end char
#
# for line in lines:
#     print(line.strip())
#
#
# print(80*"-")
# for ndx in range(len(lines)):
#     print(lines[ndx].strip())
#
# print(80*"-")
# for ndx, line  in enumerate(lines):
#     print("{} : {}".format(ndx, line.strip()))
