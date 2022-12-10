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
        let moves: Vec<u8> = line.split(" ").filter_map(|s| s.parse::<u8>().ok()).collect();
        let (iterations, from_stack, to_stack) = (*moves.get(0).unwrap(),
                                                                 *moves.get(1).unwrap(),
                                                                 *moves.get(2).unwrap()
        );

        let index = stack_part2[usize::from(to_stack-1)].len();

        for _ in 0..iterations {

            // Part 1
            let crate_to_be_moved = stack_part1[usize::from(from_stack-1)].pop().unwrap();
            stack_part1[usize::from(to_stack-1)].push(crate_to_be_moved);

            stack_part2[usize::from(to_stack-1)].insert(index, crate_to_be_moved);
        }

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
