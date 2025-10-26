from classes.agent_class import Agent
from classes.mission_class import Mission

mission = Mission("barabosa", "moskva")
mission.assigned(Agent("uri", 255))
mission.brief()