from django.shortcuts import render
from django.http import JsonResponse
import requests
from .models import Contact


BOT_TOKEN = '7651287045:AAEd1M-1FXqTHu4kOJLcx6lY1hQYR5m9xNQ'
CHAT_ID = ' 7406772742'  # admin yoki o'zingizning ID


def main_page(request):
    return render(request, 'index.html')



def contact_view(request):
    return  JsonResponse({"message": "Boglanish uchun: @N_khabibullayev_08"})




# def contact_view(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             # Form ma'lumotlarini olish
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             message = form.cleaned_data['message']

#             # Telegramga yuborish
#             text = f"📥 *Yangi murojaat!*\n\n👤 Ism: {name}\n📧 Email: {email}\n📝 Xabar:\n{message}"
#             url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
#             payload = {
#                 'chat_id': CHAT_ID,
#                 'text': text,
#                 'parse_mode': 'Markdown'
#             }
#             response = requests.post(url, data=payload)

#             if response.status_code == 200:
#                 return render(request, 'contact.html', {'form': ContactForm(), 'success': True})
#             else:
#                 return render(request, 'contact.html', {'form': form, 'error': 'Telegramga yuborilmadi'})

#     else:
#         form = ContactForm()
#     return render(request, 'contact.html', {'form': form})

# def main_page(request):
#     return render(request, 'index.html')  # bu faqat asosiy sahifa

# def contact_view(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             # Formni o'qish va Telegramga yuborish
#             ...
#             return render(request, 'contact.html', {'form': ContactForm(), 'success': True})
#     else:
#         form = ContactForm()
#     return render(request, 'contact.html', {'form': form})
# # Note: The above code includes a duplicate definition of `main_page` and `contact_view`.
