use std::fs::read_to_string;
use std::collections::*;

fn main() {

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

    // PART 1
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

    println!("Part 1: {}", sum);

    // PART 2
    let input = read_to_string("input/input.txt").unwrap();
    let vec: Vec<&str> = input.lines().collect();

    let mut sum = 0;

    for i in (0..vec.len()).step_by(3) {
        // There doesn't seem to exist an easy way to get the intersection over multiple sets
        // I have to do it in two steps.
        let set1: HashSet<char> = HashSet::from_iter(vec.get(i).unwrap().chars());
        let set2: HashSet<char> = HashSet::from_iter(vec.get(i+1).unwrap().chars());
        let set3: HashSet<char> = HashSet::from_iter(vec.get(i+2).unwrap().chars());
        let xs: HashSet<char> = set1.intersection(&set2).cloned().collect();
        let ys: HashSet<char> = set3.intersection(&xs).cloned().collect();

        assert!(ys.len() == 1);
        let c = ys.iter().next().unwrap();
        sum += h.get(c).unwrap();

    }

    println!("Part 2: {}", sum);

}

