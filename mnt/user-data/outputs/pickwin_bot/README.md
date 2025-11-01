# 🎰 PickWin Casino Bot - Professional Edition

## 📋 Overview

A **complete professional rework** of the PickWin Casino Telegram bot with:
- ✨ Modular, clean code structure
- 🎨 Dynamic images per menu
- 📱 All links open in mini app (WebAppInfo)
- 🎯 Real casino and sports betting categories
- 🔧 Easy to maintain and extend

---

## 📁 Project Structure

```
pickwin_bot/
├── main.py              # Main bot runner (entry point)
├── config.py            # All URLs, images, and constants
├── keyboards.py         # All menu/keyboard layouts
├── handlers.py          # All callback and message handlers
├── utils.py             # Helper functions
├── requirements.txt     # Python dependencies
├── .env.example         # Environment variables template
└── README.md           # This file
```

### 🎯 Why Modular?

**Before:** One 500+ line file = hard to maintain
**After:** 5 organized files = easy to find and modify anything

---

## 🚀 Quick Start (5 Minutes)

### 1️⃣ Install Requirements

```bash
cd pickwin_bot
pip install -r requirements.txt --break-system-packages
```

### 2️⃣ Create .env File

```bash
cp .env.example .env
```

Edit `.env` and add your bot token:
```
BOT_TOKEN=your_actual_telegram_bot_token
```

### 3️⃣ Run the Bot

```bash
python main.py
```

You should see:
```
============================================================
🎰 PickWin Casino Bot is RUNNING!
============================================================
✅ Ready to accept messages
💬 Type /start in Telegram to begin
⏸  Press Ctrl+C to stop the bot
============================================================
```

### 4️⃣ Test It!

Open Telegram, find your bot, type `/start` and enjoy! 🎉

---

## 🎨 Key Features

### 1. **Dynamic Images Per Menu**

Images automatically rotate based on menu:
- **Main Menu:** 2 images
- **Casino:** 2 images  
- **Sports:** 2 images
- **Promotions:** 2 images
- **Account:** 2 images

Each time a user opens a menu, they see a random image from that category!

**How it works:**
```python
# In config.py - easily add more images
IMAGES = {
    'main': ['url1', 'url2'],
    'casino': ['url3', 'url4'],
    # etc...
}

# In handlers.py - automatic random selection
image_url = utils.get_random_image('casino')
```

### 2. **All Links Open in Mini App**

Every clickable link uses `WebAppInfo` to open inside Telegram:

```python
# Example from keyboards.py
InlineKeyboardButton("🎰 Slots", web_app=WebAppInfo(url=CASINO_URLS['slots']))
```

No external browser needed - everything stays in Telegram! 📱

### 3. **Complete Casino & Sports Categories**

**Casino:**
- 🎰 Slots
- 🎲 Live Casino
- 📺 TV Games
- 🃏 Table Games
- 🎮 Virtual Games

**Sports:**
- 🏀 Basketball
- ⚽ Soccer
- 🎾 Tennis
- 🎮 Dota 2
- 🏒 Ice Hockey
- 🎮 Counter Strike
- 🏐 Volleyball
- ⚾ Baseball
- 🥊 Boxing

All with real PickWin URLs!

### 4. **Smart Message Understanding**

Bot recognizes keywords:
```
User types "casino" → Shows casino menu
User types "bonus" → Shows promotions
User types "help" → Shows support options
```

### 5. **Professional Code Organization**

Want to change something?

**Add a new image:**
→ Edit `config.py` → IMAGES dict

**Change button text:**
→ Edit `keyboards.py` → find the keyboard function

**Modify menu text:**
→ Edit `config.py` → TEXT CONTENT section

**Add new feature:**
→ Add handler to `handlers.py` → register in `main.py`

---

## 📚 File Guide

### 🔧 config.py
**What:** All configuration in one place
**Contains:**
- URLs for casino, sports, account
- Banner images by category
- Text content for all menus
- Bonus details
- Support contacts

**Example: Adding a new image**
```python
IMAGES = {
    'main': [
        'url1',
        'url2',
        'url3'  # ← Add here
    ]
}
```

