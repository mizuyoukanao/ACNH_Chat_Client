import tkinter
from tkinter import messagebox
from tkinter import ttk
import requests
import json

url = "https://web.sd.lp1.acbaa.srv.nintendo.net/api/sd/v1/messages"

def button_click():
    if v.get() == 'ローカル':
        headers = {'Authorization': 'Bearer {}'.format(input_token.get())}
        payload = {"body": "{}".format(input_message.get()), "type": "keyboard"}
        r = requests.post(url, headers=headers, data=json.dumps(payload))
        if r.status_code != 201:
            print("{}エラーが発生しました。".format(r.status_code))
        else:
            print("送信に成功しました。")
    if v.get() == '指定のフレンド':
        headers = {'Authorization': 'Bearer {}'.format(input_token.get())}
        payload = {"body": "{}".format(input_message.get()), "type": "friend", "userId": "{}".format(input_friendid.get())}
        r = requests.post(url, headers=headers, data=json.dumps(payload))
        if r.status_code != 201:
            print("{}エラーが発生しました。".format(r.status_code))
        else:
            print("送信に成功しました。")
    if v.get() == 'フレンド全員':
        headers = {'Authorization': 'Bearer {}'.format(input_token.get())}
        payload = {"body": "{}".format(input_message.get()), "type": "all_friend"}
        r = requests.post(url, headers=headers, data=json.dumps(payload))
        if r.status_code != 201:
            print("{}エラーが発生しました。".format(r.status_code))
        else:
            print("送信に成功しました。")

root = tkinter.Tk()
root.title("ACNH chat test")
root.geometry("500x120")

# メッセージラベル
input_message_label = tkinter.Label(text="メッセージ(最大32文字まで)")
input_message_label.grid(row=1, column=1)

# メッセージ入力欄
input_message = tkinter.Entry(width=32)
input_message.grid(row=1, column=2)

# TOKENラベル
input_token_label = tkinter.Label(text="ACNH TOKEN(ツールで取得したトークンを入力してください)")
input_token_label.grid(row=2, column=1)

# TOKEN入力欄
input_token = tkinter.Entry(width=32)
input_token.grid(row=2, column=2)

# 送信先ラベル
input_sendat_label = tkinter.Label(text="送信先を選んでください")
input_sendat_label.grid(row=3, column=1)

# 送信先選択欄
sendat = ['ローカル', '指定のフレンド', 'フレンド全員']
v = tkinter.StringVar()
input_sendat_cb = ttk.Combobox(textvariable=v, values=sendat, width=10)
input_sendat_cb.grid(row=3, column=2)

# フレンドのユーザーIDラベル
input_friendid_label = tkinter.Label(text="フレンドのユーザーID(送信先が「指定のフレンド」の場合のみ)")
input_friendid_label.grid(row=4, column=1)

# TOKEN入力欄
input_friendid = tkinter.Entry(width=18)
input_friendid.grid(row=4, column=2)

button = tkinter.Button(text="送信",command=button_click)
button.place(x=285, y=85, width=200)

root.mainloop()