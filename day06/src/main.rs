use std::{fs::read_to_string, collections::HashSet};

fn main() {

    let input = read_to_string("input/input.txt").unwrap();


    let vec: Vec<char> = input.chars().collect();

    let mut position = 0;

    for c in vec.clone() {
        let mut hs: HashSet<char> = HashSet::new();
        for i in position..position+4 {
            hs.insert(vec.get(i).unwrap().clone());
        }
        if hs.len() == 4 {
            break;
        }
        position += 1;
    }

    println!("Part 1: {}", position+4);

    // For part 2 same thing just change all the 4:s for 14.

}
