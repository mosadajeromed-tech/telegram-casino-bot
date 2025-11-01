# 🎰 PickWin Casino Bot - WITH BONUS FLOW

## ✅ What's Added

Your bot now has the **COMPLETE BONUS FLOW** back!

## 📱 User Experience

### Main Menu:
```
🎁 Claim Bonus          ← NEW!
🎰 Casino  |  ⚽ Sports
🔐 Login   |  ✨ Register
```

### Bonus Flow:
1. User clicks **"🎁 Claim Bonus"**
2. Bot asks: **"What type of player are you?"**
   - 🎯 Beginner Player (Low Deposit)
   - 💎 High Roller (Large Deposit)
3. Bot asks: **"Do you have a PickWin account?"**
   - ✅ Yes → Ask for username
   - ❌ No → Show registration guide
4. User provides username
5. Bot saves info and shows **"Pending Verification"** status
6. When user returns, bot shows their pending request

---

## 🎯 Complete Features

### Main Features:
- ✅ Claim Bonus flow
- ✅ Player type selection (Beginner/High Roller)
- ✅ Account check
- ✅ Username collection
- ✅ Pending verification tracking
- ✅ Status check
- ✅ Casino games (2 options)
- ✅ Sports betting (9 sports)
- ✅ Login/Register links
- ✅ 10 random rotating images

---

## 📊 How It Works

### User Journey:

**New User:**
```
/start
  → Main Menu
    → Click "Claim Bonus"
      → Select Player Type (Beginner/High Roller)
        → "No, I need account"
          → Registration guide
            → Return → Enter username
              → Pending verification
```

**Existing User:**
```
/start
  → Main Menu
    → Click "Claim Bonus"
      → Select Player Type
        → "Yes, I have account"
          → Enter username
            → Pending verification
```

**Returning User (Pending):**
```
/start
  → Shows pending status
  → Can check status or start new request
```

---

## 💾 Data Stored Per User

```python
context.user_data = {
    'player_type': '🎯 Beginner' or '💎 High Roller',
    'submitted_username': 'user123',
    'submitted_id': 'user123',
    'waiting_for': 'pending_verification'
}
```

---

## 🔔 Admin Notifications

When user submits username, bot logs:
```
🔔 NEW BONUS REQUEST
👤 User: John Doe (@johndoe)
🆔 Telegram ID: 123456789
🎯 Player Type: 🎯 Beginner
📝 Account: user123
⏳ Awaiting verification
```

*(Check your bot logs to see these)*

---

## 📁 Files

**4 Core Files:**
1. `main.py` - Runs the bot
2. `config.py` - URLs & images
3. `keyboards.py` - All buttons (with bonus keyboards)
4. `handlers.py` - Logic (with bonus flow)

**Plus:**
- `requirements.txt` - Dependencies
- `runtime.txt` - Python version
- `.env.example` - Token template

---

## 🚀 Deploy

### To Render:
1. Replace these 4 files in your repo:
   - main.py
   - config.py
   - keyboards.py
   - handlers.py
2. Push/deploy
3. Done!

### Test Locally:
```bash
pip install -r requirements.txt
python main.py
```

---

## 🎮 Test the Flow

1. Start bot: `/start`
2. Click: **"🎁 Claim Bonus"**
3. Select: **"🎯 Beginner Player"**
4. Click: **"✅ Yes, I have account"**
5. Type: `test123` (fake username)
6. See: Pending verification message
7. Restart: `/start`
8. See: Pending status shown automatically!

---

## ⚙️ Customize

### Change Bonus Text:
Edit `handlers.py` - search for `"WELCOME TO BONUS PROGRAM"`

### Add Admin Chat:
In `handlers.py` line 220, add:
```python
ADMIN_CHAT_ID = 123456789  # Your Telegram ID
await context.bot.send_message(
    chat_id=ADMIN_CHAT_ID,
    text=admin_notification,
    parse_mode='Markdown'
)
```

---

## ✨ What's Different from Before

**Kept:**
- ✅ Casino & Sports menus
- ✅ Login/Register buttons
- ✅ Random images
- ✅ Mini app links

**Added:**
- ✅ Claim Bonus button
- ✅ Player type selection
- ✅ Account verification flow
- ✅ Username collection
- ✅ Pending status tracking
- ✅ Status check menu

---

## 🎯 Summary

Your bot now has:
- **Simple navigation** (Casino, Sports, Login, Register)
- **Bonus collection flow** (Beginner/High Roller → Username → Pending)
- **Status tracking** (Shows pending requests on /start)
- **Random images** (10 images rotate)
- **Mini app links** (All open in Telegram)

**Perfect! 🚀**
