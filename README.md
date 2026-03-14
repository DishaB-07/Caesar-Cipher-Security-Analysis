# 🔐 Caesar Cipher Security Analysis

A Python-based mini cybersecurity project that demonstrates how the **Caesar Cipher** works — and more importantly, how easily it can be broken. This project covers encryption, decryption, brute force attacks, and frequency analysis to highlight the weaknesses of classical cryptography.

---

## 📌 Features

- 🔒 **Caesar Cipher Encryption & Decryption** — shift-based ASCII character manipulation
- 💥 **Brute Force Attack** — tries all 25 possible shift keys to crack the cipher
- 📊 **Frequency Analysis Attack** — exploits letter frequency patterns in English to guess the key without knowing it

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python 3 | Core language |
| ASCII manipulation | Encryption logic |
| Statistical analysis | Frequency analysis attack |

---

## 🚀 How to Run

### 1. Clone the repository
```bash
git clone https://github.com/DishaB-07/Caesar-Cipher-Security-Analysis.git
cd Caesar-Cipher-Security-Analysis
```

### 2. Run the script
```bash
python caesar_security_analysis.py
```

### 3. Choose an option from the menu
```
CAESAR CIPHER SECURITY ANALYSIS
1. Encrypt & Decrypt
2. Brute Force Attack
3. Frequency Analysis Attack
```

---

## 🧠 How It Works

### Encryption
Each letter is shifted forward in the alphabet by a fixed number (the key).
```
A → D (shift = 3)
HELLO → KHOOR
```

### Brute Force Attack
Since there are only 25 possible keys, the program tries all of them and prints every decryption. A human (or a computer) can instantly spot the readable one.

### Frequency Analysis Attack
In English, the letter **E** appears most frequently. The program counts letter occurrences in the ciphertext, assumes the most common letter maps to **E**, and uses that to guess the key — no brute force needed.

> ⚠️ Works best on longer texts where natural letter distribution is preserved.

---

## 📂 Project Structure

```
Caesar-Cipher-Security-Analysis/
│
├── caesar_security_analysis.py   # Main Python script
├── Caesar_cipher.html            # HTML version / demo
└── README.md                     # Project documentation
```

---

## 💡 Key Takeaway

> The Caesar Cipher has only **25 possible keys** — making it trivially breakable. This project shows why **security through obscurity doesn't work**, and why modern cryptography relies on mathematical complexity instead.

---

## 👩‍💻 Author

**Disha Borse** — [@DishaB-07](https://github.com/DishaB-07)

---

## ⭐ If you found this helpful, give it a star!
