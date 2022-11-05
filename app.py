from PyPDF2 import PdfFileReader,PdfFileWriter
from flask import Flask,jsonify, request
app=Flask(__name__)
@app.route('/')
def test():
    return jsonify('To rotate pdf go to /rotate and send {"path":your path,"page_no":page number,"rotate":rotate multiplier of 90}')
@app.route('/rotate',methods=['POST'])
def get_details():
    data=request.get_json()
    path,page_no,degree_rotate=data['path'],data['page_no'],data['rotate']
    original=PdfFileReader(path)
    paster=open('temp/test.pdf','wb')
    output_res=PdfFileWriter()
    total_page=original.getNumPages()
    page_no=page_no-1;
    if page_no>total_page or degree_rotate%90!=0:
        return jsonify('message: error is there')
    page=original.getPage(page_no)
    page.rotate_clockwise(degree_rotate)
   
    for i in range (total_page):
        p=original.getPage(i)
        if i==page_no:
            output_res.addPage(page)
        else:
            output_res.addPage(p)
    output_res.write(paster)
    paster.close()
    return jsonify('message: sucessfull ')

app.run(port=5000)

