use serde::Deserialize;

#[derive(thiserror::Error, Debug)]
pub enum NewsApiError {
    #[error("Faield fetching articles")]
    RequestFailed(ureq::Error),

    #[error("Failed converting response to string")]
    FailedResponseToString(std::io::Error),

    #[error("Article Parsing failed")]
    ArticleParsingFailed(serde_json::Error)
}

#[derive(Deserialize, Debug)]
pub struct Articles {
    pub articles: Vec<Article>
}

#[derive(Deserialize, Debug)]
pub struct Article {
    pub title: String,
    pub url: String
}

pub fn get_articles(url: &str) -> Result<Articles, NewsApiError> {
    // get response and return error if failed to get responsed
    let response = ureq::get(url).call().map_err(|e| NewsApiError::RequestFailed(e))
    // attempt to convert to a string
    ?.into_string().map_err(|e| NewsApiError::FailedResponseToString(e))?;

    // attempt to parse string into json
    let articles: Articles = serde_json::from_str(&response).map_err(|e| NewsApiError::ArticleParsingFailed(e))?;  // pass in reference to response variable

    Ok(articles)
}
