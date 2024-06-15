with open("D:\\Mail Merger\\names.txt", "r") as names_file:
    with open("D:\\Mail Merger\\body.txt", "r") as body_file:
        body = body_file.read()

        for name in names_file:
            mail = "Hello " + name.strip() + ",\n\n" + body

            with open("D:\\Mail Merger\\" + name.strip() + ".txt", "w") as mail_file:
                mail_file.write(mail)
print("Mails written successfully")