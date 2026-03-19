import re

def clean_text(text):
    
    text = text.lower()
    
    text = re.sub(r"[^\w\s]", "", text)
    
    return text


print(clean_text("I LOVE NLP!!!"))