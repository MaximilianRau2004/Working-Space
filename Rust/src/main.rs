fn main() {
    
    let x: i32= -2; // i32: signed 32-bit integer, default in Rust
    let y: u32 = 3; // u32: unsigned 32-bit integer
    let float: f32 = 4.9; // f64: 64-bit floating point number, default in Rust
    let boolean = true; // bool: boolean type, can be true or false (1 or 0)
    let letter: char = 'a'; // char: single Unicode character, 4 bytes in size
    let mut tup: (i32, u32, f32, bool, char) = (x, y, float, boolean, letter); // tuple: can hold multiple values of different types
    println!("Tuple: {:?}", tup); 

    tup.0 = 5; 
    tup = (tup.0, tup.1, tup.2, tup.3, 'b'); 

    println!("Tuple: {:?}", tup);

    let mut arr: [i32; 5] = [1, 2, 3, 4, 5]; // array: fixed-size list of elements of the same type
    arr[4] = 6; 
    println!("Array: {:?}", arr);

    let mut vec: Vec<i32> = vec![1, 2, 3, 4, 5]; // vector: growable array
    vec.push(6);
    println!("Vector: {:?}", vec);

    let str: &str = "Hello, World!"; // string slice: immutable reference to a string
    let mut string: String = String::from("Hello, Rust!"); // String: growable, heap-allocated string
    string.push_str(" Let's learn about data types.");
    println!("String: {}", string);
    println!("String slice: {}", str);


}
