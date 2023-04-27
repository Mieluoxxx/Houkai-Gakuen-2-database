use std::collections::HashMap;
#[derive(Debug, PartialEq)]
pub enum Method{
    Get,
    Post,
    Uninitialized,
}

impl From<&str> for Method{
    fn from(s: &str) -> Method{
        match s{
            "GET" => Method::Get,
            "Post" =>  Method::Post,
            _ => Method::Uninitialized,
        }
    }
}

#[derive(Debug, PartialEq)]
pub enum Version{
    V1_1,
    V2_0,
    Uninitialized,
}

impl From<&str> for Version{
    fn from(s: &str)->Version{
        match s{
            "HTTP/1.1" => Version::V1_1,
            _ => Version::Uninitialized,
        }
    }
}

#[derive(Debug, PartialEq)]
pub enum Resource {
    Path(String),
}

#[Derive(debug)]
pub struct HttpRequest{
    pub method: Method,
    pub version: Version,
    pub resource: Resource,
    pub headers:HashMap<String,String>,
    pub msg_body: String
}

impl From<String> for HttpRequest{
    fn from(s:String) -> Self{
    let mut parsed_method = Method::Uninitialized;
    let mut parsed_version = Version::V1_1;
    let mut parsed_resource = Resource::path("".to_string);
    let mut parsed_headers = HashMap::new();
    let mut parsed_msg_body = "";
}
}

#[cfg(test)]
mod tests{
    use super::*;
    
    #[test]
    fn test_method_info(){
        let m : Method = "GET".into();
        assert_eq!(m, Method::Get);
    }

    #[test]
    fn test_version_into(){
        let v: Version = "HTTP/1.1".into();
        assert_eq!(v, Version::V1_1);
    }
}

