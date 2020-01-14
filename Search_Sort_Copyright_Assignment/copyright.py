import sys
import re
import os
def copyright_import(cpyright):
    with open(cpyright, "r") as f:
        cpy_lst = f.read()
    return cpy_lst

def code_import(cpyright, codename, new_file_ending = None):
    with open(codename, "r") as f:
        foo = str(f.read())
    ans = re.sub('BEGIN COPYRIGHT(.*?)END COPYRIGHT',"BEGIN COPYRIGHT\n"+copyright_import(cpyright)+"END COPYRIGHT",foo, flags=re.DOTALL)
    override = open(codename, "w")
    override.write(ans)
    if new_file_ending != None:
        print(new_file_ending)
        new_total_name = re.sub("\.[a-z]*", new_file_ending, codename)
        os.rename(codename, new_total_name)

def main():
    count = 0
    new_file_ending = ""
    for x in sys.argv:
        if x == "-c":
            file_type = str(sys.argv[count + 1])
        if x == "-u":
            new_file_ending = str(sys.argv[count + 1])
        count += 1
    if len(sys.argv) <= 7 and len(sys.argv) >= 2:

        cpyright = sys.argv[1]
        if os.path.isdir(sys.argv[2]):
 
            for x in os.listdir(sys.argv[2]):
                if file_type != None:
                    if x.endswith(file_type):
                        code_import(cpyright, str(sys.argv[2] + x), new_file_ending)
                else:
                    code_import(cpyright, str(sys.argv[2] + x), new_file_ending)
        elif os.path.isfile(sys.argv[2]):
            code_import(cpyright, sys.argv[2], new_file_ending)
            print("asdf")
    else:
        print("Too many or too few aguments")
            
        return None

main()
