fn series_sum(n: u32) -> String {
    // for i in
    if n <= 0 {
        return String::from("0.00");
    }

    let mut total = 0.0;

    for i in 1..n + 1 {
        println!("i: {i}");
        total += 1.0 / ((i as f32) * 3.0 - 2.0);
    }

    return String::from(format!("{:.2}", total));
}
