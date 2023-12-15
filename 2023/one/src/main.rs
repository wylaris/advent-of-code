fn main() {
    let contents = include_str!("input.txt");
    let parts = contents.split('\n');
    let mut numbs: Vec<u8> = vec![];
    for part in parts {
        let mut first: String = "".to_string();
        let mut last: String = "".to_string();
        // println!("{}", part.trim());
        for char in part.chars() {
            if char.is_numeric(){
                // let digit = char.to_string().parse().unwrap();
                if first == "" {
                    first = char.to_string();
                    last =  char.to_string();
                }
                else {
                    last =  char.to_string();
                }
            }
        }
        first.push_str(&last);
        println!("{}", first);
        let digit: u8 = first.parse().unwrap();
        numbs.push(digit);
    }
    let mut total:u32 = 0;
    for numb in numbs {
        total = total + numb as u32;
    }
    println!("{}", total)
}
