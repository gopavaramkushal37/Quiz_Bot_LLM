# MCQ questions, choices, and correct answers
mcq_questions = [
    "What is the purpose of a public key in public-key cryptography? ",
    " What is the function of the private key in public-key cryptography? ",
    " What property do public keys and private keys in public-key cryptography share?",
    " What mathematical concept is commonly used in public-key cryptography? ",
    "What is the primary characteristic of public-key cryptography? ",
    "In public-key cryptography, what is the purpose of the KeyGen() function?",
    "In the context of public-key encryption, what does the term correctness refer to?",
    "What is the condition for selecting the encryption key (e) in RSA?",
    "What equation is solved to find the decryption key (d) in RSA?",
    "Which key must be kept secret in the key pair generation process in RSA?",
    "What is the primary defence against mathematical attacks on RSA?",
    "Which type of attack depends on the running time of the decryption algorithm in RSA?",
    "How can chosen ciphertext attacks be mitigated in RSA?",
    "How are the exponents e and d related in RSA key generation?",
    "What is a crucial requirement for the primes p and q in RSA key generation?",
    "What condition must be satisfied for the RSA algorithm to be considered satisfactory for public-key encryption?",
    "Which mathematical expression correctly represents the encryption process in the RSA algorithm?",
    "How does user A decrypt the received ciphertext C in the RSA algorithm?"
]

mcq_choices = [
    ["Only known by the person", "Used for encryption and known to everybody",
     " Used for decryption and only known by the person", "Shared among all users in a network"],

    ["Used for encryption and known to everybody", "Only known by the person",
     "Used for decryption and only known by the person", "Shared among all users in a network"],

    ["Both are known to everybody", "Both are used for encryption", "Both are used for decryption",
     "Each public key corresponds to one private key"],

    ["Symmetric key", "XOR operations", "Number theory", "Bit shifts"],

    ["Both parties share the same key", "Each person has two keys: public and private",
     "Keys are kept secret from everyone", "Only one key is used for encryption and decryption"],

    ["Encrypt a message", "Generate public and private keypair", "Verify a signature", "Decrypt a ciphertext"],

    ["The speed of encryption/decryption", "The accuracy of the encryption algorithm",
     "The ability to recover the original message after decryption", "The security of the public key"],

    ["e must be equal to n", "1 < e < ø(n)", "e should be a prime number", "e must be greater than p and q"],

    ["d=e mod ø(n)", "d= e−ø(n)", "ed=1 mod ø(n)", "d=n−e"],

    ["Encryption key (e)", "Modulus (n)", "Private decryption key (d)", "Public key (pk)"],

    ["Increased key size", "Improved encryption algorithm", "Enhanced decryption speed", "Randomized padding"],
    ["Mathematical attacks", "Timing attacks", " Chosen ciphertext attacks", "Frequency analysis attacks"],
    ["Increasing key size", "Using a faster decryption algorithm", "Employing random padding",
     "Selecting suitable primes for key generation"],
    ["They are always equal", "They have no mathematical relationship", "They are inverses",
     "They are determined by the modulus n"],
    ["They must be easily derived from the modulus n=p.q", "They must be identical", "They must be determined randomly",
     "They must be smaller than the modulus"],
    ["It is possible to find values of e, d, n such that M^ed mod n = M for all M < n",
     "It is relatively easy to calculate M^e and C^d for all values of M < n",
     "It is infeasible to determine d given e and n", "All of the above"],
    ["C = M^e mod n", "C = M^d mod n", "C = M^e + n", "C = M * d"],
    ["M= C^e mod n", "M = C^d mod n", "M = C^-1 mod n", "M = C mod n"]
]

mcq_correct_answers = [
    "Used for encryption and known to everybody",
    " Used for decryption and only known by the person",
    "Each public key corresponds to one private key",
    "Number theory",
    "Each person has two keys: public and private",
    "Generate public and private keypair",
    "The ability to recover the original message after decryption",
    "1 < e < ø(n)",
    "ed=1 mod ø(n)",
    "Private decryption key (d)",
    "Increased key size",
    "Timing attacks",
    "Employing random padding",
    "They are inverses",
    "They must be determined randomly",
    "All of the above",
    "C = M^e mod n",
    "M = C^d mod n"

]
mcq_sources = [
    " Lecture slide 11, page no: 8",
    " Lecture slide 11, page no: 8",
    " Lecture slide 11, page no: 8",
    "  Lecture slide 11, page no: 8",
    "  Lecture slide 11, page no: 8",
    "  Lecture slide 12, page no: 8",
    "  Lecture slide 12, page no: 8",
    "  Lecture slide 13, page no: 5",
    "  Lecture slide 13, page no: 5",
    "  Lecture slide 13, page no: 5",
    "  Lecture slide 14, page no: 7",
    " Lecture slide 14, page no: 7",
    " Lecture slide 14, page no: 7",
    " Lecture slide 14, page no: 5",
    "  Lecture slide 14, page no: 5",
    "Network Security Essentials Applications and Standards Sixth edition William Stallings, Page no: 102",
    "Network Security Essentials Applications and Standards Sixth edition William Stallings, Page no: 102",
    "Network Security Essentials Applications and Standards Sixth edition William Stallings, Page no: 102",
    "Network Security Essentials Applications and Standards Sixth edition William Stallings, Page no: 102"

]

