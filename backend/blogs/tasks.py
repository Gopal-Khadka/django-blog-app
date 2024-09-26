from django.core.mail import send_mail
from blog_home.celery import app


@app.task
def add_num(*args):
    sum_val = sum(args)
    print(sum_val)
    return sum_val

@app.task
def send_email():
    return send_mail(
        'Subject here',
        'Here is the message.',
        'your_email@gmail.com',
        ['recipient@example.com'],
        fail_silently=False,
    )
    
