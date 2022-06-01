from twilio.rest import Client
account_sid = 'AC022a414e9daa617a405141603f0f3733' # Account SID
auth_token = '1337b7952872d6ab3f43551b5517870b' # Auth Token
client = Client(account_sid,auth_token)

def send_sms(user_code,phone_number):
    message = client.messages.create(
                                 body=f'Assalom alaykum, sizning tasdiqlash kodingiz: {user_code}',
                                 from_='+19106657763',
                                 to=f'{phone_number}')