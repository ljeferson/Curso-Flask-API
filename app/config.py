class Config:
    "SECRET_KEY" = b'\xed\xf4\x83\xac\x92\x948\x10\xed\x04r\x94\x90\x058\xec\xf5\x84\x8bV\xfe\xceb\xea'

class Development(Config):
    "SQLALCHEMY_DATABASE_URI" = f"sqlite:///{basedir}"
    "SQLALCHEMY_TRACK_MODIFICATINS" = False

class Testing(Config):
    pass

config = {
    "development": Development
}