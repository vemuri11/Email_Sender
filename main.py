import singleEmailSend
import bulkEmailSend




if __name__ == "__main__":
    subject = input("Enter subject:")
    body = input("Enter body:")
    choice = int(input("Select your operation \n 1. Single email sender \n 2. Bulk email sender"))
    if choice==1:
        email = input("Please enter recevier email address").strip()
        singleEmailSend.single_email_send(
        to_email=email,
        subject=subject,
        body=body 
    )
    elif choice == 2:
        emails = input("Enter emails seperated by comma:").split(",")
        bulkEmailSend.bulk_email_send(
            emails=emails,
            subject=subject,
            body=body
        )

