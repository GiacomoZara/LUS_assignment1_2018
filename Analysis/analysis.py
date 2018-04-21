#!/usr/bin/env python
import plotly
from plotly.graph_objs import Bar, Layout, Margin
plotly.offline.init_notebook_mode(connected=True)

def extract_concept(raw_concept):
	cond1 = raw_concept.startswith('B-')
	cond2 = raw_concept.startswith('I-')
	cond3 = raw_concept.startswith('E-')

	if cond1 or cond2 or cond3:
		res = raw_concept[2:]
	else:
		res = raw_concept

	return res

training_file = open('LUS.P1/data/P1_data/data/NLSPARQL.train.data')

concepts_count = {}

for line in training_file:
	line_split = line.split()
	if len(line.split()) > 0:
		raw_concept = str(line.split()[1])
		concept = extract_concept(raw_concept)
		if concepts_count.get(concept):
			concepts_count[concept] += 1
		else:
			concepts_count[concept] = 1

print(concepts_count)

data = []
for concept in concepts_count:
	data.append(concepts_count[concept])

data = [go.Histogram(x=data)]


py.iplot(data, filename='basic histogram')
