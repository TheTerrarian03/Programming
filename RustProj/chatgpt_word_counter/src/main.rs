use std::{io, collections::HashMap};

fn main() {
    // Step 1: User Input
    println!("Enter a sentence or paragraph:");
    let mut input_text = String::new();
    io::stdin().read_line(&mut input_text).expect("Failed to read input!");

    // Step 2: Count Words
    let word_counts = count_words(&input_text);

    // Step 3: Display Results
    println!("Word Counts:");
    for (word, count) in word_counts {
        println!("Word \"{}\" used {} times", word, count);
    }

}

// Function to count occurrences of words
fn count_words(text: &str) -> HashMap<String, i32> {
    // declare/initialize new hashmap
    let mut word_hash = HashMap::new();

    let split_text = text.split(' ');

    for word_str in split_text {
        let mut word = String::from(word_str);
        if word.ends_with("\n") {
            word.pop();
        }

        // Get count of word
        let count = word_hash.entry(word.clone()).or_insert(0);

        if *count == 0 {
            println!("Word NOT found: {}", &word);
        } else {
            println!("Word found: {}", &word);
            
        }

        *count += 1;
    }

    // return hashmap
    word_hash
}