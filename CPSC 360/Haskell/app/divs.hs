module Divs (divs) where
    divs :: Int -> [Int]
    divs n
        | n == 0    = []
        | otherwise = [d | d <- [1..n], n `mod` d == 0]