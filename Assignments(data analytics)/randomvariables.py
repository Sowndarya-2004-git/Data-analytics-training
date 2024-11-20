import numpy as np
from typing import List, Tuple

class RandomVariable:
    def __init__(self):
        print("\n=== Random Variable Calculator ===")
        
    def get_probability_distribution(self) -> Tuple[List[float], List[float]]:
        """Get the values and their probabilities from user input"""
        n = int(input("\nEnter the number of possible values: "))
        
        values = []
        probabilities = []
        total_prob = 0
        
        print("\nEnter the values and their probabilities:")
        for i in range(n):
            value = float(input(f"Enter value {i+1}: "))
            prob = float(input(f"Enter probability for value {value}: "))
            
            values.append(value)
            probabilities.append(prob)
            total_prob += prob
        
        # Validate probabilities sum to 1
        if abs(total_prob - 1.0) > 0.0001:
            print(f"\nWarning: Probabilities sum to {total_prob}, not 1.0")
            print("Normalizing probabilities...")
            probabilities = [p/total_prob for p in probabilities]
        
        return values, probabilities
    
    def expected_value(self, values: List[float], probabilities: List[float]) -> float:
        """Calculate expected value (mean)"""
        return sum(x * p for x, p in zip(values, probabilities))
    
    def variance(self, values: List[float], probabilities: List[float], mean: float) -> float:
        """Calculate variance"""
        return sum((x - mean)**2 * p for x, p in zip(values, probabilities))
    
    def standard_deviation(self, variance: float) -> float:
        """Calculate standard deviation"""
        return np.sqrt(variance)
    
    def display_distribution(self, values: List[float], probabilities: List[float]):
        """Display the probability distribution"""
        print("\nProbability Distribution:")
        print("X\t|\tP(X)")
        print("-" * 20)
        for x, p in zip(values, probabilities):
            print(f"{x:.2f}\t|\t{p:.3f}")
    
    def calculate_statistics(self):
        """Main method to calculate all statistics"""
        # Get the probability distribution
        values, probabilities = self.get_probability_distribution()
        
        # Calculate statistics
        mean = self.expected_value(values, probabilities)
        var = self.variance(values, probabilities, mean)
        std_dev = self.standard_deviation(var)
        
        # Display results
        self.display_distribution(values, probabilities)
        
        print("\nStatistics:")
        print(f"Expected Value (Mean) = {mean:.3f}")
        print(f"Variance = {var:.3f}")
        print(f"Standard Deviation = {std_dev:.3f}")
        
        # Additional information
        print("\nInterpretation:")
        print(f"• On average, X takes the value {mean:.3f}")
        print(f"• Values typically deviate from the mean by ±{std_dev:.3f}")
        print(f"• About 68% of values fall within {mean:.3f} ± {std_dev:.3f}")
        print(f"• About 95% of values fall within {mean:.3f} ± {2*std_dev:.3f}")

def main():
    rv = RandomVariable()
    rv.calculate_statistics()

if __name__ == "__main__":
    main()