# Secure Data Transmission

This project simulates a TLS-like handshake where the client and server perform a secure key exchange using RSA, followed by encrypted communication using AES. The goal is to demonstrate how RSA and AES can be used together to ensure secure data transmission over a network.

## Project Overview

1. **TLS-like Handshake:** 
   - **Key Exchange:** The client and server perform RSA-based key exchange to securely transmit an AES key.
   - **Switch to AES:** Once the AES key is exchanged, communication between the client and server is encrypted using AES.

2. **Secure Transmission:**
   - **AES Encryption:** After the AES key is exchanged, any message sent between the client and server is encrypted with the AES key.

## Project Structure

- **`server.py`:** 
  - Handles server-side key generation (RSA), RSA decryption, and AES-based communication.
  - Listens for incoming connections, decrypts the AES key, and handles encrypted message reception and decryption.

- **`client.py`:** 
  - Handles client-side RSA encryption of the AES key and AES-based communication.
  - Generates an AES key, encrypts it using the server's RSA public key, sends the encrypted AES key to the server, and then sends encrypted messages using the AES key.

## Requirements

- OpenSSL
- Python 3.x
- The `cryptography` library (install via `pip install cryptography`)

## Setup and Execution

### 1. Generate RSA Keys

Run the server script to generate RSA keys if they do not already exist:

```bash
python3 server.py
