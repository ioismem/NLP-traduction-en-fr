from translator import DualTranslator

def main():
    translator = DualTranslator()
    state = True
    while True:
        choice = input("choose 1/to translate english to french 2/to translate french to english or 3/ to quit: ")
        if choice == "1":
            while True:
                text = input("input english text to translate to french or sisto to stop ")
                if text == "sisto":
                    break
                else:
                    french = translator.en_to_fr(text)
                    print(f"→ French: {french}")

        elif choice == "2":
            while True:
                text = input("input french text to translate to english or sisto to stop: ")
                if text == "sisto":
                    break
                else:
                    english = translator.fr_to_en(text)
                    print(f"→ English: {english}")

        elif choice =="3":
            break
        else:
            print("invalid choice")


if __name__ == "__main__":
    main()
