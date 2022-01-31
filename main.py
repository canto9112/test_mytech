from fastapi import FastAPI, UploadFile, File
import shutil
from os import path

app = FastAPI()

BAD_REQUEST = 400
SUCCESSFULLY_REQUEST = 200

word_types = ['.docx', '.docm', '.dotx', '.dotm']
exel_types = ['.xlsx', '.xlsm', '.xltx', 'xltm', '.xlsb', '.xlam']


@app.post('/')
async def save_file(file: UploadFile = File(...)):
    with open(f'{file.filename}', 'wb') as buffer:
        file_type = path.splitext(file.filename)[1]
        if file_type in word_types or exel_types:
            return {'error! word and excel files are not supported': BAD_REQUEST}
        else:
            shutil.copyfileobj(file.file, buffer)
        return {f'file - {file.filename} save': SUCCESSFULLY_REQUEST}