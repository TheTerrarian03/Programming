use std::io::{self, Write};


fn user_loop_f64(prompt: &str, error_prompt: &str) -> f64 {
    // variable for user input
    let mut user_input = String::new();

    loop {
        // prompt
        io::stdout().write_all(prompt.as_bytes()).expect("Failed to print prompt");

        // get input
        io::stdin().read_line(&mut user_input).expect("Failed to read input");

        // try to convert to number
        match user_input.trim().parse::<f64>() {
            Ok(number) => return number,
            Err(_) => io::stdout().write_all(error_prompt.as_bytes()).expect("Failed to print prompt")
        }
    }
}

fn user_loop_choice(prompt: &str) -> u32 {
    // variable for user input
    let mut user_input = String::new();

    loop {
        // prompt
        io::stdout().write_all(prompt.as_bytes()).expect("Failed to print prompt");

        // get input
        io::stdin().read_line(&mut user_input).expect("Failed to read input");

        // try to convert to number
        match user_input.trim().parse::<u32>() {
            Ok(number) => {
                if number == 1 || number == 2 {
                    return number;
                    
                } else {
                    println!("Please enter a number (1 or 2)!");
                }
            },
            Err(_) => println!("Please enter a number (1 or 2)!")
        }
    }
}

fn main() {
    // print prompts
    println!("Please choose a conversion option:");
    println!("1) Fahrenheit to Celsius");
    println!("2) Celsius to Fahrenheit");

    let choice = user_loop_choice("Enter number:\n");

    // f to c
    if choice == 1 {
        println!("Enter your temperature in F:");
        let f = user_loop_f64("Please enter your temperature in F", "Please enter a valid floating-point number");
        let c = (f - 32.0) * (5.0/9.0);
        println!("Here is your new temperature: {}", c)

    } else if choice == 2 {
        println!("Enter your temperature in C:");
        let c = user_loop_f64("Please enter your temperature in C", "Please enter a valid floating-point number");
        let f = (c * (9.0/5.0)) + 32.0;
        println!("Here is your new temperature: {}", f)
    } else {
        println!("You broke it.")
    }
}
