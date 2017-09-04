open Core.Std

let is_divisor x y =
  match y with
  | 0 -> false
  | n -> x mod n = 0

let rec sum l =
  match l with
  | [] -> 0
  | h :: t -> h + (sum t)

let find_divisors x =
  let rec loop i target =
    if i = x then [] else
      if is_divisor x i then (i :: loop (i + 1) target)
      else loop (i + 1) target in
  loop 0 x

let is_amicable x =
  x = sum (find_divisors (sum (find_divisors x))) &&
    sum (find_divisors x) != x

let amicable_numbers x =
  let rec loop i target =
    if i = x then [] else
      if is_amicable i then (i :: loop (i + 1) target)
      else loop (i + 1) target in
  loop 0 x

let myprint i = printf "%d, " i

let () =
  printf "%d\n" (sum (find_divisors 6));;
  printf "amicable_numbers: ";;
List.iter (amicable_numbers 10000) myprint;;
printf "\n";;
printf "sum of amicable numbers under 10000: %d\n"
       (sum (amicable_numbers 10000))
