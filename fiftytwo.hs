import Data.List (sort)

shareDigits :: Int -> Int -> Bool
shareDigits x y = sort (show x) == sort (show y)

findPermMult :: Int -> Int
findPermMult n =
  if (shareDigits n (2 * n) &&
      shareDigits n (3 * n) &&
      shareDigits n (4 * n) &&
      shareDigits n (5 * n) &&
      shareDigits n (6 * n))
  then n
  else findPermMult (n + 1)
