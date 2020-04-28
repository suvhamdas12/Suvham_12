def encryptDecrypt(inpString,xorKey): 
    length1=len(xorKey) 
    length = len(inpString); 
    for i in range(length): 
        for j in range(length1):
            inpString = (inpString[:i] + chr(ord(inpString[i]) ^ ord(xorKey[j])) +inpString[i + 1:]);
            #continue
        print(inpString[i], end = ""); 
    return inpString; 
if __name__ == '__main__': 
    sampleString ="messi:"
    key= "78"
    print("Encrypted String: ", end = ""); 
    sampleString = encryptDecrypt(sampleString,key); 
    print("\n");  
    print("Decrypted String: ", end = ""); 
    encryptDecrypt(sampleString,key)
