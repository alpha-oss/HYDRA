import string
import random

if __name__ == "__main__":
    s1 = string.ascii_lowercase
    #print(s1)
    s2 = string.ascii_uppercase
    #print(s2)
    s3 = string.digits
    # print(s3)
    s4 = string.punctuation
    #print(s4)

    plen = int(input("Enter the password length:"))
    p = []
    p.extend(list(s1))
    p.extend(list(s2))
    p.extend(list(s3))
    p.extend(list(s4))

    #random.shuffle(p) - this can be one option to generate password
    print("YOUR NEW PASSWORD IS :")
    #print("".join(p[0:plen]))
    #This is another alternative to generate password.
    print("".join(random.sample(p,plen)))
    