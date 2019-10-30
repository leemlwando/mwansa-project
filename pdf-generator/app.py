from flask import Flask, render_template,request, make_response, Response
import json
import requests
import pdfkit
import os
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config.from_envvar('APP_SETTINGS')

@app.route('/api/v1/generate-pdf-receipt',  methods = ['POST'])
def pdfkitgen(name=None):
    CONSTANTS = {'credit':'Electricity Credit', 'debt': '', 'service':'Service Charge'}
    # r = requests.post('http://localhost:8787/api/v1/transactions?resourceType='+request.args.get('resourceType'), data = json.dumps(request.get_json()),  headers={'Content-Type': 'application/json'})
    # return response
    # responseObject = r.json()
    # print(request.get_json(), responseObject)
    # if responseObject['success'] == False:
    #         rendered = render_template('error.html', response=responseObject)
    #         css = ['static/css/bootstrap.min.css']
    #         pdf = pdfkit.from_string(rendered, False, css=css)
    #         response = make_response(pdf)
    #         response.headers['Content-Type'] = 'application/pdf'
    #         response.headers['Content-Disposition'] = 'attachment; filename=adzlok_electricity_receipt_error.pdf'
    #         return response
    # if responseObject['response']['event']['EventCode'] == 0:
    #     rendered = render_template('receipt.html', response=responseObject)
    #     css = ['static/css/bootstrap.min.css']
    #     pdf = pdfkit.from_string(rendered, False, css=css)
    #     response = make_response(pdf)
    #     response.headers['Content-Type'] = 'application/pdf'
    #     response.headers['Content-Disposition'] = 'inline; filename=adzlok_electricity_receipt_success.pdf'
    #     return response
    print(request.json)
    rendered = render_template('ticket.html', response=request.json)
    css = ['static/css/bootstrap.min.css']
    pdf = pdfkit.from_string(rendered, False, css=css)
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'attachment; filename=ticket.pdf'
    return response


# @app.route('/api/v1/generate-pdf-receipt',  methods = ['GET'])
# def pdfkitgen(name=None):
#     CONSTANTS = {'credit':'Electricity Credit', 'debt': '', 'service':'Service Charge'}
#     # r = requests.post('http://localhost:8787/api/v1/transactions?resourceType='+request.args.get('resourceType'), data = json.dumps(request.get_json()),  headers={'Content-Type': 'application/json'})
#     # return response
#     # responseObject = r.json()
#     # print(request.get_json(), responseObject)
#     # if responseObject['success'] == False:
#     #         rendered = render_template('error.html', response=responseObject)
#     #         css = ['static/css/bootstrap.min.css']
#     #         pdf = pdfkit.from_string(rendered, False, css=css)
#     #         response = make_response(pdf)
#     #         response.headers['Content-Type'] = 'application/pdf'
#     #         response.headers['Content-Disposition'] = 'attachment; filename=adzlok_electricity_receipt_error.pdf'
#     #         return response
#     # if responseObject['response']['event']['EventCode'] == 0:
#     #     rendered = render_template('receipt.html', response=responseObject)
#     #     css = ['static/css/bootstrap.min.css']
#     #     pdf = pdfkit.from_string(rendered, False, css=css)
#     #     response = make_response(pdf)
#     #     response.headers['Content-Type'] = 'application/pdf'
#     #     response.headers['Content-Disposition'] = 'inline; filename=adzlok_electricity_receipt_success.pdf'
#     #     return response
#     print(request.args)
#     rendered = render_template('ticket.html', response=request.args)
#     css = ['static/css/bootstrap.min.css']
#     pdf = pdfkit.from_string(rendered, False, css=css)
#     response = make_response(pdf)
#     response.headers['Content-Type'] = 'application/pdf'
#     response.headers['Content-Disposition'] = 'attachment; filename=ticket.pdf'
#     return response

@app.route('/<path:path>', methods=['POST', 'GET', 'PUT', 'DELETE'])
def catch_all(path):
    response = make_response(json.dumps({'success': False, 'message': 'Page Not Found'}), 404)
    response.headers['Content-Type'] = 'application/json'
    return response
if __name__ == '__main__':
    app.run(host='0.0.0.0')