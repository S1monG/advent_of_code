use std::fs::read_to_string;

fn main() {
    let input_stack = read_to_string("input/init_stack.txt").unwrap();
    let input_moves = read_to_string("input/input.txt").unwrap();

    let mut stack_part1: [Vec<char>; 9] = Default::default();

    // Init crate positions
    for row in input_stack.split("\r\n") {
        let mut xs = row.chars();
        xs.next();
        for (i, c) in xs.step_by(4).enumerate() {
            if c != ' ' {
                stack_part1[i].insert(0, c);
            }
        }
    }

    let mut stack_part2 = stack_part1.clone();

    for line in input_moves.lines() {
        let moves: Vec<u32> = line.split(" ").filter_map(|s| s.parse::<u32>().ok()).collect();
        let (iterations, from_stack, to_stack) = (*moves.get(0).unwrap(),
                                                                 *moves.get(1).unwrap(),
                                                                 *moves.get(2).unwrap());

        // Part 1
        for _ in 0..iterations {
            let crate_to_be_moved = stack_part1[usize::try_from(from_stack-1).unwrap()].pop();
            stack_part1[usize::try_from(to_stack-1).unwrap()].push(crate_to_be_moved.unwrap());
        }

        // Part 2
        let split_at: usize = stack_part2[usize::try_from(from_stack-1).unwrap()].len() - usize::try_from(iterations).unwrap();
        let mut crates_to_be_moved = stack_part2[usize::try_from(from_stack-1).unwrap()].split_off(split_at);
        stack_part2[usize::try_from(to_stack-1).unwrap()].append(&mut crates_to_be_moved);
    }

    println!("Part 1:");
    for stack in stack_part1.iter() {
        print!("{:?}  ", stack.last().unwrap());
    }
    println!("\n\nPart 2:");
    for stack in stack_part2.iter() {
        print!("{:?}  ", stack.last().unwrap());
    }

}
