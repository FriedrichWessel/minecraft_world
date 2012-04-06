worlds["Overworld Day"] = "/home/surma/minecraft/minecraft_world/world"
worlds["Overworld Night"] = "/home/surma/minecraft/minecraft_world/world"
worlds["Overworld Cave"] = "/home/surma/minecraft/minecraft_world/world"
worlds["Nether"] = "/home/surma/minecraft/minecraft_world/world_nether"
worlds["The End"] = "/home/surma/minecraft/minecraft_world/world_the_end"

processes = 12
outputdir = "/home/surma/minecraft/rendering"

# Overworld Day
renders["overworld_day_north"] = {
	"world": "Overworld Day",
	"title": "North",
	"rendermode": "smooth_lighting",
	"northdirection": "upper_left",
}

renders["overworld_day_east"] = {
	"world": "Overworld Day",
	"title": "East",
	"rendermode": "smooth_lighting",
	"northdirection": "lower_left",
}

renders["overworld_day_south"] = {
	"world": "Overworld Day",
	"title": "South",
	"rendermode": "smooth_lighting",
	"northdirection": "lower_right",
}

renders["overworld_day_west"] = {
	"world": "Overworld Day",
	"title": "West",
	"rendermode": "smooth_lighting",
	"northdirection": "upper_right",
}

# Overworld Night
renders["overworld_night_north"] = {
	"world": "Overworld Night",
	"title": "North",
	"rendermode": "smooth_night",
	"northdirection": "upper_left",
}

renders["overworld_night_east"] = {
	"world": "Overworld Night",
	"title": "East",
	"rendermode": "smooth_night",
	"northdirection": "lower_left",
}

renders["overworld_night_south"] = {
	"world": "Overworld Night",
	"title": "South",
	"rendermode": "smooth_night",
	"northdirection": "lower_right",
}

renders["overworld_night_west"] = {
	"world": "Overworld Night",
	"title": "West",
	"rendermode": "smooth_night",
	"northdirection": "upper_right",
}

# Overworld Cave
renders["overworld_cave_north"] = {
	"world": "Overworld Cave",
	"title": "North",
	"rendermode": "cave",
	"northdirection": "upper_left",
}

renders["overworld_cave_east"] = {
	"world": "Overworld Cave",
	"title": "East",
	"rendermode": "cave",
	"northdirection": "lower_left",
}

renders["overworld_cave_south"] = {
	"world": "Overworld Cave",
	"title": "South",
	"rendermode": "cave",
	"northdirection": "lower_right",
}

renders["overworld_cave_west"] = {
	"world": "Overworld Cave",
	"title": "West",
	"rendermode": "cave",
	"northdirection": "upper_right",
}

# Nether
renders["nether_north"] = {
	"world": "Nether",
	"title": "North",
	"rendermode": "nether",
	"northdirection": "upper_left",
}

renders["nether_east"] = {
	"world": "Nether",
	"title": "East",
	"rendermode": "nether",
	"northdirection": "lower_left",
}

renders["nether_south"] = {
	"world": "Nether",
	"title": "South",
	"rendermode": "nether",
	"northdirection": "lower_right",
}

renders["nether_west"] = {
	"world": "Nether",
	"title": "West",
	"rendermode": "nether",
	"northdirection": "upper_right",
}

# The End
renders["end_north"] = {
	"world": "The End",
	"title": "North",
	"rendermode": "normal",
	"northdirection": "upper_left",
}

renders["end_east"] = {
	"world": "The End",
	"title": "East",
	"rendermode": "normal",
	"northdirection": "lower_left",
}

renders["end_south"] = {
	"world": "The End",
	"title": "South",
	"rendermode": "normal",
	"northdirection": "lower_right",
}

renders["end_west"] = {
	"world": "The End",
	"title": "West",
	"rendermode": "normal",
	"northdirection": "upper_right",
}
