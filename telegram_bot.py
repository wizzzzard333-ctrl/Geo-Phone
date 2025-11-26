#!/usr/bin/env python3
"""
Geo-Phone Telegram Bot
A Telegram bot interface for the Geo-Phone OSINT tool
Author: Adapted for Telegram by Bhindi
Original Author: evilfeonix
"""

import os
import sys
import time
import phonenumbers
from phonenumbers import carrier, timezone, geocoder, is_valid_number
from countryinfo import CountryInfo
from opencage.geocoder import OpenCageGeocode
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Configuration
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN', 'YOUR_BOT_TOKEN_HERE')
OPENCAGE_API_KEY = "42c84373c47e490ba410d4132ae64fc4"

# Bot version
VERSION = "2.0.3.6-TG"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send welcome message when /start is issued."""
    welcome_text = f"""
🌍 *Geo-Phone OSINT Bot* v{VERSION}

Welcome! I can help you track and gather information about phone numbers worldwide.

*How to use:*
📱 Send me a phone number with country code
   Example: +12345678900

*Commands:*
/start - Show this message
/help - Get help
/about - About this tool

*Note:* This tool is for educational and OSINT purposes only.
    """
    
    await update.message.reply_text(
        welcome_text,
        parse_mode='Markdown'
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send help message."""
    help_text = """
📖 *How to Use Geo-Phone Bot*

Simply send a phone number with country code:
✅ +12345678900
✅ +442071234567
✅ +919876543210

The bot will provide:
• Phone number validation
• Country information
• Service provider
• Timezone
• Geographic location
• Map coordinates

*Tips:*
• Always include the country code with +
• Make sure the number is valid
• Results may vary based on data availability
    """
    
    await update.message.reply_text(
        help_text,
        parse_mode='Markdown'
    )


async def about_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send about information."""
    about_text = """
ℹ️ *About Geo-Phone*

*Tool Name:* Geo-Phone
*Version:* v2.0.3.6-TG
*Original Author:* evilfeonix
*Telegram Bot:* Adapted by Bhindi
*Website:* www.evilfeonix.com
*GitHub:* github.com/evilfeonix

A free and open source OSINT tool that enables users to track and map phone numbers from around the world.

⭐ Star the repo: github.com/evilfeonix/Geo-Phone
    """
    
    await update.message.reply_text(
        about_text,
        parse_mode='Markdown'
    )


async def process_phone_number(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Process phone number and return information."""
    phone_input = update.message.text.strip()
    
    # Send processing message
    processing_msg = await update.message.reply_text(
        "🔍 Analyzing phone number...\nPlease wait..."
    )
    
    try:
        # Parse phone number
        phoneNumber = phonenumbers.parse(phone_input)
        
        # Validate number
        if not is_valid_number(phoneNumber):
            await processing_msg.edit_text(
                "❌ *Invalid Phone Number*\n\n"
                "Please provide a valid phone number with country code.\n"
                "Example: +12345678900",
                parse_mode='Markdown'
            )
            return
        
        # Get basic information
        inter = phonenumbers.format_number(phoneNumber, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        nation = phonenumbers.format_number(phoneNumber, phonenumbers.PhoneNumberFormat.NATIONAL)
        e164 = phonenumbers.format_number(phoneNumber, phonenumbers.PhoneNumberFormat.E164)
        
        gc = geocoder.description_for_number(phoneNumber, "en")
        c = carrier.name_for_number(phoneNumber, "en")
        tz = timezone.time_zones_for_number(phoneNumber)
        
        local = phoneNumber.national_number
        cncode = phoneNumber.country_code
        
        # Build response
        response = f"📱 *Phone Number Analysis*\n\n"
        response += f"*International:* `{inter}`\n"
        response += f"*National:* `{nation}`\n"
        response += f"*E164:* `{e164}`\n"
        response += f"*Local:* `{local}`\n\n"
        
        response += f"🌍 *Location Information*\n"
        response += f"*Country:* {gc if gc else 'Unknown'}\n"
        response += f"*Country Code:* +{cncode}\n"
        response += f"*Timezone:* {tz[0] if tz else 'Unknown'}\n"
        response += f"*Carrier:* {c if c else 'Unknown'}\n"
        response += f"*Valid:* ✅ Yes\n\n"
        
        # Get country details
        if gc:
            try:
                country = CountryInfo(gc)
                iso = country.iso()["alpha2"]
                response += f"*ISO Code:* {iso}\n"
                
                # Get coordinates
                coder = OpenCageGeocode(OPENCAGE_API_KEY)
                results = coder.geocode(gc)
                
                if results:
                    lat = results[0]['geometry']['lat']
                    lng = results[0]['geometry']['lng']
                    
                    response += f"*Latitude:* `{lat}`\n"
                    response += f"*Longitude:* `{lng}`\n"
                    
                    # Get address
                    addr = coder.reverse_geocode(lat, lng)
                    if addr:
                        address = addr[0]['formatted']
                        response += f"*Address:* {address}\n"
                    
                    # Create map link
                    map_url = f"https://google.com/maps/place/{lat},{lng}/@{lat},{lng},16z"
                    
                    # Create inline keyboard with map button
                    keyboard = [[InlineKeyboardButton("🗺️ View on Map", url=map_url)]]
                    reply_markup = InlineKeyboardMarkup(keyboard)
                    
                    await processing_msg.edit_text(
                        response,
                        parse_mode='Markdown',
                        reply_markup=reply_markup
                    )
                    return
                    
            except Exception as e:
                response += f"\n⚠️ Could not fetch detailed location data"
        
        await processing_msg.edit_text(response, parse_mode='Markdown')
        
    except phonenumbers.NumberParseException:
        await processing_msg.edit_text(
            "❌ *Invalid Phone Number Format*\n\n"
            "Please provide a phone number with country code.\n"
            "Example: +12345678900",
            parse_mode='Markdown'
        )
    except Exception as e:
        await processing_msg.edit_text(
            f"❌ *Error Processing Number*\n\n"
            f"An error occurred: {str(e)}\n\n"
            f"Please try again with a valid phone number.",
            parse_mode='Markdown'
        )


def main():
    """Start the bot."""
    if TELEGRAM_BOT_TOKEN == 'YOUR_BOT_TOKEN_HERE':
        print("❌ Error: Please set TELEGRAM_BOT_TOKEN environment variable")
        print("   export TELEGRAM_BOT_TOKEN='your_bot_token_here'")
        sys.exit(1)
    
    # Create application
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    
    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("about", about_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, process_phone_number))
    
    # Start bot
    print("🤖 Geo-Phone Telegram Bot started!")
    print(f"📱 Version: {VERSION}")
    print("⏳ Waiting for messages...")
    
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Bot stopped by user")
        sys.exit(0)
