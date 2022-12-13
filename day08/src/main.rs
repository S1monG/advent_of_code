use std::fs::read_to_string;

fn main() {

    // the grid is 99x99
    let input = read_to_string("input/example.txt").unwrap();

    let mut vec = Vec::new();

    input.lines().for_each(|line| 
        vec.append(&mut line.chars().map(|c| c.to_digit(10).unwrap()).collect::<Vec<_>>())
    );

    let size = input.lines().count();
    let qm = QuadraticMatrix::new(size, vec);

    let mut visible_trees = 0;

    for tree in 0..size*size {
        if qm.is_visable(tree) {
            visible_trees += 1
        }
    }

    println!("Part 1: {}", visible_trees);

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

    fn is_visable(&self, index: usize) -> bool {
        let tree_size = self.values.get(index).unwrap();
        let index_row = index / self.size;
        let index_col = index % self.size;

        println!("Row {index_row}    Col {index_col}");

        // check visibility from left and right
        self.get_row(index_row).iter().take(index_col).any(|value| *value >= tree_size) ||
        self.get_row(index_row).iter().skip(index_col).any(|value| *value >= tree_size) ||

        // check visibility from top and bottom
        self.get_col(index_row).iter().take(index_row).any(|value| *value >= tree_size) ||
        self.get_col(index_row).iter().skip(index_row).any(|value| *value >= tree_size)

    }
}
