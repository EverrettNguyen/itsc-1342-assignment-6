# [Everrett Nguyen] - Assignment 6

def filter_critical_scores(score_list, min_severity=70):
    critical_scores = []
    # TODO: Filter and cap scores according to the prompt
    for score in score_list:
        if score > min_severity:
            if score > 100:
                score = 100
            critical_scores.append(score)
            
    return critical_scores