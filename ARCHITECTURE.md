# 🏗️ PICKWIN BOT ARCHITECTURE

## 📐 System Design

### High-Level Overview

```
┌─────────────┐
│   Telegram  │
│    User     │
└──────┬──────┘
       │ /start or click button
       ↓
┌─────────────────────────────┐
│       main.py               │
│  (Bot Application Runner)   │
│                             │
│  - Initializes bot          │
│  - Registers handlers       │
│  - Starts polling           │
└──────────┬──────────────────┘
           │
           ↓
┌─────────────────────────────┐
│      handlers.py            │
│  (Business Logic Layer)     │
│                             │
│  - Command handlers         │
│  - Callback handlers        │
│  - Message handlers         │
│  - Menu display functions   │
└──┬────────┬─────────┬───────┘
   │        │         │
   ↓        ↓         ↓
┌──────┐ ┌──────┐ ┌──────┐
│config│ │keybd │ │utils │
└──────┘ └──────┘ └──────┘
```

---

## 📦 Module Breakdown

### 🔧 config.py
**Purpose:** Central configuration store
**Responsibility:** Hold all constants

```python
config.py
├── BOT_TOKEN          # Telegram bot token
├── URLS              # All website URLs
│   ├── CASINO_URLS   # Casino game categories
│   ├── SPORTS_URLS   # Sports betting categories
│   └── OTHER_URLS    # Account, support, etc.
├── IMAGES            # Banner images by menu type
├── TEXT_CONTENT      # All menu text/captions
├── BONUS_DETAILS     # Bonus information
└── RESOURCES         # Support contacts, help resources
```

**Why separate?**
- ✅ Change URLs without touching code
- ✅ Update text without searching files
- ✅ Add images in one place
- ✅ Easy for non-developers to update

---

### ⌨️ keyboards.py
**Purpose:** Define all button layouts
**Responsibility:** Create InlineKeyboardMarkup objects

```python
keyboards.py
├── get_main_menu()           # Main landing menu
├── get_casino_menu()         # Casino categories
├── get_sports_menu()         # Sports categories
├── get_promotions_menu()     # Bonus offers
├── get_account_menu()        # Account management
├── get_support_menu()        # Help & support
├── get_help_menu()           # Information
└── get_*_keyboard()          # Specialized keyboards
```

**Design Pattern:**
```python
def get_casino_menu():
    # Each function returns InlineKeyboardMarkup
    # All URLs from config.py
    # All use WebAppInfo for mini app
    return InlineKeyboardMarkup(keyboard)
```

**Why separate?**
- ✅ See all menus at a glance
- ✅ Easy to add/remove buttons
- ✅ Consistent button structure
- ✅ No logic mixed with UI

---

### 🎯 handlers.py
**Purpose:** Handle user interactions
**Responsibility:** Process commands, callbacks, messages

```python
handlers.py
├── Command Handlers
│   └── start_command()       # Handle /start
│
├── Callback Handlers
│   ├── button_callback()     # Main router
│   └── show_*_menu()         # Display functions
│
├── Message Handlers
│   └── handle_text_message() # Process text input
│
└── Error Handler
    └── error_handler()       # Catch exceptions
```

**Flow Diagram:**
```
User Action
    ↓
handler receives event
    ↓
loads config data
    ↓
gets keyboard layout
    ↓
uses utils for formatting
    ↓
sends response to user
```

**Why separate?**
- ✅ All interaction logic in one place
- ✅ Easy to add new features
- ✅ Clear function names (show_casino_menu)
- ✅ Separation of concerns

---

### 🛠️ utils.py
**Purpose:** Utility and helper functions
**Responsibility:** Reusable operations

```python
utils.py
├── Image Management
│   └── get_random_image()    # Random banner selection
│
├── Session Tracking
│   ├── init_user_session()   # Initialize user data
│   └── track_interaction()   # Log user actions
│
├── Formatting Functions
│   ├── format_welcome_bonus_details()
│   ├── format_vip_program_details()
│   ├── format_crypto_payment_info()
│   └── format_*()            # All content formatters
│
└── Error Handling
    ├── log_error()
    └── is_*_error()          # Error type checkers
```

**Why separate?**
- ✅ Reusable functions
- ✅ No code duplication
- ✅ Easy to test
- ✅ Clean handlers

---

### 🚀 main.py
**Purpose:** Application entry point
**Responsibility:** Initialize and run bot

```python
main.py
├── Logging setup
├── Application builder
├── Handler registration
│   ├── CommandHandler
│   ├── CallbackQueryHandler
│   └── MessageHandler
└── Bot.run_polling()
```

**Why separate?**
- ✅ Clear startup process
- ✅ Easy to modify handlers
- ✅ Professional structure
- ✅ Production-ready

---

## 🔄 Request Flow

### Example: User Clicks "🎰 Casino"

```
1. User clicks button
   ├─ callback_data='casino_menu'
   └─ Telegram sends update to bot

2. main.py receives update
   └─ Routes to CallbackQueryHandler

3. handlers.button_callback() triggered
   ├─ Reads callback_data
   ├─ Matches 'casino_menu'
   └─ Calls show_casino_menu(query, context)

4. show_casino_menu()
   ├─ Gets random image: utils.get_random_image('casino')
   ├─ Gets text: config.CASINO_TEXT
   ├─ Gets keyboard: keyboards.get_casino_menu()
   └─ Sends photo with caption and keyboard

5. User sees casino menu
   └─ With random casino banner image
```

