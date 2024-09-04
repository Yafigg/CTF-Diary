from pwn import remote
import json

connection = remote('socket.cryptohack.org', 11112)

request = {
    "buy": "flag"
}

request_json = json.dumps(request)

connection.sendline(request_json)

response = connection.recvline()

response_json = json.loads(response)

print(response_json)

connection.close()
