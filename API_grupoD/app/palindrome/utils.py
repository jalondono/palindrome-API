def longest_palindromic(text: str) -> str:
    """
    Get the largest palindrome given an string
    :param text:
    :return:
    """
    # len of string
    n = len(text)

    maxLength = 1
    start = 0

    # go through the string
    for i in range(n):
        # go through the string
        for j in range(i, n):
            flag = 1

            # Check palindrome
            for k in range(0, ((j - i) // 2) + 1):
                if (text[i + k] != text[j - k]):
                    flag = 0
                    break

            # is palindromic, save the position
            if (flag != 0 and (j - i + 1) > maxLength):
                start = i
                maxLength = j - i + 1
    return text[start: start + maxLength]
