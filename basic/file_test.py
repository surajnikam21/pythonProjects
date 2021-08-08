
#File handling - File Object


#Normal way of file accessing
# f = open("C:\\testFileHandling\\test.txt", 'r')
# #print(f.read())   #read whole file
# #print(f.readline())   #reads single line
# print(f.readlines())   #reads single line
# print(f.closed)  #False
# f.close()   #close file after the usage
# print(f.closed)  #True


# print('-----------------')
#print(f.readline())   #reads single line

# print('-----------------')
#print(f.readlines())  #reads whole files stores list.


#File context manager

# with open("C:\\testFileHandling\\test.txt", 'r') as f:
#     #print(f.read())
#     #print(f.readlines())
#     print(f.readline())
#     #print(f.name)
#     #print(f.mode)
#
# print(f.closed)



# with open("C:\\testFileHandling\\test.txt", 'r') as f:
#     for line in f.readlines():
#         print(line)

with open("C:\\testFileHandling\\test.txt", 'r') as f:
    read_to_size = 24
    contents = f.read(read_to_size)   # first 10 chars

    while len(contents) > 0:
        print(contents)
        contents = f.read(read_to_size)   #new 10 chars

