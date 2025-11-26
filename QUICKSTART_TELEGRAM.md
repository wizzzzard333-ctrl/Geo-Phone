# 🚀 Quick Start - Geo-Phone Telegram Bot

Get your Geo-Phone Telegram bot running in 5 minutes!

## Step 1: Get a Bot Token

1. Open Telegram and search for `@BotFather`
2. Send `/newbot`
3. Choose a name (e.g., "My Geo Phone Bot")
4. Choose a username (e.g., "my_geo_phone_bot")
5. Copy the token you receive (looks like: `123456789:ABCdefGHIjklMNOpqrsTUVwxyz`)

## Step 2: Clone & Setup

```bash
# Clone the repository
git clone https://github.com/wizzzzard333-ctrl/Geo-Phone.git
cd Geo-Phone

# Install dependencies
pip3 install -r requirements_telegram.txt
```

## Step 3: Set Your Token

**Linux/Mac:**
```bash
export TELEGRAM_BOT_TOKEN='your_token_here'
```

**Windows (CMD):**
```cmd
set TELEGRAM_BOT_TOKEN=your_token_here
```

**Windows (PowerShell):**
```powershell
$env:TELEGRAM_BOT_TOKEN='your_token_here'
```

## Step 4: Run the Bot

```bash
python3 telegram_bot.py
```

You should see:
```
🤖 Geo-Phone Telegram Bot started!
📱 Version: 2.0.3.6-TG
⏳ Waiting for messages...
```

## Step 5: Test Your Bot

1. Open Telegram
2. Search for your bot username
3. Send `/start`
4. Try a phone number: `+12025551234`

## 🎉 That's it!

Your bot is now running and ready to track phone numbers!

---

## 🐳 Docker Quick Start (Alternative)

If you prefer Docker:

```bash
# Build the image
docker build -f Dockerfile.telegram -t geo-phone-bot .

# Run the container
docker run -e TELEGRAM_BOT_TOKEN='your_token' geo-phone-bot
```

Or use docker-compose:

```bash
# Create .env file
echo "TELEGRAM_BOT_TOKEN=your_token_here" > .env

# Start the bot
docker-compose up -d
```

---

## 🔧 Troubleshooting

**Bot not responding?**
- Check if the bot is running
- Verify your token is correct
- Make sure you started a chat with the bot

**Dependencies error?**
- Update pip: `pip3 install --upgrade pip`
- Try: `pip3 install -r requirements_telegram.txt --upgrade`

**Token error?**
- Make sure there are no extra spaces in your token
- Verify the token with @BotFather using `/token`

---

## 📚 Next Steps

- Read the full [Telegram Bot README](TELEGRAM_BOT_README.md)
- Deploy to cloud (Heroku, Railway, Render)
- Customize the bot for your needs

---

**Need help?** Open an issue on GitHub!
