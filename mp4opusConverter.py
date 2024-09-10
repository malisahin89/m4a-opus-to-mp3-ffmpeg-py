import os
import subprocess
import re
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

input_folder = '/opus-m4a'
output_folder = '/mp3s'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(input_folder):
    if filename.endswith('.m4a') or filename.endswith('.opus'):
        input_file = os.path.join(input_folder, filename)
        
        output_filename = os.path.splitext(filename)[0] + '.mp3'
        output_file = os.path.join(output_folder, output_filename)
        
        command = ['ffmpeg', '-i', input_file, '-q:a', '0', output_file]
        
        try:
            result = subprocess.run(command, check=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
            print(f"{filename} dosyası {output_filename} olarak dönüştürüldü.")
        except subprocess.CalledProcessError as e:
            print(f"{filename} dosyası dönüştürülemedi. Hata: {e.stderr}")
