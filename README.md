
# Cyber‑Key‑Logger 🕵️‍♂️

> **IMPORTANT**  
> This project is for **educational and ethical use only**. Do **not** deploy it on machines you do not own or without clear permission. Unauthorized use may be illegal.

## 🧩 Description

This is a simple Python-based key logger that demonstrates how to capture global keyboard events. It logs each key press with a timestamp to a local file (`data.txt`), using the `pynput` library.

Ideal for:
- Learning how Python can interact with OS-level input.
- Testing and defensive tool development in controlled environments.
- Academic or ethical cybersecurity training.

## 🚀 Features

- Captures all keyboard input, including special keys.
- Logs with timestamps.
- Structured, append-mode logging for later review.

## 💻 Requirements

- Python 3.6+
- [pynput](https://pypi.org/project/pynput/)

Install dependencies:

```bash
pip install pynput
```

## ▶️ Usage

Run the key logger:

```bash
python CYBERANY.py
```

This starts monitoring keystrokes. Press **Ctrl+C** in your terminal to stop the logger.

## 📂 Output

The log file `data.txt` will contain entries like:

```
2025-06-15 20:22:45: a
2025-06-15 20:22:46: Key.space
2025-06-15 20:22:47: Key.enter
...
```

## 🛡️ Ethical and Legal Notice

**Only use on systems you own or have explicit consent to monitor.**  
Respect privacy and comply with applicable laws.

## ⚙️ Customization

- Change the log file name or path for different outputs.
- Add keyboard filters (e.g. only letters, only certain keys).
- Hook additional events (mouse clicks, screenshots).

## 🧪 Testing & Security Context

Use in secure & isolated environments only. This isn't for malicious hacking—it's to help understand logging mechanisms and develop detection tools.

## 📜 License

Distributed under the **MIT License**. See the LICENSE file for details.

---

