use core::time;
use std::io::{self, Write};
use std::thread;

fn main() {
    println!("A progress bar:");

    const MAX: i32 = 100;

    for i in 0..MAX + 1 {
        print!("\r{} - {}%\n", make_progressbar(i, MAX, 17), (i / MAX));
        // io::stdout().flush().unwrap(); // Flush the output buffer
        // thread::sleep(time::Duration::from_millis(50));
    }

    println!("\nComplete! Hooray!");
}

fn make_progressbar(current_count: i32, max_count: i32, length: i32) -> String {
    let percent_filled: f32 = current_count as f32 / max_count as f32;
    let filled: i32 = (percent_filled * length as f32) as i32;
    let empty: i32 = length - filled;

    println!(
        "c: {}, m: {}, p: {}, f: {}, e: {}",
        current_count, max_count, percent_filled, filled, empty
    );

    let mut progress_string = String::new();

    progress_string.push_str("[");

    for _ in 0..filled {
        progress_string.push_str("=");
    }

    for _ in 0..empty {
        progress_string.push_str(" ");
    }

    progress_string.push_str("]");

    progress_string
}

// fn make_progressbar(percent: i32, scale: i32) -> String {
//     let filled = if percent == 100 {10 * scale} else {(percent/10 % 10) * scale};
//     let empty = (10 * scale) - filled;

//     let mut progress_string = String::new();

//     progress_string.push_str("[");

//     for _ in 0..filled {
//         progress_string.push_str("=");
//     }

//     for _ in 0..empty {
//         progress_string.push_str(" ");
//     }

//     progress_string.push_str("]");

//     progress_string

//     // alternatively:
//     // let progress_string = format!("[{}{}]", "=".repeat(filled as usize), " ".repeat(empty as usize));
//     // from ChatGPT
// }
