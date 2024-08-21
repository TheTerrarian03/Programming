
use colour::{dark_green, yellow};
use std::error::Error;
use dotenv::dotenv;
use newsapi::{get_articles, Articles};

fn render_articles(articles: &Articles) {
    for i in &articles.articles {
        dark_green!("> {}\n", i.title);
        yellow!("- {}\n\n", i.url);
    }
}

fn main() -> Result<(), Box<dyn Error>> {
    dotenv()?;

    let api_key: String = std::env::var("API_KEY")?;

    let url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=";
    let url = format!("{}{}", url, api_key);

    let articles = get_articles(&url)?;

    render_articles(&articles);

    println!("Press enter to end program...");

    let mut buffer = String::new();

    std::io::stdin()
        .read_line(&mut buffer)
        .expect("Failed to read line");

    Ok(())
}
