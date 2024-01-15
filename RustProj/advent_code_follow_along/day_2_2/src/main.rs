// the Elf poses a second question: in each game you played, what is the fewest
// number of cubes of each color that could have been in the bag to make the
// game possible?

// Again consider the example games from earlier:

// Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
// Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
// Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
// Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
// Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green

// The power of a set of cubes is equal to the numbers of red, green, and blue
// cubes multiplied together. The power of the minimum set of cubes in game 1
// is 48. In games 2-5 it was 12, 1560, 630, and 36, respectively. Adding up
// these five powers produces the sum 2286.

// For each game, find the minimum set of cubes that must have been present.
// What is the sum of the power of these sets?

// FINAL ANSWER: 72970

use std::{fs::File, io::Read};

fn main() {
    // constants for max values allowed
    const RED_MAX: u32 = 12;
    const GREEN_MAX: u32 = 13;
    const BLUE_MAX: u32 = 14;

    // variable to hold game ID total-up
    let mut game_power_total: u32 = 0;

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
        // variable for max num of each color
        // red, green, blue
        let mut colors_maxes: Vec<u32> = vec![0, 0, 0];

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
            // split the piece of info into a vector of info about each individual cube color
            let cube_infos = info_piece.split(", ").collect::<Vec<&str>>();

            for cube_info in cube_infos {
                // if has red info
                if let Some(_) = cube_info.find("red") {
                    let red_amnt = cube_info_to_num(cube_info);
                    colors_maxes[0] = std::cmp::max(colors_maxes[0], red_amnt);
                }
                // if has green info
                if let Some(_) = cube_info.find("green") {
                    let green_amnt = cube_info_to_num(cube_info);
                    colors_maxes[1] = std::cmp::max(colors_maxes[1], green_amnt);
                }
                // if has blue info
                if let Some(_) = cube_info.find("blue") {
                    let blue_amnt = cube_info_to_num(cube_info);
                    colors_maxes[2] = std::cmp::max(colors_maxes[2], blue_amnt);
                }
            }
        }

        let game_power = colors_maxes[0] * colors_maxes[1] * colors_maxes[2];
        game_power_total += game_power;

        println!("Game #{} power: {}, color maxes: {:?}", game_n, game_power, colors_maxes);
    }

    println!("Game ID Total: {}", game_power_total);
}

fn cube_info_to_num(input_str: &str) -> u32 {
    input_str.split(" ").collect::<Vec<&str>>()[0]                  // split the string into ["#", "color"] and select the "#" item
    .parse::<u32>().expect("Failed to convert # of cubes to u32!")  // try to convert that string into a u32 and return
}