import sys
from dataset import dataset
from neuralNet import neuralNet
from genAlgorithm import genAlgorithm
from datetime import datetime

data_set=dataset(sys.argv[1])
neural_net=neuralNet([2,8,3])
start=datetime.now()
success=genAlgorithm(1000000,50,0.0000001,10).training(neural_net,data_set)
end=datetime.now()

file=open('2x8x3_params.txt','w')
for param in neural_net.params:
    file.write(str(param)+'\n')
print('Trajanje treniranja: '+str(end-start))
print('Treniranje uspjesno: '+str(success))
correct=0
not_correct=0
for data in data_set.data:
    x=data[0]
    y=data[1]
    o=neural_net.calcOutput(x,neural_net.params)
    o_pom=[]
    for _o in o:
        if _o < 0.5:
            o_pom.append(0)
        else:
            o_pom.append(1)
    if y==o_pom:
        correct+=1
    else:
        not_correct+=1
    y=str(y[0])+str(y[1])+str(y[2])
    o = str(o_pom[0]) + str(o_pom[1]) + str(o_pom[2])
    print('x = '+str(x)+', y = '+y+', o = '+str(o))
print('Broj tocno klasificiranih '+str(correct)+', broj netocno klasificiranih '+str(not_correct))