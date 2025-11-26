# 🤖 Geo-Phone Telegram Bot

A Telegram bot interface for the Geo-Phone OSINT tool that allows you to track and gather information about phone numbers worldwide directly through Telegram.

## ✨ Features

- 📱 Phone number validation and analysis
- 🌍 Country and location information
- 📡 Service provider identification
- 🕐 Timezone detection
- 🗺️ Geographic coordinates and mapping
- 💬 Easy-to-use Telegram interface
- 🔒 Privacy-focused (no data storage)

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- A Telegram Bot Token (get it from [@BotFather](https://t.me/BotFather))

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/wizzzzard333-ctrl/Geo-Phone.git
cd Geo-Phone
```

2. **Install dependencies:**
```bash
pip install -r requirements_telegram.txt
```

3. **Set up your bot token:**

**Linux/Mac:**
```bash
export TELEGRAM_BOT_TOKEN='your_bot_token_here'
```

**Windows (CMD):**
```cmd
set TELEGRAM_BOT_TOKEN=your_bot_token_here
```

**Windows (PowerShell):**
```powershell
$env:TELEGRAM_BOT_TOKEN='your_bot_token_here'
```

4. **Run the bot:**
```bash
python3 telegram_bot.py
```

## 📖 How to Use

1. Start a chat with your bot on Telegram
2. Send `/start` to see the welcome message
3. Send any phone number with country code (e.g., `+12345678900`)
4. Get detailed information about the phone number
5. Click "View on Map" to see the location on Google Maps

### Commands

- `/start` - Show welcome message
- `/help` - Get usage instructions
- `/about` - About the tool and author

### Example Usage

```
You: +12025551234
Bot: 📱 Phone Number Analysis
     International: +1 202-555-1234
     Country: United States
     Carrier: Verizon
     [View on Map button]
```

## 🔧 Configuration

### Environment Variables

- `TELEGRAM_BOT_TOKEN` - Your Telegram bot token (required)

### API Keys

The bot uses OpenCage Geocoding API for location data. The default API key is included but has rate limits. For production use, get your own free API key from [OpenCage](https://opencagedata.com/).

To use your own API key, edit `telegram_bot.py`:
```python
OPENCAGE_API_KEY = "your_api_key_here"
```

## 🐳 Docker Deployment (Optional)

Create a `Dockerfile`:
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements_telegram.txt .
RUN pip install --no-cache-dir -r requirements_telegram.txt

COPY telegram_bot.py .

CMD ["python", "telegram_bot.py"]
```

Build and run:
```bash
docker build -t geo-phone-bot .
docker run -e TELEGRAM_BOT_TOKEN='your_token' geo-phone-bot
```

## 🌐 Deploy to Cloud

### Heroku

1. Create a `Procfile`:
```
worker: python telegram_bot.py
```

2. Deploy:
```bash
heroku create your-geo-phone-bot
heroku config:set TELEGRAM_BOT_TOKEN='your_token'
git push heroku main
heroku ps:scale worker=1
```

### Railway

1. Connect your GitHub repo to Railway
2. Add environment variable: `TELEGRAM_BOT_TOKEN`
3. Deploy automatically

### Render

1. Create a new Web Service
2. Connect your GitHub repo
3. Add environment variable: `TELEGRAM_BOT_TOKEN`
4. Deploy

## 🔒 Privacy & Security

- No phone numbers are stored or logged
- All processing happens in real-time
- No user data is collected
- Open source and transparent

## ⚠️ Disclaimer

This tool is for educational and OSINT (Open Source Intelligence) purposes only. Always respect privacy laws and regulations in your jurisdiction. Do not use this tool for illegal activities.

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests

## 📝 License

This project maintains the same license as the original Geo-Phone tool.

## 👨‍💻 Credits

- **Original Tool:** [evilfeonix](https://github.com/evilfeonix)
- **Telegram Bot Adaptation:** Bhindi Team
- **Repository:** [Geo-Phone](https://github.com/evilfeonix/Geo-Phone)

## 📞 Support

For issues or questions:
- Open an issue on GitHub
- Contact: evilfeonix@gmail.com
- Original repo: https://github.com/evilfeonix/Geo-Phone

## 🌟 Show Your Support

If you find this useful:
- ⭐ Star the repository
- 🍴 Fork and contribute
- 📢 Share with others

---

**Made with ❤️ for the OSINT community**
