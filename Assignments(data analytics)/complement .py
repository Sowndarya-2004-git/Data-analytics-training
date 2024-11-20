def calculate_complement():
    print("\n=== Set Complement Calculator ===")
    
    # Get elements for Universal set
    print("\nEnter elements for Universal Set:")
    universal_set = set()
    num_U = int(input("How many elements in Universal Set? "))
    for i in range(num_U):
        element = input(f"Enter element {i+1}: ")
        universal_set.add(element)
    
    # Get elements for set A
    print("\nEnter elements for Set A:")
    set_A = set()
    num_A = int(input("How many elements in Set A? "))
    for i in range(num_A):
        element = input(f"Enter element {i+1}: ")
        # Validate if element exists in universal set
        if element not in universal_set:
            print(f"Warning: {element} is not in the Universal Set!")
            continue
        set_A.add(element)
    
    # Calculate complement
    complement_A = universal_set - set_A  # or universal_set.difference(set_A)
    
    # Display results
    print("\nResults:")
    print(f"Universal Set (U): {universal_set}")
    print(f"Set A: {set_A}")
    print(f"Complement of A (A'): {complement_A}")

if __name__ == "__main__":
    calculate_complement()