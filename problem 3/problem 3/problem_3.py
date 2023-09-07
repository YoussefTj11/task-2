def anagrams(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)

    if sorted_str1 == sorted_str2:
        print(str1, end=" and ")
        print(str2, end=" are anagram")
        print("")
        return 1
    else:
        print(str1, end=" and ")
        print(str2, end=" are not anagram ")
        print("")
        return -1


print("first string is: ")
string1 = str(input())
print("second string is: ")
string2 = str(input())
find_anagram = anagrams(string1, string2)
