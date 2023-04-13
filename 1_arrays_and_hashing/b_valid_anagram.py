def isAnagram(s, t):
        #Using ord('a') - helps to find ascii value of character
        #Time: O(n) | Space: O(n)
        if len(s) != len(t):
            return False
        ascii_s, ascii_t = 0, 0
        for i in range(len(s)):
            ascii_s += ord(s[i])
        for j in range(len(t)):
            ascii_t += ord(t[j])
        if ascii_s == ascii_t:
            return True
        return False
print("Test Cases for valid anagram: ")
s_1 = "anagram"
t_1 = "nagaram"
s_2 = "rat"
t_2 = "car"
print(isAnagram(s_1, t_1))
print(isAnagram(s_2, t_2))