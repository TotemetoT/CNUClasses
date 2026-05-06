module Main (main) where

import Lib

-- import Counting_Tuples
-- counting_tuples.hs
count :: Eq a=> a -> [a] -> Int
count x xs = length $ filter (== x) xs

counting_tuples :: Eq a => [a] -> [(a, Int)]
counting_tuples xs = [(x, count x xs) | x <- xs]

-- import Descending
-- descending.hs
descending :: Ord a => [a] -> Bool
descending []  = True
descending [_] = True
descending (x:y:xs) = x >= y && descending (y:xs)

-- import Divs
-- divs.hs
divs :: Int -> [Int]
divs n
    | n == 0    = []
    | otherwise = [d | d <- [1..n], n `mod` d == 0]

-- import IsPrime
-- isPrime.hs
isPrime :: Int -> Bool
isPrime n
    | n < 1     = False
    | otherwise = null [d | d <- [2..n-1], n `mod` d == 0]

-- import FakePrimes
-- fakePrimes.hs
numbers :: [Int]
numbers = [12..]

fakePrime :: Int -> Bool
fakePrime n =
    not (isPrime n) &&
    all (\d -> n `mod` d /= 0) [2,3,5,7,9]

primes :: [Int]
primes = filter fakePrime numbers

fakePrimes :: [Int]
fakePrimes = primes

-- import Operate
-- operate.hs
operate :: (Num a) => [a] -> [a -> a -> a] -> [a]
operate [] _ = []
operate _ [] = []
operate (n:ns) operators =
    map (\op -> foldl op n ns) operators


main :: IO ()
main = putStrLn "Compiled successfully!"