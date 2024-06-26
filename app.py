from flask import Flask, request, jsonify
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint
import os

app = Flask(__name__)

# Configure API key authorization: api-key
configuration = sib_api_v3_sdk.Configuration()
configuration.api_key['api-key'] = os.getenv('SENDINBLUE_API_KEY')

# Create an instance of the API class
api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))

@app.route('/send-email', methods=['POST'])
def send_email():
    data = request.get_json()
    if 'email' not in data or 'content' not in data or 'subject' not in data:
        return jsonify({'message': 'Email, subject, and content are required'}), 400

    recipient_email = data['email']
    email_content = data['content']
    email_subject = data['subject']

    # Define the email parameters
    email = sib_api_v3_sdk.SendSmtpEmail(
        to=[{"email": recipient_email, "name": "Recipient Name"}],
        sender={"email": "haytam.tita@gmail.com", "name": "Attijariwafa"},
        subject=email_subject,
        html_content=email_content
    )

    # Send the email
    try:
        api_response = api_instance.send_transac_email(email)
        pprint(api_response)
        return jsonify({'message': 'Email sent successfully!'}), 200
    except ApiException as e:
        print("Exception when calling TransactionalEmailsApi->send_transac_email: %s\n" % e)
        return jsonify({'message': 'Failed to send email', 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
