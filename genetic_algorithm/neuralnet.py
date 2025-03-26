import math

import numpy
class Neuralnet:

    def __init__(self,input_dim,dim):
        self.input_dim=input_dim
        self.dim=dim


    def setWeights(self):
        self.w0_map = []
        self.no_of_layers = len(self.dim)
        for i in range(self.no_of_layers):
            self.w0_map.append(numpy.random.normal(0, 0.01, self.dim[i]).tolist())
        self.w_map = []
        self.w_map.append(numpy.random.normal(0, 0.01, size=(self.input_dim, self.dim[0])).tolist())
        for i in range(self.no_of_layers - 1):
            self.w_map.append(numpy.random.normal(0, 0.01, size=(self.dim[i], self.dim[i + 1])).tolist())
        self.w_map.append(numpy.random.normal(0, 0.01, self.dim[-1]).tolist())



    def propagation(self,d):
        sum_kvadrata=0

        for i in d:
            ulaz=i[:-1]
            for j in range(self.no_of_layers):
                izlaz=[]
                for k in range(self.dim[j]):
                    net=self.w0_map[j][k]
                    for l in range(len(ulaz)):
                        umn=ulaz[l]*self.w_map[j][l][k]
                        net+=umn
                    izlaz.append(1/(1+math.pow(math.e,-net)))
                ulaz=izlaz
            net=0
            for j in range(len(ulaz)):
                umn=ulaz[j]*self.w_map[-1][j]
                net+=umn

            razlika=i[-1]-net
            sum_kvadrata+=math.pow(razlika,2)

        self.greska=sum_kvadrata/len(d)


    def matchParents(self,parent_1,parent_2):
        self.w0_map = []
        self.no_of_layers = len(self.dim)
        parent_1_w0=parent_1.w0_map
        parent_2_w0=parent_2.w0_map
        for i in range(self.no_of_layers):
            w0_layer=[]
            p1_w0=parent_1_w0[i]
            p2_w0=parent_2_w0[i]
            for j in range(len(p1_w0)):
                w0_layer.append((p1_w0[j]+p2_w0[j])/2)
            self.w0_map.append(w0_layer)
        self.w_map = []
        parent_1_w=parent_1.w_map
        parent_2_w=parent_2.w_map
        for i in range(len(parent_1_w)-1):
            w_layer=[]
            p1_w=parent_1_w[i]
            p2_w=parent_2_w[i]
            for j in range(len(p1_w)):
                w_sublayer=[]
                p1_sw=p1_w[j]
                p2_sw=p2_w[j]
                for k in range(len(p1_sw)):
                    w_sublayer.append((p1_sw[k]+p2_sw[k])/2)
                w_layer.append(w_sublayer)
            self.w_map.append(w_layer)
        w_layer=[]
        for i in range(len(parent_1_w[-1])):
            w_layer.append((parent_1_w[-1][i]+parent_2_w[-1][i])/2)
        self.w_map.append(w_layer)

    def __eq__(self, other):
        if self.input_dim==other.input_dim:
            if self.dim==other.dim:
                for i in range(self.no_of_layers):
                    for j in range(len(self.w0_map[i])):
                        if self.w0_map[i][j]!=other.w0_map[i][j]:
                            return False
                for i in range(len(self.w_map)-1):


                    for j in range(len(self.w_map[i])):



                        for k in range(len(self.w_map[i][j])):
                            if self.w_map[i][j][k]!=other.w_map[i][j][k]:

                             return False
                for i in range(len(self.w_map[-1])):
                    if self.w_map[-1][i]!=other.w_map[-1][i]:
                        return False

                return True
        return False






