### ⌨️ keyboards.py
**What:** All button layouts
**Contains:**
- Main menu
- Casino menu
- Sports menu
- Promotions menu
- Account menu
- Support menu
- Help menu

**Example: Adding a button**
```python
def get_casino_menu():
    keyboard = [
        [InlineKeyboardButton("🎰 Slots", web_app=WebAppInfo(url=CASINO_URLS['slots']))],
        [InlineKeyboardButton("🎮 New Game Type", web_app=WebAppInfo(url='url'))],  # ← Add here
        # ... rest of buttons
    ]
```

### 🎯 handlers.py
**What:** What happens when users click buttons
**Contains:**
- Command handlers (/start)
- Button callback handlers
- Menu display functions
- Text message handlers

**Example: Adding new callback**
```python
# In button_callback function
elif callback_data == 'my_new_feature':
    await show_my_feature(query, context)

# Then create the function
async def show_my_feature(query, context):
    text = "My feature content"
    await query.edit_message_caption(caption=text, ...)
```

### 🛠️ utils.py
**What:** Helper functions
**Contains:**
- Image selection (random)
- Session tracking
- Text formatting
- Bonus/payment/support info formatting

**Example: Using a utility**
```python
# Get random image for a menu
image = utils.get_random_image('casino')

# Format bonus details
bonus_text = utils.format_welcome_bonus_details()
```

### 🚀 main.py
**What:** Starts everything
**Contains:**
- Bot initialization
- Handler registration
- Error handling
- Logging setup

**Example: Adding a new command**
```python
# In main() function
application.add_handler(CommandHandler("mycommand", handlers.my_command_handler))
```

---

## 🎨 Customization Guide

### Change Bonus Amounts

**File:** `config.py`
```python
WELCOME_BONUS = {
    'amount': '$500',  # ← Change here
    'percentage': '100%',  # ← And here
    'wagering': '35x',
    # ...
}
```

### Add New Sports Category

**1. Add URL in config.py:**
```python
SPORTS_URLS = {
    # ... existing sports
    'rugby': f"{PICKWIN_BASE}/sportbook/?bt-path=/?top=/rugby-15"
}
```

**2. Add button in keyboards.py:**
```python
def get_sports_menu():
    keyboard = [
        # ... existing buttons
        [InlineKeyboardButton("🏉 Rugby", web_app=WebAppInfo(url=SPORTS_URLS['rugby']))]
    ]
```

Done! 🎉

### Change Support Email

**File:** `config.py`
```python
SUPPORT_EMAIL = "newsupport@pickwin.fun"  # ← Change here
```

### Add More Images

**File:** `config.py`
```python
IMAGES = {
    'main': [
        'existing_url',
        'https://new-image-url.com/banner.jpg',  # ← Add here
    ]
}
```

---

## 🎯 Menu Structure

```
┌─ 🏠 MAIN MENU
│
├─ 🎰 CASINO
│  ├─ Slots (Mini App)
│  ├─ Live Casino (Mini App)
│  ├─ TV Games (Mini App)
│  ├─ Table Games (Mini App)
│  └─ Virtual Games (Mini App)
│
├─ ⚽ SPORTS
│  ├─ Basketball (Mini App)
│  ├─ Soccer (Mini App)
│  ├─ Tennis (Mini App)
│  ├─ Dota 2 (Mini App)
│  ├─ Ice Hockey (Mini App)
│  ├─ Counter Strike (Mini App)
│  ├─ Volleyball (Mini App)
│  ├─ Baseball (Mini App)
│  └─ Boxing (Mini App)
│
├─ 🎁 PROMOTIONS
│  ├─ Welcome Bonus ($500)
│  ├─ Reload Bonus
│  ├─ Free Spins
│  ├─ Cashback
│  ├─ VIP Rewards
│  └─ View All (Mini App)
│
├─ 👤 MY ACCOUNT
│  ├─ Cashier (Mini App)
│  ├─ My Bonuses (Mini App)
│  ├─ History (Mini App)
│  ├─ Settings (Mini App)
│  ├─ VIP Status
│  └─ Full Account (Mini App)
│
├─ 💬 SUPPORT
│  ├─ Live Chat (Mini App)
│  ├─ Email Support
│  ├─ FAQ (Mini App)
│  └─ Responsible Gaming
│
└─ ❓ HELP
   ├─ Help Center (Mini App)
   ├─ Payment Methods
   ├─ Bonus Guide
   ├─ KYC Verification
   └─ Withdrawals
```

