def even_numbers(nums):
    """Return only the even numbers from nums."""
    result = []
    for num in nums:
        if num % 2 == 0:
            result.append(num)
    return result
   


def count_words(text):
    box = {}
    words = text.split()
    for word in words:
        box[word]=box.get(word,0) + 1
    return box



def unique_in_order(items):
   
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
 

def group_by_first_letter(names):
    # 1. make an empty box (dictionary)
    box = {}
    # 2. for each name in names:
    for name in names:
    #        get its first letter
        if name[0] not in box:
    #        if the letter is not a key yet: make an empty list for it
            box[name[0]] = []
    #        put the name into that letter's list
        box[name[0]].append(name)
    # 3. return the box after the loop
    return box

print(even_numbers([1, 2, 3, 4, 5, 6]))
print(count_words("the cat and the dog and the bird"))
print(unique_in_order([3, 1, 3, 2, 1, 4]))
print(group_by_first_letter(["amit", "raj", "anita", "ravi"]))