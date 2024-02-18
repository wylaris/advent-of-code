use std::rc;

const INPUT: &str = include_str!("input-1.txt");

fn extract_game(input: &str) -> u32 {
    let parts: Vec<&str> = input.split(' ').collect();
    parts[1].parse::<u32>().unwrap()
}


fn extract_colors(input: &str) -> (u32, u32, u32) {
    let mut r = 0;
    let mut g = 0;
    let mut b = 0;

    let mut working_str = input.replace(';', ",");
    working_str = working_str.trim().to_string();
    let parts: Vec<&str> = working_str.split(",").collect();
    for part in parts {
        let working_part: &str = part.trim();
        let split_colors: Vec<&str> = working_part.split(" ").collect();
        let color_numb = split_colors[0].parse::<u32>().unwrap();
        match split_colors[1] {
            "red" => r = if r < color_numb {color_numb} else {r},
            "green" => g = if g < color_numb {color_numb} else {g},
            "blue" => b = if b < color_numb {color_numb} else {b},
            _ => unreachable!(),
        }
    }
    (r, g, b)
}

fn determine_possible(r: u32, g: u32, b: u32) -> bool {
    if r <= 12 && g <= 13 && b <= 14 {
        return true;
    }
    return false;
}


fn main() {
    let mut possible_rounds_sum: u32 = 0;
    let mut most_cubes_sum: u32 = 0;
    for line in INPUT.lines() {
        let split_game: Vec<&str> = line.split(':').collect();
        let game_numb: u32 = extract_game(split_game[0]);
        let (r_color, g_color, b_color) = extract_colors(split_game[1]);
        let possible: bool = determine_possible(r_color, g_color, b_color);
        // dbg!(game_numb, r_color, g_color, b_color, possible);
        most_cubes_sum = most_cubes_sum + (r_color * g_color * b_color);
        if possible {
            possible_rounds_sum = possible_rounds_sum + game_numb;
            // dbg!(game_numb, possible_rounds_sum);
        }
    }
    println!("Part 1: {:?}", possible_rounds_sum);
    println!("Part 2: {:?}", most_cubes_sum);
}