import sqlite3
import pathlib
import os.path
import typing

class RailOSDatabase:
    DATABASE_FILE = os.path.join(
        pathlib.Path(__file__).parents[1],
        "database",
        "trainset.sqlite"
    )
    INIT_SCRIPT = os.path.join(
        pathlib.Path(__file__).parents[1],
        "database",
        "create_tables.sql"
    )
    def __init__(self) -> None:
        self._connection: typing.Optional[sqlite3.Connection] = None
        self._cursor: typing.Optional[sqlite3.Cursor] = None

    def __enter__(self) -> "RailOSDatabase":
        self._connection = sqlite3.connect(self.DATABASE_FILE)
        self._cursor = self._connection.cursor()
        self._init_db()
        return self

    def _init_db(self) -> None:
        with open(self.INIT_SCRIPT) as init_script:
            self._cursor.executescript(init_script.read())

    def get_train(self, name: str, country_code: str) -> typing.Dict[str, typing.Any]:
        _query = f"SELECT * FROM trainset WHERE name LIKE '%{name}%' AND country='{country_code}'"
        print(f"QUERY {_query}")
        self._cursor.execute(_query)
        names = [description[0] for description in self._cursor.description]
        results = self._cursor.fetchall()
        if not results:
            return {}
        return [dict(zip(names, result)) for result in results]

    def __exit__(self, *args, **kwargs) -> None:
        self._connection.commit()
        self._connection.close()


if __name__ in "__main__":
    with RailOSDatabase() as raildb:
        pass
