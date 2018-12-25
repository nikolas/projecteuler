-- https://stackoverflow.com/a/4695002/173630
isPrime :: Integral a => a -> Bool
isPrime k = null [x | x <- [2..k - 1], k `mod` x == 0]

findPrimeSum :: Integral a => Int -> [a] -> [a]
findPrimeSum _ [] = []
findPrimeSum 0 _ = []
findPrimeSum 1 (x:xs) = if isPrime x then [x] else findPrimeSum 1 xs
findPrimeSum n (x:xs) = if isPrime (sum testL) then testL else findPrimeSum n xs
  where
    testL = x : (take (n - 1) xs)

biggestPrimeSumSequence :: Integral a => [a] -> [a]
biggestPrimeSumSequence [] = []
biggestPrimeSumSequence list = findPrimeSum (length list) list

primesTo n = filter isPrime [1..n]

-- Find the largest one under a million.
findAnswer 0 _ = 0
findAnswer n oldSum = if mySum > 1000000 then oldSum else findAnswer (n + 1) mySum
  where
    mySum = sum (biggestPrimeSumSequence (primesTo n))

reallyFindAnswer 0 = 0
reallyFindAnswer n = if myFind == 0 then reallyFindAnswer (n - 1) else myFind
  where
    myFind = findAnswer n 0

main = putStrLn $ show (reallyFindAnswer 4000)
