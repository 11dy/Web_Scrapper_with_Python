import requests # requests는 팡썬에서 요청을 만드는 기능을 모아 놓은 것
from bs4 import BeautifulSoup 
# 데이터를 가져와서 활용하는데 사용한다. 

LIMIT = 50
URL = f"https://kr.indeed.com/jobs?q=python&limit={LIMIT}"


def extract_indeed_pages():
   result = requests.get(URL)# 한국버전 링크 )

 #indeed_soup = BeautifulSoup    (html_doc, 'html.parser') 이런 형태로 사용! 
   soup = BeautifulSoup(result.text, "html.parser")
# html 페이지 전부 가져오기 
   pagination = soup.find("div", {"class": "pagination"})
# 해당 url의 페이지 리스트 불러오기 

#print(pagination)

   links = pagination.find_all('a') # pages는 리스트다. 

   pages = []
# 각 page의 span을 찾아서 pages 배열에 넣어준다. 
   for link in links[:-1]: 
    pages.append(int(link.string))
# .string은 str만 가져온다는 뜻 
#print(pages[-1]) # -1은 마지막에서 시작해서 첫 item을 나타낸다. 
   max_page = pages[-1]
#print(range(max_page)) #맥스페이지 만큼의 배열이 생성된다. 
   return max_page


#indeed pages를 입력받아서 requests를 원하는 만큼 생성하는 함수 만들기 
def extract_indeed_jobs(last_page):
  #jobs = [] # 일자리 추출 후 저장 
  for page in range(last_page):
    result = requests.get(f"{URL}&start={page*LIMIT}") #페이지 요청 
    print(result.status_code) # status_code는 requests에 포함된 것 > 페이지 개수만큼 200 출력 
