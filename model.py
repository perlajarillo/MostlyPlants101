from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from passlib.apps import custom_app_context as pwd_context
import config

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))
    bowls = relationship("Bowl", back_populates='user',
                         cascade="all, delete, delete-orphan")


class Preparation(Base):
    __tablename__ = "preparation"
    id = Column(Integer, primary_key=True)
    preparation = Column(String(200))


class Ingredient(Base):
    __tablename__ = 'ingredient'

    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    origin = Column(String(40))
    phase = Column(String(40))
    calories = Column(Float,  nullable=True)
    carbs = Column(Float, nullable=True)
    fat = Column(Float,  nullable=True)
    protein = Column(Float, nullable=True)
    portionsize = Column(Float, nullable=True)
    preparation = Column(Integer, ForeignKey('preparation.id'), nullable=True)
    isInBowl = relationship("Bowl_Ingredient", back_populates='ingredient',
                            cascade="all, delete, delete-orphan")

    @property
    def serialize(self):
        """Return ingredient in serializeable format"""
        return {
            'name': self.name,
            'origin': self.origin,
            'id': self.id,
            'phase': self.phase,
            'calories': self.calories,
            'carbs': self.carbs,
            'fat': self.fat,
            'protein': self.protein,
            'portionsize': self.portionsize,
            'preparation': self.preparation,
        }


class Bowl(Base):
    __tablename__ = 'bowl'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    type = Column(String(40))
    calories = Column(Float,  nullable=True)
    carbs = Column(Float, nullable=True)
    fat = Column(Float, nullable=True)
    protein = Column(Float, nullable=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User", back_populates="bowls")
    ingredients = relationship("Bowl_Ingredient", back_populates='bowl',
                               cascade="all, delete, delete-orphan")

    @property
    def serialize(self):
        """Return bowl in serializeable format"""
        return {
            'name': self.name,
            'type': self.type,
            'id': self.id,
            'calories': self.calories,
            'carbs': self.carbs,
            'fat': self.fat,
            'protein': self.protein,
            'user_id': self.user_id,
        }


class Bowl_Ingredient(Base):
    __tablename__ = 'bowl_ingredient'

    id = Column(Integer, primary_key=True)
    bowl_id = Column(Integer, ForeignKey('bowl.id'))
    ingredient_id = Column(Integer, ForeignKey('ingredient.id'))
    bowl = relationship("Bowl", back_populates="ingredients")
    ingredient = relationship("Ingredient", back_populates="isInBowl")

    @property
    def serialize(self):
        """Return bowl's ingredient in easily serializeable format"""
        return {
            'bowl_id': self.bowl_id,
            'ingredient_id': self.ingredient_id
        }


db_string = config.db_credentials_string
engine = create_engine(db_string)


Base.metadata.create_all(engine)
