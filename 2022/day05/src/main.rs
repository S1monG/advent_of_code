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

    for stack in stack_part1.iter() {
        println!("{:?}  ", stack);
    }
    println!();
    for stack in stack_part2.iter() {
        println!("{:?}  ", stack);
    }

    for line in input_moves.lines() {
        let moves: Vec<u8> = line.split(" ").filter_map(|s| s.parse::<u8>().ok()).collect();
        let (iterations, from_stack, to_stack) = (*moves.get(0).unwrap(),
                                                                 *moves.get(1).unwrap(),
                                                                 *moves.get(2).unwrap()
        );

        for _ in 0..iterations {
            let crate_to_be_moved = stack_part1[usize::from(from_stack-1)].pop().unwrap();
            stack_part1[usize::from(to_stack-1)].push(crate_to_be_moved);
        }
    }

    /* println!("Part 1:");
    for stack in stack_part1.iter() {
        print!("{:?}  ", stack.last().unwrap());
    } */

    //part2(stack_part2);

}

fn part2(mut stacks: [Vec<char>; 9]) -> Option<()> {

    let input_moves = read_to_string("input/input.txt").unwrap();

    for line in input_moves.lines() {
        let mut sp = line.split(" ");
        let count = sp.nth(1)?.parse::<usize>().unwrap();
        let from_stack = sp.nth(1)?.parse::<usize>().unwrap();
        let to_stack = sp.nth(1)?.parse::<usize>().unwrap();
        println!("Length of stack is {}    subtract with {}", stacks[from_stack].len(), count);
        let split_at = stacks[from_stack].len() - count;

        let mut crates = stacks[from_stack].split_off(split_at);
        stacks[to_stack].append(&mut crates);

    }

    println!("Part 2:");
    for stack in stacks.iter() {
        print!("{:?}  ", stack.last().unwrap());
    }

    Some(())
}