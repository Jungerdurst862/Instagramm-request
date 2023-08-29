import requests
import random
import datetime
import time
import asyncio
from multiprocessing import Pool
from proxy_randomizer import RegisteredProviders
import os
#id="fe_text" class="mailtext" value="pap55608@zslsz.com"
def MailCreate(s):
    r  =s.get("https://10minutemail.net/")
    t = r.text
    d = t.find("data-clipboard-text=")
    email = t[d+21:d+39]
    return  email

def CreateSession():
    s = requests.Session()
    return  s

def lol(s): 
    r2  = s.get("https://10minutemail.net/mailbox.ajax.php")
    t2 = r2.text
    findcode = t2.find("is your Instagram code")
    dforcode = t2[findcode-7:findcode-1]
    return dforcode


def proxycreate():
    rp = RegisteredProviders()
    rp.parse_providers()
    for proxy in rp.proxies:
        randomProxy = {"https":proxy.get_proxy()}
        response    = requests.get("http://google.com", proxies=randomProxy)
        print(response)
        return  randomProxy,proxy.port,proxy.ip_address
    
def delete(f,file,username):
    print("delete",str(username)+".txt")
    if os.path.exists(str(username)+".txt"):
        print("exists")
        os.remove(str(username)+".txt")
    else:
        print("The file does not exist")

def main(x):
    s = requests.Session()
    email = MailCreate(s)
    listusername1 = ["Monte","Trymacs","Garsten","Onkel","Lol","Moin","Honey","BAck","Lets","Go42"]
    username1 = random.choice(listusername1)
    listusername2 = ["Hol","Get","My","Level","Lost","mgh","_",".","lbk"]
    username2 = random.choice(listusername2)
    listusername3 = ["Handy","Maus","Haus","Rechts","Links","Moin"]
    username3 = random.choice(listusername3)
    username4 = str(random.randint(1,999))
    usernameend = username1 + username2 + username3 + username4


    username = usernameend
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
    tokenbegin = res.text.find("csrf_token")
    csrftoken = res.text[tokenbegin+13:tokenbegin+45]
    session.headers.update({'X-CSRFToken': csrftoken})

    login_data = {'username': username, 'enc_password': enc_password, 'email': email_to_use, 'first_name': first_name,'client_id':device_id}
    print("Account: "+str(login_data)+" beginn with creating")
   
    login = session.post('https://www.instagram.com/api/v1/web/accounts/web_create_ajax/attempt/', data=login_data,allow_redirects=True)
    session.headers.update({'X-CSRFToken': csrftoken})
    if login.ok != True:
        print("fail",login.text)
        return 
    randomday = random.randint(1,30)
    randomMonth = random.randint(1,12)
    randomyear = random.randint(1975,2002)
    birthday = {'day':randomday,'month':randomMonth,'year':randomyear}
    birth = session.post("https://www.instagram.com/api/v1/web/consent/check_age_eligibility/",data=birthday,allow_redirects=True)
    if birth.ok != True:
        print("fail",birth.text)
        return 
    emaildata = {'email':email_to_use,'device_id':device_id}
    emailsend = session.post("https://www.instagram.com/api/v1/accounts/send_verify_email/",data=emaildata)
    emailjson = emailsend.json()
    if emailjson["email_sent"] != True:
        print("no sent of email")
        return 
    if emailsend.ok != True:
        print("fail",emailsend.text)
        return 
    repeat = 0
    code = None
    while True:
        repeat += 1
        time.sleep(1)
        result = lol(s)
        if result != "</tabl":
            code = result
            break
        if repeat == 100:
            print("max")
            code = "max"
            break

    if code == "max":
        print("no code came")
        return 
    if code == None:
        print("no code")
        return
    codedata = {'code':code,'device_id':device_id,'email':email_to_use}
    sendcode = session.post("https://www.instagram.com/api/v1/accounts/check_confirmation_code/",data=codedata)
    if sendcode.ok != True:
        print("fail",sendcode.text,code)
        return 
    signupcode = sendcode.json()
    forcecode = signupcode["signup_code"]
    testdata = {'enc_password':enc_password,'email':email_to_use,'first_name':first_name,'username':username,'day':randomday,'email':email_to_use,'month':randomMonth,'year':randomyear,'client_id':device_id,'force_sign_up_code':forcecode}
    test = session.post("https://www.instagram.com/api/v1/web/accounts/web_create_ajax/",data=testdata)
    testjson = test.json()
    if testjson['account_created']== False:
        print("Account not Created",testjson)
        return
    else:
        print("Account created")
    availeble = False
    if testjson['show_privacy_page']==False:
        print("Account got Blocked "+username)
        availeble = False
    else:
        print("Account Createt "+username)
        availeble = True
    f = open("username.txt","a")
    f.write("{username:"+str(username)+"};{password:"+str(password)+"}"+str(availeble)+"\n")
    print(test.text)
    f.close()
    session.close()
    s.close()   
    return 

print("Start Creating")

def Zwischen():
    p = Pool(1)
    p.map(main,"Hallo")
    print("hallo")


if __name__ == "__main__":
    Zwischen()

print("ende")



