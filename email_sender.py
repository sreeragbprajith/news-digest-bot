import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")


def build_html(news_list):
    html = """
    <html>
    <body>
    <h2>📰 Daily News Digest</h2>
    <hr>
    """

    for news in news_list:
        html += f"""
        <h3>{news['title']}</h3>
        <p><b>Source:</b> {news['source']}</p>
        <p><a href="{news['link']}">Read more</a></p>
        <hr>
        """

    html += "</body></html>"
    return html


def send_email(news_list):
    msg = MIMEMultipart()
    msg["Subject"] = "Daily News Digest"
    msg["From"] = EMAIL
    msg["To"] = EMAIL

    html_content = build_html(news_list)
    msg.attach(MIMEText(html_content, "html"))

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(EMAIL, PASSWORD)
    server.send_message(msg)
    server.quit()