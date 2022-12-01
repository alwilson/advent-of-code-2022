use std::fs;


fn solve(file: &str) {
    let contents = fs::read_to_string(file).unwrap();

    let mut elf_cals = vec![];
    let mut cals = vec![];

    for line in contents.lines() {
        if line.is_empty() {
            elf_cals.push(cals);
            cals = vec![]
        } else {
            // TODO: Why is the type needed here?
            let num: u32 = line.parse::<u32>().unwrap();
            cals.push(num);
        }
    }

    // TODO: Why is the type needed here?
    let mut tot_cals: Vec<u32> = elf_cals.iter().map(|x| x.iter().sum()).collect();
    tot_cals.sort();
    tot_cals.reverse();

    println!("Part 1 - {file}: {:?}", tot_cals[0]);
    println!("Part 2 - {file}: {:?}", tot_cals[0..3].iter().sum::<u32>());
}


fn main() {
    solve("../day_01/example.txt");
    solve("../day_01/input.txt");
}