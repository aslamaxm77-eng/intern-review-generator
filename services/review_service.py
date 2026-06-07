def calculate_score(ratings):

    avg = round(
        sum(ratings.values()) /
        len(ratings),
        1
    )

    status = "Pass"

    if avg < 6:
        status = "Failed"

    return avg, status