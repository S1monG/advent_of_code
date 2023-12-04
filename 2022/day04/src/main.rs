use std::fs::read_to_string;

fn main() {

    let input = read_to_string("input/input.txt").unwrap();

    let mut containing_pairs = 0;

    for line in input.lines() {
        if is_contained(line) {
            containing_pairs += 1;
        }
    }

    println!("Part 1: {}", containing_pairs);

    let mut overlapping_pairs = 0;

    for line in input.lines() {
        if is_overlapping(line) {
            overlapping_pairs += 1;
        }
    }

    println!("Part 2: {}", overlapping_pairs);
}

fn is_contained(s: &str) -> bool {

    let sp: Vec<&str> = s.split(",").collect();
    let first_range: Vec<&str> = sp.get(0).unwrap().split("-").collect();
    let second_range: Vec<&str> = sp.get(1).unwrap().split("-").collect();

    let first_range = (first_range.get(0).unwrap().parse::<i32>().unwrap(), first_range.get(1).unwrap().parse::<i32>().unwrap());
    let second_range = (second_range.get(0).unwrap().parse::<i32>().unwrap(), second_range.get(1).unwrap().parse::<i32>().unwrap());

    if first_range.0 <= second_range.0 && first_range.1 >= second_range.1 {
        return true;
    } else if second_range.0 <= first_range.0 && second_range.1 >= first_range.1 {
        return true;
    }

    false
}

fn is_overlapping(s: &str) -> bool {

    let sp: Vec<&str> = s.split(",").collect();
    let first_range: Vec<&str> = sp.get(0).unwrap().split("-").collect();
    let second_range: Vec<&str> = sp.get(1).unwrap().split("-").collect();

    let first_range = (first_range.get(0).unwrap().parse::<i32>().unwrap(), first_range.get(1).unwrap().parse::<i32>().unwrap());
    let second_range = (second_range.get(0).unwrap().parse::<i32>().unwrap(), second_range.get(1).unwrap().parse::<i32>().unwrap());

    if first_range.1 < second_range.0 || first_range.0 > second_range.1 {
        return false;
    }

    true
}
