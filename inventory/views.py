from django.shortcuts import render
from .models import Product
from .forms import CreateForm
from reportlab.graphics.barcode import code128
from reportlab.pdfgen import canvas
from django.core.mail import EmailMessage
from django.contrib import messages


def home_view(request, *args, **kwargs):
    form = CreateForm
    if request.method == "POST":
        if Product.objects.filter(product_id__exact=request.POST['product_id']):

            # Make a pdf and write queried data to it
            selected_product = str(Product.objects.filter(product_id__exact=request.POST['product_id']).first())
            slab = canvas.Canvas('queried.pdf')
            slab.drawString(120, 600, selected_product)
            barcode = code128.Code128(selected_product)
            barcode.drawOn(slab, 100, 720)
            slab.showPage()
            slab.save()

            # Send the e-mail
            mail = EmailMessage(
                # Title of the email
                'Insert the title of the email here',
                # Message of the email
                'Insert the message of the email here',
                # From WHO the message was sent from.
                # Needs to be the same email as in the settings.py email configuration
                'Insert email address here',
                # To whom the message is sent
                ['Insert email address here'])
            mail.attach_file('queried.pdf')
            mail.send()
        messages.success(request, 'Query success ')

    return render(request, "home.html", {'form': form})


def database_view(request, *args, **kwargs):
    products = Product.objects.all()
    return render(request, "database.html", {'products': products})
