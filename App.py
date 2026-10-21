# Let's create a zip archive containing both app.py and requirements.txt for easy download
import zipfile

zip_buffer = io.BytesIO()
with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
    zip_file.write('app.py')
    zip_file.write('requirements.txt')
zip_buffer.seek(0)
print("Zip archive created.")