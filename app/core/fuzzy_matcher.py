from rapidfuzz import process, fuzz


def find_best_match(user_input, locations):
    """
    Find the location that best matches the user's spoken input.
    """

    choices = {}

    for location in locations:
        for alias in location["aliases"]:
            choices[alias] = location

    result = process.extractOne(
        user_input,
        choices.keys(),
        scorer=fuzz.ratio
    )

    if result is None:
        return None

    matched_alias, score, _ = result

    if score < 60:
        return None

    return {
        "location": choices[matched_alias],
        "score": score,
        "matched_alias": matched_alias
    }