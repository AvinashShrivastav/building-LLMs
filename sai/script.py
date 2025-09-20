def get_data(story):
            
    words=len(story.split())
    unique_words=[]
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
    "\\", # Backslash
    ]

    punctuation_marks_count=0
    for i in story:
        if i in punctuation_marks:
            punctuation_marks_count+=1
    
        if i not in unique_words:
            unique_words.append(i)
        
   
    output_file=open("output.txt","w")
    output_file.write(f"no of words are {words} of them unique are {len(unique_words)} and finally punctuation marks are {punctuation_marks_count}")
    
myfile=open("story.txt","r",encoding="utf-8", errors="ignore")
story=myfile.read()
get_data(story)