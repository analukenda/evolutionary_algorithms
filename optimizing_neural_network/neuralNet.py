import math


class neuralNet:
    def __init__(self,dim):
        self.dim=dim
        self.numberOfLayers=len(self.dim)

    def nParams(self):
        params=self.dim[0]*self.dim[1]*2
        for i in range(1,self.numberOfLayers-1):
            params+=(self.dim[i]*self.dim[i+1]+self.dim[i+1])
        return params

    def calcOutput(self,x,params):
        if self.nParams() != len(params):
            print('Nije dobar broj parametara')
            exit(1)
        index=0
        inputs=x
        outputs=[]
        for neuron in range(self.dim[1]):
            suma=0.0
            for input in inputs:
                suma+=(math.fabs(input-params[index])/math.fabs(params[index+1]))
                index+=2
            outputs.append(1/(1+suma))
        inputs=outputs
        for layer in range(2,self.numberOfLayers):
            outputs=[]
            for neuron in range(self.dim[layer]):
                output=params[index]
                index+=1
                for input in inputs:
                    output+=(input*params[index])
                    index+=1
                outputs.append(1/(1+math.exp(-output)))
            inputs=outputs
        return outputs

    def calcError(self,data_set,params):
        err=0.0
        for d in data_set.data:
            err_s=0.0
            x=d[0]
            y=d[1]
            o=self.calcOutput(x,params)
            for i in range(len(y)):
                err_s+=math.pow(y[i]-o[i],2)
            err+=err_s
        return err/data_set.getLength()

    def setParams(self,params):
        self.params=params
