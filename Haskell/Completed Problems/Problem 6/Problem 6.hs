sumOfSquares = sum [x^2 | x <- [1..100]]
squareOfSums = (sum [1..100])^2

main = putStrLn (show (squareOfSums - sumOfSquares))
