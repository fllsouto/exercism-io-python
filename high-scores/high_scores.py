def latest(scores):
    scores_len = len(scores)
    return scores[scores_len - 1]


def personal_best(scores):
    max_score_index = _personal_best(scores)
    return scores[max_score_index]


def _personal_best(scores):
    max_score_index = 0
    for i in range(len(scores)):
        if (scores[i] > scores[max_score_index]):
            max_score_index = i
    return max_score_index

def personal_top_three(scores):
    total = len(scores) if (len(scores) < 3) else 3
    top_scores = []
    for i in range(0, total):
        index = _personal_best(scores)
        score = scores.pop(index)
        top_scores.append(score)
    return top_scores