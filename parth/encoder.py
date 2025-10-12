def encoder(story):
    char_to_num = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'k': 11,
    'l': 12,
    'm': 13,
    'n': 14,
    'o': 15,
    'p': 16,
    'q': 17,
    'r': 18,
    's': 19,
    't': 20,
    'u': 21,
    'v': 22,
    'w': 23,
    'x': 24,
    'y': 25,
    'z': 26
    }
    ans=[]
    punctuation_marks = [
    ".",  # Period / Full stop
    ",",  # Comma
    "?",  # Question mark
    "!",  # Exclamation mark
    ":",  # Colon
    ";",  # Semicolon
    "\"", # Double quotes
    "'",  # Single quote / Apostrophe
    "-",  # Hyphen
    "—",  # Dash
    "…",  # Ellipsis
    "(",  # Left parenthesis
    ")",  # Right parenthesis
    "[",  # Left square bracket
    "]",  # Right square bracket
    "{",  # Left curly bracket
    "}",  # Right curly bracket
    "/",  # Slash
    "\\",
     '’',
     '“',
      '”'
    ]
    for i in story.split():
       val=[]
        
       for j in i:
           
           if j not in punctuation_marks:
               val.append(char_to_num[j.lower()])
               
       ans.append(val)
    print(ans)
myfile=open("story.txt","r",encoding="utf-8", errors="ignore")
story=myfile.read()
encoder(story)


