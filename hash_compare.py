"""
Compare two checksums to see if they match.
"""

def compare_hashes():

    hash1 = input("Enter the first digest: ").upper()
    hash2 = input("Enter the second digest: ").upper()

    print() # Blank space for readability
    print("Hash #1: " + hash1)
    print("Hash #2: " + hash2)

    if hash1 == hash2:
        print("The digests match")
    else:
        print("The digests do NOT match!")

def main():

    compare_hashes()

main()
