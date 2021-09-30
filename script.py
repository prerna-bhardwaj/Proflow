
def generateDict(fields):
    val = 'return {\n'
    for ele in fields:
        val += "\t'" + ele + "'" + " : self." + ele + ",\n"
    val += '}'
    print(val)


fields = ['project', 'header_image', 'header_desc']

generateDict(fields)
