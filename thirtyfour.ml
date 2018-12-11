open Base
open Stdio

let rec fact x =
  if x <= 1 then 1 else x * fact (x - 1)

let rec factsum x =
  if x < 10 then fact x
  else fact (x % 10) + factsum (x / 10)

let is_curious x =
  phys_equal (factsum x) x

(* get sum of all the curious numbers up to x. *)
let rec get_curious_sum x =
  match x with
  | 0 -> 0
  | 1 -> 0
  | 2 -> 0
  | n -> if is_curious n then n + get_curious_sum (n - 1)
         else get_curious_sum (n - 1)

let () =
    printf "get_curious_sum 100000 = %d\n" (get_curious_sum 100000);;
