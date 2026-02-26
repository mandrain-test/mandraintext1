from generator import generate_code
from auto_push import upload_file

code = generate_code()
upload_file("src/ai_generated.py", code)