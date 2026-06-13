from news import get_all_news
from email_sender import send_email

def run():
    news = get_all_news()
    send_email(news)

if __name__ == "__main__":
    run()