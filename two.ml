open Core.Std

let rec sum l =
  match l with
  | [] -> 0
  | h :: t -> h + (sum t)

let fib x =
  let rec loop i a running_total =
    if i = x then a
    else loop (i + 1) (running_total) (a + running_total) in
  loop 0 0 1

let rec makelist length =
  match length with
  | 0 -> []
  | n -> fib n :: makelist (n - 1)

let () =
  printf "Fib: %d\n" (fib 50);;
printf "Sum: %d\n" (sum (List.filter
                           (List.filter (makelist 50)
                                        (fun x -> x mod 2 = 0))
                           (fun x -> x <= 4_000_000)))
