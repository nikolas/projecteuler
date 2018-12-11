open Core

let rec sum_of_squares_to x =
  match x with
  | 0. -> 0.
  | n -> n ** 2. +. sum_of_squares_to (n -. 1.)

let all n = List.map List.(range 0 n) ~f:float_of_int

let sum_list a = List.fold_left a ~init:0. ~f:(+.)

let square_of_sum_to x = (sum_list (all x)) ** 2.

let () =
  printf "sum_of_squares_to: %f\n" (sum_of_squares_to 100.);;
printf "square_of_sum_to: %f\n" (square_of_sum_to 100);;
printf "the answer: %f\n" ((square_of_sum_to 101) -. (sum_of_squares_to 100.))
