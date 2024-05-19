from flask import Flask, jsonify
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
    # Define the email parameters
    email = sib_api_v3_sdk.SendSmtpEmail(
        to=[{"email": "serge.salah4@gmail.com", "name": "Recipient Name"}],
        sender={"email": "haytam.elmoufti@gmail.com", "name": "Attijariwafa"},
        subject="Hello from Sendinblue",
        html_content="<html><body><h1>Congratulations!</h1><p>You successfully sent this email via the Sendinblue API.</p></body></html>"
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
