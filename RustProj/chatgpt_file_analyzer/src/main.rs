// [ ] Word Count:           Count the total number of words in the file.
// [ ] Line Count:           Count the total number of lines in the file.
// [ ] Character Count:      Count the total number of characters in the file.
// [ ] Most Frequent Words:  Identify and display the most frequently occurring words in the file.
// [ ] Longest Word:         Identify and display the longest word in the file.
// [ ] Average Word Length:  Calculate and display the average length of words in the file.
// [ ] Error Handling:       Implement proper error handling to gracefully handle cases where the file doesn't exist or cannot be read.

use std::io;
use utils::data::FileAnalsis;
mod utils;

fn main() {
    // Step 1: Ask for Input File
    let file_to_analyze = utils::user_interaction::ask_file_name();
    println!("Your file name: {}", file_to_analyze);

    // Step 2: Make sure file exists
    match utils::file_utils::validate_file_exists(file_to_analyze.clone()) {
        true => println!("Success! Your file exists."),
        false => panic!("**Fail! Your file either doesn't exist or isn't in the right spot.**")
    }

    // Step 3: Get file contents
    let file_contents = utils::file_utils::read_file_contents(file_to_analyze.clone());
    // println!("File contents: \n{}", file_contents);

    // Step 4: Analyze the file!
    // 4.1: declare the file analysis object to hold our data
    let mut analysis = FileAnalsis::new();

    // 4.2: Analyze the file line by line
    let lines = file_contents.split("\n");
    for line in lines {
        // This gives us info about: { word_count, line_count, character_count }
        analysis.analyze_line(line);

        // This gives us info about: { word_occurrence, number_occurrence, digit_occurrence }
        let strings_in_line = line.split_whitespace();
        for string in strings_in_line {
            analysis.analyze_string(string);
        }
    }

    // Step 4.3: Analyze the file word by word
    // This gives us info about: { word_frequency }


    // Step 5: Print info to user
    utils::user_interaction::display_analysis_info(&analysis);
    
    // 4.2: Analyze the file character by character
    // This gives us info about 



//     println!("Please enter the name of a file you want to analyze:");
//     let mut file_to_analyze = String::new();
//     io::stdin().read_line(&mut file_to_analyze).expect("Failed to read input");

//     // declare file contents object
//     let file_content: String;

//     // See if file exists or not
//     match std::fs::File::open(file_to_analyze) {
//         Ok(mut opened) => {
//             println!("Success! File found. Analyzing...");

//             // Read the file contents into the previously delcared string
//             file_content = utils::file_utils::read_file_contents(&mut opened);
//             println!("File contents: {}", file_content);
//         }
//         Err(_) => println!("Fail! File must not exist. Please check spelling and file location.")  // error, tell user
//     };
}