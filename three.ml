open Base
open Stdio

let is_divisor x y =
  match y with
  | 0 -> false
  | n -> x mod n = 0

let divisors_for x =
  let rec loop n i running_total =
    if i = n then running_total
    else (if is_divisor n i then loop n (i + 1) (running_total + 1)
          else loop n (i + 1) running_total) in
  loop x 1 1

let is_prime x = divisors_for x = 2

let is_prime_divisor x y = is_prime y && is_divisor x y

let prime_divisors x =
  let rec loop n i a =
    (*if n = i then a*)
    if List.length a > 3 then a
    else (if is_prime_divisor n i then loop n (i + 1) (i :: a)
          else loop n (i + 1) a) in
  loop x 1 []

let () =
  List.iter (prime_divisors 600851475143) ~f:(fun x -> printf "%d," x);;
printf "\ndivisors_for %d: %d\n" 13195 (divisors_for 13195);;
