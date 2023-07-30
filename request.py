import requests
import random
import datetime
import time
from requests_html import HTML, HTMLSession
from flask import Flask,render_template
from flask import request
#id="fe_text" class="mailtext" value="pap55608@zslsz.com"
s = requests.Session()
r  =s.get("https://10minutemail.net/")
t = r.text
d = t.find("data-clipboard-text=")
email = t[d+21:d+39]
print(email)

def lol(): 
    time.sleep(3)
    r2  = s.get("https://10minutemail.net/mailbox.ajax.php")
    t2 = r2.text
    findcode = t2.find("is your Instagram code")
    dforcode = t2[findcode-7:findcode-1]
    print(dforcode)
    return dforcode

def main():
    username = "OIDawdjawdja215"
    password = "Jujgai25204!"
    email_to_use = email
    first_name = "Paul"
    time2 = str(int(datetime.datetime.now().timestamp()))
    enc_password = f"#PWD_INSTAGRAM_BROWSER:0:{time2}:{password}"
    session = requests.Session()
    # set a cookie that signals Instagram the "Accept cookie" banner was close
    session.cookies.set("ig_cb", "2")
    session.headers.update({'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'})
    session.headers.update({'Referer': 'https://www.instagram.com/'})
    res = session.get('https://www.instagram.com/api/v1/web/data/shared_data/')
    device_id_d = res.text.find("device_id")
    device_id = res.text[device_id_d+12:device_id_d+48]
    print(device_id)
    tokenbegin = res.text.find("csrf_token")
    csrftoken = res.text[tokenbegin+13:tokenbegin+45]
    print(csrftoken)
    session.headers.update({'X-CSRFToken': csrftoken})

    login_data = {'username': username, 'enc_password': enc_password, 'email': email_to_use, 'first_name': first_name,}
    time.sleep(3)
    login = session.post('https://www.instagram.com/api/v1/web/accounts/web_create_ajax/attempt/', data=login_data,allow_redirects=True)
    session.headers.update({'X-CSRFToken': csrftoken})
    print(login.ok)
    time.sleep(2)
    randomday = random.randint(1,30)
    randomMonth = random.randint(1,12)
    randomyear = random.randint(1975,2002)
    birthday = {'day':randomday,'month':randomMonth,'year':randomyear}
    birth = session.post("https://www.instagram.com/api/v1/web/consent/check_age_eligibility/",data=birthday,allow_redirects=True)
    print(birth.ok)
    time.sleep(3)
    emaildata = {'email':email_to_use,'device_id':device_id}
    emailsend = session.post("https://www.instagram.com/api/v1/accounts/send_verify_email/",data=emaildata)
    print(emailsend,emailsend.text)
    repeat = 0
    code = None
    while True:
        repeat += 1
        time.sleep(1)
        result = lol()
        if result != "</tabl":
            print(result)
            code = result
            break
        if repeat == 30:
            print("max")
            break
    codedata = {'code':code,'device_id':device_id,'email':email_to_use}
    sendcode = session.post("https://www.instagram.com/api/v1/accounts/check_confirmation_code/",data=codedata)
    print(sendcode,sendcode.text)
    signupcode = sendcode.json()
    forcecode = signupcode["signup_code"]
    print(forcecode)
    testdata = {'enc_password':enc_password,'email':email_to_use,'first_name':first_name,'username':username,'day':randomday,'email':email_to_use,'month':randomMonth,'year':randomyear,'client_id':device_id,'tos_version':'eu','force_sign_up_code':forcecode}
    print(testdata)
    test = session.post("https://www.instagram.com/api/v1/web/accounts/web_create_ajax/",data=testdata)
    print(test,test.text)
    session.close()

main()