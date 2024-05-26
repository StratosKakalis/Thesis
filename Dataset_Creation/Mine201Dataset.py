import requests
import json

# Raw string of natural language questions
questions_str = """1. How many hospitals are there in Oxford?	2. How many underground lines does London have?	3. How many counties does England have?
4. Which restaurants are close to London Bridge?	5. Is there any hospital in a range of 1 km from Jubilee Gardens in London?	6. Which counties border county Lincolnshire?
7. Where is Loch Goil located?	8. Which bridges cross river Thames?	9. What is the number of universities in London?
10. Which rivers are in Wales?	11. Which counties of Scotland border England?	12. Where is Nelson's Column located?
13. Does the county of Durham border Essex?	14. Which restaurants are at most 1km away from Big Ben?	15. Is county Oxfordshire east of the county Essex?
16. Which pubs in Dublin are near Guinness Brewery?	17. Which hospitals in Liverpool are near Abercromby Square?	18. Which cafes in London are at most 3 km from St. Anthony the Great and St. John the Baptist church?
19. Which department stores are at most 2km from Central Park hotel in London?	20. Which universities are in county Essex?	21. Is there a church at most 2km from the University of Westminster?
22. Is there a mountain in the county of Greater Manchester taller than 1300 meters above sea level?	23. Which mountains in Scotland have height more than 1000 meters?	24. What's the name of the river that runs through London?
25. How many cities does Thames river crosses?	26. Which districts border London?	27. Which are the metropolitan counties of England?
28. What is the name of the river that flows under the Queensway Bridge in Liverpool?	29. Is Hampshire north of Berkshire?	30. Is there any stadium in Cardiff?
31. Which aerodromes are at most 50km from London?	32. How many rivers cross the county West Yorkshire?	33. Which are the counties of Northern Ireland?
34. Is there a National Park in England?	35. Is Cavan a county of Ireland?	36. Which lakes are in Ireland?
37. Are there cities that are at most 2km away from St. David's in Wales?	38. Is Alnwick Castle in Scotland?	39. Which colleges are in London?
40. How many districts does Northern Ireland have?	41. Which pubs are near Mercure Hotel in Glasgow	42. Is there a mountain within 20km of Cheshire?
43. Does London have a mountain?	44. Is Islington near Angel?	45. Is there a car park near a bridge on river Exe?
46. Which medieval castles are in Scotland?	47. Which bars are near Prince's street in Edinburgh?	48. Which hotels are near Loch Ness?
49. Is Liverpool part of Scotland?	50. Which museums are within 3km of Saint George's hotel in London?	51. How many rivers cross Edinburgh?
52. Which county is east of county Dorset?	53. In what county is Stonehenge located?	54. Is there a forest in county Cheshire?
55. How many counties does the river Thames cross?	56. Is there a river that crosses county Greater Manchester?	57. Is there a museum at most 1km from Liverpool?
58. Which restaurants in London are near Kensington Palace?	59. Which provinces of Ireland have population over 2 million?	60. Is the monument of the Great Fire of London east of King WIlliam Street?
61. Which city council includes Dublin?	62. Which are the non-metropolitan counties of England?	63. Which are the main railway stations in Glasgow?
64. What historical monuments are there in London?	65. What is the area of county Cheshire?	66. What is the length of river Thames?
67. How many rivers cross England's cities?	68. Is the City of London north of the Thames river?	69. Is there a castle in London near Trafalgar Square?
70. Which counties of England border country Scotland?	71. Is there any airfield in Wellesbourne village in England?	72. Is there an aerodrome in Essex?
73. Is Somerset west of Westmorland?	74. How many cities does Merseyside have?	75. What historic buildings are in Buckinghamshire?
76. Is there a mountain in Merseyside?	77. Does county Suffolk border county Durham?	78. Which restaurants are at most 500m from the University of Liverpool?
79. Which parks are near Trafalgar Square?	80. Which villages in Scotland have a population of less than 500 people?	81. Is there a Modern Art Museum in London?
82. Through which cities does River Thames flow?	83. Is there a train station in Dublin?	84. Is there a forest in Lancashire north of Burnley?
85. Is there a county of England that borders the Isle of Wight?	86. Is there a church in the county of Greater Manchester dedicated to St. Patrick?	87. Which pubs in Liverpool are at most 2km from Anfield stadium?
88. Which pubs in Liverpool are near Anfield stadium?	89. Which hotels are in England's capital?	90. Which theaters are near Trafalgar Square?
91. Through which cities does River Thames flow?	92. Which rivers are in Great Britain?	93. Which airports are in the city of Salford?
94. Where is a car park near Big Ben?	95. Is there a river that crosses Manchester?	96. Which Scottish counties border England?
97. Is there a car park at most 1km from Waterloo Bridge?	98. Where is Trafalgar Square located?	99. Is the Castle of Edinburgh less than 2km away from Calton Hill?
100. How many pharmacies are in 200 meter radius of High Street in Oxford?	101. Which restaurants are near Edinburgh Castle?	102. Which hotels are near Big Ben?
103. Which airports are in Ireland?	104. Which hospitals are close to Stirling Castle?	105. Which airports are in London?
106. Which universities are in England?	107. Which mountains are in Scotland?	108. Where is Elizabeth Tower located?
109. Which pubs in Manchester are near the Old Trafford stadium?	110. Which rivers cross Derry?	111. Which is the total area of Northern Ireland?
112. Where is Emirates Stadium located?	113. Which castles are in the Highland council area of Scotland?	114. How many are the counties of England?
115. Is there a national park near York?	116. Which cafes in Manchester are near Piccadilly Gardens?	117. Which hotels in Manchester are near Wharfside Way?
118. Which county is west of South Yorkshire?	119. Where can I find a car park in Bristol?	120. Which villages are in Herefordshire?
121. How many mountains are there in Scotland?	122. Which city is southeast of Salford?	123. Which university colleges are in Scotland?
124. In which city is Big Ben located?	125. Does the district of Coleraine border Belfast?	126. Which forests are in Northern Ireland?
127. Is there a park in Dublin near Grafton Street?	128. Is Trafalgar square located in London?	129. How many parks are there in Northampton?
130. Which aerodrome is in Essex?	131. Is Edinburgh west of Glasgow?	132. Is there an airport in Dublin?
133. Which Greek restaurants in London are near Wembley stadium?	134. Which counties of Ireland does River Shannon cross?	135. Which restaurants are near Baker Street in London?
136. Which countries border Wales?	137. Is England part of the United Kingdom ?	138. How many county councils are there in Ireland?
139. Which restaurants are near Stonehenge?	140. What tourist attractions are there in Belfast, Northern Ireland?	141. Which rivers in Scotland have more than 100 km length?
142. Which are the districts of county Chesire?	143. Where is Tower Bridge located?	144. Is London south of Manchester?
145. Are there any lakes in Scotland?	146. Which counties border county Donegal to the south?	147. Is there a forest near Manchester?
148. Is the Tower of London near river Thames?	149. Does Hammersmith Bridge connect Hammersmith with Barnes?	150. In which part of England is Liverpool located?
151. Which rivers discharge into the Solway Firth?	152. Which art museums are at most 1km from Charlotte Square in Edinburgh?	153. Which rivers cross county Cheshire?
154. Where can I find a car park in Exeter?	155. Which is the highest mountain in Ireland?	156. Where is the closest market to Elephant and Castle underground station?
157. What is the name of Britain's longest river?	158. Which cities in England have at least 2 castles?	159. Which is the biggest county council in the Republic of Ireland?
160. Which football stadium has the biggest capacity in Ireland?	161. Which site of Manchester is the most popular?	162. Which is the oldest bridge of London?
163. Where is the nearest gas station to St. Peter's Square in Manchester?	164. Which city in Scotland has the largest population?	165. Which cities or towns of the United Kingdom have a university?
166. What is the elevation of the most elevated spot in county Down?	167. Which is the largest county of England?	168. What is the longest river in England and Wales?
169. What is the most populated city in the United Kingdom except London?	170. Which city in Scotland has the largest population?	171. Which city of England is nearest to London?
172. Is there a river in Ireland that crosses more than 3 cities?	173. Which is the largest royal borough of London?	174. Which river crosses the most cities in England?
175. Which is the largest lake by area in Great Britain?	176. Does Everton FC plays in Liverpool?	177. Which is the largest city of Ireland?
178. Which car park is closest to a bridge on river Exe?	179. What is the most densely populated city in Ireland?	180. Is Glasgow the largest city of Scotland in terms of population?
181. Does England have more counties than Ireland?	182. Which is the largest lake in England?	183. Are the cities that River Thames crosses more than 10?
184. Are there any rivers that cross both England and Wales?	185. Which county of England occupies the largest area?	186. What is the longest bridge in Scotland?
187. Which hospital is nearest to Calton Hill in Edinburgh?	188. Which is the closest airport to London?	189. Which is the highest point in Cheshire?
190. Which is the highest building in London?	191. Is the county of Antrim bigger than the county of Armagh?	192. Which is the smallest lake in Scotland?
193. Which hotel is the nearest to Old Trafford Stadium in Manchester?	194. Which county of England has the biggest population?	195. Which Welsh district has the most adjacent Welsh districts?
196. Which town has the biggest population in Scotland?	197. Which is the longest river in Scotland?	198. Which towns of England have at least two hospitals?
199. Are there more than 10 districts in Hampshire, England ?	200. What London underground stations are closest to the British Museum?	201. What is the distance between Liverpool and Glasgow?"""

# Parse the questions string into a list
questions = {}
for line in questions_str.split("?"):
    if line.strip():
        parts = line.split(". ", 1)
        if len(parts) == 2:
            number = parts[0].strip()
            question = parts[1].strip() + "?"
            questions[number] = question

# Initialize the JSON dataset dictionary
dataset = {}

# Function to fetch SPARQL query from URL
def fetch_query(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

# Fetch SPARQL queries and combine with questions
base_url = "https://geoqa.di.uoa.gr/assets/queries/"
for i in range(1, 202):  # 1 to 201 inclusive
    question_num = str(i)
    question = questions.get(question_num)
    if question:
        query_url = f"{base_url}{i}.sparql"
        query = fetch_query(query_url)
        if query:
            dataset[question_num] = {
                "Question": question,
                "Query": query
            }

# Save dataset to JSON file
with open("201_questions_dataset.json", "w") as json_file:
    json.dump(dataset, json_file, indent=4)

print("Dataset created and saved as dataset.json")
