from flask import Flask, render_template, request
import string
import secrets
import main

app = Flask(__name__)

# Hàm sinh khóa ngẫu nhiên
def generate_random_key():
    chars = string.digits + 'ABCDEF'
    return ''.join(secrets.choice(chars) for _ in range(16))

@app.route('/', methods=['GET', 'POST'])
def index():
    plaintext = ""
    key = ""
    action = ""
    ki_data = []
    k_left_right_data = []
    message = ""
    message_type = ""
    result = ""
    
    if request.method == 'POST':
        plaintext = request.form.get('plaintext', '')
        key = request.form.get('key', '')
        action = request.form.get('action', '')
        generate_key = request.form.get('generateKey', '')
        
        # Xử lý sinh khóa
        if generate_key:
            key = generate_random_key()
            return render_template('index.html', 
                          plaintext=plaintext,
                          result = result,
                          key=key,
                          action=action,
                          ki_data=ki_data,
                          k_left_right_data=k_left_right_data,
                          message=message,
                          message_type=message_type)
        
        # Kiểm tra dữ liệu đầu vào
        if not plaintext:
            message = 'Vui lòng nhập bản rõ M'
            message_type = 'error'
        elif not key:
            message = 'Vui lòng nhập khóa K'
            message_type = 'error'
        elif not action:
            message = 'Vui lòng chọn Mã hóa hoặc Giải mã'
            message_type = 'error'
        else:
            # Xử lý mã hóa/giải mã
            K_bits = main.hex_to_bits(key,64)
            keys, data = main.generate_keys(K_bits)
            for i in keys:
              ki_data.append(main.bits_to_hex(i))
            ki_data = enumerate(ki_data)
            k_left_right_data = enumerate(data)
            if action == 'encrypt':
              M_bits = main.hex_to_bits(plaintext,64)
              
              C_bits = main.encode(M_bits, keys)
              result = main.bits_to_hex(C_bits).zfill(16)
            else:
              C_bits = main.hex_to_bits(plaintext, 64)
              M2_bits = main.decode(C_bits, keys)
              result = main.bits_to_hex(M2_bits).zfill(16)
                
            
            message = 'Xử lý thành công! Dữ liệu đã được hiển thị trong bảng.'
            message_type = 'success'
    
    return render_template('index.html', 
                          plaintext=plaintext,
                          result = result,
                          key=key,
                          action=action,
                          ki_data=ki_data,
                          k_left_right_data=k_left_right_data,
                          message=message,
                          message_type=message_type)

if __name__ == '__main__':
    app.run(debug=True)