# Modified version of Problem 18

def LoadTriangleFromFile(name):
    L = []
    File = open(name)
    for line in File:
        L.append([int(n) for n in line.split(" ")])
    File.close()
    return L

Triangle = LoadTriangleFromFile("triangle.txt")
MaxRows = len(Triangle)
   
for r in range(MaxRows-1, 1, -1):   
    for n in range(0, len(Triangle[r-1])):
        Triangle[r-1][n] += max(Triangle[r][n], Triangle[r][n+1])

print Triangle[0][0] + max(Triangle[1])


