def solve_8_queens():
    """
    8-Queens Problem using Backtracking: Place 8 queens such that none attack each other
    Time Complexity: O(N!) | Space Complexity: O(N) for recursion stack
    """
    # Board represented as list where index=row, value=column
    board = [-1] * 8
    solutions = []
    
    def is_safe(row, col):
        """Check if placing queen at (row, col) is safe"""
        # Check all previously placed queens
        for prev_row in range(row):
            prev_col = board[prev_row]
            
            # Check column conflict
            if prev_col == col:
                return False
            
            # Check diagonal conflict
            if abs(prev_row - row) == abs(prev_col - col):
                return False
        
        return True
    
    def backtrack(row):
        """Backtracking function to place queens"""
        # Base case: all 8 queens placed successfully
        if row == 8:
            solutions.append(board[:])  # Store solution
            return
        
        # Try placing queen in each column of current row
        for col in range(8):
            # If position is safe, place queen
            if is_safe(row, col):
                board[row] = col  # Place queen
                backtrack(row + 1)  # Move to next row
                board[row] = -1  # Backtrack: remove queen
    
    backtrack(0)  # Start from row 0
    return solutions

def print_8_queens(board):
    """Helper: Display board with queens"""
    for row in range(8):
        line = ""
        for col in range(8):
            if board[row] == col:
                line += "Q "  # Queen
            else:
                line += ". "  # Empty
        print(line)
    print()

# Driver code
if __name__ == "__main__":
    solutions = solve_8_queens()
    print(f"Total solutions for 8-Queens: {len(solutions)}\n")
    
    # Print first solution
    if solutions:
        print("First solution:")
        print_8_queens(solutions[0])
