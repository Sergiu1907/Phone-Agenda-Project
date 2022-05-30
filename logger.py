# debug("Mesaj") -> [DEBUG] Mesaj
# info("Mesaj") -> [INFO] Mesaj
# warining("Mesaj") -> [WARNING] Mesaj
# error("Mesaj") -> [ERROR] Mesaj
# critical("Mesaj") -> [CRITICAL] Mesaj

def log (level,msg):
    print ("[",level,"]",msg)

def debug (msg):
    log ("DEBUG",msg)


def info (msg):
    log ("INFO",msg)


def warning (msg):
    log ("WARNING", msg)


def error (msg):
    log ("ERROR", msg)


def critical (msg):
    log ("CRITICAL", msg)
