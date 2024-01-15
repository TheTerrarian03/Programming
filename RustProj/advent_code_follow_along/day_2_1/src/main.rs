// You play several games and record the information from each game (your
// puzzle input). Each game is listed with its ID number (like the 11 in
// Game 11: ...) followed by a semicolon-separated list of subsets of
// cubes that were revealed from the bag (like 3 red, 5 green, 4 blue)

// an example might look like this:

// Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
// Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
// Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
// Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
// Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green

// The Elf would first like to know which games would have been possible
// if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?

// Determine which games would have been possible if the bag had been
// loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes.
// What is the sum of the IDs of those games?

// FINAL ANSWER: 3099

use std::{fs::File, io::Read};

fn main() {
    // constants for max values allowed
    const RED_MAX: u32 = 12;
    const GREEN_MAX: u32 = 13;
    const BLUE_MAX: u32 = 14;

    // variable to hold game ID total-up
    let mut game_id_total: u32 = 0;

    // variable to hold file contents
    let mut file_contents = String::new();

    // open file, read, and put contents into String buffer
    {
        let mut file = File::open("puzzle.txt").expect("Failed to open file");
        file.read_to_string(&mut file_contents).expect("Failed to read contents of file to String");
    }

    // split file into lines
    let file_lines = file_contents.split("\n");

    // loop through each line
    for line in file_lines {
        // variable for is game valid
        let mut game_valid = true;
        
        // get the game #, also known as the game ID
        let game_n = {
            line.split(": ").collect::<Vec<&str>>()[0]          // split into ["Game #", "Info; Info; ..."] and select the "Game #" item
            .split(" ").collect::<Vec<&str>>()[1]               // split into ["Game", "#"] and select the "#" item
            .parse::<u32>().expect("Failed to convert game #")  // then convert to u32 number for adding
        };
        
        // get a vector of all seperate pieces of info about the game (i.e. ["# red, # blue", "# green", etc])
        let game_infos = {
            line.split(": ").collect::<Vec<&str>>()[1]  // Split into ["Game #", "Info; Info; ..."] and select the "Info; ..." item
            .split("; ").collect::<Vec<&str>>()         // split into seperate ["Info", "Info", ...] items and set as the vector
        };

        // loop through each piece of info shown at one time
        for info_piece in game_infos {
            // info about each color for the current info piece
            let mut red_amnt:   u32 = 0;
            let mut green_amnt: u32 = 0;
            let mut blue_amnt:  u32 = 0;
            
            // split the piece of info into a vector of info about each individual cube color
            let cube_infos = info_piece.split(", ").collect::<Vec<&str>>();

            for cube_info in cube_infos {
                // if has red info
                if let Some(_) = cube_info.find("red") {
                    red_amnt = cube_info_to_num(cube_info);
                }
                // if has green info
                if let Some(_) = cube_info.find("green") {
                    green_amnt = cube_info_to_num(cube_info);
                }
                // if has blue info
                if let Some(_) = cube_info.find("blue") {
                    blue_amnt = cube_info_to_num(cube_info);
                }
            }

            if (red_amnt > RED_MAX) || (green_amnt > GREEN_MAX) || (blue_amnt > BLUE_MAX) {
                game_valid = false;
            }
        }

        if game_valid {
            game_id_total += game_n;
        }

        println!("Game #{} valid: {}", game_n, game_valid);
    }

    println!("Game ID Total: {}", game_id_total);
}

fn cube_info_to_num(input_str: &str) -> u32 {
    input_str.split(" ").collect::<Vec<&str>>()[0]                  // split the string into ["#", "color"] and select the "#" item
    .parse::<u32>().expect("Failed to convert # of cubes to u32!")  // try to convert that string into a u32 and return
}
