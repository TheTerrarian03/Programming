use std::fs::{File, OpenOptions};
use std::io::prelude::*;
use std::io::{self, Write};
use core::time;
use std::thread;

// vec!["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "!", "\"", "#", "$", "%", "&", "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@", "[", "\\", "]", "^", "_", "`", "{", "|", "}", "~", " "];
fn main() {
    // define constraints:
    // character set
    let characters: Vec<&str> = vec!["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "!", "\"", "#", "$", "%", "&", "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@", "[", "\\", "]", "^", "_", "`", "{", "|", "}", "~", " "];
    let string_len: u32 = 5;

    // print info about how many combinations should be generated
    println!("{} combos will be generated!", usize::pow(characters.len(), u32::from(string_len)));

    // make data obj
    let mut combo_data = ComboData::new("combinations.txt");
    combo_data.clear_file();
    combo_data.total_count = usize::pow(characters.len(), u32::from(string_len));

    // gen files
    generate_combinations(&characters, string_len, String::from(""), &mut combo_data);

    println!("\ndone");
}

// custom struct to hold file data
struct ComboData {
    file: File,
    curr_count: usize,
    total_count: usize,
}

impl ComboData {
    pub fn new(filename: &str) -> Self {
        Self {
            file: File::create(filename).expect("Failed to open/create file"),
            curr_count: 0,
            total_count: usize::MAX
        }
    }

    pub fn clear_file(&mut self) {
        self.file.set_len(0).expect("Failed to truncate file");
    }

    pub fn add_combo(&mut self, new_combo: String) {
        let new_combo = new_combo + "\n";
        self.file.write_all(new_combo.as_bytes()).expect("Failed to write new combo to file");
        self.curr_count += 1;
    }

    pub fn get_curr_count(&mut self) -> usize {
        self.curr_count
    }

    pub fn get_total_count(&mut self) -> usize {
        self.total_count
    }
}

fn generate_combinations(characters: &Vec<&str>, length: u32, current_combination: String, combo_data: &mut ComboData) {
    if length == 0 {
        // no more to add, print/return combination
        // println!("Found combination: {}", current_combination);
        combo_data.add_combo(current_combination);
        // println!("Current num: {}", combo_data.get_curr_count())
        print_curent_progress(combo_data.get_curr_count(), combo_data.get_total_count())
    } else {
        for character in characters {
            // add next character to the current combination
            let new_combination: String = current_combination.clone() + character;

            generate_combinations(characters, length - 1, new_combination, combo_data);
        }
    }
}

fn print_curent_progress(current_count: usize, total_count: usize) {
    print!("\r{} - {}%             ", make_progressbar(current_count, total_count, 20), (current_count as f32 / total_count as f32 * 100.0));
    io::stdout().flush().unwrap(); // Flush the output buffer
    // thread::sleep(time::Duration::from_millis(1));
}

fn make_progressbar(current_count: usize, max_count: usize, length: i32) -> String {
    let percent_filled: f32 = current_count as f32 / max_count as f32;
    let filled: i32 = (percent_filled * length as f32) as i32;
    let empty: i32 = length - filled;

    // println!("c: {}, m: {}, p: {}, f: {}, e: {}", current_count, max_count, percent_filled, filled, empty);

    let mut progress_string = String::new();

    progress_string.push_str("[");
    
    for _ in 0..filled {
        progress_string.push_str("=");
    }

    for _ in 0..empty {
        progress_string.push_str(" ");
    }

    progress_string.push_str("]");

    progress_string
}