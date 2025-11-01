# 🚀 PICKWIN BOT - ULTRA QUICK START

## ⚡ 3-Minute Setup

### 1. Install (30 seconds)
```bash
cd pickwin_bot
pip install -r requirements.txt --break-system-packages
```

### 2. Configure (30 seconds)
```bash
cp .env.example .env
nano .env  # or use any text editor
```

Add your bot token:
```
BOT_TOKEN=123456789:ABCdefGHIjklMNOpqrsTUVwxyz
```

### 3. Run (5 seconds)
```bash
python main.py
```

### 4. Test (5 seconds)
Open Telegram → Find your bot → Type `/start` → Done! ✅

---

## 🎯 That's It!

Your bot is now running with:
- ✅ All casino games categories
- ✅ All sports betting categories
- ✅ Dynamic images
- ✅ Mini app integration
- ✅ Professional menus

---

## 📝 Need to Change Something?

### Change Images
→ Edit `config.py` → `IMAGES` dict

### Change Text
→ Edit `config.py` → `TEXT CONTENT` section

### Change URLs
→ Edit `config.py` → URLs sections

### Add Buttons
→ Edit `keyboards.py` → find relevant menu function

---

## 🎨 File Overview

```
pickwin_bot/
├── main.py        ← Start here (python main.py)
├── config.py      ← All URLs, images, text
├── keyboards.py   ← All button layouts
├── handlers.py    ← What happens when clicked
└── utils.py       ← Helper functions
```

---

## 🔥 Key Features

### 1. Dynamic Images
Different image each time user opens a menu!

### 2. Mini App
All links open inside Telegram (no browser)

### 3. Modular Code
Easy to find and change anything

### 4. Complete Categories
- Casino: Slots, Live, TV, Table, Virtual
- Sports: Basketball, Soccer, Tennis, Esports, etc.

---

## ❓ Common Questions

### "How do I add more images?"

```python
# In config.py
IMAGES = {
    'main': [
        'existing_url',
        'https://new-image-url.com/banner.jpg'  # ← Add here
    ]
}
```

### "How do I change bonus amount?"

```python
# In config.py
WELCOME_BONUS = {
    'amount': '$500',  # ← Change here
}
```

### "How do I add a new sport?"

**1. config.py:**
```python
SPORTS_URLS = {
    'rugby': f"{PICKWIN_BASE}/sportbook/?bt-path=/?top=/rugby-15"
}
```

**2. keyboards.py:**
```python
InlineKeyboardButton("🏉 Rugby", web_app=WebAppInfo(url=SPORTS_URLS['rugby']))
```

### "Bot not starting?"

Check:
```bash
# 1. Python version (need 3.8+)
python --version

# 2. Dependencies installed?
pip list | grep telegram

# 3. Token in .env?
cat .env
```

---

## 🎯 What's Different?

### OLD BOT:
❌ One big file (500+ lines)
❌ Hard to modify
❌ Generic images
❌ Limited categories

### NEW BOT:
✅ 5 organized files
✅ Easy to modify
✅ Dynamic images per menu
✅ Complete categories
✅ All links in mini app

---

## 📊 Structure at a Glance

```
User clicks button
    ↓
keyboards.py (defines button)
    ↓
handlers.py (handles click)
    ↓
config.py (gets content)
    ↓
utils.py (formats data)
    ↓
Shows result to user
```

---

## 🎰 Menu Overview

```
Main → Casino → Slots, Live, TV, Table, Virtual
    → Sports → Basketball, Soccer, Tennis, etc.
    → Promotions → Welcome, Reload, Spins, etc.
    → Account → Cashier, Bonuses, History, VIP
    → Support → Live Chat, Email, FAQ
    → Help → Payments, Bonuses, KYC, Withdrawals
```

All organized and easy to navigate!

---

## ✨ Pro Tips

### Development
```bash
# Run bot
python main.py

# View logs
tail -f pickwin_bot.log

# Stop bot
Ctrl+C
```

### Production
```bash
# Run in background
nohup python main.py > output.log 2>&1 &

# Check if running
ps aux | grep main.py

# Stop
kill [PID]
```

---

## 🎉 You're Ready!

Your bot has:
- ✅ Professional structure
- ✅ Complete features
- ✅ Easy maintenance
- ✅ Production ready

**Start it and test:**
```bash
python main.py
```

Then open Telegram and type `/start`

---

## 📚 Need More Info?

Read the full `README.md` for:
- Detailed explanations
- Customization guides
- Troubleshooting
- Best practices
- Deployment options

---

**🎰 Good luck! 🎰**