# true/false questions
true_false_questions = [
    "Public-key schemes use only one key per person. ",
    "In public-key cryptography, the private key is known to everyone. ",
    "Every public key in public-key cryptography corresponds to a unique private key. ",
    "Public-key cryptography and symmetric-key cryptography have the same approach to key management. ",
    "Digital signatures are a public-key application that primarily provides encryption and decryption services.",
    "Public-key algorithms are only suitable for encryption/decryption purposes and cannot be used for digital signatures or key exchange.",
    "Digital signatures, a public-key application, are primarily used for providing confidentiality to messages.",
    "In RSA, the system modulus, n, is computed as the product of two random prime numbers, p and q.",
    "In RSA, the function, ø(n), is defined as (p+1)(q+1).",
    "In RSA, the decryption key, d, is computed as d = e^(-1) mod ø(n).",
    "Increasing the key size in RSA provides defence against timing attacks",
    "Chosen ciphertext attacks can be mitigated by using a large key size in RSA.",
    "The primary defence against timing attacks in RSA is the use of specialized hardware accelerators.",
    "In RSA key generation, should users select primes  p and q that are easily derived from the modulus n=p.q",
    "It is recommended to use small prime numbers for p and q in RSA key generation",
    "In a RSA public-key encryption system, the private key d cannot be feasibly determined with knowledge of the public key (e,n).",
    "The public key for encryption in RSA algorithm is {d, n}.",
    "The values of p and q must be prime numbers in the RSA encryption algorithm.",
    "The modulus n (product of p and q) is used for both encryption and decryption in RSA."
]

true_false_correct_answers = [
    False, False, True, False, False, False, False, True, False, True, False, False, False, False, False, True, False,
    True, True
]

true_false_sources = [
    "Lecture slide 11, page no: 8",
    "  Lecture slide 11, page no: 8",
    " Lecture slide 11, page no: 8",
    " Lecture slide 11, page no: 8",
    "  Lecture slide 12, page no: 11",
    "  Lecture slide 12, page no: 11",
    " Lecture slide 12, page no: 11",
    "  Lecture slide 13, page no: 5",
    " Lecture slide 13, page no: 5",
    " Lecture slide 13, page no: 5",
    " Lecture slide 14, page no: 7",
    "  Lecture slide 14, page no: 7",
    " Lecture slide 14, page no: 7",
    "  Lecture slide 14, page no: 5",
    "Lecture slide 14, page no: 5",
    "Network Security Essentials Applications and Standards Sixth edition William Stallings, Page no: 102",
    "Network Security Essentials Applications and Standards Sixth edition William Stallings, Page no: 102",
    "Network Security Essentials Applications and Standards Sixth edition William Stallings, Page no: 102",
    "Network Security Essentials Applications and Standards Sixth edition William Stallings, Page no: 102"

]

# Open-ended questions and correct answers
open_ended_questions = [
    " What is the public key used for in public-key cryptography?",
    " How many keys does each person have in public-key cryptography?",
    " What is kept confidential in public-key cryptography?",
    "In public-key systems, what is freely distributed to everyone?",
    "What does the Enc() function do in public key encryption?",
    "What is the main purpose of digital signatures in public key cryptography?",
    "Which property ensures that decrypting a ciphertext results in the original message?",
    "What information is included in the public encryption key (pk)",
    "What information is kept secret in the private decryption key (sk)?",
    "What is the primary defence mechanism against mathematical attacks in RSA?",
    "What aspect of the decryption algorithm do timing attacks rely on, in RSA?",
    "How can chosen ciphertext attacks be prevented in RSA?",
    "What is the relationship between the exponents e and d in RSA key generation?",
    "What kind of test is typically used to check the primality of guessed numbers in RSA key generation?",
    "What is the primary purpose of the private key in RSA?",
    "What ensures the confidentiality of the message during transmission in RSA?",
    "What is calculated as the multiplicative inverse of e , modulo f(n)?",
    "What property should e have in relation to f(n)?"
]

open_ended_correct_answers = [
    " Encryption",
    " Two",
    " Private key",
    " Public key",
    "Encrypts",
    "Authentication",
    "Correctness",
    "e, n",
    "d, p, q",
    "Key size",
    "Running time",
    "Padding",
    "Inverses",
    "Probabilistic",
    "Decryption",
    "Private key (d)",
    "d",
    "relatively prime"
]

open_ended_sources = [
    " Lecture slide 11, page no: 8",
    " Lecture slide 11, page no: 8",
    " Lecture slide 11, page no: 8",
    " Lecture slide 11, page no: 8",
    " Lecture slide 12, page no: 8",
    " Lecture slide 12, page no: 11",
    "Lecture slide 12, page no: 8",
    "Lecture slide 13, page no: 5",
    "Lecture slide 13, page no: 5",
    "Lecture slide 14, page no: 7",
    "Lecture slide 14, page no: 7",
    "Lecture slide 14, page no: 7",
    "Lecture slide 14, page no: 5",
    "Lecture slide 14, page no: 5",
    "Network Security Essentials Applications and Standards Sixth edition William Stallings, Page no: 102",
    "Network Security Essentials Applications and Standards Sixth edition William Stallings, Page no: 102",
    "Network Security Essentials Applications and Standards Sixth edition William Stallings, Page no: 102",
    "Network Security Essentials Applications and Standards Sixth edition William Stallings, Page no: 102"

]
