// "The newly-improved calibration document consists of lines of text; each
// line originally contained a specific calibration value that the Elves now
// need to recover. On each line, the calibration value can be found by
// combining the first digit and the last digit (in that order) to form 
// single two-digit number"

// "Consider your entire calibration document. What is the sum of all of
// the calibration values?"

// i.e. 12 + 38 + 15 + 77. Adding these together produces 142.

// FINAL ANSWER = 53921

use std::{fs::File, io::Read};

fn main() {
    // define variable to hold file contents
    let mut file_contents = String::new();
    
    // scope for file handling
    {
        // define file object
        let mut file: File;

        // try to open file and set variable to object
        match File::open("puzzle.txt") {
            Ok(opened) => file = opened,
            Err(_) => panic!("Failed to open file.")
        }
    
        // read the contents into the contents variable
        file.read_to_string(&mut file_contents).expect("Failed to read content from file.");
    }

    // split the contents into seperate lines
    let file_lines = file_contents.split_whitespace();

    // variable for end total
    let mut cal_number: u32 = 0;

    // scope for number finding
    {
        // iterate through each line
        for line in file_lines {
            // variables for char position
            let mut left_pos: usize = 0;
            let mut right_pos: usize = line.len()-1;

            let mut left_num: u32 = 69;
            let mut right_num: u32 = 69;

            // loop to go through all characters in the line
            while left_pos <= right_pos {
                // if left not zero, get left
                if left_num == 69 {
                    if let Some((_, l_char)) = line.char_indices().nth(left_pos) {
                        // println!("{}", l_char);
                        if l_char.is_numeric() {
                            match l_char.to_digit(10) {
                                Some(number) => left_num = number,
                                None => {}
                            }
                        }
                    }
                }

                // if right not zero, get right
                if right_num == 69 {
                    if let Some((_, r_char)) = line.char_indices().nth(right_pos) {
                        // println!("{}", r_char);
                        if r_char.is_numeric() {
                            match r_char.to_digit(10) {
                                Some(number) => right_num = number,
                                None => {}
                            }
                        }
                    }
                }

                left_pos += if left_num == 69 {1} else {0};
                right_pos -= if right_num == 69 {1} else {0};

                if (left_num != 69) && (right_num != 69) {
                    break;
                }
            }

            // check if any digits are still a 69
            if (left_num == 69) && (right_num == 69) {
                left_num = 0;
                right_num = 0;
            } else if right_num == 69 {
                right_num = left_num;
            } else if left_num == 69 {
                left_num = right_num
            }

            // make digits into number
            let number: u32 = (left_num * 10) + right_num;

            println!("number: {}", number);
            cal_number += number;
        }

        println!("Final Calibration Number: {}", cal_number);
    }
}
