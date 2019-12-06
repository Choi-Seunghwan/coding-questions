from collections import Counter

def solution(cards, words):
    answer = []
    
    for word in words:
        count_word = Counter(word)
        flag = True
        for card in cards:
            count_card = Counter(card)
            
            if not count_word & count_card:
                flag = False
                break
            count_word -= count_card
            
        if flag and not count_word:
            answer.append(word)
            
    if answer:
        return answer
    else:
        return ["-1"]