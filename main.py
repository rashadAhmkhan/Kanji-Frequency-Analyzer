import collections
import matplotlib.pyplot
import requests

# TODO: You will need a library to plot graphs later. Maybe 'matplotlib'?

def read_file(filename):
    """
    Reads a text file and returns the content as a string.
    """
    try:
        # TODO: Open the file using 'utf-8' encoding so it can read Japanese!
        # with open(filename, 'r', encoding='...') as f:
        #     return f.read()

        with open(filename, 'r' , encoding='utf-8') as f:
            return f.read()

    except FileNotFoundError:
        print("Error: File not found.")
        return ""

def is_kanji(char):
    """
    Checks if a character is a Kanji.
    Kanji ranges usually fall between \u4e00 and \u9faf.
    """
    # TODO: Write a simple if statement checking the unicode range.
    # if '\u4e00' <= char <= '\u9faf':
    #     return True

    if '\u4e00' <= char <= '\u9faf':
        return True
    else:
        return False

def analyze_text(text):
    """
    Counts frequency of Kanji characters only.
    """
    kanji_counts = collections.Counter()
    
    for char in text:
        # TODO: Use the is_kanji function here.
        if is_kanji(char):
            kanji_counts[char] += 1
        # If it is kanji, add it to the counter.
    return kanji_counts 

def plot_results(counter):
    import matplotlib.pyplot as plt
    import matplotlib as mpl
    
    # This line tells Matplotlib to use the Japanese font specifically
    mpl.rcParams['font.family'] = 'Noto Sans CJK JP'
    
    common = counter.most_common(10)
    labels, values = zip(*common)
    
    plt.figure(figsize=(10, 6))
    plt.bar(labels, values, color='skyblue')
    plt.title("Top 10 Kanji Frequency")
    plt.xlabel("Kanji")
    plt.ylabel("Frequency")
    plt.show()

#Getting Meaning Of Kanjii Version-3 of adding features I guess


def get_meaning(kanji):
    """
    Fetches the English meaning of a single Kanji from Jisho API.
    """
    url = f"https://jisho.org/api/v1/search/words?keyword={kanji}"
    try:
        response = requests.get(url)
        data = response.json() # This converts the web response into a Python Dictionary
        
        # We navigate the dictionary to find the first English definition
        # Jisho returns a list of results; we take the first one [0]
        meaning = data['data'][0]['senses'][0]['english_definitions']
        return ", ".join(meaning[:3]) # Join the first 3 meanings into a string
    except:
        return "Meaning not found"


# --- Main Execution ---
if __name__ == "__main__":
    # 1. Create a dummy file named 'sample.txt' with some Japanese text manually first.ṇ
    input_file = "sample.txt" 
    
    print(f"Reading {input_file}...")
    content = read_file(input_file)
    
    if content:
        print("Analyzing Kanji...")
        results = analyze_text(content)

        #counting kanji
        total_kanji_found = sum(results.values())
        char_count = len(content)
        kanji_percentage = (total_kanji_found / char_count) * 100

        print(f'Kanji Percentage: {kanji_percentage:.2f}%')

        # Print top 5 common Kanji
        print("\n--- Top 5 Kanji & Meanings ---")
        for kanji, count in results.most_common(5):
            definition = get_meaning(kanji)
            print(f"{kanji} (Count: {count}) -> {definition}")

        #Geraph Of Top 5 Kanji
        print("The GRaph Of Kanji-Frequency: ")
        plot_results(results)