swagger docs tai http:/127.0.0.1/docs

POST http://127.0.0.1/report cung tham so:

{
  "TemplateName": "datatest.docx",
  "Content": "{\"datatest\":\"ok\"}"
}
return File .doc

POST http://127.0.0.1/sendmail cung tham so:

{
  "Subject": "Xin chao toi la Vu Tri An",
  "To": "an.vt172933@sis.hust.edu.vn",
  "ListNameTemplate": [
    "datatest.docx","baocaotest.docx"
  ],
  "ListDataTemplate": [
    "{\"datatest\":\"vu tri an 1105\"}","{}"
  ],
  "Content": "Mail nay duoc gui tu dong"
}


Get http://127.0.0.1/listemplate
return list name of templates

Get http://127.0.0.1/gettemplate/{nametemplate}
return a template by name

#build image docker 
docker build -t myimage .

#run image docker 
docker run -d --name mycontainer -p 80:80 myimage



