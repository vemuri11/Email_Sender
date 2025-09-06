import singleEmailSend

# bulk email sender function
def bulk_email_send(emails:list, subject:str, body:str):
    for email in emails:
        try:
            singleEmailSend.single_email_send(
                to_email=email,
                subject=subject,
                body=body
                
            )
            
        except:
            print("Email send field")