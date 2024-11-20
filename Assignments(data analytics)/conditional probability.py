def calculate_conditional_probability():
    print("\n=== Conditional Probability Calculator ===")
    
    # Get total number of elements in sample space
    total_elements = int(input("\nEnter total number of elements in sample space: "))
    
    # Get elements for event A
    print("\nEnter elements for Event A:")
    set_A = set()
    num_A = int(input("How many elements in Event A? "))
    for i in range(num_A):
        element = input(f"Enter element {i+1}: ")
        set_A.add(element)
    
    # Get elements for event B
    print("\nEnter elements for Event B:")
    set_B = set()
    num_B = int(input("How many elements in Event B? "))
    for i in range(num_B):
        element = input(f"Enter element {i+1}: ")
        set_B.add(element)
    
    # Calculate probabilities
    intersection = set_A.intersection(set_B)
    
    # Calculate P(B)
    prob_B = len(set_B) / total_elements
    
    # Calculate P(A∩B)
    prob_intersection = len(intersection) / total_elements
    
    # Calculate P(A|B) = P(A∩B)/P(B)
    if prob_B == 0:
        print("\nError: P(B) = 0, conditional probability undefined")
        return
        
    conditional_prob = prob_intersection / prob_B
    
    # Display results
    print("\nResults:")
    print(f"Event A: {set_A}")
    print(f"Event B: {set_B}")
    print(f"A ∩ B (Intersection): {intersection}")
    
    print("\nProbabilities:")
    print(f"P(B) = {prob_B:.3f}")
    print(f"P(A ∩ B) = {prob_intersection:.3f}")
    print(f"P(A|B) = P(A ∩ B)/P(B) = {conditional_prob:.3f}")
    
    # Additional information
    print("\nInterpretation:")
    print(f"Given that event B has occurred, ")
    print(f"the probability of event A occurring is {conditional_prob:.3f}")

def show_example():
    print("\nExample Scenario:")
    print("Consider drawing a card from a standard deck of 52 cards")
    print("A: Event of drawing a King")
    print("B: Event of drawing a Face card (Jack, Queen, or King)")
    
    # Calculate example probabilities
    total_cards = 52
    kings = 4
    face_cards = 12
    kings_in_face_cards = 4
    
    prob_B = face_cards / total_cards
    prob_intersection = kings_in_face_cards / total_cards
    conditional_prob = prob_intersection / prob_B
    
    print("\nExample Calculations:")
    print(f"P(B) = {face_cards}/{total_cards} = {prob_B:.3f}")
    print(f"P(A ∩ B) = {kings_in_face_cards}/{total_cards} = {prob_intersection:.3f}")
    print(f"P(A|B) = {kings_in_face_cards}/{face_cards} = {conditional_prob:.3f}")

if __name__ == "__main__":
    show_example()
    calculate_conditional_probability()
