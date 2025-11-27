def is_valid_parentheses(s):
    """
    Valid Parentheses: Check if brackets are balanced and properly nested
    Time Complexity: O(n) | Space Complexity: O(n) for stack
    Supports (), {}, []
    """
    # Stack to track opening brackets
    stack = []
    
    # Mapping of closing to opening brackets
    bracket_map = {')': '(', '}': '{', ']': '['}
    
    # Process each character
    for char in s:
        # If opening bracket, push to stack
        if char in bracket_map.values():
            stack.append(char)
        # If closing bracket
        elif char in bracket_map:
            # If stack empty, no matching opening bracket
            if not stack:
                return False
            # If top doesn't match, brackets mismatched
            if stack[-1] != bracket_map[char]:
                return False
            # Pop matching opening bracket
            stack.pop()
    
    # Stack should be empty if all brackets matched
    return len(stack) == 0

def count_valid_parentheses(s):
    """
    Count valid parentheses combinations in string
    """
    count = 0
    # Try removing each character and check if valid
    for i in range(len(s)):
        temp = s[:i] + s[i+1:]
        if is_valid_parentheses(temp):
            count += 1
    return count

def generate_valid_parentheses(n):
    """
    Generate all valid parentheses combinations for n pairs
    Time Complexity: O(4^n / sqrt(n)) | Space Complexity: O(n)
    """
    result = []
    
    def backtrack(current, open_count, close_count):
        """
        Backtracking: Build valid combinations
        open_count: number of opening brackets used
        close_count: number of closing brackets used
        """
        # Base case: generated valid combination
        if open_count == n and close_count == n:
            result.append(current)
            return
        
        # Add opening bracket if not exceeded
        if open_count < n:
            backtrack(current + '(', open_count + 1, close_count)
        
        # Add closing bracket if we have opening brackets to match
        if close_count < open_count:
            backtrack(current + ')', open_count, close_count + 1)
    
    backtrack('', 0, 0)
    return result

# Driver code
if __name__ == "__main__":
    # Test valid parentheses
    test_cases = [
        "(){}[]",
        "([{}])",
        "([)]",
        "{[}]",
        ""
    ]
    
    print("Valid Parentheses Check:")
    for test in test_cases:
        result = is_valid_parentheses(test)
        print(f"'{test}' -> {result}")
    
    # Generate valid combinations
    print("\nGenerate Valid Parentheses (n=3):")
    combinations = generate_valid_parentheses(3)
    for combo in combinations:
        print(combo)
