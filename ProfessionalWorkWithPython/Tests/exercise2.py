

def get_lowest_course(courses, mentors, durations):
	courses_list = []
	for cours, mentors, duration in zip(courses, mentors, durations):
		course_dict = {
			"title": cours,
			"mentors": mentors,
			"duration": duration
		}
		courses_list.append(course_dict)
	minis = []
	for index, duration in enumerate(durations):
		if duration == min(durations):
			minis.append(index)
	courses_min = []
	for id in minis:
		courses_min.append(courses_list[id]["title"])
	return ", ".join(courses_min)


def get_highest_course(courses, mentors, durations):
	courses_list = []
	for cours, mentors, duration in zip(courses, mentors, durations):
		course_dict = {
			"title": cours,
			"mentors": mentors,
			"duration": duration
		}
		courses_list.append(course_dict)
	maxes = []
	for index, duration in enumerate(durations):
		if duration == max(durations):
			maxes.append(index)
	courses_max = []
	for id in maxes:
		courses_max.append(
			courses_list[id]["title"])
	return ", ".join(courses_max)


