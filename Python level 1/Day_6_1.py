contents = ['All carrots are slicked \nnicely', 'The carrots sliced \nproperly', 'The soup is ready.']
filenames = ['doc.txt', 'report.txt', 'presentation.txt']

# for file, content in zip(filenames, contents): # convert different list and combine them into single list
#     # but data in for form of tuple
#     # print(file, content)
#     doc = open(f'files/{file}', 'w')
#     doc.writelines(content)
#     doc.close()

from os import path,getcwd,listdir

print(getcwd())
print(listdir())
