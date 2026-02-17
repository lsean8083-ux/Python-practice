text = [chr(i)for i in range(ord('A'),ord('Z')+1)]
smaller_text = [chr(i)for i in range(ord('a'),ord('z')+1)]

print(text)
print(smaller_text)

def jia_mi(text_in, shift):
    output = ''
    shift = shift % 26
    
    
    for num_1 in text_in:
        if num_1 in text:
            address_1 = text.index(num_1)
            new_address = (address_1 + shift) % 26
            output += text[new_address]
            
            
            
        elif num_1 in smaller_text:
            address_2 = smaller_text.index(num_1)
            new_address_2 = (address_2 + shift) % 26
            output += smaller_text[new_address_2]
            
            
        else:
            output += num_1
            
            
    return output


def jie_mi(wen_ben, shift):
    output = ''
    
    
    shift = shift % 26
    
    
    for num_1 in wen_ben:
            if num_1 in text:
                address_1 = text.index(num_1)
                new_address = (address_1 + 26 - shift)%26
                output+= text[new_adress]
                
                
         
            elif num_1 in smaller_text:
                address_2 = smaller_text.index(num_1)
                new_address_2 = (address_2 + 26 - shift)%26
                output+= smaller_text[new_address_2]
                
                
            
            else:
                output+= num_1
                
                
                
    return output

aaa= "hello world! abcdkfjaofjaz !%^$$#"
shift = 1000
print(jia_mi(aaa, shift))
print(jie_mi(jia_mi(aaa, shift),shift))

                    
                


