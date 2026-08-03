from configparser import ConfigParser, ExtendedInterpolation
cfg = ConfigParser(interpolation=ExtendedInterpolation(), allow_no_value=True)
cfg.read("./modules/config.cfg")

HOST = cfg.get("MySQL", "host")
PORT = cfg.get("MySQL", "port")
USER = cfg.get("Tibia", "user")
PASS = cfg.get("Tibia", "pass")
DB = cfg.get("Tibia", "db")