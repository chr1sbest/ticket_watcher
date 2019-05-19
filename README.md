# Ticket Monitor

## Goal
- Scrape ticket websites and monitor for updates
- Send myself an SMS if anything notable changes
- Run on AWS Lambda with free tier infrastructure

## Components
1) AWS Lambda with CloudWatch Cron to run once a minute
2) Python BeautifulSoup HTML Parsers to look for notable stuff
3) AWS DynamoDB datastore to track diffs
4) AWS SNS Publisher to push SMS text messages to subscribers
