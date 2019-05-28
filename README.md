# Ticket Monitor

## Goal
- Scrape ticket websites using headless Chrome
- Send myself an SMS if anything notable changes
- Run on AWS Lambda with free tier infrastructure

## Components
1) AWS Lambda with CloudWatch Cron to run once a minute
2) Selenium headless browser to bypass anti-scrapers
3) Python BeautifulSoup to parse rendered HTML
4) AWS DynamoDB datastore to track diffs
5) AWS SNS Publisher to push SMS text messages to subscribers
