import sqlite3


def main():
    # Connect to the database.
    conn = sqlite3.connect('cities.db')

    # Get a database cursor.
    cur = conn.cursor()

    # Add the Cities table.
    add_cities_table(cur)

    # Add rows to the Cities table.
    add_cities(cur)

    # Commit the changes.
    conn.commit()

    # Display the cities (your original function)
    display_cities(cur)

    # --- ADDED REQUIRED OUTPUTS BELOW ---
    print("\n--- Cities Sorted By Population (Ascending) ---")
    show_sorted_population_asc(cur)

    print("\n--- Cities Sorted By Population (Descending) ---")
    show_sorted_population_desc(cur)

    print("\n--- Cities Sorted By Name ---")
    show_sorted_name(cur)

    print("\n--- Total Population ---")
    show_total_population(cur)

    print("\n--- Average Population ---")
    show_average_population(cur)

    print("\n--- City With Highest Population ---")
    show_highest_population(cur)

    print("\n--- City With Lowest Population ---")
    show_lowest_population(cur)

    # Close the connection.
    conn.close()


# -----------------------------------------------------------------------
# ORIGINAL FUNCTIONS
# -----------------------------------------------------------------------

def add_cities_table(cur):
    cur.execute('DROP TABLE IF EXISTS Cities')
    cur.execute('''CREATE TABLE Cities (CityID INTEGER PRIMARY KEY NOT NULL,
                                        CityName TEXT,
                                        Population REAL)''')


def add_cities(cur):
    cities_pop = [(1, 'Tokyo', 38001000),
                  (2, 'Delhi', 25703168),
                  (3, 'Shanghai', 23740778),
                  (4, 'Sao Paulo', 21066245),
                  (5, 'Mumbai', 21042538),
                  (6, 'Mexico City', 20998543),
                  (7, 'Beijing', 20383994),
                  (8, 'Osaka', 20237645),
                  (9, 'Cairo', 18771769),
                  (10, 'New York', 18593220),
                  (11, 'Dhaka', 17598228),
                  (12, 'Karachi', 16617644),
                  (13, 'Buenos Aires', 15180176),
                  (14, 'Kolkata', 14864919),
                  (15, 'Istanbul', 14163989),
                  (16, 'Chongqing', 13331579),
                  (17, 'Lagos', 13122829),
                  (18, 'Manila', 12946263),
                  (19, 'Rio de Janeiro', 12902306),
                  (20, 'Guangzhou', 12458130)]

    for row in cities_pop:
        cur.execute('''INSERT INTO Cities (CityID, CityName, Population)
                           VALUES (?, ?, ?)''', (row[0], row[1], row[2]))


def display_cities(cur):
    print('Contents of cities.db/Cities table:')
    cur.execute('SELECT * FROM Cities')
    results = cur.fetchall()
    for row in results:
        print(f'{row[0]:<3}{row[1]:20}{row[2]:,.0f}')


# -----------------------------------------------------------------------
# ADDED FUNCTIONS FOR THE 7 REQUIRED TASKS
# -----------------------------------------------------------------------

def show_sorted_population_asc(cur):
    cur.execute("SELECT CityName, Population FROM Cities ORDER BY Population ASC")
    for city, pop in cur.fetchall():
        print(f"{city:20} {pop:,.0f}")


def show_sorted_population_desc(cur):
    cur.execute("SELECT CityName, Population FROM Cities ORDER BY Population DESC")
    for city, pop in cur.fetchall():
        print(f"{city:20} {pop:,.0f}")


def show_sorted_name(cur):
    cur.execute("SELECT CityName, Population FROM Cities ORDER BY CityName ASC")
    for city, pop in cur.fetchall():
        print(f"{city:20} {pop:,.0f}")


def show_total_population(cur):
    cur.execute("SELECT SUM(Population) FROM Cities")
    total = cur.fetchone()[0]
    print(f"Total Population: {total:,.0f}")


def show_average_population(cur):
    cur.execute("SELECT AVG(Population) FROM Cities")
    avg = cur.fetchone()[0]
    print(f"Average Population: {avg:,.2f}")


def show_highest_population(cur):
    cur.execute("SELECT CityName, Population FROM Cities ORDER BY Population DESC LIMIT 1")
    city = cur.fetchone()
    print(f"{city[0]} - {city[1]:,.0f}")


def show_lowest_population(cur):
    cur.execute("SELECT CityName, Population FROM Cities ORDER BY Population ASC LIMIT 1")
    city = cur.fetchone()
    print(f"{city[0]} - {city[1]:,.0f}")


# Run the program
if __name__ == '__main__':
    main()