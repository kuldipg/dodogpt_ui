from flask import Flask, redirect, url_for, request, render_template
import requests
import json
app = Flask(__name__, template_folder= 'templates')
context_set = ""


#UPLOAD_PATH = '/home/ubuntu/STT_Hackathon/webscraping'
UPLOAD_PATH = "D:\\webscraping\\src\\question_answering"
ALLOWED_ENTENSIONS = ['pdf','png','jpg','jpeg']

# @app.route('/', methods = ['POST', 'GET'])
# def index():
#   # if request.method == 'GET':
#   val = str(request.args.get(text))
#   data = json.dumps({"sender": "Rasa","message": val})
#   headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
#   res = requests.post('http://localhost:5005/webhooks/rest/webhook', data= data, headers = headers)
#   res = res.json()
#   val = res[0]['text']
#   return render_template('index.html', val=val)


@app.route('/') 
def index():
  return render_template('main_page.html')

@app.route('/upload_image', methods=['POST']) 
def upload_image():
  data = request.files['image']
  target = os.path.join(UPLOAD_PATH,'document_extraction_data')
  print('came here into the upload image path')
  if not os.path.isdir(target):
    os.mkdir(target)
  if data:
    timestr = time.strftime("%Y%m%d-%H%M%S")
    timestr = timestr+'.jpg'
    data.save(os.path.join(target, timestr))
  else:
    return jsonify({'error':'Unable to upload file'})
  

@app.route('/page2')
def page2():
  return render_template('page2.html')

@app.route('/page3')
def page3():
  return render_template('page3.html')

@app.route('/page4')
def page4():
  return render_template('page4.html')

@app.route('/page5')
def page5():
  return render_template('page5.html')  

@app.route('/page6')
def page6():
  return render_template('page6.html') 

@app.route('/page7')
def page7():
  return render_template('page7.html') 


@app.route('/page8')
def page8():
  return render_template('page8.html') 

@app.route('/page9')
def page9():
  return render_template('page9.html') 

@app.route('/page10')
def page10():
  return render_template('page10.html') 

@app.route('/page11')
def page11():
  return render_template('page11.html') 
# import os
# os.system("pip install git+https://github.com/openai/whisper.git")

# import gradio as gr
# import whisper
# model = whisper.load_model("large")

# import time

# def transcribe(audio):
#     # load audio for 30 seconds
#     audio = whisper.load_audio(audio)
#     audio = whisper.pad_or_trim(audio)

#     # make log-Mel spectrogram and move to device as the model
#     mel = whisper.log_mel_spectrogram(audio).to(model.device)

#     # detect the spoken language
#     _, probs = model.detect_language(mel)


if __name__ == '__main__':
  app.run(debug=True)