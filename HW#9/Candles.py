def solution(candle_number: int, make_new: int, all_candle=0,
             ostatok=0) -> int:
    """
    This function calculates how many candles you can get,
    including the remainder.
    """
    if candle_number == 0:
        return all_candle
    else:
        if ostatok >= make_new:
            ostatok -= ostatok // make_new
        else:
            ostatok += candle_number % make_new
        all_candle += candle_number
        candle_number = candle_number // make_new + ostatok // make_new
        return solution(candle_number, make_new, all_candle, ostatok)


assert solution(5, 2) == 9
assert solution(1, 2) == 1
assert solution(15, 5) == 18
assert solution(12, 2) == 23
assert solution(6, 4) == 7
assert solution(13, 5) == 16
assert solution(2, 3) == 2