---

## 🎨 Image System

### How Dynamic Images Work

```python
# config.py
IMAGES = {
    'casino': ['image1.jpg', 'image2.jpg']
}

# utils.py
def get_random_image(menu_type):
    return random.choice(IMAGES[menu_type])

# handlers.py
image_url = utils.get_random_image('casino')
```

**Result:**
- User opens casino → sees image1.jpg
- User closes and reopens → sees image2.jpg (50% chance)
- Feels fresh and dynamic! ✨

---

## 🔌 WebApp Integration

### How Mini App Links Work

```python
# config.py
CASINO_URLS = {
    'slots': 'https://pickwin.fun/casino/spins/'
}

# keyboards.py
InlineKeyboardButton(
    "🎰 Slots",
    web_app=WebAppInfo(url=CASINO_URLS['slots'])
)
```

**User Experience:**
```
User clicks "🎰 Slots"
    ↓
Telegram opens mini app
    ↓
Shows pickwin.fun/casino/spins/
    ↓
Inside Telegram (no external browser)
    ↓
User plays games in Telegram! 🎮
```

---

## 🎯 Design Principles

### 1. Separation of Concerns
- **Config:** Data only
- **Keyboards:** UI only
- **Handlers:** Logic only
- **Utils:** Helpers only
- **Main:** Startup only

### 2. Single Responsibility
Each function does ONE thing:
- `get_casino_menu()` → Returns casino keyboard
- `show_casino_menu()` → Displays casino menu
- `format_crypto_info()` → Formats crypto text

### 3. DRY (Don't Repeat Yourself)
```python
# ❌ BAD: Copy-paste in every handler
text = "🎰 Casino Games..."

# ✅ GOOD: Define once, use everywhere
text = config.CASINO_TEXT
```

### 4. Easy to Extend
Adding new feature is straightforward:

```python
# 1. Add URL to config.py
NEW_FEATURE_URL = "https://..."

# 2. Add button to keyboards.py
def get_new_menu():
    return InlineKeyboardMarkup([...])

# 3. Add handler to handlers.py
async def show_new_menu(query, context):
    # ... implementation

# 4. Register in main.py
# (if needed for new command)
```

---

## 📊 Data Flow

### Configuration Flow
```
config.py (defines)
    ↓
keyboards.py (uses for buttons)
    ↓
handlers.py (uses for text)
    ↓
User sees result
```

### User Interaction Flow
```
User action (click/type)
    ↓
Telegram API
    ↓
main.py (routes)
    ↓
handlers.py (processes)
    ↓
keyboards.py (creates UI)
    ↓
config.py (provides data)
    ↓
utils.py (formats)
    ↓
Response sent to user
```

---

## 🏛️ Architecture Benefits

### For Developers
✅ **Easy to understand:** Clear file purposes
✅ **Easy to modify:** Know exactly where to look
✅ **Easy to test:** Isolated functions
✅ **Easy to extend:** Add without breaking

### For Maintenance
✅ **Change URLs:** Edit config.py only
✅ **Update text:** Edit config.py only
✅ **Add buttons:** Edit keyboards.py only
✅ **Add features:** Add to handlers.py

### For Scaling
✅ **Add new menus:** Follow pattern
✅ **Add new categories:** Update config & keyboards
✅ **Add analytics:** Extend utils.py
✅ **Add multi-language:** Add language files

---

## 🔒 Error Handling

### Layered Approach

```
User Action
    ↓
Try-Catch in handlers
    ↓
Specific error checks (BadRequest)
    ↓
Utils error logging
    ↓
Main error handler (global)
    ↓
Log to pickwin_bot.log
```

### Example
```python
try:
    await show_menu(query)
except BadRequest as e:
    if utils.is_message_too_old_error(e):
        logger.warning("Old message, ignoring")
    else:
        utils.log_error(e, update)
```

---

## 📈 Performance Considerations

### Image Loading
- Images served from CDN (fungamess.games)
- Compressed (avif format)
- Loaded on-demand
- Cached by Telegram

### Button Responses
- Instant callback_query.answer()
- Edit existing messages (faster than new)
- Fallback to new message if edit fails

### Error Recovery
- Graceful fallbacks
- Continue on non-critical errors
- Log for debugging
- Never crash

---

## 🎓 Learning Path

### Understanding the Bot (15 minutes)

**1. Start with config.py (5 min)**
- See all URLs
- See all text
- See all images
- Understand data structure

**2. Look at keyboards.py (3 min)**
- See main menu
- See casino menu
- Notice WebAppInfo usage
- Understand button structure

**3. Read handlers.py (5 min)**
- Start with button_callback()
- See how it routes
- Look at show_casino_menu()
- Understand flow

**4. Glance at main.py (2 min)**
- See initialization
- See handler registration
- Understand startup

---

## 🎯 Summary

### Architecture Pattern: MVC-Style

```
Model (Data)       → config.py
View (UI)          → keyboards.py
Controller (Logic) → handlers.py
Utilities          → utils.py
App Runner         → main.py
```

### Key Advantages
1. ✅ **Modular:** Each file has one purpose
2. ✅ **Maintainable:** Easy to find and fix
3. ✅ **Scalable:** Easy to extend
4. ✅ **Professional:** Industry-standard structure

### Perfect For
- ✅ Small teams
- ✅ Solo developers
- ✅ Growing bots
- ✅ Production use

---

**🏗️ Professional architecture for professional bots! 🏗️**
