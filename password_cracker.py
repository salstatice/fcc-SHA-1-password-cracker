import hashlib

def crack_sha1_hash(hash, use_salts=False):
    with open('top-10000-passwords.txt', newline='') as common_passwords:
        password_list = common_passwords.read().split('\n')
    with open('known-salts.txt', newline='') as common_salts:
        salt_list = common_salts.read().split('\n')

    rainbow_table = {}
    for word in password_list:
        if (use_salts):
            for salt in salt_list:
                salted_word_1 = salt + word
                hash_word_1 = hashlib.sha1(salted_word_1.encode()).hexdigest()
                rainbow_table[hash_word_1] = word

                salted_word_2 = word + salt
                hash_word_2 = hashlib.sha1(salted_word_2.encode()).hexdigest()
                rainbow_table[hash_word_2] = word
        else:
            hash_word = hashlib.sha1(word.encode()).hexdigest()
            rainbow_table[hash_word] = word

    password = rainbow_table.get(hash, "PASSWORD NOT IN DATABASE")

    return password