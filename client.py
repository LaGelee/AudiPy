import socket
import threading
import pyaudio
import os
import time

from termcolor import colored
import colorama

colorama.init()

def header():
    print()
    print("    ___             ___ ____       ")
    print("   /   | __  ______/ (_) __ \__  __")
    print("  / /| |/ / / / __  / / /_/ / / / /")
    print(" / ___ / /_/ / /_/ / / ____/ /_/ / ")
    print("/_/  |_\__,_/\__,_/_/_/    \__, /  ")
    print("                          /____/   ")
    print("                                   ")
    print("--------------CLIENT!--------------")
    print("                                   ")
    
class Client:
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        while 1:
            try:
                self.target_ip = input('Enter IP address of server --> ')
                self.target_port = int(input('Enter target port of server --> '))

                self.s.connect((self.target_ip, self.target_port))

                break
            except:
                print("Couldn't connect to server")

        chunk_size = 1024 # 512
        audio_format = pyaudio.paInt16
        channels = 1
        rate = 20000

        self.mic = colored("ON", "green")
        self.sound = colored("ON", "green")

        # initialise microphone recording
        self.p = pyaudio.PyAudio()
        self.playing_stream = self.p.open(format=audio_format, channels=channels, rate=rate, output=True, frames_per_buffer=chunk_size)
        self.recording_stream = self.p.open(format=audio_format, channels=channels, rate=rate, input=True, frames_per_buffer=chunk_size)
        
        header()
        print("Connected to Server")

        # start threads
        receive_thread = threading.Thread(target=self.receive_server_data)
        receive_thread.start()
        print("[*] Data recieving handler ON")
        send_thread = threading.Thread(target=self.send_data_to_server)
        send_thread.start()
        print("[*] Data sending handler ON")
        time.sleep(1)
        self.command_input()

    def receive_server_data(self):
        while True:
            try:
                data = self.s.recv(1024)
                if self.sound == colored("ON", "green"):
                    self.playing_stream.write(data)
            except Exception as prblm:
                print("[*] Problem recieving and playing data")
                print(prblm)
                pass


    def send_data_to_server(self):
        while True:
            try:
                data = self.recording_stream.read(1024)
                if self.mic == colored("ON", "green") :
                    self.s.sendall(data)
            except Exception as prblm:
                print("[*] Problem recording and sending data")
                print(prblm)
                pass
    
    def command_input(self):
        while True:
            try:
                os.system("cls")
                header()
                print("[*] Mic   :",self.mic)
                print("[*] Sound :",self.sound)
                print()
                cmd = input(">>>")
                if cmd == "mic off":
                    self.mic = colored("OFF", "red")
                elif cmd == "mic on":
                    self.mic = colored("ON", "green")
                elif cmd == "sound off":
                    self.sound = colored("OFF", "red")
                elif cmd == "sound on":
                    self.sound = colored("ON", "green")
            except Exception as prblm:
                print("[*] Problem with commands")
                print(prblm)
                pass

client = Client()
