import sys
import neuralnet
import genetic_algorithm
def reading(file,data):
    line = file.readline()
    while (line):
        arr = line.strip().split(',')
        vx = []
        for i in range(len(arr)):
            vx.append(float(arr[i]))

        data.append(vx)
        line = file.readline()
arr=sys.argv
arg_map={}
key=''
for i in range(1,len(arr)):
    if i%2==1:
        key=arr[i][2:]
        if(key=='train' or key=='test'):
            arg_map[key]=r'{}'.format(arr[i+1])
        i+=2
    else:
        arg_map[key]=arr[i]
file=open(arg_map['train'],'r')
test_file=open(arg_map['test'],'r')
d=[]
test_d=[]
input_dim=len(file.readline().strip().split(',')[:-1])
reading(file,d)
test_file.readline()
reading(test_file,test_d)
dim=[int(i) for i in arg_map['nn'].split('s')[:-1]]
iter=int(arg_map['iter'])
popsize=int(arg_map['popsize'])
population=[]
for i in range(popsize):
    neural_net=neuralnet.Neuralnet(input_dim,dim)
    neural_net.setWeights()
    neural_net.propagation(d)
    population.append(neural_net)
population=sorted(population,key=lambda a:a.greska)
no_it=1

while(no_it<iter):
    no_it+=1
    population=genetic_algorithm.gen_alg(population,popsize,int(arg_map['elitism']),float(arg_map['K']),float(arg_map['p']))
    for i in range(popsize):
        population[i].propagation(d)
    population=sorted(population,key=lambda a:a.greska)
    if (no_it % 2000 == 0):
        print('[Train error @{}]: {:.6f}'.format(no_it,population[0].greska))
for i in range(popsize):
    population[i].propagation(test_d)
print('[Test error]: {:.6f}'.format(sorted(population,key=lambda a:a.greska)[0].greska))
