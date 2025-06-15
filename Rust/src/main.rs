fn main() {
   let result = add(5, 7);
   println!("The result of adding 5 and 7 is: {}", result);
}

fn add(x: i32, y: i32) -> i32 {
    x + y
}
