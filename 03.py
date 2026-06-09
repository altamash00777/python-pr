import keyword as kw

def isHardKeyword(keyword):
    return kw.iskeyword(keyword.lower())

# hard

print('is hard: ',isHardKeyword('true'))
print('is hard: ',isHardKeyword('as'))
print('is hard: ',isHardKeyword('import'))
print('is hard: ',isHardKeyword('if'))
print('is hard: ',isHardKeyword('else'))


 
 