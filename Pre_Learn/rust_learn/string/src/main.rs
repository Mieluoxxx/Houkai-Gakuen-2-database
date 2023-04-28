fn main(){
    let mut s = String::from("foo");
    let s1 = String::from("bar");
    s.push_str(&s1);

    println!("{}", s);

    let s3 = String::from("Hello, ");
    let s4 = String::from("World!");

    let s5 = s3 + &s4;
    println!("{}", s5);

    let s6 = String::from("tic");
    let s7 = String::from("tac");
    let s8 = String::from("toe");

    // let s9 = s6 + "-" + &s2 + "-" + &s3;
    // println!("{}", s3);

    let s10 = format!("{}-{}-{}",s6,s7,s8); // format! 不获取所有权
    println!("{}", s10);

    let l1 = String::from("abcdefghijklmn");
    let l = &l1[0..3];
    println!("{}", l);
}
