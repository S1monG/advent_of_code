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
        
        let from_left = self.get_row(index_row).iter().take(index_col).all(|value| tree_size > value);
        let from_right = self.get_row(index_row).iter().skip(index_col+1).all(|value| tree_size > value);
        
        // from top doesn't seem to be working right, need to check that more in depth
        // probobly easiest to do with println debugging.
        let from_top = self.get_col(index_row).iter().take(index_row).all(|value| tree_size > value);
        let from_bottom = self.get_col(index_row).iter().skip(index_row+1).all(|value| tree_size > value);
        
        println!("From left {}   From right {}   From top {}   From bottom {}", from_left, from_right, from_top, from_bottom);

        from_left || from_right || from_top || from_bottom
        
    }
}
