def get_num_words(text: str) -> int:
    return len(text.split())


def get_chars_usage(text: str) -> dict:
    usages = {}
    for char in text:
        if char.lower() in usages:
            usages[char.lower()] += 1
        else:
            usages[char.lower()] = 1
    
    return usages


def sort_usages(usages: dict) -> list:
    sorted_usages = []
    for key in usages:
        sorted_usages.append({"char": key, "num": usages[key]})

    sorted_usages.sort(reverse=True, key=sort_on)
    return sorted_usages
    

def sort_on(usages):
    return usages["num"]

