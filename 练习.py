#!/usr/bin/envpython
#coding=utf-8
fromTkinterimport*
fromPILimportImageTk,Image
fromtkMessageBoximport*
importrequests
importjson
root=Tk()
root.title("PyOSv1.0.0")
root.geometry("1920x1080")
Order=StringVar()
defApollo():
    url=\'http://www.tuling123.com/openapi/api\'
payload={"key":"8436d7ef102d4e1d94eab34d50e6d689",
"info":""
}
headers={\'content-type\':\'application/json\'}

whileTrue:
payload【\'info\'】=Order.get()
r=requests.post(url,data=json.dumps(payload),headers=headers)
showinfo("Answer",(\'FromApollo:%s\'%r.json()【\'text\'】))
return
Order_entry= Entry(root,bd=15,width=85,textvariable=Order)
Order_entry.place(x=625,y=650)
Confirm_Button=Button(root,text="Launch",command=Apollo)
Confirm_Button.place(x=620,y=400)
root.mainloop()