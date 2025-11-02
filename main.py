from classes.agent_class import Agent
from classes.mission_class import Mission
from classes.inteltools import IntelTools
from classes.report import Report
from classes.mission_control import MissionControl

agent1 = Agent("mester been", 8200)
report = Report("alibaba", 4, agent1.code_name)
MissionControl.analyze_report(report)
IntelTools.log_transmission(agent1.code_name,IntelTools.encrypt_massage("aridurlacher"))
