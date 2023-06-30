from http.server import HTTPServer, SimpleHTTPRequestHandler

# 設定伺服器的地址和埠號
server_address = ('', 8000)

# 建立HTTP伺服器
httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)

# 啟動伺服器
print('伺服器已啟動...')
httpd.serve_forever()