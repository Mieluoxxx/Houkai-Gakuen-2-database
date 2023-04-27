use rocket::{get, routes, post, put, delete};

#[get("/")]
async fn hello() -> String{
    "hello world!".to_string()
}

// restful 
#[get("/ex")]
async fn get_exs() -> String{
    "ex list".to_string()
}

#[get("/ex/<_id>")]
async fn get_ex(_id:usize) -> String{
    "ex".to_string()
}

#[post("/ex")]
async fn post_ex() -> String{
    "ex".to_string()
}

#[put("/ex/<_id>")]
async fn put_ex(_id: usize) -> String{
    "ex".to_string()
}

#[delete("/ex/<_id>")]
async fn delete_ex(_id: usize) -> String{
    "ex".to_string()
}

#[rocket::main]
async fn main() -> Result<(), Box<dyn std::error::Error>>{
    rocket::build()
        .mount("/hello", routes![hello])
        .mount("/base", routes![get_ex, post_ex, put_ex, delete_ex, get_exs])
        .mount("/second", routes![get_ex, post_ex, put_ex, delete_ex, get_exs])
        .launch().await?;
    Ok(())
}

