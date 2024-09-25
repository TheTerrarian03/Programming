
use colour::{dark_green, yellow};
use std::error::Error;
use dotenv::dotenv;
use newsapi::*;

fn render_articles(articles: &Vec<Article>) {
    for i in articles {
        dark_green!("> {}\n", i.title());
        yellow!("- {}\n\n", i.url());
    }
}

fn main() -> Result<(), Box<dyn Error>> {
    dotenv()?;

    let api_key: String = std::env::var("API_KEY")?;

    let mut newsapi = NewsAPI::new(&api_key);
    newsapi.endpoint(Endpoint::TopHeadlines).country(Country::Us);

    let newsapi_response = newsapi.fetch()?;

    render_articles(newsapi_response.articles());

    Ok(())
}
