"""
Simple script to demonstrate handling dictionaries

No need to change this, just review the code and make sure you understand it!

Dictionaries are a powerful tool for organizing and accessing data in Python.

Learn to use them well!

"""
# https://en.wikipedia.org/wiki/Super_Bowl_XIV#Starting_lineups
# Given data as list of strings, or TAB separated strings
UNITS = ["Offense", "Defense", "Kickers"]

HEADING_DATA ="Los Angeles	Position	Pittsburgh"

# Lists of TAB separated strings
OFFENSE_LINES = ["Billy Waddy	WR	John Stallworth",
"Doug France	LT	Jon Kolb",
"Kent Hill	LG	Sam Davis",
"Rich Saul	C	Mike Webster",
"Dennis Harrah	RG	Gerry Mullins",
"Jackie Slater	RT	Larry Brown",
"Terry Nelson	TE	Bennie Cunningham",
"Preston Dennard	WR	Lynn Swann",
"Vince Ferragamo	QB	Terry Bradshaw",
"Cullen Bryant	FB	Franco Harris",
"Wendell Tyler	HB	Rocky Bleier"]

DEFENSE_LINES = ['Jack Youngblood	LE	L. C. Greenwood',
'Mike Fanning	LT	Joe Greene',
'Larry Brooks	RT	Gary Dunn',
'Fred Dryer	RE	John Banaszak',
'Jim Youngblood	LLB	Dennis Winston',
'Jack Reynolds	MLB	Jack Lambert',
'Bob Brudzinski	RLB	Robin Cole',
'Pat Thomas	LCB	Ron Johnson',
'Rod Perry	RCB	Mel Blount',
'Dave Elmendorf	SS	Donnie Shell',
'Nolan Cromwell	FS	J. T. Thomas']

SPEC_LINES = ["Frank Corral	K	Matt Bahr", "Ken Clark	P	Craig Colquitt"]


def print_team(team_name, team_dict):
    """
    Helper function for printing the roster of specific team
    @param team_name : Name of team (for labeling in header)
    @param team_dict : Dictionary of Dictionaries containing roster by unit
    @return Nothing
    """
    print(f"\n\n======== {team_name} =========")
    for unit_name, unit_dict in team_dict.items():
        print(f" ------- {unit_name} -------")
        print(" ---- Posn - Player ----")
        for posn, player_name in unit_dict.items():
            print(f"    {posn:>4s}   {player_name}")


# Convert strings to lists of lists using list comprehension
heading_data = [val.strip() for val in HEADING_DATA.split("\t")]
print(heading_data)

team1 = heading_data[0]
team2 = heading_data[-1]  # last team name in list of strings

# Declare dictionary to hold the data
teams = {} # empty base dictionary to hold info per team

# Declare a dictionary per team (dictionary of dictionaries)
teams[team1] = dict()  # Empty dictionary for roster of each team
teams[team2] = dict()  # Empty dictionary (dict() and {} both work (PyLint prefers dict())

# Print showing empty dictionaries
print("Teams:")
print(teams)


# Set up offense, defense, and kickers dictionaries for each team
# So, we now have a dictionary (team) of dictionaries (units) of dictionaries (position)
# Demoing for (each) key in dictionary loop
# PyLint suggests using key, value in teams.items() style loop
for team in teams:
    for unit in UNITS:
        teams[team][unit] = dict()  # Empty dictionary (or set)

# Demo for (each) key, value in dictionary items loop
print("Storage pattern:")
print(teams)
print(30*"-")
for name, team_data in teams.items():  # PyLint's preferred approach to iterating
    print(name)
    print(team_data)

# Read in data from strings and populate the dictionaries
print(30*"-")
print(30*"-")
for line in OFFENSE_LINES:
    player1, position, player2 = line.split("\t")
    teams[team1]["Offense"][position] = player1  # Note: This depends on matching Unit key string
    teams[team2]["Offense"][position] = player2

for line in DEFENSE_LINES:
    player1, position, player2 = line.split("\t")
    teams[team1]["Defense"][position] = player1
    teams[team2]["Defense"][position] = player2

for line in SPEC_LINES:
    player1, position, player2 = line.split("\t")
    teams[team1]["Kickers"][position] = player1
    teams[team2]["Kickers"][position] = player2


# Now access our data and print
print("\n\nSuper Bowl XIV (January 1981)")
# could have used PyLint's preferred for team_name, team_data in teams.items() loop as well.
for team in teams:
    print_team(team, teams[team])

print("\n\n")
print("Steelers win!")

# Demonstrate accessing data by key.  Note, this is processed left to right,
# The code below is equivalent to:
#   pittsburg_team = teams["Pittsburgh"]
#   pittsburg_offense = pittsburg_team["Offense"]
pittsburgh_offense = teams["Pittsburgh"]["Offense"]
print("         Offensive QB for the Steelers: ", pittsburgh_offense["QB"])
print("Left defensive tackle for the Steelers: ", teams["Pittsburgh"]["Defense"]["LT"])
