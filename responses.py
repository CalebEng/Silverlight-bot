import random
'''
Responses and things that the bot can do. 
later down the line maybe add chat bot functionality and some other things?

'''
def handle_response(msg) -> str:
    pmsg = msg.lower()

    if pmsg == 'silverlight':
        responses =["Yes?","That's me!","Reporting for duty!", "Need somthing?"]
        ans = random.randint(0,3)
        return responses[ans]
    
    if pmsg == 'hello silverlight' or pmsg == 'hi silverlight':
        return "Hello!"
  
    if pmsg == 'how are you silverlight?'or pmsg =='how are u silverlight?'or pmsg =='how are you silverlight' or pmsg =='how are u silverlight': 
        responses =["I'm good!","doing fine","I'm ok", "Been better"]
        ans = random.randint(0,3)
        return responses[ans]
     
    
    if pmsg == '!help':
        return 'I do things but idk what I do so deal wit it :)'
    
    else: return ''