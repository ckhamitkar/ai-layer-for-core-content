# This file contains the core template for a math problem.
# We'll use this as the foundation for generating personalized variants.

CORE_PROBLEM_TEMPLATE = {
    "id": "fractions-of-a-group-1",
    "type": "math/fractions",
    "difficulty": "easy",
    "core_prompt": "{count} of the {total_count} {objects} are {property}. What fraction of the {objects} are {property}?",
    "placeholders": {
        "objects": {
            "sports": "soccer balls",
            "food": "pizzas",
            "animals": "kittens"
        },
        "property": {
            "sports": "blue",
            "food": "pepperoni",
            "animals": "sleeping"
        }
    }
}
