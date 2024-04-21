from flask import Flask, render_template, request, send_file

from ultralytics import YOLO

app = Flask(__name__)
model = YOLO('models/best1.pt')


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    file = request.files['file']
    file_location = f"temp/test.{file.filename.split('.')[-1]}"
    print(file_location)
    file.save(file_location)
    res = model([file_location])
    res[0].save(filename=f"temp/res_test.{file.filename.split('.')[-1]}")
    import base64
    with open(f"temp/res_test.{file.filename.split('.')[-1]}", "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    return str(encoded_string)[2:-1]
    
if __name__ == '__main__':
    app.run(host='0.0.0.0')
