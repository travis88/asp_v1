from flask_login import UserMixin
from sqlalchemy.dialects.postgresql import UUID
from . import db
import uuid

class User(db.Model, UserMixin):
    __tablename__ = "cd_users"
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = db.Column(db.String(), unique=True)
