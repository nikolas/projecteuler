open Core

let reverse s =
  let len = String.length s in
  String.init len ~f:(fun i -> s.[len - 1 - i])

let is_palindrome s = reverse s = s

let () =
  for i = 900 to 999 do
    for j = 900 to 999 do
      if is_palindrome (string_of_int (i * j))
      then printf "%d * %d = %d" i j (i * j)
      else printf ":PPPPpppp"
    done
  done
