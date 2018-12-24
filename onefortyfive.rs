/**
 * Reverse a number.
 *
 * reversed(65) -> 56
 */
fn reversed(n: u32) -> u32 {
    let s = n.to_string();
    let reversed = s.chars().rev().collect::<String>();
    let n: u32 = reversed.parse().unwrap();
    return n;
}

/**
 * Returns true if n's digits are all odd.
 */
fn is_all_odd(n: u32) -> bool {
    let s = n.to_string();
    for c in s.chars() {
        let x: u32 = c.to_digit(10).unwrap();
        if x % 2 == 0 {
            return false;
        }
    }
    return true;
}

fn main() {
    //let mut vec = Vec::new();
    let mut count = 0;

    for i in 10..100_000_000 {
        if i % 10 != 0 {
            let n: u32 = reversed(i);
            let sum = i + n;
            if is_all_odd(sum) {
                //vec.push(i);
                count += 1;
            }
        }
    }
    println!("done");
    println!("count: {}", count);
}
