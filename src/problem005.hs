evenDivides max n = all (== True) [mod n x == 0 | x <- [1..max]]
answer = head $ filter (\x -> evenDivides 20 x) [20, 40..]