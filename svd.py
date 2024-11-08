import numpy as np

def svd(m: np.matrix):

    rank=np.linalg.matrix_rank(m)
    
    mm_t = np.dot(m, m.T)  
    m_tm = np.dot(m.T, m)  

    eigvals_u, u = np.linalg.eig(mm_t)

    eigvals_v, v = np.linalg.eig(m_tm)

    idx_u = np.argsort(eigvals_u)[::-1]  
    # Sort in descending order
    idx_v = np.argsort(eigvals_v)[::-1]  

    u = u[:, idx_u]
    v = v[:, idx_v]

    eigvals_u = eigvals_u[idx_u]
    eigvals_u = eigvals_u[:rank]
    
    u = u[:, :rank] 
    v = v[:, :rank]


    singular_values = np.sqrt(np.abs(eigvals_u))
    sigma_matrix = np.diag(singular_values)

   
    u = u / np.linalg.norm(u, axis=0)
    v = v / np.linalg.norm(v, axis=0)

    

    v_t = v.T

 
    return u, sigma_matrix, v_t

def main():
    m = np.matrix('1, 0, 5; 3, 4, 15; 5, 6, 25; 7, 8, 35')
    u, s, v_t = svd(m)
    
    print (m)
    print("\n")
    print("U:\n", u)
    print("S:\n", s)
    print("V^T:\n", v_t)
    
    # Reconstruct the matrix from U, S, and V
    reconstructed_m = u @ s @ v_t
    print("\nReconstructed Matrix:\n", reconstructed_m)
    if (np.allclose(reconstructed_m, m)):
        print("Close")
    else:
        print("Not close")

if __name__ == "__main__":
    main()
