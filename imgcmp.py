import numpy as np
from PIL import Image as im
import matplotlib.pyplot as plt


def svd(m: np.matrix):

    rank=np.linalg.matrix_rank(m)
    
    mm_t = np.dot(m, m.T)  
    m_tm = np.dot(m.T, m)  

    eigvals_u, u = np.linalg.eig(mm_t)

    eigvals_v, v = np.linalg.eig(m_tm)

    idx_u = np.argsort(eigvals_u)[::-1]  # Sort in descending order
    idx_v = np.argsort(eigvals_v)[::-1]  # Sort in descending order

    u = u[:, idx_u]
    v = v[:, idx_v]

    eigvals_u = eigvals_u[idx_u]
    eigvals_u = eigvals_u[:rank]
    
    u = u[:, :rank] 
    v = v[:, :rank]


    # Step 6: The singular values are the square roots of the sorted eigenvalues
    singular_values = np.sqrt(np.abs(eigvals_u))
    sigma_matrix = np.diag(singular_values)

    # Step 7: Normalize U and V to make sure they are orthonormal
    u = u / np.linalg.norm(u, axis=0)
    v = v / np.linalg.norm(v, axis=0)

    
    # Step 8: Transpose V to get V^T
    v_t = v.T

    # Return U, Sigma, and V^T
    return u, sigma_matrix, v_t

import os
def dir():
    print("Current Working Directory: ", os.getcwd())

def preprocess(img: str):
    image = im.open(img)
    A = np.array(image, dtype=float) / 255.0
    A = np.dot(A, [0.2989, 0.5870, 0.1140])
    plt.imshow(A)
    plt.axis('off')  # Turn off axis labels
    plt.show()
    return A

def compress(rank: int, image: np.array):
    u,s,v = svd(image)
    print (u.shape)
    print (s.shape)
    print (v.shape)

def main():
    # dir()
    A = preprocess('tj.jpg')
    compress(100, A)

if __name__ =="__main__":
    main()





