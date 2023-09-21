#!/usr/bin/env python3
"""this module contains a function that returns an obfuscated log message"""


import re
import logging
import os
import mysql.connector
from typing import List

PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Uses `filter_datum` to edit lines for our log files.
        """
        record.msg = filter_datum(self.fields, RedactingFormatter.REDACTION,
                                  record.msg, RedactingFormatter.SEPARATOR)
        return super().format(record)


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    """
    edits lines for our log files, aww yeah
    """
    new_str = message
    for item in fields:
        new_str = re.sub('{}=.*?(?={})'.format(item, separator),
                         '{}={}'.format(item, redaction),
                         new_str)
    return new_str


def get_logger() -> logging.Logger:
    """
    creates a logger object with the correct data hidden
    """
    new_logger: logging.Logger = logging.getLogger('user_data')
    new_logger.setLevel(logging.INFO)
    new_logger.propagate = False
    handler: logging.StreamHandler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(PII_FIELDS))
    new_logger.addHandler(handler)
    return new_logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    returns a connector to a MySQL database for our use.
    """
    return mysql.connector.\
        connect(user=os.getenv('PERSONAL_DATA_DB_USERNAME', 'root'),
                password=os.getenv('PERSONAL_DATA_DB_PASSWORD', ''),
                host=os.getenv('PERSONAL_DATA_DB_HOST', 'localhost'),
                database=os.getenv('PERSONAL_DATA_DB_NAME')
                )


def main() -> None:
    """
    entry point for the program, returns nothing
    """
    logger = get_logger()
    db: mysql.connector.connection.MySQLConnection = get_db()
    cursor = db.cursor()

    query = ("SELECT * FROM users;")

    cursor.execute(query)
    users = cursor.fetchall()
    field_names = [i[0] for i in cursor.description]
    for user in users:
        user_dict = dict(zip(field_names, user))
        user_str = RedactingFormatter.SEPARATOR.join(
            f"{key}={value}" for key, value in user_dict.items()
        )
        logger.info(user_str)

    db.close()


if __name__ == '__main__':
    main()
