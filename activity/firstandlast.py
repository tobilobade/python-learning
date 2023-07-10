word=input("Enter String:")
def solve(word):
    if len(word)<2:
        return ""
    return word[0:2] + word[-2:]

print(solve(word))