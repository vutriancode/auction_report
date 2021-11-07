from docxtpl import DocxTemplate
from fastapi import FastAPI
from fastapi import FastAPI
from fastapi.responses import StreamingResponse,FileResponse
import uvicorn
from typing import List
from fastapi import FastAPI, File
import json
from fastapi.middleware.cors import CORSMiddleware
import io
from pydantic.main import BaseModel
import smtplib
import mimetypes
from io import BytesIO
from email.message import EmailMessage
import json
from os import listdir
from os.path import isfile, join

from Settings import  *


class EmailMessageTB(BaseModel):
    Subject:str
    To:str
    ListNameTemplate:list
    ListDataTemplate:list
    Content:str
    
class Templates(BaseModel):
    TemplateName:str
    Content:str


def attach_bytesio_to_email(email, buf, filename):
    buf.seek(0)
    binary_data = buf.read()
    # Guess MIME type or use 'application/octet-stream'
    maintype, _, subtype = (mimetypes.guess_type(filename)[0] or 'application/octet-stream').partition("/")
    # Add as attachment
    email.add_attachment(binary_data, maintype=maintype, subtype=subtype, filename=filename)

def send_mail_smtp(mail, host, username, password):
    s = smtplib.SMTP(host)
    s.starttls()
    s.login(username, password)
    s.send_message(mail)
    s.quit()

origins = [
    "*"
]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
"""
    return File .doc
"""
@app.post("/report")

async def report_file(templates:Templates): 
    body = json.loads(templates.Content)
    report_template = templates.TemplateName
    doc = DocxTemplate("template/"+report_template)
    output = io.BytesIO()

    doc.render(body)
    doc.save(output)
    output.seek(0)

    return StreamingResponse(output,media_type="application/msword")

@app.get("/listtemplate")
async def get_list_template():
    onlyfiles = [f for f in listdir("template") if isfile(join("template", f))]
    return onlyfiles

@app.get("/gettemplate")
async def get_list_template(templatename:str):
    return FileResponse("template/{}".format(templatename))
@app.post("/sendmail")
async def send_email(emailMessage:EmailMessageTB):
    msg = EmailMessage()
    msg['Subject'] = emailMessage.Subject
    msg['From'] =  USERNAME
    msg['To'] =  emailMessage.To
    msg.set_content(emailMessage.Content)
    for i,j in zip(emailMessage.ListNameTemplate,emailMessage.ListDataTemplate):
        doc = DocxTemplate("template/"+i)
        output = io.BytesIO()
        print(j)
        j = json.loads(str(j))
        doc.render(j)
        doc.save(output)
        output.seek(0)
        attach_bytesio_to_email(msg,output,i)
    send_mail_smtp(msg,HOST,USERNAME,PASSWORD)
    return "email da duoc tu {} gui den {}".format(USERNAME,msg['To'])
# if __name__=="__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8006)
#     #encode_qr()