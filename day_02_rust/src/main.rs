fn solve(file: &str) {
    let content = std::fs::read_to_string(file).unwrap();
    let mut score = 0;

    for line in content.lines() {
        let split: Vec<&str> = line.split_ascii_whitespace().collect();
        let play  = split[0];
        let response = split[1];
        if play == "A" {
            if response == "X" { score += 1; score += 3; }
            if response == "Y" { score += 2; score += 6; }
            if response == "Z" { score += 3; score += 0; }
        }
        if play == "B" {
            if response == "X" { score += 1; score += 0; }
            if response == "Y" { score += 2; score += 3; }
            if response == "Z" { score += 3; score += 6; }
        }
        if play == "C" {
            if response == "X" { score += 1; score += 6; }
            if response == "Y" { score += 2; score += 0; }
            if response == "Z" { score += 3; score += 3; }
        }
    }

    println!("Part 1 - {file}: {:?}", score);

    score = 0;
    for line in content.lines() {
        let split: Vec<&str> = line.split_ascii_whitespace().collect();
        let play  = split[0];
        let response = split[1];
        if play == "A" {
            if response == "Z" { score += 2; score += 6; }
            if response == "Y" { score += 1; score += 3; }
            if response == "X" { score += 3; score += 0; }
        }
        if play == "B" {
            if response == "Z" { score += 3; score += 6; }
            if response == "Y" { score += 2; score += 3; }
            if response == "X" { score += 1; score += 0; }
        }
        if play == "C" {
            if response == "Z" { score += 1; score += 6; }
            if response == "Y" { score += 3; score += 3; }
            if response == "X" { score += 2; score += 0; }
        }
    }

    println!("Part 2 - {file}: {:?}", score);
}


fn main() {
    solve("../day_02/example.txt");
    solve("../day_02/input.txt");
}
