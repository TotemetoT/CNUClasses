module CountDown (countDown) where
    countDown :: Int -> [Int]
    countDown n 
        | n == 0 = [0] 
        | otherwise = n : countDown (n-1)