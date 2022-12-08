use std::fs::read_to_string;
use std::collections::*;

fn main() {

    part1();
}

fn part1() {

    let input = read_to_string("input/input.txt");

    let mut h: HashMap<char, usize> = HashMap::new();
    
    let lowercase_range = 'a'..='z';
    lowercase_range.enumerate().for_each(|(i, c)| {
        h.insert(c, i+1);
    });
    let uppercase_range = 'A'..='Z';
    uppercase_range.enumerate().for_each(|(i, c)| {
        h.insert(c, i+27);
    });
    
    let mut sum = 0;

    for line in input.unwrap().lines() {
        let half = line.len()/2;
        let first_half: Vec<char> = line.chars().take(half).collect();
        let second_half: Vec<char> = line.chars().skip(half).collect();
        for c in first_half {
            if second_half.contains(&c) {
                sum += h.get(&c).unwrap();
                break;
            }
        }
    }

    println!("{}", sum);
}