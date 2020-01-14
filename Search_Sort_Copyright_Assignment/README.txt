This assignment had the purpose of teaching us methods of sorting and searching in python3. The last part of the assignment was also to create a program that would automatically insert copyright information in a file or all files in a folder between certain markers if any exist. In this example between "BEGIN COPYRIGHT" and "END COPYRIGHT". It also supports only targeting a certain file ending with the "-c" flag and changing the ending of the files with the "-u" flag.

Usage in its simplest form:
>> python3 copyright.py [info_file] [target_file/directory]

Usage with name change:
>> python3 copyright.py [info_file] [target_file/directory] -u [new_ending]

Example in this directory:
>> python3 copyright.py doc1py testfil.txt -u .py


Made in 2018, by Andrei Moga(Me) and William.
