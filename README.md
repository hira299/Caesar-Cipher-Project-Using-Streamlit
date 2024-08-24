# Caesar-Cipher-Project-Using-Streamlit


This project is a simple implementation of the Caesar Cipher, a well-known encryption technique, using the Streamlit library in Python. The Caesar Cipher is a type of substitution cipher where each letter in the plaintext is shifted by a certain number of positions down or up the alphabet.

## Features

- **Encryption and Decryption:** The app allows users to both encrypt and decrypt messages using a specified shift value.
- **Supports Letters and Numbers:** The cipher works with both lowercase and uppercase letters, as well as digits.
- **Interactive User Interface:** The project uses Streamlit to provide an easy-to-use web interface where users can input their message, choose a shift value, and select whether to encrypt or decrypt the message.

## How It Works

1. **Input the Message:** Enter the text you want to encrypt or decrypt.
2. **Select the Shift Value:** Choose a shift value between 0 and 25. This determines how much each letter in the message is shifted.
3. **Choose Action:** Select either "Encrypt" to encode the message or "Decrypt" to decode an encrypted message.
4. **View the Result:** The app will display the result based on the inputs provided.


## Usage

Once the app is running, you can access it in your web browser. Simply input the message you want to process, select the shift value and the desired action (Encrypt/Decrypt), and click "Submit" to see the result.

## Example

If you input the message "Hello World" with a shift value of 3 and choose "Encrypt," the result will be "Khoor Zruog". 

![Screenshot (17)](https://github.com/user-attachments/assets/ac37a31c-47ff-4ff7-90a5-9d678dceec48)

![Screenshot (18)](https://github.com/user-attachments/assets/02484c1d-f140-4f53-8109-6a00055b281f)



If you then input "Khoor Zruog" with the same shift value and choose "Decrypt," the result will return to "Hello World."

