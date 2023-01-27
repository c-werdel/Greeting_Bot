import urllib3
import json
import os
http = urllib3.PoolManager()

def lambda_handler(event, context):

    hook_url = os.environ["webhook"]

    payload = {
# 	"blocks": [
# 		{
# 			"type": 'section',
# 			"text": {
# 				"type": "mrkdwn",
# 				"text": "Good Morning: Cascade Team"
# 				{
	 "attachments": [
		{
		    "fallback": "Error could not show image.",
		    "text": "Good Morning: Cascade Team"
		    "image_url": "https://dribbble.com/shots/3502310-Toolio/attachments/9861572?mode=media",
		    "thumb_url": "http://example.com/path/to/thumb.png"
		}
	    ]
	}
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
