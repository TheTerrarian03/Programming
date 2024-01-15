fn main() {
    // define constraints:
    // character set
    let characters: Vec<&str> = vec!["a", "b", "c"];
    let string_len: u32 = 22;

    // print info about how many combinations should be generated
    println!("{} combos will be generated!", usize::pow(characters.len(), u32::from(string_len)));

    // make sure file exists and clear it
    let mut file = File::create("combinations.txt").expect("Failed to create/open file");
    clear_file(&mut file);

    // gen files
    generate_combinations(&characters, string_len, String::from(""), &mut file);

    println!("done");
}

fn clear_file(file: &mut File) {
    file.set_len(0).expect("Failed to truncate file");
}

fn write_to_file(file: &mut File, to_write: String) {
    let to_write = to_write + "\n";
    file.write_all(to_write.as_bytes()).expect("Failed to write to file");
}

fn generate_combinations(characters: &Vec<&str>, length: u32, current_combination: String, file: &mut File) {
    if length == 0 {
        // no more to add, print/return combination
        // println!("Found combination: {}", current_combination);
        write_to_file(file, current_combination);
    } else {
        for character in characters {
            // add next character to the current combination
            let new_combination: String = current_combination.clone() + character;

            generate_combinations(characters, length - 1, new_combination, file);
        }
    }
}
