import psycopg2

try:
    conn = psycopg2.connect(
    dbname="APP",
    host="localhost",
    user="postgres",
    password = 's197328645S!'    
    )
    print('Success!')
except:
    print('Cannot connect to databse') 
print(conn)
cur = conn.cursor()

    # Database init
try:
    cur.execute("CREATE TABLE goods (id serial NOT NULL, PRIMARY KEY (id), name text, value numeric(4,2), quantity integer);")
    cur.execute("INSERT INTO goods (name, value, quantity) VALUES ('Apple', 15.5, 10);")
    conn.commit()
    print('Table created, record inserted')
except:
    print('Failure!')

test = cur.execute("SELECT * FROM goods;")

print(test)

cur.close()
conn.close()