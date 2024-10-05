import os
from dotenv import load_dotenv, find_dotenv


# getting api keys
def load_env():
    _ = load_dotenv(find_dotenv())

def get_openai_api_key():
    load_env()
    openai_api_key = os.getenv('OPENAI_API_KEY')
    return openai_api_key

def get_groq_api_key():
    load_env()
    groq_api_key = os.getenv('GROQ_API_KEY')
    return groq_api_key

def get_serper_api_key():
    load_env()
    serper_api_key = os.getenv('SERPER_API_KEY')
    return serper_api_key

# function to break lines if longer then 80 charactors
# dont break if in the middle of the word

def pretty_print_result (result):
    parsed_result:str =[]
    for line in result.splitlines():
        if len(line) > 80:
            words = line.split(' ')
            new_line=''
            for word in words:
                if len(new_line) +len(word) + 1 >80:
                    parsed_result.append(new_line)
                    new_line = word
                else:
                    if new_line == '':
                        new_line = word
                    else:  
                        new_line = new_line + ' ' + word
            parsed_result.append(new_line)
        else:
            parsed_result.append(line)
    return '\n'.join(parsed_result)

