module Counting_Tuples (counting_tuples) where
    count :: Eq a=> a -> [a] -> Int
    count x xs = length $ filter (== x) xs

    counting_tuples :: Eq a => [a] -> [(a, Int)]
    counting_tuples xs = [(x, count x xs) | x <- xs]