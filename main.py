def main():
    book_path="books\\frankenstein.txt"
    text=get_book_text(book_path)
    num_words=count_words(text)
    num_letters=get_chars_dict(text)
    report= get_char_report(num_letters)
    print(f'--- Begin report of {book_path} ---')
    print(f'{num_words} words found in the document')
    print()
    for item in report:
        print(f"The '{item['char']}' character was found {item['value']} times")
    print('--- End report ---')

def get_book_text(path:str):
    with open(path) as f:
        return f.read()

def count_words(text:str):
    words=text.split()
    return len(words)

def get_chars_dict(text:str):
    chars={}
    for c in text:
        lowered=c.lower()
        if lowered in chars:
            chars[lowered]+=1
        else: 
            chars[lowered]=1
    return chars

def sort_on(d):
    return d['value']

def get_char_report(data:dict):
    report=[{'char':k,'value':v} for k,v in data.items() if k.isalpha()]
    # return report
    report.sort(reverse=True,key=sort_on)
    return report



if __name__=='__main__':
# print(__name__)
    main()