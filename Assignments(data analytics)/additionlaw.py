def calculate_addition_law():
    print("\n=== Addition Law of Probability Calculator ===")
    
    # Get total number of elements in sample space
    total_elements = int(input("Enter total number of elements in sample space: "))
    
    # Get elements for set A
    print("\nEnter elements for Event A:")
    set_A = set()
    num_A = int(input("How many elements in Event A? "))
    for i in range(num_A):
        element = input(f"Enter element {i+1}: ")
        set_A.add(element)
    
    # Get elements for set B
    print("\nEnter elements for Event B:")
    set_B = set()
    num_B = int(input("How many elements in Event B? "))
    for i in range(num_B):
        element = input(f"Enter element {i+1}: ")
        set_B.add(element)
    
    # Calculate probabilities
    intersection = set_A.intersection(set_B)
    union = set_A.union(set_B)
    
    prob_A = len(set_A) / total_elements
    prob_B = len(set_B) / total_elements
    prob_intersection = len(intersection) / total_elements
    prob_union = len(union) / total_elements
    
    # Calculate using addition law
    addition_law = prob_A + prob_B - prob_intersection
    
    # Display results
    print("\nResults:")
    print(f"Event A: {set_A}")
    print(f"Event B: {set_B}")
    print(f"A ∩ B (Intersection): {intersection}")
    print(f"A ∪ B (Union): {union}")
    print("\nProbabilities:")
    print(f"P(A) = {prob_A:.3f}")
    print(f"P(B) = {prob_B:.3f}")
    print(f"P(A ∩ B) = {prob_intersection:.3f}")
    print(f"P(A ∪ B) = {prob_union:.3f}")
    print(f"\nAddition Law Verification:")
    print(f"P(A) + P(B) - P(A ∩ B) = {addition_law:.3f}")
    print(f"P(A ∪ B) = {prob_union:.3f}")

if __name__ == "__main__":
    calculate_addition_law()