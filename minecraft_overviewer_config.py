worlds["Overworld"] = "world"
worlds["Nether"] = "world_nether"
worlds["The End"] = "world_the_end"

processes = 2
outputdir = "rendering2"
texturepath = "/root/dokucraft.zip"

# Overworld
renders["overworld_day_north"] = {
	"world": "Overworld",
	"title": "North",
	"rendermode": "smooth_lighting",
	"northdirection": "upper_left",
}

renders["overworld_day_east"] = {
	"world": "Overworld",
	"title": "East",
	"rendermode": "smooth_lighting",
	"northdirection": "lower_left",
}

renders["overworld_day_south"] = {
	"world": "Overworld",
	"title": "South",
	"rendermode": "smooth_lighting",
	"northdirection": "lower_right",
}

renders["overworld_day_west"] = {
	"world": "Overworld",
	"title": "West",
	"rendermode": "smooth_lighting",
	"northdirection": "upper_right",
}

# Overworld Cave
renders["overworld_cave_north"] = {
	"world": "Overworld",
	"title": "Cave North",
	"rendermode": "cave",
	"northdirection": "upper_left",
}

renders["overworld_cave_east"] = {
	"world": "Overworld",
	"title": "Cave East",
	"rendermode": "cave",
	"northdirection": "lower_left",
}

renders["overworld_cave_south"] = {
	"world": "Overworld",
	"title": "Cave South",
	"rendermode": "cave",
	"northdirection": "lower_right",
}

renders["overworld_cave_west"] = {
	"world": "Overworld",
	"title": "Cave West",
	"rendermode": "cave",
	"northdirection": "upper_right",
}

# Nether
renders["nether_north"] = {
	"world": "Nether",
	"title": "North",
	"rendermode": "nether_smooth_lighting",
	"northdirection": "upper_left",
}

renders["nether_smooth_lighting_east"] = {
	"world": "Nether",
	"title": "East",
	"rendermode": "nether_smooth_lighting",
	"northdirection": "lower_left",
}

renders["nether_smooth_lighting_south"] = {
	"world": "Nether",
	"title": "South",
	"rendermode": "nether_smooth_lighting",
	"northdirection": "lower_right",
}

renders["nether_smooth_lighting_west"] = {
	"world": "Nether",
	"title": "West",
	"rendermode": "nether_smooth_lighting",
	"northdirection": "upper_right",
}

# The End
renders["end_north"] = {
	"world": "The End",
	"title": "North",
	"rendermode": "smooth_lighting",
	"northdirection": "upper_left",
}

renders["end_east"] = {
	"world": "The End",
	"title": "East",
	"rendermode": "smooth_lighting",
	"northdirection": "lower_left",
}

renders["end_south"] = {
	"world": "The End",
	"title": "South",
	"rendermode": "smooth_lighting",
	"northdirection": "lower_right",
}

renders["end_west"] = {
	"world": "The End",
	"title": "West",
	"rendermode": "smooth_lighting",
	"northdirection": "upper_right",
}
