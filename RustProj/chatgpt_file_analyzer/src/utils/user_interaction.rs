use std::io;

use super::data::FileAnalsis;

pub fn ask_file_name() -> String {
    // Ask for input
    println!("Please enter the name of a file you want to analyze:");  // prompt
    let mut file_to_analyze = String::new();  // declaration of variable to hold input
    io::stdin().read_line(&mut file_to_analyze).expect("Failed to read input");  // collect input

    // pop (remove) newline if needed
    if file_to_analyze.ends_with("\n") {
        file_to_analyze.pop();
    }

    // return file name String
    file_to_analyze
}

pub fn display_analysis_info(analysis: &FileAnalsis) {
    println!("{}", analysis);
}