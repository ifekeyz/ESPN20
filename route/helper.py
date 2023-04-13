from django.core.mail import send_mail
import uuid
from django.conf import settings

def send_forget_password_maill(email,token):
    # token = str(uuid.uuid4())
    subject = "Your forget password link"
    message = f"Hey,{{user.username}} clink on the link to reset your password\n http://127.0.0.1:8000/changePassword/{token}"
    email_form = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message,email_form,recipient_list)

    return True