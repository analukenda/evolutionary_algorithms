import random
import neuralnet
import numpy
import Parents
def gaussian(K,p):
    rand_p = round(random.uniform(0, 1), 30)
    if rand_p <= p:
        return float(numpy.random.normal(0, K))
    return False

def gen_alg(population,popsize,elitism,K,p):
    new_population = []
    for i in range(elitism):
        new_population.append(population[i])
    dijeljenik=[]

    sum_fit=0
    for i in population:
        gr=i.greska
        sum_fit+=gr
        dijeljenik.append(gr)
    donj_gr=0
    prob_sel={}
    for i in range(popsize):
        ps=dijeljenik[popsize-1-i]/sum_fit
        gornj_gr=ps+donj_gr
        prob_sel[(donj_gr,gornj_gr)]=population[i]
        donj_gr=gornj_gr

    already_matched=[]
    while(len(new_population)<popsize):
        found_unmatched=False
        while(found_unmatched == False):
            rand_p=random.uniform(0,1)
            parent_1=None
            for j in prob_sel.keys():
                if rand_p>=j[0] and rand_p<j[1]:
                    parent_1=prob_sel[j]
                    break
            parent_2=parent_1
            while parent_1==parent_2:
                rand_p = random.uniform(0, 1)
                for j in prob_sel.keys():
                    if rand_p >= j[0] and rand_p < j[1]:
                        parent_2 = prob_sel[j]
                        break
            parents=Parents.Parents(parent_1,parent_2)
            if not parents in already_matched:
                already_matched.append(parents)
                found_unmatched=True


        kid=neuralnet.Neuralnet(parent_1.input_dim,parent_1.dim)
        kid.matchParents(parent_1,parent_2)


        for i in range(len(kid.w0_map)):
            for j in range(len(kid.w0_map[i])):
                rand_noise=gaussian(K,p)
                if rand_noise!=False:
                    kid.w0_map[i][j]+=rand_noise


        for i in range(len(kid.w_map)-1):
            for j in range(len(kid.w_map[i])):
                for k in range(len(kid.w_map[i][j])):
                    rand_noise = gaussian(K, p)
                    if rand_noise != False:
                        kid.w_map[i][j][k] += rand_noise
        for i in range(len(kid.w_map[-1])):
            rand_noise = gaussian(K, p)
            if rand_noise != False:
                kid.w_map[-1][i] += rand_noise

        new_population.append(kid)

    return new_population





