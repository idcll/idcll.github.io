from flask import Flask, render_template

app = Flask(__name__)

standings = [
    {"pos": 1, "driver": "Denny Hamlin", "points": 791},
    {"pos": 2, "driver": "Tyler Reddick", "points": 767},
    {"pos": 3, "driver": "Ryan Blaney", "points": 726},
    {"pos": 4, "driver": "Ty Gibbs", "points": 665},
    {"pos": 5, "driver": "Chase Elliott", "points": 610},
]

races = [
    {
        "date": "19 Jul 2025",
        "track": "North Wilkesboro Speedway",
        "status": "Próxima"
    },
    {
        "date": "26 Jul 2025",
        "track": "Indianapolis Motor Speedway",
        "status": "Pendiente"
    },
    {
        "date": "9 Ago 2025",
        "track": "Iowa Speedway",
        "status": "Pendiente"
    },
    {
        "date": "15 Ago 2025",
        "track": "Watkins Glen",
        "status": "Pendiente"
    },
    {
        "date": "23 Ago 2025",
        "track": "New Hampshire Motor Speedway",
        "status": "Pendiente"
    },
    {
        "date": "29 Ago 2025",
        "track": "Daytona International Speedway",
        "status": "Pendiente"
    }
]

drivers_list = [
    {"number": 1, "name": "Ross Chastain", "team": "Trackhouse Racing", "manufacturer": "Chevrolet"},
    {"number": 2, "name": "Austin Cindric", "team": "Team Penske", "manufacturer": "Ford"},
    {"number": 3, "name": "Austin Dillon", "team": "Richard Childress Racing", "manufacturer": "Chevrolet"},
    {"number": 4, "name": "Noah Gragson", "team": "Front Row Motorsports", "manufacturer": "Ford"},
    {"number": 5, "name": "Kyle Larson", "team": "Hendrick Motorsports", "manufacturer": "Chevrolet"},
    {"number": 6, "name": "Brad Keselowski", "team": "RFK Racing", "manufacturer": "Ford"},
    {"number": 7, "name": "Daniel Suarez", "team": "Spire Motorsports", "manufacturer": "Chevrolet"},
    {"number": 8, "name": "Kyle Busch (Q.E.P.D.)", "team": "Richard Childress Racing", "manufacturer": "Chevrolet"},
    {"number": 9, "name": "Chase Elliott", "team": "Hendrick Motorsports", "manufacturer": "Chevrolet"},
    {"number": 10, "name": "Ty Dillon", "team": "Kaulig Racing", "manufacturer": "Chevrolet"},
    {"number": 11, "name": "Denny Hamlin", "team": "Joe Gibbs Racing", "manufacturer": "Toyota"},
    {"number": 12, "name": "Ryan Blaney", "team": "Team Penske", "manufacturer": "Ford"},
    {"number": 16, "name": "AJ Allmendinger", "team": "Kaulig Racing", "manufacturer": "Chevrolet"},
    {"number": 17, "name": "Chris Buescher", "team": "RFK Racing", "manufacturer": "Ford"},
    {"number": 19, "name": "Chase Briscoe", "team": "Joe Gibbs Racing", "manufacturer": "Toyota"},
    {"number": 20, "name": "Christopher Bell", "team": "Joe Gibbs Racing", "manufacturer": "Toyota"},
    {"number": 21, "name": "Josh Berry", "team": "Wood Brothers Racing", "manufacturer": "Ford"},
    {"number": 22, "name": "Joey Logano", "team": "Team Penske", "manufacturer": "Ford"},
    {"number": 23, "name": "Bubba Wallace", "team": "23XI Racing", "manufacturer": "Toyota"},
    {"number": 33, "name": "Austin Hill*", "team": "Richard Childress Racing", "manufacturer": "Chevrolet"},
    {"number": 24, "name": "William Byron", "team": "Hendrick Motorsports", "manufacturer": "Chevrolet"},
    {"number": 34, "name": "Todd Gilliland", "team": "Front Row Motorsports", "manufacturer": "Ford"},
    {"number": 35, "name": "Riley Herbst", "team": "23XI Racing", "manufacturer": "Toyota"},
    {"number": 38, "name": "Zane Smith", "team": "Front Row Motorsports", "manufacturer": "Ford"},
    {"number": 41, "name": "Cole Custer", "team": "Haas Factory Team", "manufacturer": "Ford"},
    {"number": 42, "name": "John Hunter Nemechek", "team": "Legacy Motor Club", "manufacturer": "Toyota"},
    {"number": 43, "name": "Erik Jones", "team": "Legacy Motor Club", "manufacturer": "Toyota"},
    {"number": 45, "name": "Tyler Reddick", "team": "23XI Racing", "manufacturer": "Toyota"},
    {"number": 47, "name": "Ricky Stenhouse Jr.", "team": "Hyak Motorsports", "manufacturer": "Chevrolet"},
    {"number": 48, "name": "Alex Bowman", "team": "Hendrick Motorsports", "manufacturer": "Chevrolet"},
    {"number": 51, "name": "Cody Ware", "team": "Rick Ware Racing", "manufacturer": "Ford"},
    {"number": 54, "name": "Ty Gibbs", "team": "Joe Gibbs Racing", "manufacturer": "Toyota"},
    {"number": 71, "name": "Michael McDowell", "team": "Spire Motorsports", "manufacturer": "Chevrolet"},
    {"number": 77, "name": "Carson Hocevar", "team": "Spire Motorsports", "manufacturer": "Chevrolet"},
    {"number": 88, "name": "Shane van Gisbergen", "team": "Trackhouse Racing", "manufacturer": "Chevrolet"},
]

@app.route("/")
def inicio():
    return render_template(
        "index.html",
        standings=standings
    )

@app.route("/drivers")
def drivers():
    return render_template(
        "drivers.html",
        drivers=drivers_list
    )

@app.route("/schedule")
def schedule():
    return render_template(
        "schedule.html",
        races=races
    )

@app.route("/stats")
def stats():
    return render_template("stats.html")

@app.route("/news")
def news():
    return render_template("news.html")

if __name__ == "__main__":
    app.run(debug=True)