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
        
    no_of_unique=len(unique_words)
    print(f"no of words are {words} of them unique are {len(unique_words)} and finally punctuation marks are {punctuation_marks_count}")
story="""Story: The Clockmaker’s Secret

In the quiet town of Brimwood, there lived an old clockmaker named Elias. His shop was filled with clocks of every size and style, each ticking in perfect harmony. But Elias had a secret: one special clock, hidden behind a velvet curtain, could reverse time—just for one minute.

Every night, he used it to undo small mistakes: a spilled cup of tea, a dropped key, or a misdialed number. One evening, a young girl named Lila wandered into the shop, fascinated by the ticking symphony. She noticed the hidden clock and accidentally pressed its golden lever.

Suddenly, everything froze except Lila and Elias. He explained the clock’s power and warned her never to misuse it. But curiosity got the better of her, and she pressed the lever again—this time reversing time for an entire day. Chaos ensued: townspeople repeated conversations, events overlapped, and the market turned into a confusing loop of repeated trades.

Realizing the danger, Elias and Lila worked together to set things right. With careful timing, they returned the town to normal, hiding the clock once more. Lila left with a sense of wonder—and a promise to never meddle with time again.

Moral: Even small powers can have big consequences, and curiosity must be tempered with responsibility.

"""
get_data(story)

