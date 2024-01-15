use std::io;
use std::cmp::Ordering;
use rand::Rng;
use std::fs::File;
use std::io::Write;


fn write_to_file(file: &mut File, to_write: &str) {
    match file.write_all(to_write.as_bytes()) {
        Ok(_) => println!("Success writing"),
        Err(error) => println!("Error writing because: {error}")
    }
}

fn main() {
    // generate a random secret number
    let secret_number = rand::thread_rng().gen_range(1..=100);

    // print a user prompt and ask for input
    println!("Welcome to guess the number!");

    let guess: u32;

    // user input loop
    loop {
        // declare variable to hold guess
        let mut input = String::new();

        // read input from terminal
        println!("Please enter your guess:");
        io::stdin()
            .read_line(&mut input)
            .expect("Failed to read input");

        // try to convert from string to number
        match input.trim().parse::<u32>() {
            Ok(number) => {
                println!("Valid number entered. Continuing.");
                guess = number;
                break;
            },
            Err(error) => {
                println!("Error! Please enter a number. Error: {error}")
            }
        }
    }

    // compare guess to secret number
    match guess.cmp(&secret_number) {
        Ordering::Less => println!("Too Small! :("),
        Ordering::Equal => println!("You got it! On Point! :D"),
        Ordering::Greater => println!("Too Large! :(")
    };

    // set up file for writing to as output
    let filename = "output.txt";
    let mut file: File = File::create(filename).expect("Failed to create/open file");

    // add secret number info
    let info_secret_number = format!("The secret number was: {secret_number}\n");
    write_to_file(&mut file, &info_secret_number);

    // add user-inputted number info
    let info_user_input = format!("You entered: {guess}\n");
    write_to_file(&mut file, &info_user_input);

    // add info on whether the user guessed it or not
    let user_info_correct = match guess.cmp(&secret_number) {
        Ordering::Less => "Too Small! :(\n",
        Ordering::Equal => "You got it! On Point! :D\n",
        Ordering::Greater => "Too Large! :(\n"
    };
    write_to_file(&mut file, &user_info_correct)

}
