# 🚀 START HERE - SIMPLE SETUP

## ✅ What Changed

Your bot is now **SUPER SIMPLE**:

### Main Menu (4 buttons):
- 🎰 Casino
- ⚽ Sports  
- 🔐 Login → `https://pickwin.fun/promotions/?modal=login`
- ✨ Register → `https://pickwin.fun/promotions/?modal=registration`

### Casino Menu (2 buttons):
- 🎰 Casino → `https://pickwin.fun/casino/`
- 🎲 Live Casino → `https://pickwin.fun/casino/live/`

### Sports Menu (9 buttons):
- All 9 sports you specified

### Images:
- 10 images rotate randomly on every menu

---

## 📦 Files You Need

**For Render (7 files):**

1. ✅ [main.py](computer:///mnt/user-data/outputs/main.py) - Runs the bot
2. ✅ [config.py](computer:///mnt/user-data/outputs/config.py) - All URLs & images
3. ✅ [keyboards.py](computer:///mnt/user-data/outputs/keyboards.py) - All buttons
4. ✅ [handlers.py](computer:///mnt/user-data/outputs/handlers.py) - Button actions
5. ✅ [requirements.txt](computer:///mnt/user-data/outputs/requirements.txt) - Dependencies
6. ✅ [runtime.txt](computer:///mnt/user-data/outputs/runtime.txt) - Python 3.12 (fixes error)
7. ✅ [.env.example](computer:///mnt/user-data/outputs/.env.example) - Token example

---

## 🎯 Deploy to Render

### Step 1: Upload Files
Upload all 7 files to your Render project

### Step 2: Set Environment Variable
In Render dashboard:
- Go to Environment
- Add: `BOT_TOKEN` = your bot token

### Step 3: Deploy
Click "Manual Deploy" or push to git

---

## 🖥️ Test Locally

```bash
# 1. Install
pip install -r requirements.txt

# 2. Create .env
echo "BOT_TOKEN=your_token" > .env

# 3. Run
python main.py
```

---

## ✨ What Was Removed

**Removed (as requested):**
- ❌ Popular Games
- ❌ New Releases  
- ❌ Providers
- ❌ Deposit button
- ❌ VIP Club
- ❌ Promotions menu
- ❌ Support 24/7
- ❌ Help menu
- ❌ Play Responsibly

**Kept:**
- ✅ Casino (2 options)
- ✅ Sports (9 options)
- ✅ Login
- ✅ Register

---

## 🎨 Features

✅ **10 Random Images** - Different image each time
✅ **All Mini App Links** - Opens inside Telegram
✅ **Correct URLs** - Login/Register use modal links
✅ **Simple Structure** - Only 4 code files
✅ **Easy to Edit** - Everything in config.py

---

## 🔧 Quick Edits

### Change Login URL:
`config.py` line 18

### Change Register URL:
`config.py` line 19

### Add More Images:
`config.py` line 50-61 (just add to list)

### Change Button Text:
`keyboards.py` - edit button labels

---

## ✅ Summary

**Old Bot:** Complicated, many menus, hard to manage
**New Bot:** Simple, clean, easy to understand

**Files:** 
- 4 code files
- 1 requirements.txt
- 1 runtime.txt (fixes Python error)
- 1 .env.example

**Total:** 7 simple files. That's it!

---

🎰 **Your bot is ready!** 🎰
