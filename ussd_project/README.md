# USSD News Subscription Service

This Django project implements a USSD-based news subscription service using Africa's Talking API.

## USSD Code


## Features

- User can subscribe to different news categories:
  - Sports
  - Political
  - Local
  - International
- Multiple subscription plans available:
  - Daily
  - Weekly
  - Monthly
- Options for auto-renewal or one-off purchases

## Prerequisites

- Python 3.8+
- Django 5.1+
- Redis (optional, for session management)

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/ussd-news-subscription.git
   cd ussd-news-subscription
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Apply migrations:
   ```
   python manage.py migrate
   ```

4. Run the development server:
   ```
   python manage.py runserver
   ```

## Africa's Talking Configuration

1. Log in to your Africa's Talking account.
2. Navigate to the USSD section.
3. Set up a new USSD channel with the code.
4. Set the callback URL to your application's endpoint:
   ```
   https://your-domain.com/ussd/
   ```
   Note: For local development, you may need to use a tool like ngrok to expose your local server to the internet.

5. Ensure your Africa's Talking API key is properly configured in your Django settings.

## Usage

Once set up, users can dial your ussd code on their phones to access the USSD menu and subscribe to news services.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.