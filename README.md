# RSA Algorithm

This project is a simple **RSA encryption and decryption tool** built using **Python** and **PyQt5**.  
It allows you to:
- Generate RSA public and private keys
- Encrypt text messages
- Decrypt encrypted messages
- View generated RSA key details

## Features
- **Key Generation**: Random primes chosen from a provided list (`primes_to_100k.txt`).
- **Encryption**: Each character of the message is encrypted individually.
- **Decryption**: Encrypted integers are decrypted back to the original text.
- **PyQt5 GUI**: Simple and clean user interface for interaction.

## How It Works
- Select two random prime numbers `p` and `q`.
- Compute `n = p * q` and Euler's Totient `phi = (p-1)*(q-1)`.
- Choose public key exponent `e` such that `gcd(e, phi) = 1`.
- Compute private key exponent `d` using the Extended Euclidean Algorithm.

## Requirements
- Python 3.x
- PyQt5

Install requirements:
```bash
pip install PyQt5
```

## Files
- `main.py` - The main GUI application.
- `primes_to_100k.txt` - Text file containing prime numbers up to 100,000.

## How to Run
```bash
python main.py
```
