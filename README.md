
# **Learning Cryptography**

## Symmetric Cipher:

- Def: a cipher defined over K M C is pair of efficient algs (E, D) where 
  - Encryption(E) —> Key(K) \* Message(M) —>Cipher text (C).
  - Decryption(D) —> Key(K) \* Cipher text(C) —> Message(M).
- E is often randomized because E generates random bits to encrypt the message and D is always deterministic because it need that particular thing to decrypt the encrypted part (because the output is same everytime no randomness)

#### **Formalizing the privacy definition:**

- An encryption process is secure if the ciphertext does not help to compute any function of the underlying plaintext.
  - This definition has its loop holes:
  - how to formalize whether a given ciphertext helps to a compute a given function of the underlying plaintext?
  - What is the underlying adversary/attack model?
    - is adversary is passive or malicious? 
    - does the adversary have the access to any kind of additional information?
    - Note 1: passive adversary - one how just watches the ciphertext and not change it
    - Note 2: malicious adversary - one who changes the ciphertext and check the output in the reciever end and trying to make malicious.
  - all encrypted messages do not remain indefinitely private
    - Example : The first word in an email is usually “hello”/”dear”, etc

## **Various Attack Models:**

1. Ciphertext-only attack (COA)
1. Known plaintext attack (KPA)
3. Chosen plaintext attack (CPA)
3. Chosen ciphertext attack (CCA)
- in all the models, goal of the adversary is to compute some function of the underlying plaintext from the ciphertext.

### **Ciphertext-only attack:**

