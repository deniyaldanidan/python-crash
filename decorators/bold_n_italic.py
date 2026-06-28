def italic(base_fn):
    print("hello italic")

    def wrapper(*args, **kwargs):
        return f"<i>{base_fn(*args, **kwargs)}</i>"

    return wrapper


def bold(base_fn):
    print("hello bold")

    def wrapper(*args, **kwargs):
        return f"<b>{base_fn(*args, **kwargs)}</b>"

    return wrapper


@bold
@italic
def sentence(word):
    return f"The argument is ${word}"


print(sentence("Hello World!"))
# Italic is first executed
# Bold is next
# bold(italic(sentence))
