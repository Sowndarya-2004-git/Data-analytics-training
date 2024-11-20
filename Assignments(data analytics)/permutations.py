import math
from itertools import permutations

def calculate_permutation():
    print("\n=== Permutation Calculator ===")
    
    # Ask user which type of permutation to calculate
    print("\nSelect Permutation Type:")
    print("1. Regular Permutation (nPr)")
    print("2. Permutation with all n items (n!)")
    print("3. Permutation with Repetition")
    choice = input("Enter your choice (1-3): ")
    
    if choice == '1':
        # Calculate nPr
        n = int(input("\nEnter the total number of items (n): "))
        r = int(input("Enter the number of items to arrange (r): "))
        
        if r > n:
            print("Error: r cannot be greater than n")
            return
            
        result = math.perm(n, r)
        formula = f"{n}P{r} = {n}!/{(n-r)}!"
        print(f"\nFormula used: {formula}")
        print(f"Result: {result}")
        
        # Show a few examples if the result isn't too large
        if result <= 100:
            items = list(range(1, n + 1))
            perms = list(permutations(items, r))
            print("\nSome possible arrangements:")
            for perm in perms[:10]:  # Show first 10 permutations
                print(perm)
    
    elif choice == '2':
        # Calculate n!
        n = int(input("\nEnter the number of items (n): "))
        result = math.factorial(n)
        formula = f"{n}! = {n} × {n-1} × {n-2} × ... × 2 × 1"
        print(f"\nFormula used: {formula}")
        print(f"Result: {result}")
        
        # Show a few examples if n is small
        if n <= 5:
            items = list(range(1, n + 1))
            perms = list(permutations(items))
            print("\nAll possible arrangements:")
            for perm in perms:
                print(perm)
    
    elif choice == '3':
        # Permutation with repetition
        n = int(input("\nEnter the number of positions: "))
        r = int(input("Enter the number of different items: "))
        
        result = r ** n
        formula = f"{r}^{n}"
        print(f"\nFormula used: {formula}")
        print(f"Result: {result}")
        
        # Show example with small numbers
        if n <= 3 and r <= 3:
            print("\nExample with items:", list(range(1, r + 1)))
            def generate_perms_with_rep(n, r):
                from itertools import product
                return list(product(range(1, r + 1), repeat=n))
            
            perms = generate_perms_with_rep(n, r)
            print("All possible arrangements:")
            for perm in perms:
                print(perm)
    
    else:
        print("Invalid choice!")

def explain_permutations():
    print("\nPermutation Types Explained:")
    print("\n1. Regular Permutation (nPr):")
    print("   - Arranging r items from n distinct items")
    print("   - Order matters")
    print("   - Formula: P(n,r) = n!/(n-r)!")
    
    print("\n2. Full Permutation (n!):")
    print("   - Arranging all n items")
    print("   - Order matters")
    print("   - Formula: n!")
    
    print("\n3. Permutation with Repetition:")
    print("   - n positions, r different items")
    print("   - Items can be repeated")
    print("   - Formula: r^n")

if __name__ == "__main__":
    explain_permutations()
    calculate_permutation()