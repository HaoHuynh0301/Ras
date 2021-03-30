import websocket
try:
    import thread
except ImportError:
    import _thread as thread
import json

# Connect to Django Server
ws = websocket.WebSocket()
# ws.connect('ws://10.10.34.158:8000/ws/realtime/')
ws.connect('ws://localhost:8000/ws/realtimeData/')
# ws.connect('ws://192.168.123.147:8000/ws/realtime/')

try:
    pp = json.dumps({
        'command': "getInfo",
        'name': "Pi 2",
        'time_start': 1,
        'time_end': 2,
    })
    ws.send(pp)
    ws.close()
    

    
# try:
#     pp = json.dumps({
#         'command': "getInfo",
#         'name': "Pi 2",
#         'datetime': datetime
#     })
#     ws.send(pp)
#     ws.close()
    
except Exception as e:
    print("[INFOR REQUEST]: " + str(e))

        