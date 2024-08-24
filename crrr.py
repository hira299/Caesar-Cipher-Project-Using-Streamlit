import streamlit as st

def caesar_cipher(message, shift, ac):
    
    result = ''
    
    if not ac:
        shift = -shift

    for char in message:
        if char.islower():
            start = ord('a')
            result += chr(((ord(char) - start + shift) % 26) + start)
        elif char.isupper():
            start = ord('A')
            result += chr(((ord(char) - start + shift) % 26) + start)
        elif char.isdigit():
            start = ord('0')
            result += chr(((ord(char) - start + shift) % 10) + start)
        else:
            result += char  #if char is not alphabet/num

    return result

# Streamlit app
st.title('Caesar Cipher')

# Inputs
message = st.text_input('Enter message:')
shift = st.number_input('Enter shift number:', min_value=0, max_value=25, value=0)
action = st.selectbox('Select Action:', ['Encrypt', 'Decrypt'])

# ecrypt / decrypt
encrypt = action == 'Encrypt'


if st.button('Submit'):
    magic = caesar_cipher(message, int(shift), encrypt)
    
    st.divider()
    st.info(f'#### Result :\t  {magic}')
    
