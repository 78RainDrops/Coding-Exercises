
inputText = "secret message"

key = 5

mode = 'encrypt'

ledger = 'abcdefghijklmnopqrstuvwxyz 123457890'

outputText = ''

for char in inputText:
    inputIndex = ledger.find(char)

    if mode == 'encrypt':
        outputIndex = inputIndex + key
    elif mode == 'decrypt':
        outputIndex = inputIndex - key

    if outputIndex >= len(ledger):
        outputText = outputIndex - len(ledger)
    elif outputIndex < 0:
        outputIndex = outputIndex + len(ledger)
    
    outputText = outputText + ledger[outputIndex]

print(outputText)
