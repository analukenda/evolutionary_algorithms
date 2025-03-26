import sys
import matplotlib.pyplot as plt

dat=open(sys.argv[1],'r')
lines=dat.readlines()
classes={'100':[],
         '010':[],
         '001':[]
         }
for line in lines:
    arr=line.split()
    y=arr[-3]+arr[-2]+arr[-1]
    x=[]
    for i in range(2):
        x.append(float(arr[i]))
    classes[y].append(x)
colors=['blue','red','orange']
cl=['100','010','001']
for i in range(len(cl)):
    x_1=[]
    x_2=[]
    for x in classes[cl[i]]:
        x_1.append(x[0])
        x_2.append(x[1])
    plt.scatter(x_1,x_2,color=colors[i])
plt.legend(cl)
plt.xlabel('x1')
plt.ylabel('x2')
plt.title('2D prikaz primjera')
plt.show()

