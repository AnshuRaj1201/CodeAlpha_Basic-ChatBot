# 🤖 ChatBot 3000 — Rule-Based Python Chatbot

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![Level](https://img.shields.io/badge/Level-Beginner-green?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

A simple **rule-based chatbot** built with pure Python — no libraries, no AI, just clean beginner-friendly code using `if-elif`, functions, loops, and input/output.

---

## 📋 Table of Contents

- [About the Project](#about-the-project)
- [Demo](#demo)
- [Features](#features)
- [Concepts Used](#concepts-used)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [How to Run](#how-to-run)
- [Sample Conversation](#sample-conversation)
- [What You Can Add Next](#what-you-can-add-next)
- [Author](#author)

---

## 📖 About the Project

This project is a **beginner Python exercise** that demonstrates how to build a simple chatbot using only core Python concepts. The chatbot listens to user input and replies with predefined responses based on pattern matching.

> Built as part of learning Python fundamentals — no external libraries required!

---

## 🎬 Demo

```
===================================
   Welcome to ChatBot 3000! 🤖
   Type 'bye' to exit.
===================================

You: hello
Bot: Hi there! 👋

You: how are you
Bot: I'm just a bot, but I'm doing great! 😄

You: what is your name
Bot: I'm ChatBot 3000! 🤖

You: bye
Bot: Goodbye! See you soon! 👋
```

---

## ✨ Features

- 💬 Responds to common greetings like `hello`, `how are you`, `bye`
- 🔁 Keeps the conversation going with a `while` loop
- 🔡 Case-insensitive input — `Hello`, `HELLO`, and `hello` all work
- 🧹 Handles extra spaces in user input automatically
- ⚠️ Handles empty input gracefully
- 🚪 Exits cleanly when the user types `bye`

---

## 🧠 Concepts Used

| Concept | How It's Used |
|---|---|
| `input()` / `print()` | Getting user input and displaying bot replies |
| `if-elif-else` | Matching user input to predefined replies |
| `functions` | `get_reply()` and `run_chatbot()` separate logic cleanly |
| `while` loop | Keeps the chatbot running until user exits |
| `break` | Exits the loop when user says `bye` |
| `.lower()` / `.strip()` | Normalizes input to avoid case/space mismatches |

---

## 📁 Project Structure

```
chatbot-3000/
│
├── chatbot.py       # Main chatbot script
└── README.md        # Project documentation
```

---

## 🚀 Getting Started

### Prerequisites

- Python **3.x** installed on your system
- Check your version by running:

```bash
python --version
```

### Installation

1. **Clone the repository**

```bash
git clone https://github.com/your-username/chatbot-3000.git
```

2. **Navigate into the project folder**

```bash
cd chatbot-3000
```

---

## ▶️ How to Run

```bash
python chatbot.py
```

That's it! No installs, no dependencies. Just Python. 🐍

---

## 💬 Sample Conversation

| You Type | Bot Replies |
|---|---|
| `hello` | Hi there! 👋 |
| `how are you` | I'm just a bot, but I'm doing great! 😄 |
| `what is your name` | I'm ChatBot 3000! 🤖 |
| `bye` | Goodbye! See you soon! 👋 |
| *(anything else)* | Hmm, I don't understand that. Try: hello, how are you, bye |

---

## 🔮 What You Can Add Next

Want to level up this project? Here are some ideas:

- [ ] 🕐 Add `"what time is it"` using Python's `datetime` module
- [ ] 😂 Add `"tell me a joke"` with a random joke from a list
- [ ] 📊 Add a **message counter** to track how many messages were sent
- [ ] 📝 Save the **chat history** to a `.txt` file
- [ ] 🌐 Expand responses using a **dictionary** instead of if-elif
- [ ] 🧠 Upgrade to NLP using the `nltk` library

---

## 👤 Author

**Anshu Raj**
- GitHub: [@AnshuRaj1201](https://github.com/AnshuRaj1201/CodeAlpha_Basic-ChatBot)

---

## 📄 License

This project is licensed under the **MIT License** — feel free to use, modify, and share it!

---

> ⭐ If you found this helpful, consider giving the repo a star!
