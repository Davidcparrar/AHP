import numpy as np
import pandas as pd
from numpy import linalg as LA


fundamental_scale = {
    1:'Igualmente preferible',
    2:'Entre igualmente y moderadamente preferible',
    3:'Moderadamente preferible',
    4:'Entre moderadamente y fuertemente preferible',
    5:'Fuertemente preferible',
    6:'Entre fuertemente y muy fuertemente preferible',
    7:'Muy fuertemente preferible',
    8:'Entre muy fuertemente y extremadamente preferible',
    9:'Extremadamente preferible'
}

escala = '1:Igualmente preferible \n\
2:Entre igualmente y moderadamente preferible \n\
3:Moderadamente preferible \n\
4:Entre moderadamente y fuertemente preferible \n\
5:Fuertemente preferible \n\
6:Entre fuertemente y muy fuertemente preferible \n\
7:Muy fuertemente preferible \n\
8:Entre muy fuertemente y extremadamente preferible \n\
9:Extremadamente preferible'

data = pd.read_excel('../Demo Propuesta.xlsx', sheet_name= 'Prioridades Nivel Superior', header = 0, index_col = 0, usecols = range(0,9), nrows = 8)

print(data)
priorities = (data.values)

n = data.shape[0]

pairwise_comparisons = n*(n*-1)/2

def eigenvalue(A, v):
    Av = A.dot(v)
    return v.dot(Av)

def power_iteration(A, num_simulations):
    n, d = A.shape

    v = np.ones(d) / np.sqrt(d)
    ev = eigenvalue(A, v)

    for _ in range(num_simulations):
        Av = A.dot(v)
        v_new = Av / np.linalg.norm(Av)

        ev_new = eigenvalue(A, v_new)
        #if np.abs(ev - ev_new) < 0.01:
        #    break

        v = v_new
        ev = ev_new
    return ev_new, v_new

w, v = power_iteration(priorities,1000)
v = v/np.sum(v)
print(w,v)

CI = (w - n)/(n - 1)
RI = 1.41
CR = CI/RI

print(CR)
n_alternativas = 3
Alternativas = pd.read_excel('../Demo Propuesta.xlsx', sheet_name= 'Alternativas', header = [0,1], index_col = 0)



local_priorities = pd.DataFrame()
for i in range(n):
    nombre = Alternativas.columns[i*n_alternativas][0]
    
    X = Alternativas.iloc[:,i*n_alternativas:(i+1)*n_alternativas].values
    w_i, v_i = power_iteration(X,1000)
    v_i = v_i/np.sum(v_i)

    CI = (w_i - n_alternativas)/(n_alternativas - 1)
    RI = 0.58
    CR = CI/RI
    d = pd.DataFrame({nombre:[v[i]] + v_i.tolist()}, index = ['w',1,2,3])
    local_priorities = pd.concat([local_priorities,d], axis = 1)
    
    

local_priorities.to_excel('../local_priorities.xlsx')