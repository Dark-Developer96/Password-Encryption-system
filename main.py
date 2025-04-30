import random
import os
import time

file = "data.txt"
if not os.path.exists(file):
    with open(file, "w") as f:
        f.write("")
mpass_file = "mpass.txt"
if not os.path.exists(mpass_file):
    with open(mpass_file, "w") as f:
        f.write("")


def greet(func):
    def wrapper(*args, **kwargs):
        print("Please wait while the task is being processed...")
        time.sleep(0.5)
        result = func(*args, **kwargs)
        print("Task completed.")
        return result

    return wrapper


class Pass:
    def compare_mpass(self, mpass):
        with open(mpass_file, "r") as f:
            for line in f:
                if mpass.strip() == self.decrypt(line.strip()):
                    return True
        return False

    @greet
    def entry(self, web, usn, passw):
        self.usn = usn
        self.passw = passw
        self.web = web
        with open(file, "a") as f:
            f.write(
                f"{self.encrypt(web)} : {self.encrypt(usn)} : {self.encrypt(passw)}\n"
            )

    def encrypt(self, text: chr):
        encrypted = ""
        for char in text:
            if char.isalpha():
                encrypted += chr(ord(char) + 3)
            elif char.isdigit():
                encrypted += chr(ord(char) + 3)
            elif char == " " or char == ":" or char == "\n":
                encrypted += char
            else:
                encrypted += chr(ord(char) + 3)
        return encrypted

    def decrypt(self, text: chr):
        decrypted = ""
        for char in text:
            if char.isalpha():
                decrypted += chr(ord(char) - 3)
            elif char.isdigit():
                decrypted += chr(ord(char) - 3)
            elif char == " " or char == ":" or char == "\n":
                decrypted += char
            else:
                decrypted += chr(ord(char) - 3)
        return decrypted

    def check_mpass(self):
        l = []
        with open(mpass_file, "r") as f:
            for lines in f:
                l.append(self.decrypt(lines.strip()))
        return bool(l)

    @greet
    def add_mpass(self, mpass):
        if not self.check_mpass():
            with open(mpass_file, "a") as f:
                f.write(self.encrypt(mpass.strip()) + "\n")

    @greet
    def display(self, mpass):
        with open(mpass_file, "r") as f:
            for line in f:
                if self.decrypt(line.strip()) == mpass.strip():

                    with open(file, "r") as f1:
                        for line in f1:
                            l = line.split(":")
                            print(
                                f"Website: {self.decrypt(l[0].strip())}\t Username: {self.decrypt(l[1].strip())}\t Password: {self.decrypt(l[2].strip())}"
                            )

    @greet
    def gen(self, len):
        characters = (
            "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789@*#!?"
        )
        generated_pass = ""
        for i in range(len):
            generated_pass += random.choice(characters)
        return generated_pass

    @greet
    def delete(self, arg):
        l = []
        with open(file, "r") as f:
            for i in f:
                if arg.lower() not in self.decrypt(i).lower():
                    l.append(i)

        with open(file, "w") as f:
            for line in l:
                f.write(line)

    @greet
    def search(self, arg):
        l = []
        results = []
        with open(file, "r") as f:
            for line in f:
                l.append(self.decrypt(line))

        for items in l:
            if arg.lower() in items.lower():
                a = items.split(":")
                results.append(
                    f"Website : {a[0].strip()} Username : {a[1].strip()}  Password : {a[2].strip()}"
                )
        if results:
            return "\n".join(results)
        else:
            return "Your given argument is nowhere to be found"


Admin = Pass()


def main():
    while True:
        print("Welcome To Password generator")
        print("Enter 1 to Save Passwords")
        print("Enter 2 to add a master password")
        print("Enter 3 to display all saved passwords")
        print("Enter 4 to generate a password of custom length")
        print("Enter 5 to delete a password")
        print("Enter 6 to search a password via webiste/username")
        print("Enter 7 to exit")
        x = int(input("Enter your choice:\n"))
        if x == 1:
            mpass = input("Enter the Mpass:\n")
            if Admin.compare_mpass(mpass):
                web = input("Enter the website name:\n")
                usn = input("Enter the username:\n")
                passw = input("Enter the password:\n")
                Admin.entry(web, usn, passw)
            else:
                print("Incorrect Master Password")

        elif x == 2:
            if not Admin.check_mpass():
                mpass = input("Enter the master password:\n")
                Admin.add_mpass(mpass)
            else:
                print("Sorry you already have a master password")
        elif x == 3:
            if Admin.check_mpass():
                mpass = input("Enter the master password:\n")
                if Admin.compare_mpass(mpass):
                    Admin.display(mpass)
                else:
                    print("Incorrect Mpass")
        elif x == 4:
            length = int(input("Enter the custom length of your desired password:\n"))
            print(f"Your custom password is {Admin.gen(length)}")
        elif x == 5:
            if Admin.check_mpass():
                mpass = input("Enter the master password:\n")
                if Admin.compare_mpass(mpass):
                    Admin.display(mpass)
                    arg = input("Enter the Website/Username to delete the password:\n")
                    Admin.delete(arg)
                else:
                    print("Incorrect Mpass")
            else:
                print("You don't have a master password")
        elif x == 6:
            if Admin.check_mpass():
                mpass = input("Enter the master password:\n")
                if Admin.compare_mpass(mpass):
                    arg = input("Enter the website/username to search:\n")
                    print(Admin.search(arg))
                else:
                    print("Incorrect Mpass")
            else:
                print("You don't have a master password")

        elif x == 7:
            break
        else:
            print("Wrong input")


main()
