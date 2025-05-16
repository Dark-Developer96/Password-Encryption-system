# 🔐 Password Manager in Python

A simple command-line password manager built in Python. It allows you to:

- Encrypt and save website usernames and passwords
- Use a master password for security
- Generate strong random passwords
- Search and delete credentials
- Store data securely in text files

---

## 📁 Files

- `data.txt` — Stores encrypted website credentials.
- `mpass.txt` — Stores encrypted master password.

---

## 🚀 Features

- ✅ **Master Password Authentication**
- ✅ **Caesar Cipher Encryption**
- ✅ **Credential Storage & Retrieval**
- ✅ **Password Generator**
- ✅ **Search & Delete Functionality**
- ✅ **Progress Messages via Decorators**

---

## 🛡️ How It Works

1. On first run, you can set a master password.
2. You can then:
   - Add credentials (website, username, password)
   - Generate random passwords of custom length
   - Search for saved credentials
   - Delete credentials
   - View all stored credentials (requires master password)

Passwords and data are encrypted using a simple character-shift technique.

---

## 📦 Requirements

- Python 3.x
- No external libraries required

---

## ▶️ Running the Program

Run the script using Python:

```bash
python password_manager.py

📌 Author
Built with 💻 by Dark-Developer
