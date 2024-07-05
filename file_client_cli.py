import base64
import socket


#request server
def send_request(request):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("127.0.0.1", 9999))
    client.send(request.encode())
    response = client.recv(4096).decode()
    client.close()
    return response


def delete_file(filename):
    request = f"DELETE {filename}"
    return send_request(request)



def upload_file(filename):
    with open(filename, 'rb') as file:
        file_content = file.read() #read content file
    file_content_base64 = base64.b64encode(file_content).decode() ## Encode konten file ke base64 dan mendecode ke string
    request = f"UPLOAD {filename} {file_content_base64}"
    return send_request(request) # # Mengirim permintaan DELETE ke server dan mengembalikan respons
    ## Mengirim permintaan DELETE ke server dan mengembalikan respons



if __name__ == "__main__":
    while True:
        command = input("Enter (UPLOAD <filename> / DELETE <filename> / EXIT): ") #input pengguna
        if command.startswith("UPLOAD "):
            filename = command.split(' ')[1]
            response = upload_file(filename)
            print(response)
        elif command.startswith("DELETE "):
            filename = command.split(' ')[1]
            response = delete_file(filename)
            print(response)
        elif command == "EXIT":
            break
        else:
            print("Error Invalid")