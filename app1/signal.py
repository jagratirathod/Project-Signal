from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Blog
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail





@receiver(post_save, sender=Blog)
def send_blog_email(sender, instance, created, **kwargs):
    if created:
        message = Mail(
            from_email='from_email@example.com',
            to_emails='to@example.com',
            subject='New Blog post',
            html_content = """
            <html>
            <head></head>
            <body>
                <a href="http://www.examplesite.com">Link Text</a>
            </body>
            </html>
            """)
            
        try:
            sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            response = sg.send(message)

        except Exception as e:
            response =e.message
            print(e.message)