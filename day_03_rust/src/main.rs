use std::collections::HashSet;

fn calc_priority(c: char, score: &mut u32) {
    if c.is_uppercase() {
        *score += c as u32 - 'A' as u32 + 27;
    } else {
        *score += c as u32 - 'a' as u32 + 1;
    }
}


fn solve(file: &str) {
    let content = std::fs::read_to_string(file).unwrap();
    let mut score = 0;

    for line in content.lines() {
        let comp1: HashSet<_> = line[..line.len()/2].chars().into_iter().collect();
        let comp2: HashSet<_> = line[line.len()/2..].chars().into_iter().collect();

        // Use set intersection to find common character
        let comp_inter = comp1.intersection(&comp2);

        let c = comp_inter.last().unwrap().clone();
        calc_priority(c, &mut score);
    }
    println!("Part 1 - {file}: {:?}", score);

    score = 0;
    // Use Lines iterator to examine sacks in groups of 3
    let mut lines = content.lines();
    while let Some(line) = lines.next() {
        let sack1: HashSet<_> = line.chars().into_iter().collect();
        let sack2: HashSet<_> = lines.next().unwrap().chars().into_iter().collect();
        let sack3: HashSet<_> = lines.next().unwrap().chars().into_iter().collect();

        // Use set intersection to find common character across 3 sacks
        // TODO: Is there a better way to chain intersections? What's up the the HashSet vs Intersection objects?
        let sacks_inter12 = &sack1 & &sack2;
        let sacks_inter123 = &sacks_inter12 & &sack3;

        let c = sacks_inter123.iter().next().unwrap().clone();
        calc_priority(c, &mut score);
    }
    println!("Part 2 - {file}: {:?}", score);
}


fn main() {
    solve("../day_03/example.txt");
    solve("../day_03/input.txt");
}
