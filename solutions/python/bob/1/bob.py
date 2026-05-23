def response(hey_bob):
    cleaned_text = hey_bob.strip()
    
    if not cleaned_text:
        return "Fine. Be that way!"
        
    if cleaned_text.isupper() == True:
        if cleaned_text.endswith('?'):
            return "Calm down, I know what I'm doing!"
        return "Whoa, chill out!"

    if cleaned_text.endswith('?'):
        return "Sure."

    return "Whatever."
