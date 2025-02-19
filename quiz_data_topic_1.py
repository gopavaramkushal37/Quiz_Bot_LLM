
mcq_questions = ["What is the block size typically used in symmetric encryption algorithms like DES, 3DES, and AES?",
                 "Which encryption algorithm among the following uses a Feistel structure?",
                 "What is the relationship between the ciphertext and the secret key in symmetric encryption?",
                 "What is the primary factor that determines the security of symmetric encryption?",
                 "In symmetric encryption, why is it assumed that the algorithm does not need to be kept secret?",
                 "What is the purpose of the subkey generation algorithm in a symmetric block cipher?",
                 "Which aspect of security involves ensuring the accuracy and reliability of data within the system.",
                 "What is the primary goal of preserving the availability of an automated information system?",
                 "In the context of security, what does confidentiality aim to prevent",
                 "Which components fall under the category of information system resources?",
                 "What are the three main objectives mentioned in the context of application objectives for an automated information system?",
                 "What is a characteristic of the mechanisms used to meet security requirements?",
                 "What is emphasized when developing security mechanisms?",
                 "What is a common trait of security mechanisms, according to the text?",
                 "When developing security mechanisms, what aspect must always be considered?",
                 "What is mentioned about the complexity of security mechanisms?",
                 "When should security be included in the design of a new system?"]

mcq_choices = [["64 bits", "32 bits", "28 bits", "256 bits"],
               ["Data Encryption Standard (DES)", "Triple DES (3DES)", "Advanced Encryption Standard (AES)", "All of the above"],
               ["Ciphertext depends only on the plaintext", "Ciphertext depends only on the secret key", "Ciphertext depends on both the plaintext and the secret key", "Ciphertext is independent of both plaintext and secret key"],
               ["Complexity of the algorithm", "Secrecy of the key", "Availability of ciphertext", "Use of multiple algorithms"],
               ["The algorithm is publicly available", "The algorithm is complex", "The algorithm changes frequently", "The algorithm is part of the key"],
               ["Encryption of plaintext", "Generation of ciphertext", "Decryption of ciphertext", "Generation of round-specific keys"],
               ["Confidentiality", "Availability", "Integrity", "Telecommunications"],
               ["Preventing unauthorized access", "Ensuring data accuracy", "Minimizing downtime", "Controlling telecommunications"],
               ["Unauthorized access or disclosure of sensitive information", "Data accuracy and reliability", "System availability", "Telecommunications errors"],
               ["Hardware, Software, Firmware", "Data, Information, Telecommunications", "Integrity, Availability, Confidentiality", "Automated, Information, System"],
               ["Integrity, Availability, Confidentiality", "Data, Software, Hardware", "Telecommunications, Security, Protection", "Confidentiality, Reliability, Accessibility"],
               ["Simplicity", "Complexity", "Subtlety", "Commonality"],
               ["Potential attacks", "Ease of development", "Intuitive reasoning", "Algorithm efficiency"],
               ["Straightforward", "Predictable", "Counterintuitive", "Simple"],
               ["Potential attacks", "Algorithm efficiency", "Ease of development", "Subtle reasoning"],
               ["They are always straightforward", "They involve simple reasoning", "They can be quite complex", "They are predictable"],
               ["Only after system implementation", "During system testing", "As part of system design", "After discovering vulnerabilities"]]

mcq_correct_answers = ["64 bits", "All of the above", "Ciphertext depends on both the plaintext and the secret key", "Secrecy of the key", "The algorithm is publicly available", "Generation of round-specific keys", "Integrity", "Minimizing downtime", "Unauthorized access or disclosure of sensitive information", "Hardware, Software, Firmware", "Integrity, Availability, Confidentiality", "Subtlety", "Potential attacks", "Counterintuitive", "Potential attacks", "They can be quite complex", "As part of system design", "Security vulnerabilities"]

mcq_sources = ["Lecture slide:5, pg:4", "Lecture slide:5, page : 4", "Textbook:Network Security Essentials Applications and Standards Sixth edition William Stallings, Page:46", "Textbook:Network Security Essentials Applications and Standards Sixth edition William Stallings, Page:47", "Textbook:Network Security Essentials Applications and Standards Sixth edition William Stallings, Page:47", "Textbook:Network Security Essentials Applications and Standards Sixth edition William Stallings, Page:50", "Lecture Slide 1, Page :5", "Lecture Slide 1, Page :5", "Lecture Slide 1, Page :5", "Lecture Slide 1, Page :5", "Lecture Slide 1, Page :5", "Lecture Slide 2 Page :4", "Lecture Slide 2 Page :4", "Lecture Slide 2 Page :4", "Lecture Slide 2 Page :4", "Lecture Slide 2 Page :4", "Lecture Slide 3 Page :3"]


