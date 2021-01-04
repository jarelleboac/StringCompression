#Implement a method to perform basic string compression using the counts of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the "compressed" string would not become smaller than the original string, your method should return the original string. You can assume the string has only uppercase and lowercase letters (a - z). 

#set a temp variable to keep track
#for loop to iterate

#aab

def stringCompression(string):
  counter = 0
  #list = []
  print("length of string -1 is", len(string)-1)
  output = ""
  for i in range(len(string)):
    for j in range(len(string)):
      #print("string[",i,"] is:", string[i])
      temp_char = string[i]
      print("temp char at i," , i, ",is: ", temp_char)
      #print("counter is", counter)
      print("string at j", j, " is: ", string[j])
      if(j== len(string)-1):
        break
      if(i == len(string)-1):
        break
      if(temp_char == string[j]):
        print("match")
        counter += 1
        print("counter is now: ", counter)
      else:
        #print(counter + )
        #list.append(string[i])
        #list.append(counter)
        print("not equal, end count is, ", counter)
        converted = str(counter)
        output += temp_char
        output += converted
        i = j
        j= j+1
        counter=1
        #use find to find index counter index 3
  
  return output

input = "aabcccccaaa"
print('output is: ', stringCompression(input))




