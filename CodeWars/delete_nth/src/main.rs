use std::iter::Filter;

fn main() {
    delete_nth(&[20,37,20,21], 1);
}

fn delete_nth(lst: &[u8], n: usize) -> Vec<u8> {
    let motifs: Vec<u8> = Vec::new();

    for motif in lst {
        if (motifs.iter().filter(|&x) )
        println!("Motif: {motif}")
    }

    motifs
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_basic() {
        assert_eq!(delete_nth(&[20,37,20,21], 1), vec![20,37,21]);
        assert_eq!(delete_nth(&[1,1,3,3,7,2,2,2,2], 3), vec![1, 1, 3, 3, 7, 2, 2, 2]);
    }
}
