def calculate_multiplication_law():
    print("\n=== Multiplication Law of Probability Calculator ===")
    
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
    
    prob_A = len(set_A) / total_elements
    prob_B = len(set_B) / total_elements
    prob_intersection = len(intersection) / total_elements
    
    # Calculate conditional probability P(B|A)
    prob_B_given_A = len(intersection) / len(set_A) if len(set_A) > 0 else 0
    
    # Calculate probabilities for both independent and dependent cases
    independent_prob = prob_A * prob_B
    dependent_prob = prob_A * prob_B_given_A
    
    # Display results
    print("\nResults:")
    print(f"Event A: {set_A}")
    print(f"Event B: {set_B}")
    print(f"A ∩ B (Intersection): {intersection}")
    
    print("\nProbabilities:")
    print(f"P(A) = {prob_A:.3f}")
    print(f"P(B) = {prob_B:.3f}")
    print(f"P(A ∩ B) = {prob_intersection:.3f}")
    print(f"P(B|A) = {prob_B_given_A:.3f}")
    
    print("\nMultiplication Law Results:")
    print("For Independent Events:")
    print(f"P(A) × P(B) = {independent_prob:.3f}")
    
    print("\nFor Dependent Events:")
    print(f"P(A) × P(B|A) = {dependent_prob:.3f}")
    
    # Check if events are likely independent
    if abs(independent_prob - prob_intersection) < 0.0001:
        print("\nNote: Events appear to be independent")
    else:
        print("\nNote: Events appear to be dependent")

if __name__ == "__main__":
    calculate_multiplication_law()