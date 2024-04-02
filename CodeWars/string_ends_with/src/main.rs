fn main() {
    println!("Hello, world!");
}

fn solution(word: &str, ending: &str) -> bool {
    word.ends_with(ending)
}

// Rust test example:
// TODO: replace with your own tests (TDD), these are just how-to examples.
// See: https://doc.rust-lang.org/book/testing.html

#[test]
fn returns_expected() {
  assert_eq!(true, solution("abc", "c"));
  assert_eq!(false, solution("strawberry", "banana"));
  assert_eq!(true, solution("abc", "bc"));
  assert_eq!(false, solution("abc", "d"));
  assert_eq!(true, solution("soda", "oda"));
}
