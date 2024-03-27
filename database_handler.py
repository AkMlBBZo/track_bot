import json
import time

from sqlalchemy import Column, create_engine, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import settings


Base = declarative_base()


# Настройки для самой бд
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, unique=True)
    message_id = Column(Integer, default=0)
    select_route = Column(Integer, default=0)
    

class Ways(Base):
    __tablename__ = "ways"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    coords = Column(String, default="[]")
    texts = Column(String, default="[]")
    photo_paths = Column(String, default="[]")
    audio_paths = Column(String, default="[]")
    start_photo_path = Column(String, default="[]")
    start_coords = Column(String, default="[]")
    cities = Column(Integer, default=-1)

class BotDatabaseHandler:
    # Создаем подключение к базе данных и сессию, создаем таблицу, если ее нет
    def __init__(self, db_name):
        engine = create_engine(
            f"sqlite:///{settings.BASE_DIR}/{db_name}", echo=False
        )
        self.session = sessionmaker(bind=engine)()
        Base.metadata.create_all(engine)

    # Проверяем, есть ли юзер в БД
    def user_exist(self, user_id):
        exists = self.session.query(User.id).filter_by(user_id=user_id).first()
        return exists is not None

    # Добавляем нового пользователя
    def add_user(self, user_id):
        user = User(user_id=user_id)
        self.session.add(user)
        return self.session.commit()

    # Устанавливаем coords
    def set_coords(self, coords, way_id):
        way = self.session.query(Ways).filter_by(id=way_id).first()
        way.coords = json.dumps(coords)
        return self.session.commit()

    # Устанавливаем start_coords
    def set_start_coords(self, coords, way_id):
        way = self.session.query(Ways).filter_by(id=way_id).first()
        way.start_coords = json.dumps(coords)
        return self.session.commit()

    # Устанавливаем message_id
    def set_message_id(self, message_id, user_id):
        user = self.session.query(User).filter_by(user_id=user_id).first()
        user.message_id = message_id
        return self.session.commit()

    # Устанавливаем select_route
    def set_select_route(self, select_route, user_id):
        user = self.session.query(User).filter_by(user_id=user_id).first()
        user.select_route = select_route
        return self.session.commit()

    # Получаем select_route
    def get_select_route(self, user_id):
        select_route = (
            self.session.query(User.select_route)
            .filter(User.user_id == user_id)
            .scalar()
        )
        return select_route

    # Получаем coords
    def get_coords(self, way_id):
        coords = (
            self.session.query(Ways.coords)
            .filter(Ways.id == way_id)
            .scalar()
        )
        return json.loads(coords)
    
    def get_texts(self, way_id):
        texts = (
            self.session.query(Ways.texts)
            .filter(Ways.id == way_id)
            .scalar()
        )
        return json.loads(texts)
    
    # Получаем start_coord
    def get_start_coord(self, way_id):
        coords = (
            self.session.query(Ways.start_coords)
            .filter(Ways.id == way_id)
            .scalar()
        )
        return json.loads(coords)

    # Получаем start_photo_path
    def get_start_photo_path(self, way_id):
        image_paths = (
            self.session.query(Ways.start_photo_path)
            .filter(Ways.id == way_id)
            .scalar()
        )
        return json.loads(image_paths)
    
    def get_photo_path(self, way_id):
        image_paths = (
            self.session.query(Ways.photo_paths)
            .filter(Ways.id == way_id)
            .scalar()
        )
        return json.loads(image_paths)

    # Получаем message_id
    def get_message_id(self, user_id):
        message_id = (
            self.session.query(User.message_id)
            .filter(User.user_id == user_id)
            .scalar()
        )
        return message_id

    # Получаем всю информацию о путях экскурсий
    def get_way_names(self):
        ways = self.session.query(Ways).all()
        return ways
    
    def get_audio_paths(self, way_id):
        # path = self.session.query(Ways.audio_paths).all()
        path = (self.session.query(Ways.audio_paths)
            .filter(Ways.id == way_id)
            .scalar()
        )
        return json.loads(path)

    # Удаляем пользователя
    def delete_user(self, user_id):
        user = self.session.query(User).filter_by(user_id=user_id).first()
        self.session.delete(user)
        return self.session.commit()
    

    def add_way(self, way_id, name="...", coords=[0, 0], texts=["..."], photo_paths=[], audio_paths=[], start_photo_path=[], start_coords=[0, 0], cities=-1):
        way = Ways(id=way_id, 
                   name=name, 
                   coords=coords, 
                   texts=texts, 
                   photo_paths=photo_paths, 
                   audio_paths=audio_paths, 
                   start_photo_path=start_photo_path,
                   start_coords=start_coords,
                   cities=cities)
        self.session.add(way)
        return self.session.commit()
                



    # Закрываем соединение
    def close(self):
        self.session.close()
