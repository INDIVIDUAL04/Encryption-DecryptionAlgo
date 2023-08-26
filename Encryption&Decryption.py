def get_task():
    task = input('Do you want to encrypt or decrypt?')
    return task

def get_message():
    message = input('Enter the secret message: ')
    return message

def get_key():
    key = input('Enter the secret key: ')
    return key

def convert_ascii(inp):
    list_a = []
    for count in range(0,len(inp)):
        y = ord(inp[count])
        x = int(y)+int(69)
        list_a.append(x)
    return list_a

def formula(list1,key1):
    list0=[]
    l1 = len(list1)
    l2 = len(key1)
    i = 0
    j = 0
    while(i<l1 and j<l2+1):
        x = list1[i] % key1[j]
        i = i+1
        if(j<l2-1):
            j = j+1
        else:
            j = 0
        list0.append(x)
    return list0

def reverse_formula(list1,key1):
    list0=[]
    l1 = len(list1)
    l2 = len(key1)
    i = 0
    j = 0
    while(i<l1 and j<l2+1):
        if(int(list1[i])<98):
            x = int(list1[i]) + key1[j]
        else:
            x = int(list1[i])
        i = i+1
        if(j<l2-1):
            j = j+1
        else:
            j = 0
        y = int(x)-69
        list0.append(y)
    return list0

def cifer(inp):
    list_c = []
    for i in range(0,len(inp)):
        x = int(inp[i])
        y = chr(x)
        list_c.append(y)
        out =("" . join(list_c))
    return out

def cipher():
    message=input("Enter the cipher text : ")
    list_num = message.split(',')
    return list_num


def decryption():
    list_num = cipher()
    key = get_key()
    key_num = convert_ascii(key)
    list_form = reverse_formula(list_num,key_num)
    list_c = cifer(list_form)
    return list_c

def encryption():
    message = get_message()
    list1 = convert_ascii(message)
    key = get_key()
    key1 = convert_ascii(key)
    list_form = formula(list1,key1)
    return list_form


while True:
    task = get_task()
    if task == 'encrypt' :
        encrypted =encryption()
        print('Ciphertext of the secret message is:', encrypted)

    elif task == 'decrypt' :
        decrypted = decryption()
        print('plaintext of the secret message is:', decrypted)

    else :
        break

