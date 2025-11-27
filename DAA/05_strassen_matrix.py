def matrix_multiply_strassen(A, B):
    """
    Strassen's Matrix Multiplication: Optimized D&C approach
    Time Complexity: O(n^2.807) vs naive O(n³) | Space Complexity: O(n²)
    Only works for square matrices of size 2^k x 2^k
    """
    n = len(A)
    
    # Base case: 1x1 matrices
    if n == 1:
        return [[A[0][0] * B[0][0]]]
    
    # Divide matrices into 4 quadrants each
    A11, A12, A21, A22 = divide_matrix(A)
    B11, B12, B21, B22 = divide_matrix(B)
    
    # Calculate 7 intermediate products using Strassen's formulas
    P1 = matrix_multiply_strassen(add_matrices(A11, A22), add_matrices(B11, B22))
    P2 = matrix_multiply_strassen(add_matrices(A21, A22), B11)
    P3 = matrix_multiply_strassen(A11, subtract_matrices(B12, B22))
    P4 = matrix_multiply_strassen(A22, subtract_matrices(B21, B11))
    P5 = matrix_multiply_strassen(add_matrices(A11, A12), B22)
    P6 = matrix_multiply_strassen(subtract_matrices(A21, A11), add_matrices(B11, B12))
    P7 = matrix_multiply_strassen(subtract_matrices(A12, A22), add_matrices(B21, B22))
    
    # Combine results using Strassen's formulas
    C11 = add_matrices(subtract_matrices(add_matrices(P1, P4), P5), P7)
    C12 = add_matrices(P3, P5)
    C21 = add_matrices(P2, P4)
    C22 = add_matrices(subtract_matrices(add_matrices(P1, P3), P2), P6)
    
    # Merge quadrants to form result matrix
    return merge_matrix([C11, C12, C21, C22])

def divide_matrix(matrix):
    """Helper: Divide matrix into 4 quadrants"""
    n = len(matrix) // 2
    A11 = [row[:n] for row in matrix[:n]]
    A12 = [row[n:] for row in matrix[:n]]
    A21 = [row[:n] for row in matrix[n:]]
    A22 = [row[n:] for row in matrix[n:]]
    return A11, A12, A21, A22

def add_matrices(A, B):
    """Helper: Add two matrices element-wise"""
    n = len(A)
    return [[A[i][j] + B[i][j] for j in range(n)] for i in range(n)]

def subtract_matrices(A, B):
    """Helper: Subtract matrix B from A element-wise"""
    n = len(A)
    return [[A[i][j] - B[i][j] for j in range(n)] for i in range(n)]

def merge_matrix(quadrants):
    """Helper: Merge 4 quadrants into single matrix"""
    C11, C12, C21, C22 = quadrants
    n = len(C11)
    result = [[0] * (2*n) for _ in range(2*n)]
    
    for i in range(n):
        for j in range(n):
            result[i][j] = C11[i][j]
            result[i][j+n] = C12[i][j]
            result[i+n][j] = C21[i][j]
            result[i+n][j+n] = C22[i][j]
    
    return result

# Driver code
if __name__ == "__main__":
    A = [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10, 11, 12],
         [13, 14, 15, 16]]
    
    B = [[1, 0, 1, 0],
         [0, 1, 0, 1],
         [1, 0, 1, 0],
         [0, 1, 0, 1]]
    
    result = matrix_multiply_strassen(A, B)
    print("Strassen's Matrix Multiplication Result:")
    for row in result:
        print(row)
