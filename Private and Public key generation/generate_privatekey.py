from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.serialization import load_pem_private_key
from cryptography.hazmat.primitives.serialization import Encoding, PrivateFormat, NoEncryption

import json

def create_private_key():
    # generate private key
    private_key = ec.generate_private_key(ec.SECP256K1(), default_backend())
    return private_key

def create_public_key(private_key):
    # generate public key
    public_key = private_key.public_key()
    rsa_pem = public_key.public_bytes(encoding=serialization.Encoding.PEM, format=serialization.PublicFormat.SubjectPublicKeyInfo)
    return rsa_pem.decode()

def clean_public_key(public_key):
    # remove the first and last lines of the public key
    lines = public_key.strip().split('\n')
    if len(lines) >= 3 and lines[0].startswith("-----BEGIN ") and lines[-1].startswith("-----END "):
        return '\n'.join(lines[1:-1])
    else:
        return public_key

def read_private_key(private_key, flag=True):
    # print out the private key
    if flag:
        try:
            value = private_key.private_numbers()
            return value.private_value
        except Exception as e:
            print(f'Error reading private key: {e}')
            return False
    else:
        try:
            private_key = private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=serialization.NoEncryption()  # No encryption for private key
            ).decode('utf-8')

            return private_key
    
        except Exception as e:
            print(f'Error encoding private key: {e}')
            return False

def load_private_key_from_json():
    # load existing private key from the config file
    with open('config.json', 'r') as file:
        data = json.load(file)
    private_key = data['Private-key'].encode('utf-8')
    private_key = serialization.load_pem_private_key(
    private_key,
    password=None,  # No password since there's no encryption
    backend=default_backend()
    )   
    return private_key

def get_public_key():
    # return the public key
    with open('config.json', 'r') as file:
        data = json.load(file)
    public_key = data['Public-key']
    return public_key

def print_status(status):
    # print the status of the key generation
    if status:
        print('Keys generated and saved to config.ini')
    else:
        print('Error generating keys')

def write_keys(private_key, public_key, flag=False):
    # write the keys to the config.json file and return True if successful

    if flag:
        private_key = read_private_key(private_key, False)

        try:
            with open('config.json', 'r') as file:
                data = json.load(file)

            data['Private-key'] = private_key
            data['Public-key'] = public_key

            with open('config.json', 'w') as file:
                json.dump(data, file)

            return True
        
        except Exception as e:
            print(f'Error writing to config file: {e}')
            return False
        
    else:

        try:
            with open('config.json', 'r') as file:
                data = json.load(file)
                
            data['Public-key'] = public_key

            with open('config.json', 'w') as file:
                json.dump(data, file)
        
        except Exception as e:
            print(f'Error writing to config file: {e}')
            return False


if __name__ == '__main__':

    generation = int(input("1. Generate New Private and Public keys\n2. Generate New Public-key from existing Private-key\n3. Print Public-key\nEnter your choice: "))

    if generation == 1:
        print('Generating keys...')
        private_key = create_private_key()
        public_key = create_public_key(private_key)
        status = write_keys(private_key, public_key, True)
        print_status(status)
    
    elif generation == 2:
        print('Generating New Public-key...')
        private_key = load_private_key_from_json()
        public_key = create_public_key(private_key)
        status = write_keys(private_key, public_key, True)
        print_status(status)

    elif generation == 3:
        print('Printing Public-key...')
        public_key = get_public_key()
        print(clean_public_key(public_key))

    else:
        print("Exiting...")
