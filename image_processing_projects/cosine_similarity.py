import numpy as np
A = [5,5,5,5,5]
B = [1,2,3,4,5]

qd = np.dot(np.vstack(A), np.vstack(B).T)
rel = 1
for r in np.amax(qd, axis=1):
    rel *= r
print(r)
#Calculate cosine distance between each word vectors in both vector sets (A and B)
#Find pairs from A and B with maximum score
#Multiply or sum it to get similarity score of A and B