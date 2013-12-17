import urllib
import re

def get_info(Term, Subject):
	url = "https://ssbp.mycampus.ca/prod/bwckschd.p_get_crse_unsec?TRM=U&term_in=" + Term + "&sel_subj=dummy&sel_day=dummy&sel_schd=dummy&sel_insm=dummy&sel_camp=dummy&sel_levl=dummy&sel_sess=dummy&sel_instr=dummy&sel_ptrm=dummy&sel_attr=dummy&sel_subj=" + Subject + "&sel_crse=&sel_title=&sel_from_cred=&sel_to_cred=&sel_camp=UON&begin_hh=0&begin_mi=0&begin_ap=a&end_hh=0&end_mi=0&end_ap=a"
	htmltext = urllib.urlopen(url).read();
	regex = '<TH CLASS="ddheader" scope="col" >(.+?)<BR><BR></TH>'
	pattern = re.compile(regex)
	courses = re.split(pattern, htmltext)
	re.purge()
	for course in courses:
		regex = '<TD CLASS="dbdefault">(.+?)</TD>\n<TD CLASS="dbdefault">(.+?)</TD>\n<TD CLASS="dbdefault">(.+?) - (.+?)</TD>\n<TD CLASS="dbdefault">(.+?)</TD>\n<TD CLASS="dbdefault">(.+?)</TD>\n<TD CLASS="dbdefault">(.+?) - (.+?)</TD>\n<TD CLASS="dbdefault">(.+?)</TD>\n<TD CLASS="dbdefault">(.+?) \(<ABBR title= "Primary">P</ABBR>\)</TD>'
		regex2 = '<TD CLASS="dbdefault">(.+?)</TD>\n<TD CLASS="dbdefault">(.+?)</TD>\n<TD CLASS="dbdefault">(.+?) - (.+?)</TD>\n<TD CLASS="dbdefault">(.+?)</TD>\n<TD CLASS="dbdefault">(.+?)</TD>\n<TD CLASS="dbdefault">(.+?) - (.+?)</TD>\n<TD CLASS="dbdefault">(.+?)</TD>\n<TD CLASS="dbdefault"><ABBR title = "To Be Announced">(.+?)</ABBR></TD>'
		regex3 = '<TD CLASS="dbdefault">(.+?)</TD>\n<TD CLASS="dbdefault">(.+?)</TD>\n<TD CLASS="dbdefault"><ABBR title = "To Be Announced">(.+?)</ABBR></TD>\n<TD CLASS="dbdefault">(.+?)</TD>\n<TD CLASS="dbdefault"><ABBR title = "To Be Announced">(.+?)</ABBR></TD>\n<TD CLASS="dbdefault">(.+?) - (.+?)</TD>\n<TD CLASS="dbdefault">(.+?)</TD>\n<TD CLASS="dbdefault"><ABBR title = "To Be Announced">(.+?)</ABBR></TD>'
		regex4 = '<TD CLASS="dbdefault">(.+?)</TD>\n<TD CLASS="dbdefault">(.+?)</TD>\n<TD CLASS="dbdefault">(.+?) - (.+?)</TD>\n<TD CLASS="dbdefault">(.+?)</TD>\n<TD CLASS="dbdefault">(.+?)</TD>\n<TD CLASS="dbdefault">(.+?) - (.+?)</TD>\n<TD CLASS="dbdefault">(.+?)</TD>\n<TD CLASS="dbdefault">(.+?) \(<ABBR title= "Primary">P</ABBR>\)(.+)?</TD>'
		pattern = re.compile(regex)
		pattern2 = re.compile(regex2)
		pattern3 = re.compile(regex3)
		pattern4 = re.compile(regex4)
		entries = re.findall(pattern, course)				#this pattern is for default structure of courses
		if entries:											 
			print entries
		else:
			entries = re.findall(pattern2, course)			#this pattern is for instructor TBA
			if entries:
				print entries
			else:
				entries = re.findall(pattern3, course)		#this pattern is for courses that do not have a start time or class assigned
				if entries:
					print entries
				else:
					entries = re.findall(pattern4, course)	#this pattern returns two values for instructor
					print entries


#TermList = open("Webscraper/term.txt").read().split("\n")
#ProgramList = open("Webscraper\prog.txt").read().split("\n"
t = get_info("201401", "CSCI")



