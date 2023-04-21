def count_amount_of_words(sentence):
    better_counter = sentence.count("better")
    never_counter = sentence.count("never")
    is_counter = sentence.count("is")

    print(f"<better {better_counter}> <never {never_counter}> <is {is_counter}>)")

    return f"{sentence.upper().replace('I', '&')}"

print(count_amount_of_words('If the implementation is easy to explain, it may be a good idea.'))
