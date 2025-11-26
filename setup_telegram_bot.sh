#!/bin/bash

# Geo-Phone Telegram Bot Setup Script
# This script automates the setup process

echo "🤖 Geo-Phone Telegram Bot Setup"
echo "================================"
echo ""

# Check Python version
echo "📋 Checking Python version..."
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2 | cut -d'.' -f1,2)
echo "✅ Python $PYTHON_VERSION found"
echo ""

# Install dependencies
echo "📦 Installing dependencies..."
pip3 install -r requirements_telegram.txt

if [ $? -ne 0 ]; then
    echo "❌ Failed to install dependencies"
    exit 1
fi

echo "✅ Dependencies installed successfully"
echo ""

# Check for bot token
echo "🔑 Checking for Telegram Bot Token..."
if [ -z "$TELEGRAM_BOT_TOKEN" ]; then
    echo "⚠️  TELEGRAM_BOT_TOKEN environment variable not set"
    echo ""
    echo "To get a bot token:"
    echo "1. Open Telegram and search for @BotFather"
    echo "2. Send /newbot and follow the instructions"
    echo "3. Copy the token you receive"
    echo ""
    read -p "Enter your Telegram Bot Token: " BOT_TOKEN
    
    if [ -z "$BOT_TOKEN" ]; then
        echo "❌ No token provided. Exiting."
        exit 1
    fi
    
    export TELEGRAM_BOT_TOKEN="$BOT_TOKEN"
    
    # Save to .env file
    echo "TELEGRAM_BOT_TOKEN=$BOT_TOKEN" > .env
    echo "✅ Token saved to .env file"
    echo ""
    echo "💡 To make this permanent, add this to your ~/.bashrc or ~/.zshrc:"
    echo "   export TELEGRAM_BOT_TOKEN='$BOT_TOKEN'"
else
    echo "✅ Bot token found"
fi

echo ""
echo "🎉 Setup complete!"
echo ""
echo "To start the bot, run:"
echo "   python3 telegram_bot.py"
echo ""
echo "Or if you saved the token to .env:"
echo "   source .env && python3 telegram_bot.py"
echo ""
