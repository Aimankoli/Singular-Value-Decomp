import numpy as np

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

def main():
    m = np.matrix('1, 2, 1, 0; 2, 3, 10, 4; 1, 10, 1, 3; 0, 4, 3, 0')
    u, s, v_t = svd(m)
    
    print("U:\n", u)
    print("S:\n", s)
    print("V^T:\n", v_t)
    
    # Reconstruct the matrix from U, S, and V^T
    reconstructed_m = u @ s @ v_t
    print("\nReconstructed Matrix:\n", reconstructed_m)
    if (np.allclose(reconstructed_m, m)):
        print("Close")
    else:
        print("No")

if __name__ == "__main__":
    main()
