from problem_template import CORE_PROBLEM_TEMPLATE

def personalize_problem(interest, count, total_count, template=CORE_PROBLEM_TEMPLATE):
    """
    Generates a personalized problem based on a template and an interest.
    """
    prompt = template["core_prompt"]
    placeholders = template["placeholders"]

    # Select the placeholder values based on the interest
    # Use a default value if the interest is not found
    objects = placeholders["objects"].get(interest, "items")
    property_val = placeholders["property"].get(interest, "special")

    # Format the prompt string with the selected values and numbers
    personalized_prompt = prompt.format(
        count=count,
        total_count=total_count,
        objects=objects,
        property=property_val
    )

    return personalized_prompt
