use std::fs::read_to_string;

struct Dir {
    files: Vec<u32>,
    dirs: Vec<Dir>
}

impl Dir {
    
    fn new() -> Dir {
        Dir {
            files: Vec::new(),
            dirs: Vec::new(),
        }
    }

    fn add_file(&mut self, size: u32) {
        self.files.push(size);
    }

    fn add_dir(&mut self, dir: Dir) {
        self.dirs.push(dir);
    }

    fn size_of_files(&self) -> u32 {
        self.files.iter().sum()
    }
}

fn main() {

    let input = read_to_string("input/input.txt").unwrap();

    let root = Dir::new();
    let current_directory = root;

}

