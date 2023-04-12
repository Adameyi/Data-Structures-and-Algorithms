import math
import jovian
from jovian.pythondsa import evaluate_test_cases


test = {
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 7
    },
    'output': 3
}

# EXHAUSTIVE TEST CASES
tests = []
# query occurs in the middle
tests.append(test)

tests.append({
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 1
    },
    'output': 6
})

# query is the first element
tests.append({
    'input': {
        'cards': [4, 2, 1, -1],
        'query': 4
    },
    'output': 0
})

# query is the last element
tests.append({
    'input': {
        'cards': [3, -1, -9, -127],
        'query': -127
    },
    'output': 3
})

# cards contains just one element, query
tests.append({
    'input': {
        'cards': [6],
        'query': 6
    },
    'output': 0
})

# cards does not contain query
tests.append({
    'input': {
        'cards': [9, 7, 5, 2, -9],
        'query': 4
    },
    'output': -1
})

# cards is empty
tests.append({
    'input': {
        'cards': [],
        'query': 7
    },
    'output': -1
})

# numbers can repeat in cards
tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 3
    },
    'output': 7
})

# query occurs multiple times
tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 6
    },
    'output': 2
})


# def locate_card(cards, query):
#     pos = 0

#     # If length of the array is smaller than position, return -1
#     while pos < len(cards):
#         # Check if element at current pos matches query.
#         if cards[pos] == query:
#             # Return the answer and exit
#             return pos

#         # Increment position
#         pos += 1
#     # Check if the end of the array is reached.
#     if pos == len(cards):
#         return -1
#     return -1

def test_location(cards, query, mid):
    mid_num = cards[mid]
    print(f"mid: {mid}, mid_number: {mid_num}")

    if mid_num == query:
        if mid-1 >= 0 and cards[mid-1] == query:
            return 'left'
        else:
            return 'found'
    elif mid_num < query:
        return 'left'
    else:
        return 'right'


def locate_card(cards, query):
    low, high = 0, len(cards) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_num = cards[mid]
        print(f"lo: {low}, hi: {high}, mid: {mid}, mid_number: {mid_num}")

        # If query matches the middle number, return mid.
        if mid_num == query:
            return mid

        # If mid number is less than the given query, count down (decrement)
        elif mid_num < query:
            high = mid - 1

        # If mid number is higher than the given query, count up (increment)
        elif mid_num > query:
            low = mid + 1
    return - 1


result = locate_card(test['input']['cards'], test['input']['query'])
print("Output:", result)
evaluate_test_cases(locate_card, tests)

# Save and upload code via Jovian
# jovian.commit(project='python-binary-search', environment=None)
