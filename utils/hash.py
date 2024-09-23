import os
from passlib.context import CryptContext

passwordContext = CryptContext(schemes=["bcrypt"], deprecated="auto")


def generateHash(rowPassword: str) -> str:
    return passwordContext.hash(rowPassword)

def verifyHash(rowPassword: str, hashedPassword: str) -> bool:
    return passwordContext.verify(rowPassword, hashedPassword)