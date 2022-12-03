use std::env;
use std::fs;

fn main() {
    let file_path = "../challenge.txt";
    println!("Hello, world!");
    println!("In file {}", file_path);

    let contents = fs::read_to_string(file_path)
              .expect("Should have been able to read the file");

    let split = contents.split("\n\n").map(String::from).collect::<Vec<String>>();
    //let vec = split.collect::<Vec<&str>>();

}
