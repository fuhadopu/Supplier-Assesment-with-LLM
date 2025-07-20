def clamp_score(num, low=1, high=5):
    try:
        n = int(num)
    except ValueError:
        n = 1
    return max(low, min(high, n))

def normalize_score(score: int) -> float:
    return round((clamp_score(score) - 1) / 4, 3)
