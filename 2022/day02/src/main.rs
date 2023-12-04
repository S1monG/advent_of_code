use std::{fs::read_to_string, collections::HashMap};

fn main() {

    part1();
    part2();
    
}

fn part1() {

    let input = read_to_string("input/input.txt").unwrap();

    let mut options: HashMap<&str, usize> = HashMap::new();
    options.insert("B X", 1);
    options.insert("C Y", 2);
    options.insert("A Z", 3);
    options.insert("A X", 4);
    options.insert("B Y", 5);
    options.insert("C Z", 6);
    options.insert("C X", 7);
    options.insert("A Y", 8);
    options.insert("B Z", 9);

    let sum = input.lines().fold(0, |acc, line| acc + options.get(line).unwrap());

    println!("Part 1: {}", sum);
}

fn part2() {
    let input = read_to_string("input/input.txt").unwrap();

    let mut options: HashMap<&str, usize> = HashMap::new();
    options.insert("A X", 3);
    options.insert("A Y", 4);
    options.insert("A Z", 8);
    options.insert("B X", 1);
    options.insert("B Y", 5);
    options.insert("B Z", 9);
    options.insert("C X", 2);
    options.insert("C Y", 6);
    options.insert("C Z", 7);

    let sum = input.lines().fold(0, |acc, line| acc + options.get(line).unwrap());

    println!("Part 2: {}", sum);
}