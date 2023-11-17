def palindrome(s):
    return s==s[: : -1]
s='greeks'
x=palindrome(s)
if x:
    print('yes')
else:
    print('no')

