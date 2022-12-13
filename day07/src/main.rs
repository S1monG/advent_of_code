use std::{fs::read_to_string, ops::Index, collections::HashMap};

fn main() {

    let input = read_to_string("input/example.txt").unwrap();

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
                    let mut filename = stack.last().unwrap_or(&String::new()).clone();
                    
                    if &line[5..] != "/" {
                        filename.push_str("/");
                    }
                    
                    filename.push_str(&line[5..]);
                    stack.push(filename.clone());
                    hm.insert(filename, Vec::new());
                }
            },
            "$ ls" => {
                continue;
            },
            "dir " => {
                /* the dir is processed when you cd into it. 
                if you never cd into it and it is empty it doesn't contribute to the sulotion */
                continue;
            },
            _ => {
                let file_size: u32 = line.split(" ").next().unwrap().parse().unwrap();
                let current_dir = stack.last().unwrap().clone();
                hm.insert(current_dir, Vec::new());

                

                for dir in stack.clone() {
                    let mut new_vec: Vec<u32> = Vec::new();
                    new_vec.push(file_size);
                    let old_vec = hm.get(&dir).unwrap();
                    new_vec.append(&mut old_vec.clone());
                    hm.insert(dir, new_vec);
                }

            },
        }
    };

    println!("{:#?}", hm);
    let values = hm.values().map(|xs| xs.iter().sum::<u32>());
    let res: u32 = values.filter(|v| v <= &100000).sum();
    println!("{res}");
}

