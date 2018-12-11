open Core

let rec fact x =
  if x <= 1 then 1 else x * fact (x - 1)

let rec factsum x =
  if x < 10 then fact x
  else fact (x mod 10) + factsum (x / 10)

let is_curious x =
  phys_equal (factsum x) x

let rec sum l =
  match l with
  | [] -> 0
  | h :: t -> h + (sum t)

let () =
  for i = 0 to 10000000 do
    if is_curious i
    then printf "%d is curious!\n" i
    else printf ""
  done
