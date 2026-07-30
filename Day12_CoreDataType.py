'''
*Q3. Count Vowels*
Count number of vowels a, e, i, o, u in the string.
`Input: "education"`
`Output: 5
'''

inputData = input("Enter a String :")

vowel = ['a', 'e', 'i', 'o', 'u']
vowelCount = 0
for i in inputData:
    if i in vowel:
        vowelCount+=1
print(f"Total Vowels in {inputData} :",vowelCount)

'''
Q3. Count Even and Odd*
Count how manyeven andoddnumbers are in the list.
`Input: [1, 2, 3, 4, 5, 6]`
`Output: Even = 3, Odd = 3
'''

inputList = [1, 2, 3, 4, 5, 6]
oddCount = 0
evenCount = 0
for i in inputList:
    if i%2==0:
        oddCount+=1
    elif i%2==1:
        evenCount+=1
print(oddCount," ",evenCount)
