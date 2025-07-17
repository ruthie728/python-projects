def main():
    text = input("Enter a sentence: ")

    def convert(text):
        if ":(" in text:
            text_emoji = text.replace(":(","🙁")
        elif ":)" in text:
            text_emoji = text.replace(":)", "🙂")
        print(text_emoji)

    convert(text)
main()



