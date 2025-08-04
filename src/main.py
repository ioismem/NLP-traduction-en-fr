from translator import Translator

def main():
    translator = Translator()
    
    while True:
        text = input("Enter English text (or 'q' to quit): ")
        if text.lower() == 'q':
            break
        french = translator.translate(text)
        print(f"→ French: {french}")

if __name__ == "__main__":
    main()
