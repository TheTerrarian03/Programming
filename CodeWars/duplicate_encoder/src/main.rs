fn main() {}

fn duplicate_encode(word: &str) -> String {
    let mut final_str = String::new();

    for char in word.to_lowercase().chars() {
        match (word.find(char), word.rfind(char)) {
            (Some(first), Some(last)) if first != last => final_str.push(')'),
            _ => final_str.push('('),
        }
    }

    // for char in word.to_lowercase().chars() {
    //     if word.find(char).unwrap() != word.rfind(char).unwrap() {
    //         final_str += ")";
    //     } else {
    //         final_str += "(";
    //     }
    // }

    final_str
}

#[test]
fn run_tests() {
    assert_eq!(duplicate_encode("din"), "(((");
    assert_eq!(duplicate_encode("recede"), "()()()");
    assert_eq!(duplicate_encode("Success"), ")())())", "should ignore case");
    assert_eq!(duplicate_encode("(( @"), "))((");
    assert_eq!(duplicate_encode(""), "");
}
