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


# def get_chars_usage_(text: str) -> list:
#     usages = []
#     for ch in text:
#         usage = get_usage(usages, ch)
#         if usages is None:
#             set_usage(usages, ch, 0)
#         else:
#             set_usage(usages, ch, usage + 1)
    
#     return usages


# def get_usage(usages: list, char: str) -> int | None:
#     for dict in usages:
#         for value in dict:
#             if char == value["char"]:
#                 return value["usage"]
    
#     return None


# def set_usage(usages: list, char: str, usage: int):
#     found = False
#     for dict in usages:
#         for value in dict:
#             if char == value["char"]:
#                 found = True
#                 value["usage"] = usage
#                 break
    
#     if not found:
#         usages.append({"char": char, "usage": usage})
