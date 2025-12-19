# Kanji Frequency Analyzer 🇯🇵📊

A Data Science tool that analyzes Japanese text files to determine Kanji usage frequency. Built for language learners to identify high-value Kanji from real-world texts (news, novels, subtitles).

## 🚀 Features
- **File Parsing:** Reads Japanese text files with UTF-8 encoding.
- **Frequency Analysis:** Uses `collections.Counter` for O(1) counting logic.
- **Visualization:** Generates a bar chart of the Top 10 Kanji using `matplotlib`.
- **Statistics:** Automatically calculates the percentage of Kanji in a text file.

## 🛠️ Tech Stack
- **Language:** Python 3.12
- **Libraries:** Matplotlib, Collections
- **OS:** Linux (Ubuntu/WSL)

## ⚙️ How to Run
1. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/Kanji-Frequency-Analyzer.git](https://github.com/YOUR_USERNAME/Kanji-Frequency-Analyzer.git)

2. Install Dependencies:
   ```bash
    sudo apt install fonts-noto-cjk  # Required for Japanese graph labels
    pip install matplotlib

3. Run The Script
   ```bash
    python3 main.py