/// Return a String with all characters masked as '#' except the last 4.
fn maskify(cc: &str) -> String {
    if cc.len() <= 4 {
        return String::from(cc);
    }

    let split = cc.split_at(cc.len() - 4);

    return "#".repeat(split.0.len()) + split.1;
}
