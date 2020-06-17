

sumsquare n = sum $ map (^ 2) [1..n]
squaresum n = (^ 2) $ sum [1..n]
answer n = squaresum n - sumsquare n