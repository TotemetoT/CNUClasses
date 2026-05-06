module IsPrime (isPrime) where
    isPrime :: Int -> Bool
    isPrime n 
        | n < 1     = False
        | otherwise = null [d | d <- [2..n-1], n `mod` d == 0]