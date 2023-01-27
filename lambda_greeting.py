import urllib3
import json
import os
http = urllib3.PoolManager()

def lambda_handler(event, context):

    hook_url = os.environ["webhook"]

    payload = {
	"blocks": [
		{
			"type": "section",
			"block_id": "section567",
			"text": {
				"type": "mrkdwn",
				"text": "Good Morning Cascade Team \n"
			},
			"accessory": {
				"type": "image",
				"image_url": "https://cdn.dribbble.com/users/224717/screenshots/3502310/media/260976f18084809312abb35127cb158c.jpg",
				"alt_text": "Mr Bot"
			}
		}
	]
}
    encoded_data = json.dumps(payload).encode('utf-8')

    r = http.request( 
        'POST',
        hook_url ,
        body=encoded_data,
        headers={'Content-Type': 'application/json'})

if __name__ == "__main__":
    lambda_handler(None, None)
