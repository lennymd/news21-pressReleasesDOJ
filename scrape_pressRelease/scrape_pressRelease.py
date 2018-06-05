import requests
import urllib.parse as parse
from bs4 import BeautifulSoup
import lxml
from time import sleep
import csv
from pathlib import Path

#Import csv with the relative urls as an array
url_list = []
out_pr_list = []
with open('out_url_list_withoutHeader.csv') as csvDataFile:
	csvReader = csv.reader(csvDataFile)
	for row in csvReader:
		url_list.append(row)

url_list_length = len(url_list) #Should be 12694 as of 4-15-18 
baseurl = "https://www.justice.gov"

for i in range(0,1):
	i = url_list_length+1
	#Outfiles from the search
	outfile_html = "pressReleases/release_%05d.html" % i
	outfile_txt = "pressReleases_txt/release_%05d.txt" % i

	#Add in code to check if html file exists. If it exists, pass to checking if txt file exists.
	#Add in code to check if txt file exists. If true, go to next iteration.

	#Get the i-th press release
	rel_url = url_list[i][3]
	abs_url = baseurl + rel_url
	#print(abs_url)

	#Let's get that website content
	response = requests.get(abs_url)
	html = response.text
	html = html.encode('ascii','ignore').decode('utf-8')
	html = parse.unquote(html)

	#Now we save a copy of the page for just in case
	out = open(outfile_html, 'w+')
	out.write(html)
	out.close()

	try:
		page_of_interest = BeautifulSoup(html,"lxml")

		#Piece 1: get all the body text into txt file
		body = page_of_interest.find('div', class_="field field--name-field-pr-body field--type-text-long field--label-hidden")
		body_grafs = body.find_all('p')
		#print(len(body_grafs))

		
		#Let's get all the text to be in one string
		grafs = ''
		for g in range(0,len(body_grafs)):
			new_graf = body_grafs[g]
			if len(new_graf) > 0: 
				grafs = grafs + str(new_graf.string)
			else:
				if g == len(body_grafs):
					pass
				else:
					grafs = grafs + " "

		#Now we take that string and write it to the output txt file
		out_txt = open(outfile_txt, 'w+')
		out_txt.write(grafs)
		out_txt.close()

		sleep(0.25)

		#Piece 2: Let's get the pr-fields: topics, components, and pr_number
		topics = ''
		components = ''
		pr_number = ''

		topic_field = page_of_interest.find('div',class_="field field--name-field-pr-topic field--type-taxonomy-term-reference field--label-above")
		if topic_field: 
			all_topics = topic_field.find('div',class_='field__items').find_all('div')
			for l in range(0,len(all_topics)):
					topics = topics + str(all_topics[l].string) + '; '
		else:
			print("No topics found for release #"+ str(i))
			topics = 'None'
			pass

		component_field = page_of_interest.find('div', class_='field field--name-field-pr-component field--type-taxonomy-term-reference field--label-above')
		if component_field:
			all_components = component_field.find('div',class_='field__items').find_all('a')
			for l in range(0,len(all_components)):
				components = components + str(all_components[l].string) + '; '
		else:
			print("No components found for release #"+ str(i))
			components = 'None'
			pass

		pr_number_field = page_of_interest.find('div',class_="field field--name-field-pr-number field--type-text field--label-above")
		if pr_number_field:
			all_pr_number = pr_number_field.find('div',class_='field__items').find_all('div')
			for l in range(0,len(all_pr_number)):
				pr_number = pr_number + str(all_pr_number[l].string)+ '; '
		else:
			print("No Press Release number found for release #"+ str(i))
			pr_number = 'None'
			pass

		#Let's store all the fields in the same csv file that matches the id number of the press release
		out_pr_list.append([i, topics, components, pr_number ])
		with open("out_pr_list.csv","r+") as my_csv:
			csvWriter = csv.writer(my_csv,delimiter=',')
			csvWriter.writerows(out_pr_list)

	except Exception as e: print(e)
	print("UPDATE: Done with press release #" + str(i))
	sleep(3) #sleep 3 seconds in between link iterations
