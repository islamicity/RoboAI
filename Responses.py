from datetime import datetime


def sample_responses(input_text):

    user_message = str(input_text).lower()
        
    if user_message in ('halo', 'hi'):
        return "Haloo kak, ada yang bisa Robo AI bantu?"

    if user_message in ('jam?'):
        now = datetime.now()
        # date_time = now.strptime("%d/%m/%y", '%H:%M:%S')

        return str(now)

    return "Maaf kak, Robo AI belum paham... :("