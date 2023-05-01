use std::collections::HashMap;
use std::io::{Result, Write};

#[derive(Debug, PartialEq)]
pub struct HttpResponse<'a>{
    version: &'a str,
    status_code: &'a str,
    status_text: &'a str,
    headers: Option<HashMap<&'a str, &'a str>>,
    body: Option<String>,
}

impl<'a> Default for HttpResponse<'a>{
    fn default() -> Self{
        Self{
            version: "HTTP/1.1".into(),
            status_code: "200".into(),
            status_text: "OK".into(),
            headers: None,
            body: None,
        }
    }
}

impl<'a> HttpResponse<'a>{
    pub fn new(
        status_code: &'a str,
        headers: Option<HashMap<&'a str, &'a str>>
    ) -> HttpResponse<'a>{
        let mut response = HttpResponse::default();
        if status_code != "200"{
            
        }
    }
}