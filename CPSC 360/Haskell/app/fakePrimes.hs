module FakePrimes (fakePrimes) where
    numbers :: [Int]
    numbers = [12..]

    isPrime :: Int -> Bool
    isPrime n
        | n < 1 = False
        | otherwise = null [d | d <- [2..n-1], n `mod` d == 0] 
    
    fakePrime :: Int -> Bool
    fakePrime n =
        not (isPrime n) &&
        all (\d -> n `mod` d /= 0) [2,3,5,7,9]
    
    primes :: [Int]
    primes = filter fakePrime numbers

    fakePrimes :: [Int]
    fakePrimes = primes