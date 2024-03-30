# 45.041004181,41.910118103
import settings
import json
# settings.Bot_DB.set_start_coords([45.041004181,41.910118103], 1)

name = json.dumps("Фантанчик", ensure_ascii=False)
coords = json.dumps([[45.023507, 41.896176], [45.023507, 41.896176], [45.023507, 41.896176]], ensure_ascii=False)
texts = json.dumps(["Текст 1", "Текст 2", "Текст 3"], ensure_ascii=False)
photo_paths = json.dumps(["https://clck.ru/39hiSw", "https://clck.ru/39hiYw", "https://clck.ru/39hiaC"], ensure_ascii=False)
audio_paths = json.dumps(["plug.mp3", "plug.mp3", "plug.mp3"], ensure_ascii=False)
start_photo_path = json.dumps("https://clck.ru/39hiRi", ensure_ascii=False)
start_coord = json.dumps([45.023507, 41.896176], ensure_ascii=False)
cities = json.dumps(settings.cities_dict.get(1), ensure_ascii=False)

settings.Bot_DB.add_way(way_id=2, name=name, coords=coords, texts=texts, 
                        
                        photo_paths=photo_paths, audio_paths=audio_paths,

                        start_photo_path=start_photo_path, 
                        
                        start_coords=start_coord, cities=cities)


name = json.dumps("СКФУ", ensure_ascii=False)
coords = json.dumps([[45.0428270, 41.9643760]], ensure_ascii=False)
texts = json.dumps(["Северо-Кавказский федеральный университет"], ensure_ascii=False)
photo_paths = json.dumps(["https://clck.ru/39kTu6"], ensure_ascii=False)
audio_paths = json.dumps(["skfu.wav"], ensure_ascii=False)
start_photo_path = json.dumps("https://clck.ru/39kU42", ensure_ascii=False)
start_coord = json.dumps([45.0428270, 41.9643760], ensure_ascii=False)
cities = json.dumps(settings.cities_dict.get(1), ensure_ascii=False)

settings.Bot_DB.add_way(way_id=1, name=name, coords=coords, texts=texts, 
                        
                        photo_paths=photo_paths, audio_paths=audio_paths,

                        start_photo_path=start_photo_path, 
                        
                        start_coords=start_coord, cities=cities)