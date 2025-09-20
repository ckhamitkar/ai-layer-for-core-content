# main.py
import sys
# Add src to the path to allow imports from our src folder
sys.path.insert(0, './src')

from personalizer import personalize_problem

def main():
    """
    An example script to demonstrate the personalization of a math problem.
    """
    print("--- Demonstrating Problem Personalization ---")
    print()

    # --- Example 1: Sports Interest ---
    sports_problem = personalize_problem(interest="sports", count=2, total_count=6)
    print("Interest: sports")
    print(f"Generated Problem: {sports_problem}")
    print()

    # --- Example 2: Food Interest ---
    food_problem = personalize_problem(interest="food", count=4, total_count=8)
    print("Interest: food")
    print(f"Generated Problem: {food_problem}")
    print()

    # --- Example 3: Animal Interest ---
    animal_problem = personalize_problem(interest="animals", count=3, total_count=5)
    print("Interest: animals")
    print(f"Generated Problem: {animal_problem}")
    print()

    # --- Example 4: Unknown Interest (fallback) ---
    unknown_interest_problem = personalize_problem(interest="history", count=1, total_count=4)
    print("Interest: history (not in template)")
    print(f"Generated Problem: {unknown_interest_problem}")
    print()


if __name__ == "__main__":
    main()
