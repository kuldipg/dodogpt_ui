Install Python 3.8 or more and Anaconda 3

For Windows
Set C:\ProgramData\Anaconda3\Scripts, C:\Users\Smeel\AppData\Roaming\Python\Python39\Scripts and Python path i.e. C:\Program Files\Python39\, C:\Program Files\Python39\Scripts in Env Variables PATH


Open Anaconda Prompt
Switch to \rasa-webchat\dodogpt_ui>

Create and activate env =>
conda create --name rasa_env python=3.8
conda activate rasa_env
conda deactivate

If not new environment created then base environment is Ok.

py -m pip install --upgrade pip --user

py -m pip install autopep8 --user
py -m pip install openai --user
py -m pip install flask --user
py -m pip install rasa --user



Edit actions.py inside dodogpt_ui\back_end_code\chat_gpt_rasa\actions, go to line 7, add/modify 
openai.api_key = "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"



Open 3  Anaconda prompts

Action server =>
\rasa-webchat\dodogpt_ui\back_end_code\chat_gpt_rasa
rasa run actions

Python server =>
\rasa-webchat\dodogpt_ui
python app.py

UI server =>
\rasa-webchat\dodogpt_ui\back_end_code\chat_gpt_rasa
rasa run --enable-api --cors "*"



Open in browser
http://localhost:5000/