import Data (List)

productNumbers = [x*y | x <- [100..999], y <- [100..999], (x*y == read (reverse (show (x*y))))]

main = putStrLn (show (last (sort productNumbers)))
