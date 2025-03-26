import math
import random

import numpy as np

class genAlgorithm:

    def __init__(self,max_iter,population_size,max_err,k):
        self.max_iter=max_iter
        self.population_size=population_size
        self.max_err=max_err
        self.k=k
        self.crossoverMethods=[self.simpleArithmetic,self.wholeArithemitc,self.simulatedBinary]
        self.t=[4,3,2]
        self.mutationMethods=[self.additiveGaus,self.additiveGaus,self.substGauss]
        self.ps=[0.3,0.1,0.1]
        self.vars=[0.01,0.06,0.02]

    def training(self,neural_net,data_set):
        population=[]
        for i in range(self.population_size):
            chromosom=[random.uniform(-2,2) for j in range(neural_net.nParams())]
            population.append(chromosom)
        errors=self.calcErrors(population,neural_net,data_set)
        eval=self.evaluate(errors)
        if eval[0][1] <=self.max_err:
            neural_net.setParams(population[eval[0][0]])
            return True
        iter=0
        while(iter<self.max_iter):
            if iter%100==0:
                print(str(iter)+' '+str(eval[0][1]))
            iter+=1
            fitness=self.calcFitness(errors)
            new_population=[]
            for i in range(self.k):
                new_population.append(population[eval[i][0]])
            while(len(new_population)<self.population_size):
                parents = self.selection(population,fitness)
                children = self.crossoverMethods[random.randint(0,1)](parents)
                mutants = self.mutation(children)
                for mutant in mutants:
                    new_population.append(mutant)
            errors=self.calcErrors(new_population,neural_net,data_set)
            eval=self.evaluate(errors)
            if eval[0][1] <= self.max_err:
                neural_net.setParams(new_population[eval[0][0]])
                return True
            population=new_population
        neural_net.setParams(population[eval[0][0]])
        return False

    def calcErrors(self,population,neural_net,data_set):
        errors=[]
        for i in range(self.population_size):
            errors.append(neural_net.calcError(data_set,population[i]))
        return errors

    def evaluate(self,errors):
        dictionary=enumerate(errors)
        dictionary=sorted(dictionary,key=lambda x:x[1])
        return dictionary

    def selection(self,population,fitness):
        sum_fitness=sum(fitness)
        lengths=[fitness[0]/sum_fitness]
        for solution in fitness[1:]:
            lengths.append((solution/sum_fitness)+lengths[-1])
        parents=[]
        rand=random.random()
        for i in range(self.population_size):
            if rand<=lengths[i]:
                parents.append(population[i])
                break
        while(len(parents) < 2):
            rand = random.random()
            for i in range(self.population_size):
                if rand <= lengths[i]:
                    if population[i] != parents[0]:
                        parents.append(population[i])
                    break
        return parents

    def calcFitness(self,errors):
        fitness=[]
        for err in errors:
            fitness.append(1000*(1/(1+err)))
        return fitness

    def simpleArithmetic(self,parents):
        point=random.randint(1,len(parents[0])-1)
        child_1=parents[0][:point]
        for i in range(point,len(parents[0])):
            child_1.append((parents[0][i]+parents[1][i])/2)
        child_2=[]
        for i in range(point):
            child_2.append((parents[0][i]+parents[1][i])/2)
        child_2+=parents[1][point:]
        return [child_1,child_2]

    def wholeArithemitc(self,parents):
        child=[]
        for i in range(len(parents[0])):
            child.append((parents[0][i]+parents[1][i])/2)
        return [child]

    def simulatedBinary(self,parents):
        child=[]
        alpha=random.random()
        for i in range(len(parents[0])):
            child.append((1-alpha)*parents[0][i]+alpha*parents[1][i])
        return [child]

    def setT(self,index,t):
        t_pom=self.t.copy()
        t_pom[index]=t
        if sum(t_pom)>0:
            self.t[index]=t
        else:
            print('Krivo zadan t!')

    def mutation(self,children):
        mutants=[]
        sum_t = sum(self.t)
        lengths=[self.t[0]/sum_t]
        for t in self.t[1:]:
            lengths.append((t/sum_t)+lengths[-1])
        for child in children:
            rand=random.random()
            for i in range(len(self.t)):
                if rand<=lengths[i]:
                    mutant=[]
                    for x in child:
                        mutant.append(self.mutationMethods[i](self.ps[i],self.vars[i],x))
                    mutants.append(mutant)
                    break
        return mutants

    def additiveGaus(self,p,var,x):
        if random.random()<=p:
            pass
            x+=np.random.normal(0.0,math.sqrt(var))
        return x

    def substGauss(self,p,var,x):
        if random.random()<=p:
            x=np.random.normal(0.0,math.sqrt(var))
        return x










