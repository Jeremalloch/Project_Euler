fibonacci :: (Integral a) => a -> a
fibonacci n
    | n <= 1    = 1
    | otherwise = (fibonacci (n - 1)) + (fibonacci (n - 2))

let fibonacciList = [fibonacci x | x <- [0..]]

main = putStrLn (sum [fibonacci x | x <- [0..], (fibonacci x) <= 4000000, ((fibonacci x) `mod` 2 == 0)])
