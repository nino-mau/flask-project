from sqlalchemy import Text, String, ForeignKey
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


class Image(db.Model):
    __tablename__ = "images"
    id: Mapped[str] = mapped_column(Text, primary_key=True)
    hash: Mapped[str] = mapped_column(Text, nullable=False)
    character: Mapped["Character"] = relationship("Character", back_populates="image")


class Character(db.Model):
    __tablename__ = "characters"
    id: Mapped[str] = mapped_column(Text, primary_key=True)
    name: Mapped[str] = mapped_column(Text, nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    image_id: Mapped[str] = mapped_column(
        String, ForeignKey("images.id"), nullable=False
    )
    image: Mapped["Image"] = relationship("Image", back_populates="character")
