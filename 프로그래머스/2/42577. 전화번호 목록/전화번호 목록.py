def solution(phone_book):
    phone_book.sort()
    for idx,num in enumerate(phone_book):
        if idx==0:
            continue
        if phone_book[idx-1] in phone_book[idx][:len(phone_book[idx-1])]:
            return False
    return True