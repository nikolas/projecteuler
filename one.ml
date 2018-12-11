open Core

let rec sum l =
  match l with
  | [] -> 0
  | h :: t -> h + (sum t)

let rec makelist length =
  let test n = n mod 3 = 0 || n mod 5 = 0 in
  match length with
  | 0 -> []
  | n -> if test n then n :: (makelist (n - 1)) else makelist (n - 1)

let () =
  printf "Sum: %d\n" (sum (makelist 999))
