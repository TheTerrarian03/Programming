// It looks like some of the digits are actually spelled out with letters: one,
// two, three, four, five, six, seven, eight, and nine also count as valid "digits".

// Equipped with this new information, you now need to find the real first
// and last digit on each line

// FINAL ANSWER: 54676

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
            // variables for leftmost and rightmost numbers
            let mut left_num: u32 = 69;
            let mut left_pos: usize = line.len()-1;

            let mut right_num: u32 = 69;
            let mut right_pos: usize = 0;

            // vector for all valid digits
            let valid_nums: Vec<u32> = vec![0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
            let valid_words: Vec<&str> = vec!["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];

            // LEFT
            {
                // go through all valid NUMBER digits
                for &num in &valid_nums {
                    // try to find num in the string
                    let num_as_char = char::from_digit(num, 10).expect("Failed to convert number");
                    let pos = line.find(num_as_char);

                    match pos {
                        Some(index) => {
                            if index <= left_pos {
                                left_num = num;
                                left_pos = index;
                            }
                        },
                        None => { }
                    }
                }

                //  go through all valid WORD digits
                for &word in &valid_words {
                    // try to find num in the string
                    let pos = line.find(word);

                    match pos {
                        Some(index) => {
                            if index <= left_pos {
                                // get the index of the equivalent number: u32
                                if let Some(word_index) = valid_words.iter().position(|&x| x == word) {
                                    left_num = valid_nums[word_index];
                                    left_pos = index;
                                }
                            }
                        },
                        None => { }
                    }
                }
            }

            // RIGHT
            {
                // go through all valid NUMBER digits
                for &num in &valid_nums {
                    // try to find num in the string
                    let num_as_char = char::from_digit(num, 10).expect("Failed to convert number");
                    let pos = line.rfind(num_as_char);

                    match pos {
                        Some(index) => {
                            if index >= right_pos {
                                right_num = num;
                                right_pos = index;
                            }
                        },
                        None => { }
                    }
                }


                //  go through all valid WORD digits
                for &word in &valid_words {
                    // try to find num in the string
                    let pos = line.rfind(word);

                    match pos {
                        Some(index) => {
                            if index >= right_pos {
                                // get the index of the equivalent number: u32
                                if let Some(word_index) = valid_words.iter().position(|&x| x == word) {
                                    right_num = valid_nums[word_index];
                                    right_pos = index;
                                }
                            }
                        },
                        None => { }
                    }
                }
            }

            // println!("Left: {} @ {}", left_num, left_pos);
            // println!("Right: {} @ {}", right_num, right_pos);

            // make digits into number
            let number: u32 = (left_num * 10) + right_num;

            // println!("number: {}", number);
            cal_number += number;
        }

        println!("Final Calibration Number: {}", cal_number);
    }
}
