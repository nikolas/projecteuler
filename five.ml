open Base
open Stdio

let is_divisor x y =
  match y with
  | 0 -> false
  | n -> x mod n = 0

let rec is_divisible x y =
  if y = 0 then true
  else is_divisor x y && is_divisible x (y - 1)

let rec find_divisible x =
  if is_divisible x 20 then x
  else find_divisible (x + 1)

let () =
  printf "find_divisible: %d\n" (find_divisible 200)
