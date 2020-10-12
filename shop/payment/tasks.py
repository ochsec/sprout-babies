from io import BytesIO
from celery import task
import weasyprint
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from orders.models import Order

@task
def payment_completed(order_id):
    """
    Task to send an email notification when an order is
    successfully created.
    """
    order = Order.objects.get(id=order_id)

    # create invoice email
    subject = f"Sprout Babies - Order Number {order.id}"
    message = "Thank you for your purchase with Sprout Babies! Please \
    find attached the receipt for your recent purchase."
    email = EmailMessage(subject,
        message,
        "admin@sproutbabies.com",
        [order.email])

    # generate PDF
    html = render_to_string("orders/order/pdf.html", {'order': order})
    out = BytesIO()
    stylesheets = [weasyprint.CSS(settings.STATIC_ROOT + 'css/pdf.css')]
    weasyprint.HTML(string=html).write_pdf(out, stylesheets=stylesheets)

    # attach PDF file
    email.attach(f'order_{order.id}.pdf', out.getvalue(), 'application/pdf')

    # send email
    email.send()
    