def ceasarencode(letter,shift):
    list = []
    for i,c in enumerate(letter):
        if letter[i].islower():
            list.append(chr((ord(letter[i])-ord("a") + shift)%26 + ord("a")))
        elif letter[i].isupper():
            list.append(chr((ord(letter[i])-ord("A") + shift)%26 + ord("A")))
        else:
            list.append(letter[i])
    return("".join(list))
    
def ceasardecode(message,word):
    shift = 0
    list = []
    while word != message:
        shift +=1 
        test = ceasarencode(message,shift)
            
        if word in test:
            shift = 26 - shift
            return test, shift
        
def vigenereencode(message,keyword):    
    keyword = list(keyword)
    for i in range(len(message) -len(keyword)): 
        keyword.append(keyword[i % len(keyword)]) 
    encrypt_text = [] 
    for i in range(len(message)): 
        if message[i].islower():
            encrypt_text.append(chr((((ord(message[i])-97) +(ord(keyword[i])-97)) % 26)+97))
        elif message[i].isupper():
            encrypt_text.append(chr((((ord(message[i])-65) +(ord(keyword[i])-97)) % 26)+65))
        else:
            encrypt_text.append(message[i])
    return("" . join(encrypt_text)) 
    
def vigeneredecode(message,keyword):    
    keyword = list(keyword)
    for i in range(len(message) -len(keyword)): 
        keyword.append(keyword[i % len(keyword)]) 
    encrypt_text = [] 
    for i in range(len(message)): 
        x = (ord(message[i]) - ord(keyword[i])) % 26
        if message[i].isupper():
            encrypt_text.append(chr((((ord(message[i])-65) -(ord(keyword[i])-97)) % 26)+65)) 
        elif message[i].islower():
            encrypt_text.append(chr((((ord(message[i])-97) -(ord(keyword[i])-97)) % 26)+97))
        else:
            encrypt_text.append(message[i])
    return("" . join(encrypt_text)) 

choice = input("E for Encode, D for Decode, Q for Quit: ")

while choice == "E":
    encode_type = input("Type c to encode ceasar cipher or v for vingere cipher: ")
    if encode_type == "c":
        letter = input("enter a message: ")
        shift = int(input("enter a shift: "))
        print("The message encoded to ceasar is: " + ceasarencode(letter,shift))
    elif encode_type == "v":
        message = input("Enter a message: ")
        keyword = str(input("what is the keyword: "))
        print("The message encoded to vingere is: " + vigenereencode(message,keyword))
    
while choice == "D":
    decode_type = input("Would you like to encode ceasar cipher or vingere cipher")
    if decode_type =="c":
        message = input("what message would you like to Decode: ")
        word = input("enter a word you know was in the message: ")
        message,shift = ceasardecode(message,word)
        print("The encoded message was: "+ str(message))
        print("the shift was: " + str(shift))
    if decode_type == "v":
        message = input("what is the message you want to decode: ")
        keyword = str(input("What was the keyword: "))
        print("The encoded message was: "+ vigeneredecode(message,keyword))
        
while choice == "Q":
    print("Bye")
    exit()
