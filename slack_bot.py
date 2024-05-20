import logging, os
import io
import matplotlib.pyplot as plt
# Sets the debug level. 
# If you're using this in production, you can change this back to INFO and add extra log entries as needed.
logging.basicConfig(level=logging.DEBUG)
# Initialize the Web API client.
# This expects that you've already set your SLACK_BOT_TOKEN as an environment variable.
# Try to resist the urge to put your token directly in your code; it is best practice not to.
from slack_sdk import WebClient

# Create the plot
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
plt.plot(x, y, marker='o')
plt.title('Simple Line Graph')
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')

# Save the plot to a BytesIO object
buf = io.BytesIO()
plt.savefig(buf, format='png')
buf.seek(0)  # Rewind the buffer


client = WebClient(os.environ["BOT_USER_OAUTH_TOKEN"])
auth_test = client.auth_test()
bot_user_id = auth_test["user_id"]
print(f"App's bot user: {bot_user_id}")

# files = client.files_list(user=bot_user_id)

# new_file = client.files_upload_v2(
#     title="Requirements",
#     filename="./requirements.txt",
#     ub
# )

# files = client.files_list(user=bot_user_id)

#file_url = new_file.get("file").get("permalink")
# new_message = client.chat_postMessage(
#     channel="C0742STH338",
#     text=f"Here is the file: {file_url}",
# )

response = client.files_upload_v2(
        channels="C0742STH338",
        file=buf,
        filename='simple_graph.png',
        title="Simple Line Graph",
        initial_comment="Here is the file:"
    )

