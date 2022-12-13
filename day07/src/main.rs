use std::{collections::HashMap, fs::read_to_string, ops::Index};

fn main() {
    let input = read_to_string("input/input.txt").unwrap();

    parse(input);
}

fn parse(input: String) {
    let mut stack: Vec<String> = Vec::new();

    let mut hm: HashMap<String, Vec<u32>> = HashMap::new();

    for line in input.lines() {
        match &line[0..4] {
            "$ cd" => {
                if &line[5..] == ".." {
                    stack.pop();
                } else {
                    let mut parent_dir = stack.last().unwrap_or(&String::new()).clone();
                    if !parent_dir.is_empty() {
                        parent_dir.push_str("/");
                    }
                    let current_dir = &line[5..];
                    parent_dir.push_str(current_dir);
                    hm.insert(parent_dir.clone(), Vec::new());
                    stack.push(parent_dir.clone());
                }
            }
            "$ ls" => {
                continue;
            }
            "dir " => {
                continue;
            }
            _ => {
                // parse size of file
                let size: u32 = line.split(" ").next().unwrap().parse().unwrap();

                // add size of file to the vec in the hashmap of all the dirs in the stack
                for dir in stack.clone() {
                    if !hm.contains_key(&dir) {
                        panic!("hashmap doesn't contain the dir {dir} but it should");
                    }

                    let mut vec = hm.get(&dir).unwrap().clone();
                    vec.push(size);
                    hm.insert(dir, vec);
                }
            }
        }
    }

    let values = hm.values().map(|xs| xs.iter().sum::<u32>());
    let result_part1: u32 = values.clone().filter(|v| v <= &100000).sum();
    println!("Part 1: {result_part1}");

    let total_size: u32 = input.lines().filter(|line| 
        line.chars().next().unwrap().is_digit(10)
    ).map(|line| 
        line.split(" ").next().unwrap().parse::<u32>().unwrap()
    ).sum();

    let needed_space = 30000000 - (70000000 - total_size);

    let result_part2: u32 = values.clone().filter(|v| v >= &needed_space).min().unwrap();
    println!("Part 2: {result_part2}");
}
