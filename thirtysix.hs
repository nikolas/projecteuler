import Numeric (showIntAtBase)
import Data.Char (intToDigit)

isPalindrome :: (Eq a) => [a] -> Bool
isPalindrome xs = xs == (reverse xs)

intToBin :: (Integral a, Show a) => a -> String
intToBin n = showIntAtBase 2 intToDigit n ""

findDoubleBasePalindromesTo :: Int -> [Int]
findDoubleBasePalindromesTo 0 = []
findDoubleBasePalindromesTo n = if (
  isPalindrome (show n) && isPalindrome (intToBin n))
  then n : (findDoubleBasePalindromesTo (n-1))
  else (findDoubleBasePalindromesTo (n-1))

main = putStrLn $ show $ sum $ findDoubleBasePalindromesTo 999999
