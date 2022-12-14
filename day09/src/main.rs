use std::fs::read_to_string;
use std::collections::HashSet;
use std::ops::{Sub, Add, AddAssign};
use Direction::*;

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

    let result_part1 = rope.visited_positions_by_tail.len();

    println!("Part 1: {}", result_part1);

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

/* impl Add for Point {
    type Output = Self;

    fn add(self, other: Self) -> Self::Output {
        Self {
            x: self.x + other.x,
            y: self.y + other.y,
        }
    }
} */

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
    head: Point,
    tail: Point,
    visited_positions_by_tail: HashSet<Point>
}

impl RopeGrid {

    fn new(starting_position: Point) -> RopeGrid {
        RopeGrid { 
            head: starting_position, 
            tail: starting_position,
            visited_positions_by_tail: HashSet::new(),
        }
    }

    fn move_head(&mut self, dir: Direction) {
        match dir {
            Up => self.head += Point::new(0, 1),
            Down => self.head += Point::new(0, -1),
            Right => self.head += Point::new(1, 0),
            Left => self.head += Point::new(-1, 0),
        }

        self.update_tail();
    }

    fn update_tail(&mut self) {
        let diff = (self.head - self.tail).get_tuple();

        match diff {
            (2, 0) => self.tail += Point::new(1, 0),
            (-2, 0) => self.tail += Point::new(-1, 0),
            (0, 2) => self.tail += Point::new(0, 1),
            (0, -2) => self.tail += Point::new(0, -1),
            (2, 1) | (1, 2) => self.tail += Point::new(1, 1),
            (-2, 1) | (-1, 2) => self.tail += Point::new(-1, 1),
            (2, -1) | (1, -2) => self.tail += Point::new(1, -1),
            (-2, -1) | (-1, -2) => self.tail += Point::new(-1, -1),
            _ => (),
        }

        self.visited_positions_by_tail.insert(self.tail.clone());
    }
}

enum Direction {
    Up,
    Down,
    Right,
    Left,
}
