import numpy as np

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

criteria = {0:'Visibility',1:'Competition',2:'Frequency',3:'Rental cost'}
n = len(criteria)
pairwise_comparisons = n*(n*-1)/2

# for i in criteria.keys():
#     comp = [x for x in criteria.keys() if x > i]
#     for j in comp:
#         print("De acuerdo a la siguiente escala: ")
#         print("-------------------------------------")
#         print(escala)
#         print("-------------------------------------")
#         print("Evalue los criterios")
#         text = int(input(criteria[i] + "vs" + criteria[j]))

priorities =  np.matrix([[1, 1/4.0, 1/5.0, 2],
                        [4, 1, 1/2.0, 1],
                        [5, 2, 1, 4],
                        [1/2.0, 1, 1/4.0, 1],])
print(priorities)
