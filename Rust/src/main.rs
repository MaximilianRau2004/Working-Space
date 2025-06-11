fn main() {
   let result = add(5, 7);
   println!("The result of adding 5 and 7 is: {}", result);
}

fn add(x: i32, y: i32) -> i32 {
    let result = x + y;
    if result > 10 {
        return result - 10;
    }
    result
}
