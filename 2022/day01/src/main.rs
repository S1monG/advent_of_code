use std::fs::read_to_string;

fn main() {

    let input = read_to_string("input/input.txt").unwrap();

    let sp = input.split("\r\n\r\n");
    let totals = sp.map::<usize, _>(|s| 
        s.split("\r\n").map(|number| 
            number.parse::<usize>().unwrap_or(0)
        ).sum()
    );

    println!("Part 1: {}", totals.clone().max().unwrap());

    let mut top_three = vec![0,0,0];

    for nbr in totals {
        if nbr > *top_three.iter().min().unwrap() {
            top_three.sort();
            top_three.remove(0);
            top_three.push(nbr);
        }
    }

    println!("Part 2: {}", top_three.iter().sum::<usize>());
}


