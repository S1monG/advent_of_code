use std::fs::read_to_string;
use std::collections::HashSet;
use std::ops::{Sub, AddAssign};
use Direction::*;

const NBR_OF_KNOTS: usize = 10;

fn main() {

    let input = read_to_string("input/input.txt").unwrap();

    let mut rope = RopeGrid::new(Point::new(0,0));

    for line in input.lines() {
        let mut split = line.split(" ");
        let dir = split.next().unwrap();
        let iterations = split.next().unwrap().parse::<u32>().unwrap();

        match dir {
            "U" => (0..iterations).for_each(|_| rope.move_head(Up)),
            "D" => (0..iterations).for_each(|_| rope.move_head(Down)),
            "R" => (0..iterations).for_each(|_| rope.move_head(Right)),
            "L" => (0..iterations).for_each(|_| rope.move_head(Left)),
            _ => panic!("Wrong input"),
        }

    }

    let result = rope.visited_positions_by_tail.len();

    /* For answer to part 1 the constant 'NBR_OF_KNOTS' should be 2.
    For answer to part 2 the constant 'NBR_OF_KNOTS' should be 10. */
    println!("Answer: {}", result);

}

#[derive(Debug, Copy, Clone, PartialEq, Eq, Hash)]
struct Point {
    x: i32,
    y: i32,
}

impl Sub for Point {
    type Output = Self;

    fn sub(self, other: Self) -> Self::Output {
        Self {
            x: self.x - other.x,
            y: self.y - other.y,
        }
    }
}

impl AddAssign for Point {
    fn add_assign(&mut self, other: Self) {
        *self = Self {
            x: self.x + other.x,
            y: self.y + other.y,
        };
    }
}

impl Point {
    fn new(x: i32, y: i32) -> Point {
        Point { x, y, }
    }

    fn get_tuple(&self) -> (i32, i32) {
        (self.x, self.y)
    }
}

struct RopeGrid {
    knots: [Point; NBR_OF_KNOTS],
    visited_positions_by_tail: HashSet<Point>
}

impl RopeGrid {

    fn new(starting_point: Point) -> RopeGrid {
        RopeGrid { 
            knots: [starting_point; NBR_OF_KNOTS],
            visited_positions_by_tail: HashSet::new(),
        }
    }

    fn move_head(&mut self, dir: Direction) {
        match dir {
            Up => self.knots[0] += Point::new(0, 1),
            Down => self.knots[0] += Point::new(0, -1),
            Right => self.knots[0] += Point::new(1, 0),
            Left => self.knots[0] += Point::new(-1, 0),
        }

        self.update_tail();
    }

    fn update_tail(&mut self) {

        for i in 1..NBR_OF_KNOTS {
            let diff = (self.knots[i-1] - self.knots[i]).get_tuple();

            match diff {
                (2, 0) => self.knots[i] += Point::new(1, 0),
                (-2, 0) => self.knots[i] += Point::new(-1, 0),
                (0, 2) => self.knots[i] += Point::new(0, 1),
                (0, -2) => self.knots[i] += Point::new(0, -1),
                (2, 1) | (1, 2) | (2, 2) => self.knots[i] += Point::new(1, 1),
                (-2, 1) | (-1, 2) | (-2, 2) => self.knots[i] += Point::new(-1, 1),
                (2, -1) | (1, -2) | (2, -2) => self.knots[i] += Point::new(1, -1),
                (-2, -1) | (-1, -2) | (-2, -2) => self.knots[i] += Point::new(-1, -1),
                _ => (),
            }

        }

        self.visited_positions_by_tail.insert(self.knots[NBR_OF_KNOTS-1]);
    }
}

enum Direction {
    Up,
    Down,
    Right,
    Left,
}
