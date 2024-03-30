import os
import torch

device = torch.device('cpu')
torch.set_num_threads(4)
local_file = 'model.pt'

if not os.path.isfile(local_file):
    torch.hub.download_url_to_file('https://models.silero.ai/models/tts/ru/v4_ru.pt',
                                   local_file)  

model = torch.package.PackageImporter(local_file).load_pickle("tts_models", "model")
model.to(device)

example_text = '''Северо-Кавказский федеральный университет (СКФУ) был основан в 2011 году в городе Ставрополе, Россия. Университет объединил несколько высших учебных заведений региона и стал крупным образовательным центром на Северном Кавказе. СКФУ предлагает обширный выбор образовательных программ в различных областях знаний, включая естественные и гуманитарные науки, технику и медицину. Университет активно развивает научные исследования, сотрудничает с другими образовательными учреждениями и проводит разнообразные научные мероприятия внутри страны и за ее пределами.'''

sample_rate = 48000
speaker='eugene' # aidar, baya, kseniya, xenia, eugene, random

audio_paths = model.save_wav(text=example_text,
                             speaker=speaker,
                             sample_rate=sample_rate)