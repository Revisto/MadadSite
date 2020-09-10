import requests
from flask import Flask
from flask import Flask, render_template, request,redirect

def SendTelMes(Text):
    bot_token = '1367451572:AAHxjR9P7imVqNnQ_l0ea661Zl6LLDUF2Ps'
    bot_chatID = '-445001984'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + Text
    response = requests.get(send_text)
    print (response)


app=Flask (__name__,static_url_path="/static") #static_url_path="/static"
@app.route('/', methods=['post', 'get'])
def Web():
    return open('index.html','r').read()


    
@app.route('/Message', methods=['POST'])
def handle_data():
    Name = request.form.get('name') 
    Email = request.form.get('email') 
    Message = request.form.get('message')  


    print (Name,Email,Message)
    SendTelMes(str('Added Message : '+Name+'          '+Email+'          '+Message))


    return redirect('/')



if __name__== '__main__':
    #app.send_static_file("index.html")
    app.run(debug=True,port=3333)