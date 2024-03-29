use itertools::Itertools;

const NUMBERS: &[&str] = &[
    "0", "zero", "1", "one", "2", "two", "3", "three", "4", "four", "5", "five", "6", "six", "7",
    "seven", "8", "eight", "9", "nine",
];

fn main() {
    let contents = include_str!("input-2.txt");


    let sum: usize = contents
        .lines()
        .map(|line| {
            let (a, b) = NUMBERS
                .iter()
                .enumerate()
                .flat_map(|(i, &n)| line.match_indices(n).map(move |(idx, _)| (idx, i / 2)))
                .minmax()
                .into_option()
                .unwrap();
            a.1 * 10 + b.1
        })
        .sum();
    println!("{}", sum);
}
