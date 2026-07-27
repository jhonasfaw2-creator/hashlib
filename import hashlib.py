import hashlib

def create_hashlist(plain_text_words):
    """
    Generates a dictionary mapping MD5 hashes to their plain text originals.
    """
    hashlist = {}
    for word in plain_text_words:
        # Convert the string to bytes, then compute the MD5 hex digest
        md5_hash = hashlib.md5(word.encode('utf-8')).hexdigest()
        hashlist[md5_hash] = word
    return hashlist

def lookup_hash():
    # Example wordlist used to build the internal lookup table
    sample_words = [
        "password",
        "123456",
        "admin",
        "hello",
        "letmein",
        "welcome"
    ]
    
    # Step 2: Build the hashlist table
    hash_table = create_hashlist(sample_words)
    
    # Step 1: User inputs an MD5 hash
    user_input = input("Enter MD5 Hash: ").strip().lower()
    
    # Step 3: Match and output result
    if user_input in hash_table:
        print(f"Match found! Plaintext: {hash_table[user_input]}")
    else:
        print("No matching hash identified. Please try again.")

if __name__ == "__main__":
    lookup_hash()