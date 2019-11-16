# Final Assignment of part 2 Python (Intro_
palindromeText = input('Type in a word or phrase that may be a palindrome:')
# <<remove char >>>
palindromeText = palindromeText.replace(' ','')
palindromeText = palindromeText.casefold()

palindromeArray = []
palindromeArray2 = []
i = 0
# <<<< counts character # >>>>
for x in palindromeText:
    palindromeArray.append(0)
    palindromeArray2.append(0)

for x in palindromeText:
    palindromeArray[i] = x
    i = i + 1
    #print(i)

j = i 
#print(j)
# <<<<<<<<<<<[j-1] SINCE ARRAYS START AT 0 >>>>>>>>>>
for x in palindromeText:
    palindromeArray2[j-1] = x
    j -= 1

if palindromeArray == palindromeArray2:
    print('palindrome = true')

else:
    print('The provided is not a palindrome')
    needHelp = input('Type "help" for definition and examples of Palindromes: ')
    if needHelp == 'help':
        defineP = 'a word, phrase, or sequence that reads the same backward as forward'
        examples = "Examples: madam, nurses run, race car, civic, taco cat"
        print('+---------------------------------------------------------------------+')
        print("|", defineP, "|")
        print("|", examples.center(67, " "), '|')
        print('+---------------------------------------------------------------------+')


  

    