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
from email.utils import make_msgid
import dateutil.parser

from email.message import EmailMessage
import json
from os import listdir
from os.path import isfile, join
import zipfile 

from Settings import  *

class EmailMessageTB(BaseModel):
    To:str
    ListNameTemplate:list
    ListDataTemplate:list
    
class Templates(BaseModel):
    TemplateName:str
    Content:str
class ZipTemplates(BaseModel):
    ReportFileName:str
    ContractFileName:str
    NotifyFileName:str
    DataString:str

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
@app.post("/zipreport")

async def report_zip_file(templates:ZipTemplates): 
    body = json.loads(templates.DataString)
    report_template = templates.ReportFileName
    doc = DocxTemplate("template/"+report_template)
    output = io.BytesIO()

    doc.render(body)
    doc.save(output)
    output.seek(0)
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, "a", zipfile.ZIP_DEFLATED, False) as zip_file:
        for file_name, data in [('BB_DGTS.docx', output)]:
            zip_file.writestr(file_name, data.getvalue())
        for i in body["assets"]:
            body["asset"] = i
            doc = DocxTemplate("template/"+templates.NotifyFileName)
            output = io.BytesIO()
            doc.render(body)
            doc.save(output)
            output.seek(0)
            file_name = "TBTrungDGTS-{}.docx".format(i["AssetName"])
            zip_file.writestr(file_name, output.getvalue())
            doc = DocxTemplate("template/"+templates.ContractFileName)
            output = io.BytesIO()
            doc.render(body)
            doc.save(output)
            output.seek(0)
            file_name = "HDMuaBanTSDG-{}.docx".format(i["AssetName"])
            zip_file.writestr(file_name, output.getvalue())
    zip_buffer.seek(0)
    response = StreamingResponse(zip_buffer,media_type="application/zip")
    response.headers["Content-Disposition"] = "attachment; filename=tonghopketqua.zip"
    return response

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
    msg['Subject'] = SUBJECT
    msg['From'] =  USERNAME
    msg['To'] =  emailMessage.To
    HTMLL = HTML.replace("DVDGTS",emailMessage.ListDataTemplate[0]["DVDGTS"])
    HTMLL = HTMLL.replace("ReceiverCode",emailMessage.ListDataTemplate[0]["ReceiverCode"])
    HTMLL = HTMLL.replace("nowday",str(emailMessage.ListDataTemplate[0]["nowday"]))
    HTMLL = HTMLL.replace("nowmonth",str(emailMessage.ListDataTemplate[0]["nowmonth"]))
    HTMLL = HTMLL.replace("nowyear",str(emailMessage.ListDataTemplate[0]["nowyear"]))
    msg.add_alternative(HTMLL, subtype='html')
    for i,j in zip(emailMessage.ListNameTemplate,emailMessage.ListDataTemplate):
        for ii in range(len(j['history'])):
            j['history'][ii]['price'] = "{:,.0f}".format(j['history'][ii]['price'])
            a = dateutil.parser.isoparse(j['history'][ii]['time'])
            j['history'][ii]['time']=  "{}/{}/{}".format(a.day,a.month,a.year) +" "+ str(a.hour)+":"+str(a.minute)+":"+str(a.second)
        doc = DocxTemplate("template/"+i)
        output = io.BytesIO()
        doc.render(j)
        doc.save(output)
        output.seek(0)
        attach_bytesio_to_email(msg,output,i)
    send_mail_smtp(msg,HOST,USERNAME,PASSWORD)
    return "email da duoc tu {} gui den {}".format(USERNAME,msg['To'])
# if __name__=="__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8006)
