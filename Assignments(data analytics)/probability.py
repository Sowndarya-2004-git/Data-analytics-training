def calculate_sets():
    print("\n=== Set Operations Calculator ===")
    
    # Get elements for set A
    print("\nEnter elements for Set A:")
    set_A = set()
    num_A = int(input("How many elements in Set A? "))
    for i in range(num_A):
        element = input(f"Enter element {i+1}: ")
        set_A.add(element)
    
    # Get elements for set B
    print("\nEnter elements for Set B:")
    set_B = set()
    num_B = int(input("How many elements in Set B? "))
    for i in range(num_B):
        element = input(f"Enter element {i+1}: ")
        set_B.add(element)
    
    # Calculate intersection and union
    intersection = set_A.intersection(set_B)
    union = set_A.union(set_B)
    
    # Display results
    print("\nResults:")
    print(f"Set A: {set_A}")
    print(f"Set B: {set_B}")
    print(f"Intersection (A ∩ B): {intersection}")
    print(f"Union (A ∪ B): {union}")

if __name__ == "__main__":
    calculate_sets()