from gtts import gTTS

import config
import fileManager


def voice(text: str, lang='ru'):
    """
    Озвучивает текст
    :param text: Текст озвучки
    :param lang: Язык озвучки
    :return: Название созданного звукового файла
    """

    tts = gTTS(text, lang=lang)
    filename = config.voiceDir + fileManager.randomFileName('.mp3')
    tts.save(filename)
    return filename
