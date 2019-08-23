print("Created by Diyorbek Vakhidov 2019y")
n= int(input("n="))
array=[]
for i in range(n):
    s=[]
    for j in range(n):
        s.append(float(input("A["+str(i)+"]["+str(j)+"]=")))
    array.append(s)

print("Chop etish")
for i in range(len(array)):
    for j in range(len(array)):
        print(array[i][j], end=" ")
    print()

for k in range(0, len(array)-1):
    for i in range(1+k, len(array)):
        if array[i][k]!=0:
            c=array[i][k]/array[k][k]
            for j in range(k, len(array)):
                array[i][j]=array[i][j]-c*array[k][j]
    print(str(k+1)+"-Qadam====")
    for i in range(len(array)):
        for j in range(len(array)):
            print(array[i][j], end=" ")
        print()

c=1
for i in range(len(array)):
    c*=array[i][i]
if c==-0.0:
    c=0.0
    print("Teskari matritsa:"+str(c))
else:
    print("Teskari matritsa:"+str(c))


input()