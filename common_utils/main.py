import kuzu

def main() -> None:
    # Initialize database
    db = kuzu.Database("common_utils/demo_db")
    conn = kuzu.Connection(db)

    # Create schema
    conn.execute("CREATE NODE TABLE User(name STRING, age INT64, PRIMARY KEY (name))")
    conn.execute("CREATE NODE TABLE City(name STRING, population INT64, PRIMARY KEY (name))")
    conn.execute("CREATE REL TABLE Follows(FROM User TO User, since INT64)")
    conn.execute("CREATE REL TABLE LivesIn(FROM User TO City)")

    # Insert data
    conn.execute('COPY User FROM "common_utils/data/user.csv"')
    conn.execute('COPY City FROM "common_utils/data/city.csv"')
    conn.execute('COPY Follows FROM "common_utils/data/follows.csv"')
    conn.execute('COPY LivesIn FROM "common_utils/data/lives-in.csv"')

    # Execute Cypher query
    response = conn.execute(
        """
        MATCH (a:User)-[f:Follows]->(b:User)
        RETURN a.name, b.name, f.since;
        """
    )
    while response.has_next():
        print(response.get_next())
main()