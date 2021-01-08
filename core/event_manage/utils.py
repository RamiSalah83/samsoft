# Download the helper library from https://www.twilio.com/docs/python/install

from twilio.rest import Client



# account_sid = "ACd9c1171a2f222163a125b83bc79a088d"
# auth_token = "10e4e67fb0e9a29da0ed13cacbcda6cb"
# client = Client(account_sid, auth_token)
# def send_whatsapp_messages(body,to):
#     message = client.messages.create(
#             #media_url=['https://images.unsplash.com/photo-1545093149-618ce3bcf49d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=668&q=80'],
#             from_='whatsapp:+14155238886',
#             body=body,
#             to= f'whatsapp:{to}'
#         )

#     print(message.sid)


#for whatsapp
# account_sid = "ACd9c1171a2f222163a125b83bc79a088d"
# auth_token = "10e4e67fb0e9a29da0ed13cacbcda6cb"
# client = Client(account_sid, auth_token)
# def twilio_send_whatsapp(body,to):
#     message = client.messages.create(
#             from_='whatsapp:+14155238886',
#             body=body,
#             to= f'whatsapp:{to}'
#         )

#     print(message.sid)



#for sms
account_sid = "AC1ccec2f3b5f799708ef740dce3340264"
twilio_phone_number = "Phil"
auth_token = "35f995eb90907231fe8c991dc193392b"
client = Client(account_sid, auth_token)
def twilio_send_sms(body,to):
    message = client.messages.create( 
                              from_='+12679301615',  
                              body=body,      
                              to=f'+{to}' 
                          ) 
 
    print(message.sid)


 
 
def twilio_send_whatsapp(body,to):
    message = client.messages.create( 
                                from_='whatsapp:+201201200129',  
                                body='Your appointment is coming up on July 21 at 3PM',      
                                to='whatsapp:+201200553380'
                            ) 
    
    print(message.sid)
















+12053013431

#+12053013431


# from nexmo import Sms

# NEXMO_API_KEY="2a456ef0"
# NEXMO_API_SECRET="F4AG4ieSVrbd4yka"
# sms = Sms(key=NEXMO_API_KEY, secret=NEXMO_API_SECRET)
# def send_sms_messages(to):
#     sms.send_message({
#                 "from": "NEXMO_BRAND_NAME",
#                 "to": to,
#                 "text": "A text message sent using the Nexmo SMS API",
#     })



# import nexmo

# client = nexmo.Client(key='45833284', secret='rUfMuKUv2Y0KPnWe')
# def send_sms_messages_auto(body,to):
#     client.send_message({
#         'from': 'Vonage APIs',
#         'to': to,
#         'text': body,
#         'type': 'unicode',
#     })   


# import nexmo

# client = nexmo.Client(key='2a456ef0', secret='F4AG4ieSVrbd4yka')
# def send_sms_messages_auto(body,to):
#     client.send_message({
#         'from': 'Vonage APIs',
#         'to': to,
#         'text': body,
#         'type': 'unicode',
#     })  



