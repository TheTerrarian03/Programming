fn main() {
    const TOWER_HEIGHT: usize = 35;

    for inc_height in 1..TOWER_HEIGHT {
        println!();
        let tower = tower_builder(inc_height);

        for floor in tower {
            println!("{floor}");
        }
    }

}

fn tower_builder(n_floors: usize) -> Vec<String> {
    let mut tower: Vec<String> = Vec::new();                // tower to build & return
    let max_floor_width: usize = 1 + (2 * (n_floors - 1));  // width of bottom floor

    for i in 1..n_floors+1 {
        // establish information about the floor
        let floor_width = 1 + 2 * (i-1);              // width of the floor, only stars
        let space = (max_floor_width-floor_width)/2;  // space on each side to be filled

        tower.push(format!(
            "{}{}{}",                 // {left}{floor}{right} format
            " ".repeat(space),        // left  space
            "*".repeat(floor_width),  // floor stars
            " ".repeat(space))        // right space
        );
    }

    tower
}

#[cfg(test)]
mod tests {
    use super::tower_builder;

    #[test]
    fn fixed_tests() {
        assert_eq!(tower_builder(1), vec!["*"]);
        assert_eq!(tower_builder(2), vec![" * ", "***"]);
        assert_eq!(tower_builder(3), vec!["  *  ", " *** ", "*****"]);
        assert_eq!(tower_builder(6), vec!["     *     ", "    ***    " ,"   *****   ", "  *******  ", " ********* ", "***********"]);
    }
}
