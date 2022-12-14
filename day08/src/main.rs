use std::fs::read_to_string;

fn main() {

    // the grid is 99x99
    let input = read_to_string("input/input.txt").unwrap();

    let mut vec = Vec::new();

    input.lines().for_each(|line| 
        vec.append(&mut line.chars().map(|c| c.to_digit(10).unwrap()).collect::<Vec<_>>())
    );

    let size = input.lines().count();
    let qm = QuadraticMatrix::new(size, vec);

    let mut visible_trees = 0;

    for tree in 0..size*size {
        if qm.is_visable_from_outside(tree) {
            visible_trees += 1
        }
    }

    println!("Part 1: {}", visible_trees);

    let max_scenic_score = (0..size*size).map(|index| qm.scenic_score(index)).max().unwrap();
    println!("Part 2: {}", max_scenic_score);

}

struct QuadraticMatrix {
    size: usize,
    values: Vec<u32>,
}

impl QuadraticMatrix {

    fn new(size: usize, values: Vec<u32>) -> QuadraticMatrix {
        QuadraticMatrix { 
            size,
            values,
        }
    }

    fn get_row(&self, index: usize) -> Vec<&u32> {
        self.values.iter().skip(index*self.size).take(self.size).collect::<Vec<_>>()
    }

    fn get_col(&self, index: usize) -> Vec<&u32> {
        self.values.iter().skip(index).step_by(self.size).collect::<Vec<_>>()
    }

    fn is_visable_from_outside(&self, index: usize) -> bool {
        let tree_size = self.values.get(index).unwrap();
        let index_row = index / self.size;
        let index_col = index % self.size;

        let from_left = self.get_row(index_row).iter().take(index_col).all(|value| tree_size > value);
        let from_right = self.get_row(index_row).iter().skip(index_col+1).all(|value| tree_size > value);
        let from_top = self.get_col(index_col).iter().take(index_row).all(|value| tree_size > value);
        let from_bottom = self.get_col(index_col).iter().skip(index_row+1).all(|value| tree_size > value);
        
        from_left || from_right || from_top || from_bottom
        
    }

    fn scenic_score(&self, index: usize) -> u32 {
        let tree_size = self.values.get(index).unwrap();
        let index_row = index / self.size;
        let index_col = index % self.size;

        let to_left: Vec<u32> = self.get_row(index_row).iter().take(index_col).map(|v| **v).rev().collect();
        let to_right: Vec<u32> = self.get_row(index_row).iter().skip(index_col + 1).map(|v| **v).collect();

        let to_top: Vec<u32> = self.get_col(index_col).iter().take(index_row).map(|v| **v).rev().collect();
        let to_bottom: Vec<u32> = self.get_col(index_col).iter().skip(index_row + 1).map(|v| **v).collect();

        /* println!("Vec to the left {:?}", to_left);
        println!("Vec to the right {:?}", to_right);
        println!("Vec to the top {:?}", to_top);
        println!("Vec to the bottom {:?}", to_bottom); */

        QuadraticMatrix::get_score_from_vec(to_left, *tree_size) *
        QuadraticMatrix::get_score_from_vec(to_right, *tree_size) *
        QuadraticMatrix::get_score_from_vec(to_top, *tree_size) *
        QuadraticMatrix::get_score_from_vec(to_bottom, *tree_size)

    }

    fn get_score_from_vec(vec: Vec<u32>, tree_size: u32) -> u32 {

        let mut score = 0;

        for value in vec {
            score += 1;
            if value >= tree_size {
                break;
            }
        }

        score
    }
}
