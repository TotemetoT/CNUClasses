module Operate (operate) where
    operate :: (Num a) => [a] -> [a -> a -> a] -> [a]
    operate [] _ = []
    operate _ [] = []
    operate (n:ns) operators =
        map (\op -> foldl op n ns) operators