![Aspose Words 241bfbc5-17e8-46b7-8db9-3755e281e6f0 001](https://user-images.githubusercontent.com/57310710/185761147-f241f630-0206-43e8-b972-8eb8341b160d.png)


- Attacker has access to the ciphertext
- passive in nature
- here adversary only has ciphertext and he can only do functions based on the ciphertext

### **Known plaintext attack:**

![Aspose Words 241bfbc5-17e8-46b7-8db9-3755e281e6f0 002](https://user-images.githubusercontent.com/57310710/185761148-b4d532af-9f50-4a62-887a-160716a39e1d.png)


- Attacker has access to several (plain-text, cipher-text) pairs under the same unknown key.
  - all encrypted messages do not remain indefinitely private
    - Example : The first word in an email is usually “hello”/”dear”, etc
- Goal is to compute some functions of the underlying plaintext in a new cipher text.

### **Chosen Plain-text Attack:**

- In this attack, attacker may get the access to the encryption algorithm for some limited time so that in that time attacker send a plaintext to algo. so that he will get a ciphertext so next he will store this information in (Plaintext , Ciphertext) pair and do furthur computition.
- Here attacker get the temporary access to the encryption algorithm. (say temporary access instead of limited time)

### **Chosen Ciphertext Attack:**

- In this attack, attacker may get the access to the decryption algorithm for some limited time so that in that time attacker send a ciphertext to algo. so that he will get a plaintext so next he will store this information in (Ciphertext , Plaintext) pair and do furthur computition
- Here attacker get the temporary access to the decryption algorithm. (say temporary access instead of limited time)

## **Perfect Security:**

Shannon C. E

- ***Informal Definition***: Irrespective of any ***prior info***. The attacker has about M, the Ciphertext C should leak ***no additional information*** about the plaintext.  k
- If the key is truly random, is at least as long as the plaintext, is never reused in whole or in part, and is kept completely secret, then the resulting ciphertext will be impossible to decrypt or break.
- Observing the cipher text C does not change the attackers knowledge about hte distributio of plaintext. even if adversary is computationally unbounded.
1. Interpretation: Probability of knowing a plaintext remains the same before and after seeing the ciphertext —> Perfect Security.
1. Interpretation: Probability distribution of ciphertext is independent of plaintext.
![Aspose Words 241bfbc5-17e8-46b7-8db9-3755e281e6f0 003](https://user-images.githubusercontent.com/57310710/185761149-5e253cb5-e327-43e8-88fd-01d8295fc7fe.png)


## **Shift Cipher(Ceaser Cipher):**

- This method is like shifting by certain order.
- like if i shift by 1, then A become B; B become C. If i shift by 2 then A become C; B become D like that.

1. An attacker can decrypt by brute force because key is in range from 0 to 25 because there is only 26 letters in alphabets. so he will try every possible key using brute force.

## **Mono-alphabetic Substitution Cipher:**

- Map each plain-text character to an arbitrary cipher-text character in a one-to-one fashion.
- Like it maps one alphabet letter in plaintext to any random alphabet from A-Z in cyphertext.
  - Example: If the plaintext contain ABCD then A can be mapped with V; B can be mapped with K; C can be mapped with P; D can be mapped with L. its not like shifting all alphabets like shift cipher, it will be mapped singly of each character.
- Here A is mapped with V, so every instance of A is mapped with V.
1. Brute force attack is not possible because the key range is 2^88 or 26!.
1. Most frequently occuring character in ciphertext, corresponds to most frequently occuring character in plaintext. By using frequent letters adversary can perform the decryption. 

## **The One Time Pad :**

(vernam 1917)

- length of key is as long as length of message.
- The key is made up of random symbols.
- Cipher text is created just by XOR of message and key.
- in addition the key is to be used to encrypt and decrypt a single message and then that key is decarded.
- Each new message requires a new key of the same length as the new message
- C = E(K, M) = K (XOR) M
- M = D(K, C) = K (XOR) C

![Aspose Words 241bfbc5-17e8-46b7-8db9-3755e281e6f0 004](https://user-images.githubusercontent.com/57310710/185761150-bdf8c161-90c8-4c75-aeee-06729e926f68.png)

## **Affine Cipher:**

- In Affine cipher Encryption is E(x) = (a(x) + b) Mod 26
  - Here a and b are generated key pair. K = (a,b)
  - x is message that user gave.
  - a and b are randomly generated or can be given as a input in our code.
- In Affine cipher Decryption is x = a^-1(y - b) Mod 26
  - a^-1 or a inverse is calculated by Eulerphi Function.

### **Encryption in Affine cipher:**

1. First we take Input message from user and convert it into a List. 
1. We do indexing to the every letter in the message. example Indexing of a is 0, b is 1 etc…
1. Then we do the E(x) = (a(x) + b) Mod 26 to get the ciphertext.
1. Example :

![Aspose Words 241bfbc5-17e8-46b7-8db9-3755e281e6f0 005](https://user-images.githubusercontent.com/57310710/185761151-627f88cd-eaca-4b44-81fc-668d92059dfc.jpeg)

![Aspose Words 241bfbc5-17e8-46b7-8db9-3755e281e6f0 006](https://user-images.githubusercontent.com/57310710/185761152-10b35988-4433-4e8a-ac40-31fe980f4bed.png)
- **y = E(x)** 

### **Decryption in Affine cipher:**

1. First we take ciphertext which was generated by Encryption and we do indexing.
1. Then we do x = a^-1(y - b) Mod 26 to get the plaintext.
1. Example:

![Aspose Words 241bfbc5-17e8-46b7-8db9-3755e281e6f0 007](https://user-images.githubusercontent.com/57310710/185761153-76df537a-4a8f-4c84-8c8f-838352f700d1.jpeg)

## **Hill Cipher:**

- Hill cipher is a polygraphic substitution cipher based on linear algebra.Each letter is represented by a number modulo 26.
- To encrypt a message, each block of n letters (considered as an n-component vector) is multiplied by an invertible n × n matrix, against modulus 26.
- The matrix used for encryption is the cipher key, and it should be chosen randomly from the set of invertible n × n matrices (modulo 26).
- To decrypt the message, each block is multiplied by the inverse of the matrix used for encryption.

### **Encryption of Hill Cipher:**

1. ![Aspose Words 241bfbc5-17e8-46b7-8db9-3755e281e6f0 008](https://user-images.githubusercontent.com/57310710/185761154-987a5a04-10d6-47ba-8084-29f273a44ee3.png)
2. ![Aspose Words 241bfbc5-17e8-46b7-8db9-3755e281e6f0 009](https://user-images.githubusercontent.com/57310710/185761155-c4805a6e-ab51-4dcd-a5ee-2c10a1676100.png)
2. ![Aspose Words 241bfbc5-17e8-46b7-8db9-3755e281e6f0 010](https://user-images.githubusercontent.com/57310710/185761156-ef104f0e-507a-42b6-939a-d3b648d97156.png)

### **Decryption of Hill Cipher:**

1. To decrypt the message, we turn the ciphertext back into a vector, then simply multiply by the inverse matrix of the key matrix.
1. ![Aspose Words 241bfbc5-17e8-46b7-8db9-3755e281e6f0 011](https://user-images.githubusercontent.com/57310710/185761157-b0b3ba48-3b97-4687-ad45-a6e76dc8b014.png)
3. ![Aspose Words 241bfbc5-17e8-46b7-8db9-3755e281e6f0 012](https://user-images.githubusercontent.com/57310710/185761158-a2bad89f-b5bc-41e7-aae8-612558da5cd1.png)

![](Aspose.Words.241bfbc5-17e8-46b7-8db9-3755e281e6f0.013.png) ***Source:  <https://www.geeksforgeeks.org/hill-cipher/?ref=gcse>***

## **Vignere Cipher:**

- Encryption in Vignere Cipher is E(Message) = ( Message + Key) Mod 26.
- Key is random or user input in our code.
  - key is further converted to the pseudo random key (basically matching the length of Message).
- Decryption of Vignere Cipher is  Message = (E(Message) - Key) Mod 26.

### **Encryption of Vignere Cipher:**

1. Take the Message as a user input.
1. Convert the Message into a list and then convert the each letter into value by indexing and store it in list.
3. Then do the Encryption E(Message) = ( Message + Key) Mod 26. we will get the Ciphertext.


### **Decryption of Vignere Cipher:**

1. Convert the Ciphertext into a list and then convert the each letter using indexing and store in list.
1. Then do the Decryption Message = (E(Message) - Key) Mod 26. To get Plaintext.
Learning Cryptography: 11

 RSA - (Rivest Shamir Adleman):
------------------------------

1.  We need to pick p and q; Both p and q should be prime numbers. it is picked without any calculations.

2.  We need to compute N ; (p) *(q) = N.

3.  Then compute φ(N); φ(N) is coprimes between the 1 and N. (by doing (p - 1)*(q - 1) to get φ(N)).

4.  we need to choose e. By getting e we can continue to encrypt message. here is the twist, e is no chosen randomly.

    1.  to pick e we have 2 rules. first is e should be greater than 1 and less than φ(N)
    2.  second is e should be a Coprime with both N and φ(N).
5.  we need to choose d. By getting d we can decrypt the encrypted message. we can find d by :

    1.  d * e (Mod φ(N)) should equal to 1.
    2.  d is chosen according to he condition we stated above.

    ### RSA Encryption:

    1.  Get the Encryption key pair which is (e, N).
    2.  Do mathematical function ((Message)^e)(Mod N).
    3.  Then we get the ciphertext. which is huge number or list of numbers based on Message.

    ### RSA Decryption:

    1.  Get the Decryption pair which is (d, N).
    2.  Then compute, ((ciphertext)^d)(Mod N).
    3.  Then we get the Message which we encrypted before.

Diffie - Hellman key exchange:
------------------------------

-   Diffie - Hellman key exchange is used to get the symmetric cipher key for both the sender and receiver.
-   futher key is used to decrypt the encrypted message by the receiver.
-   Sending the key in any source lead to going to the hacker's hand, so we use the Diffie - Hellman key exchange to get key safely.
-   *Take Alice and Bob as a example.*

1.  First Alice and Bob has got their Private keys as example a and b respectively.
2.  we got g and n as a public variable which was established in the public channel. hacker can see g and n. They are random Integers.
3.  In Alice side ((g)^a)Mod n ; In Bob side ((g)^b)Mod n will be done simultaneously. lets be (g)^a)Mod n as (x) ; (g)^b)Mod n as (y).
4.  Now both x and y got exchange through the public channel. If hacker see this he/she may could only see the some random bits not the key.
5.  now in Alice side ((y)^a)Mod n , let it be as Sa; in Bob side ((x)^b)Mod n should be done, let it be as Sb. Now both Sa and Sb are same they are the public key which is used to encrypt and decrypt in symmetric cipher.
6.  Sa will be (g^(a * b)) Mod n and Sb will be (g^(a * b)) Mod n. we can see that both Sa and Sb was same, so this is the key.

[Learning_Cryptography.pdf](https://github.com/neerajchowdary889/learning-Cryptography/files/9387871/Learning_Cryptography.pdf)