---

## 🔍 How It Works

### User Flow Example:

1. **User sends `/start`**
   - `main.py` receives command
   - Calls `handlers.start_command()`
   - Gets random 'main' image from `utils`
   - Loads welcome text from `config`
   - Shows main menu from `keyboards`

2. **User clicks "🎰 Casino"**
   - `handlers.button_callback()` triggered
   - Detects `callback_data='casino_menu'`
   - Calls `show_casino_menu()`
   - Gets random 'casino' image
   - Loads casino text from `config`
   - Shows casino menu with WebApp buttons

3. **User clicks "🎰 Slots"**
   - WebAppInfo opens mini app
   - URL: `https://pickwin.fun/casino/spins/`
   - User plays directly in Telegram!

### Image Rotation:

```python
# Every time casino menu opens:
image = utils.get_random_image('casino')
# Returns randomly: image1 OR image2

# Result: Menu looks fresh every time! ✨
```

---

## 💡 Best Practices

### ✅ DO:
- Keep URLs updated in `config.py`
- Add new images to `config.py`
- Use existing utility functions
- Test changes before deploying
- Keep backups of working code

### ❌ DON'T:
- Mix configuration and logic
- Hardcode URLs in handlers
- Duplicate code
- Forget to update both keyboard and handler
- Remove error handling

---

## 🐛 Troubleshooting

### Bot Not Starting?

**Check:**
1. Is BOT_TOKEN set in .env?
2. Are dependencies installed?
3. Is Python 3.8+ installed?

```bash
python --version
pip list | grep telegram
```

### Images Not Loading?

**Check:**
1. Are image URLs accessible?
2. Try opening URL in browser
3. Check console for errors

### Links Not Working?

**Check:**
1. URLs in `config.py`
2. WebAppInfo syntax in `keyboards.py`
3. Test links manually in browser

### Buttons Not Responding?

**Check:**
1. Is callback_data in `handlers.button_callback()`?
2. Is handler registered in `main.py`?
3. Check logs: `tail -f pickwin_bot.log`

---

## 📊 Logging

Bot creates `pickwin_bot.log` with all activities:

```bash
# View logs in real-time
tail -f pickwin_bot.log

# View last 50 lines
tail -50 pickwin_bot.log

# Search for errors
grep ERROR pickwin_bot.log
```

---

## 🚀 Deployment

### Local (Development)

```bash
python main.py
```

### Server (Production)

```bash
# Using screen
screen -S pickwin_bot
python main.py
# Ctrl+A, D to detach

# Using nohup
nohup python main.py > output.log 2>&1 &

# Using systemd (recommended)
# Create /etc/systemd/system/pickwin-bot.service
```

---

## 📈 Future Enhancements

Easy to add:
- ✅ Multi-language support
- ✅ User statistics tracking
- ✅ Admin panel
- ✅ Automated promotions
- ✅ Game recommendations
- ✅ Daily challenges
- ✅ Referral system

All thanks to modular structure! 🎉

---

## 🎯 Summary

### What You Got:

**✅ Clean Code**
- 5 organized files
- Easy to understand
- Professional structure

**✅ Complete Features**
- All casino categories
- All sports categories
- Dynamic images
- Mini app integration

**✅ Easy Maintenance**
- Change URLs: edit config.py
- Change text: edit config.py
- Add buttons: edit keyboards.py
- Add features: edit handlers.py

**✅ Production Ready**
- Error handling
- Logging system
- Session tracking
- User analytics ready

---

## 🎰 Ready to Launch!

Your PickWin Casino bot is now:
- **Professional** ✨
- **Complete** 🎯
- **Maintainable** 🔧
- **Scalable** 📈

**Start the bot and watch it work! 🚀**

```bash
python main.py
```

---

## 📞 Support

For modifications or questions, check:
- 📖 This README (most common solutions)
- 📝 Code comments (detailed explanations)
- 🔍 Logs (pickwin_bot.log)

---

**🎰 Good luck with your casino! 🎰**

Made with 💚 for PickWin Casino
