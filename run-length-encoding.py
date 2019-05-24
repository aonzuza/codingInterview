def decodeMsg(msg):

    result = '';
    total  = '';

    for current in msg:
        if current.isdigit():
            total += current;
        else:
            total = int(total);
            for i in range(total):
                result += current;
            total = '';
    return result;



def encodeMsg(msg):
    length = len(msg);
    counter = 1;
    encodedMsg = '';
    for i in range(length):
        current = msg[i];
        next    = msg[i+1] if i+1 <= length - 1 else '';
        if current == next :
            counter +=1;
        else:
            encodedMsg += str(counter) + current;
            counter = 1;
    return encodedMsg;

msg = 'VVABCAABBBBBBBBBBBB';

encoded_msg = encodeMsg(msg);
print('input is ' + msg);
print('encoded msg is ' + encoded_msg);
print('decoded msg is ' + decodeMsg(encoded_msg));