true_false_questions = ["In a symmetric encryption scheme, the same key is used for both encryption and decryption."," The primary security problem in symmetric encryption is maintaining the secrecy of the algorithm.","The complexity of the subkey generation algorithm and round function in a symmetric block cipher does not affect the difficulty of cryptanalysis.","A larger block size in a symmetric block cipher typically results in greater security but at the cost of reduced encryption/decryption speed.","DES as an example, is known for its easily analyzed functionality, contributing to a higher level of assurance in its strength.","Data confidentiality ensures that private or confidential information is intentionally disclosed to unauthorized individuals.","Privacy involves individuals controlling or influencing the collection and storage of information related to them, including who may access or disclose that information.","Data confidentiality is not relevant when dealing with student grade information.","Privacy encompasses decisions about who can access and disclose information about an individual.","Data confidentiality and privacy are unrelated concepts and do not overlap in any way.","Eavesdropping involves altering the data being transmitted.","The goal of eavesdropping is to release the message contents.","Traffic analysis is a type of eavesdropping that involves actively modifying the data.","Eavesdropping is very difficult to detect because it often involves altering the data being transmitted.","Users prioritize convenience over security.","If a security system is difficult to use, users are likely to avoid using it.","Users will not attempt to find ways to subvert security systems for their convenience.","Programmers are immune to making mistakes in their code."]

true_false_correct_answers = ["True","False","False","True","False","False","True","False","True","False","False","True","False", "True","True","True","False","False"]

true_false_sources = ["Textbook:Network Security Essentials Applications and Standards Sixth edition William Stallings, Page:46","Textbook:Network Security Essentials Applications and Standards Sixth edition William Stallings, Page:46","Textbook:Network Security Essentials Applications and Standards Sixth edition William Stallings, Page:50","Textbook:Network Security Essentials Applications and Standards Sixth edition William Stallings, Page:48","Textbook:Network Security Essentials Applications and Standards Sixth edition William Stallings, Page:52","Lecture Slide 1 Page :6","Lecture Slide 1 Page :6","Lecture Slide 1 Page :6","Lecture Slide 1 Page :6","Lecture Slide 1 Page :6","Lecture Slide 2 Page :9","Lecture Slide 2 Page :9","Lecture Slide 2 Page :9","Lecture Slide 2 Page :9","Lecture Slide 3 Page :4","Lecture Slide 3 Page :4","Lecture Slide 3 Page :4","Lecture Slide 3 Page :4"]

open_ended_questions = ["What is the key size used in DES algorithm?"," What is the size of plain text ?","What is the structure first described by Horst Feistel commonly used in symmetric block encryption algorithms like DES?","In symmetric encryption, what term is used for running the encryption algorithm in reverse to produce the original plaintext?","The number of rounds performed in DES algorithm?"," What assures that data and programs are changed only in a specified and authorized manner?","What ensures that a system performs its intended function in an unimpaired manner free from unauthorized manipulation?"," In the context of a hospital patient's allergy information, what assures that the data remains unchanged and is modified only in an authorized way?","Name a key aspect of information security that involves the authorized and specified modification of data."," In the context of system security, what guarantees that a system operates as intended without unauthorized interference?","What is the term for assuring that data in transmitted packets is changed only in an authorized manner","What type of attack involves the repetition of previously captured data?","What is the term for the action of altering the content of messages during transmission?","What type of attack aims to disrupt or degrade the normal functioning of a system or network?"," What is the term for an attack in which an unauthorized entity pretends to be a legitimate user or system?"]

open_ended_correct_answers = ["56 bits","128 bits","Feistel structure","Decryption","16","Integrity","SystemIntegrity","DataIntegrity","Authorization","System Integrity", "Integrity","Replay","Modification","Denial", "Masquerade"]

open_ended_sources = ["Lecture slide:6, page:3"," Lecture slide:6, page:3","Textbook:Network Security Essentials Applications and Standards Sixth edition William Stallings, Page:50","Textbook:Network Security Essentials Applications and Standards Sixth edition William Stallings, Page:47","Lecture slide:6, page:3","Lecture Slide 1 Page :7","Lecture Slide 1 Page :7","Lecture Slide 1 Page :7","Lecture Slide 1 Page :7","Lecture Slide 1 Page :7","Lecture Slide 1 Page :7","Lecture Slide 2 Page :10","Lecture Slide 2 Page :10","Lecture Slide 2 Page :10","Lecture Slide 2 Page :10"]



