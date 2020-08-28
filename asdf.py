import requests
#from selenium import webdriver
#from selenium.webdriver.support.ui import Select

#driver = webdriver.Firefox()
#driver.get('url')


anime_list=[]
zrodla=[]

v_url='https://animedesu.pl/anime/list-mode/'
r = requests.get(v_url)
page_source = r.content.split(b'<a class="tip series"')


for x in page_source[1:]:
	start=x.find(b'href=')
	end=x.find(b'/">')
	anime_list.append(x[start+6:end].decode('ascii'))
	pass

# for x in anime_list[123:125]:
# 	if 'deca-dence' in x:
# 		print(x)
# 	pass

episode=1

v_url=anime_list[124].replace('anime/', '') + '-odcinek-' + str(episode)
# print(v_url)
r = requests.get(v_url)
page_source = r.content.split(b'<li data-id=')

# print(page_source[2:3])

print(v_url)

# start=page_source.find('<div class="episodelist">'.encode('utf-8'))
# end=page_source.find('<a href="</span></div> </a>'.encode('utf-8'))
# print(page_source[1:])
for x in page_source[1:]:
	print(x[:150])
	pass

# print(page_source[start:])
# end=x.find('data-index'.encode('utf-8'))

# # for x in page_source[2:]:
	
# # 	start=x.find('lue='.encode('utf-8'))
# # 	end=x.find('data-index'.encode('utf-8'))
# # 	zrodla.append(x[start+4:end].decode('utf-8'))
# # 		#print(x[:250])
		
# # 	pass
# # start=page_source.find('<option value='.encode('utf-8'))
# # end=page_source.find('data-index="1"'.encode('utf-8'))

# # zrodlo=page_source[start:end]

# for x in zrodla[:]:
# 	print(x)
# 	pass