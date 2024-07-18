main=input("Enter main string..")
sub=input("Enter sub string..")

print(sub in main)
indian_lang = ["Hindi", "Bengali", "Telugu", "Marathi", "Tamil", "Gujarati", "Kannada", "Malayalam", "Odia", "Punjabi"]
listLength = len(indian_lang)
for i in range(0,listLength):
   print(indian_lang[-i])
   i=i-1