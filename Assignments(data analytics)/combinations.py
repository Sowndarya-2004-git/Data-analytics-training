import math
from itertools import combinations, combinations_with_replacement

def calculate_combination():
    print("\n=== Combination Calculator ===")
    
    print("\nSelect Combination Type:")
    print("1. Regular Combination (nCr)")
    print("2. Combination with Repetition")
    choice = input("Enter your choice (1-2): ")
    
    if choice == '1':
        # Calculate nCr
        n = int(input("\nEnter the total number of items (n): "))
        r = int(input("Enter the number of items to select (r): "))
        
        if r > n:
            print("Error: r cannot be greater than n")
            return
            
        result = math.comb(n, r)
        formula = f"{n}C{r} = {n}!/({r}!({n}-{r})!)"
        print(f"\nFormula used: {formula}")
        print(f"Result: {result}")
        
        # Show examples if the result isn't too large
        if result <= 20:
            items = list(range(1, n + 1))
            combs = list(combinations(items, r))
            print("\nAll possible combinations:")
            for comb in combs:
                print(comb)
    
    elif choice == '2':
        # Calculate combination with repetition
        n = int(input("\nEnter the number of types of items (n): "))
        r = int(input("Enter the number of items to select (r): "))
        
        result = math.comb(n + r - 1, r)
        formula = f"(n+r-1)C(r) = {n+r-1}C{r}"
        print(f"\nFormula used: {formula}")
        print(f"Result: {result}")
        
        # Show examples if numbers are small
        if n <= 5 and r <= 3:
            items = list(range(1, n + 1))
            combs = list(combinations_with_replacement(items, r))
            print("\nAll possible combinations with repetition:")
            for comb in combs:
                print(comb)
    
    else:
        print("Invalid choice!")

def explain_combinations():
    print("\nCombination Types Explained:")
    print("\n1. Regular Combination (nCr):")
    print("   - Selecting r items from n distinct items")
    print("   - Order doesn't matter")
    print("   - Formula: C(n,r) = n!/(r!(n-r)!)")
    print("   - Example: Selecting 2 cards from 52 cards")
    
    print("\n2. Combination with Repetition:")
    print("   - Selecting r items from n types of items")
    print("   - Items can be repeated")
    print("   - Order doesn't matter")
    print("   - Formula: C(n+r-1,r)")
    print("   - Example: Selecting 3 ice cream scoops from 5 flavors")

def show_practical_examples():
    print("\nPractical Examples:")
    
    print("\nExample 1: Regular Combination")
    print("Selecting 2 cards from a deck of 52 cards:")
    result = math.comb(52, 2)
    print(f"52C2 = {result} possible combinations")
    
    print("\nExample 2: Combination with Repetition")
    print("Selecting 3 scoops from 5 ice cream flavors:")
    result = math.comb(5 + 3 - 1, 3)
    print(f"Result = {result} possible combinations")

if __name__ == "__main__":
    explain_combinations()
    show_practical_examples()
    calculate_combination()