use std::fs::File;
use std::io::Read;

pub fn validate_file_exists(filename: String) -> bool {
    match File::open(filename) {
        Ok(_) => true,
        Err(_) => false
    }
}

pub fn read_file_contents(filename: String) -> String {
    // declare file content string and file object
    let mut file_content = String::new();
    let mut file: File;
    
    // try opening file
    match std::fs::File::open(filename) {
        Ok(opened) => {
            // success, assign file to object
            file = opened;
        }
        Err(_) => panic!("Fail! File must not exist. Please check spelling and file location.")  // error, tell user
    };
    
    // read file content to string
    file.read_to_string(&mut file_content).expect("Failed to read file contents");

    // return content
    file_content
}