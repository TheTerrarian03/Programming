use std::{fmt, collections::HashMap};

// Define a struct to hold information about the file in one nice object
pub struct FileAnalsis {
    word_count: usize,
    line_count: usize,
    character_count: usize,
    word_occurrence: HashMap<String, usize>,
    number_occurrence: HashMap<String, usize>,
    digit_occurrence: HashMap<u32, usize>,
}

impl FileAnalsis {
    // Constructor to create a new instance with initial counts of 0
    pub fn new() -> Self {
        Self {
            word_count: 0,
            line_count: 0,
            character_count: 0,
            word_occurrence: HashMap::new(),
            number_occurrence: HashMap::new(),
            digit_occurrence: HashMap::new(),
        }
    }

    // Method to update counts based off of a line of text
    // Finds info for: { word_count, line_count, character_count }
    pub fn analyze_line(&mut self, line: &str) {
        self.word_count += line.split_whitespace().count();
        self.line_count += 1;
        self.character_count += line.chars().count();
    }

    fn analyze_word(&mut self, word: &str) {
        // get mutable reference to value in key for word
        let current_count = self.word_occurrence.entry(word.to_string()).or_insert(0);
        // increment the value
        *current_count += 1;
    }

    fn analyze_number(&mut self, number: f64) {
        // get mutable reference to value in key for word
        let current_count = self.number_occurrence.entry(number.to_string()).or_insert(0);
        // increment the value
        *current_count += 1;
    }

    // Finds info for: { word_occurrence, number_occurrence, digit_ocurrence }
    pub fn analyze_string(&mut self, string: &str) {
        // test if the string is a number only, or is otherwise a word
        let is_numeric = string.parse::<f64>();
        match is_numeric {
            Ok(number) => self.analyze_number(number),
            Err(_) => self.analyze_word(string),
        }

        // split the string into individual characters
        let individual_chars = string.chars();
        for character in individual_chars {
            // check if number
            println!("{}", character);
        }
        // println!("{:?}", is_numeric);
    }

    pub fn get_info(self) -> FileAnalsis {
        self
    }
}

// allow data to be printed prettily with println!("{}", fileAnalysisObj)
// by implementing the display trait for FileAnalysis
impl fmt::Display for FileAnalsis {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(
            f,
            "Word Count: {}\nLine Count: {}\nCharacter Count: {}",
            self.word_count, self.line_count, self.character_count
        )
    }
}