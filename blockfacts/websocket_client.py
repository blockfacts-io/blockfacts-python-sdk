import websocket
import ssl 
import json
from threading import Thread
from time import sleep

class WebsocketClient(object):
    def __init__(self, key = "api-key-not-specified", secret = "api-secret-not-specified"):
        self.key = key
        self.secret = secret
        self.websocketURL = 'wss://ws.blockfacts.io/v1/'
        self.onOpen = None
        self.onMessage = None
        self.onClose = None
        self.onError = None
        self.isConnected = 0
        self.connecting = 0

    """
    Connects to the BlockFacts websocket server.     
    """
    def connect(self):
        if self.isConnected == 0:
            self.connecting = 1
            def _callback(callback, *args):
                callback(*args)

            def _on_ws_open(ws):
                self.isConnected = 1
                self.connecting = 0
                _callback(self.onOpen)

            def _on_ws_msg(ws, msg):
                _callback(self.onMessage, msg)

            def _on_ws_close(ws):
                self.isConnected = 0
                self.connecting = 0
                _callback(self.onClose)

            def _on_ws_error(ws, error):
                _callback(self.onError, error)

            self.ws = websocket.WebSocketApp(self.websocketURL, on_open = _on_ws_open, on_message = _on_ws_msg, on_close = _on_ws_close, on_error = _on_ws_error) 

            def _start_ws():
                self.ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})

            thread = Thread(target = _start_ws)
            thread.start()   
            
            while self.connecting == 1:
                sleep(0.1)

    """
    Disconnects from the BlockFacts websocket server. 
    """
    def disconnect(self):
        if self.isConnected == 1 and self.connecting == 0:
            self.ws.close()

    """
    Subscribe method used for subscribing to BlockFacts real-time crypto data fetching.
    @param {list} channels List of channels (dict) you are subscibing to.
    Reference: https://docs.blockfacts.io/#subscribe
    """    
    def subscribe(self, channels, msgId = None, snapshot = None):
        if type(channels) != list:            
            raise Exception("Parameter 'channels' must be of 'list' type")

        subscribeMsg = {
            "type":"subscribe",
            "X-API-KEY":self.key,
            "X-API-SECRET":self.secret,
            "channels": channels
        }

        if msgId is not None:
            subscribeMsg['id'] = msgId

        if snapshot is not None:
            if type(snapshot) != bool:            
                raise Exception("Parameter 'snapshot' must be of 'bool' type")
            subscribeMsg['snapshot'] = snapshot

        self.ws.send(json.dumps(subscribeMsg))
    
    """
    Unsubscribe method used to unsubscribe from certain channels or pairs.
    @param {list} channels List of channels (dict) you are unsubscibing from.
    Reference: https://docs.blockfacts.io/#unsubscribe
    """
    def unsubscribe(self, channels, msgId = None):
        if type(channels) != list:            
            raise Exception("Parameter 'channels' must be of 'list' type")

        unsubscribeMsg = {
            "type":"unsubscribe",
            "channels": channels
        }

        if msgId is not None:
            unsubscribeMsg['id'] = msgId

        self.ws.send(json.dumps(unsubscribeMsg))

    """
    Sends a ping type message to the server to determine if the server is online.
    Reference: https://docs.blockfacts.io/#ping
    """
    def ping(self, msgId = None):   
        pingMsg = {
            "type":"ping"
        }

        if msgId is not None:
            pingMsg['id'] = msgId
        
        self.ws.send(json.dumps(pingMsg))    

    """
    Sends a pong type message to the server to let the server know that the client is still connected.
    Reference: https://docs.blockfacts.io/#pong
    """
    def pong(self):
        self.ws.send(json.dumps({
            "type":"pong"
        }))