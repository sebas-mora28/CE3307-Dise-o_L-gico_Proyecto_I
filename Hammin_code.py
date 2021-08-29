from math import sqrt
def calcRedundantBits(m):
    # Use the formula 2 ^ r >= m + r + 1
    # to calculate the no of redundant bits.
    # Iterate over 0 .. m and return the value
    # that satisfies the equation
    for i in range(m):
        if(2**i >= m + i + 1):
            return i

def get_hamming_string(parity_list,r):
    res = ""
    pos = 1
    r_counter = 0
    for i in parity_list[0]:
        if is_power_of_two(pos):
            while is_power_of_two(pos) and r_counter<r:
                res = res + parity_list[r_counter+1][0]
                pos+=1
                r_counter+=1
        res = res+i
        pos+=1
    return res
 
def count_parity(pos,block_size,array):
    counter = 0
    bit_array = []
    in_block_counter = 0
    while pos < len(array):
        if in_block_counter<block_size:
            if array[pos] == '1':
                counter+=1
            bit_array.append(array[pos])
            pos+=1
            in_block_counter+=1  
        else:
            pos+=block_size
            in_block_counter = 0
    return (counter,bit_array) 

def insert_parity_bits(data):
    res = ""
    pos = 1
    for i in data:
        if is_power_of_two(pos):
            while is_power_of_two(pos):
                res = res + '0'
                pos += 1        
        res = res + i
        pos += 1
    return res

def is_power_of_two(num):
    while num != 1:
        if num < 1:
            return False
        else:
            num = num/2
    return True

def get_hamming_array(data,r,parity_type):
    array = insert_parity_bits(data)
    res = []
    res.append(data)
    if parity_type:
        for i in range(0,r):
            parity_data = count_parity((2**i)-1,2**i, array)
            if parity_data[0]%2 == 1:
                parity_data[1][0]='1'
            res.append(parity_data[1])
    else:
        for i in range(0,r):
            parity_data = count_parity((2**i)-1,2**i, array)
            if parity_data[0]%2 == 0:
                parity_data[1][0]='1'
            res.append(parity_data[1])
    res.append(get_hamming_string(res,r))
    return res


def hamming_encode(data,parity_type):
    return get_hamming_array(data,calcRedundantBits(len(data)),parity_type)

#print(get_hamming_string(['0110101', ['1', '0', '1', '0', '1', '1'], ['0', '0', '1', '0', '0', '1'], ['0', '1', '1', '0'], ['0', '1', '0', '1']],4))
print(hamming_encode('0110101',False))
