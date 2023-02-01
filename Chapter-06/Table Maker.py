tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
def printTable(tableData):
    width=[0]*len(tableData)
    k=0
    while k<len(tableData):
        width[k]=len(max(tableData[k]))
        k = k + 1

    
    for x in range(len(tableData[0])):
        for y in range(len(width)):
            print(tableData[y][x].rjust(width[y]), end=' ')
        print(end='\n')
printTable(tableData)
    