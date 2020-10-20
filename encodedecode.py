import base64

# Encrypt / decrypt functions
# 'https://stackabuse.com/encoding-and-decoding-base64-strings-in-python/#encodingstringswithpython'
def encode(message):
  message_bytes = message.encode()
  base64_bytes = base64.b64encode(message_bytes)
  base64_message = base64_bytes.decode()
  return base64_message

def decode(base64_message):
  base64_bytes = base64_message.encode()
  message_bytes = base64.b64decode(base64_bytes)
  message = message_bytes.decode()
  return message
