module Descending (descending) where
    descending :: Ord a => [a] -> Bool
    descending []  = True
    descending [_] = True
    descending (x:y:xs) = x >= y && descending (y:xs)
