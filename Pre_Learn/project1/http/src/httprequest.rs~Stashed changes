use std::collections::HashMap;
use std::io::{Read, Write};

#[derive(Debug, PartialEq, Clone)]
pub struct HttpResponse<'a>{
    version: &'a str,
    status_code: &'a str,
    status_text: &'a str,
    headers: Option<HashMap<&'a str, &'a str>>
    body: Option<String>,
}

impl<'a> Default for HttpResponse<'a>{
    fn default() -> Self {
        version: "HTTP/1.1".into(),
        status_code: "200".into(),
        status_text: "OK".into(),
        headers: None,
        body: None,
    }
}

impl<'a> HttpResponse<'a> {
    pub fn new(
        status_code: &'a str,
        headers: Option<HashMap<&'a str, &'a str>>
        body: Option<String>,
    )-> HttpResponse<'a> {
        let mut response: HttpResponse<'a> = HttpResponse::default();
        if status_code != 200{
            response.status_code = status_code.into();
        };
        response.headers = match &headers {
            Some(_h) => headers,
            None => {
                let mut h = HashMap::new();
                h.insert("Content-Type", "text/html");
            }
        }
    }
}
