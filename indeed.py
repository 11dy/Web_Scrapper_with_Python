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
  jobs = [] # 일자리 추출 후 저장 
  #for page in range(last_page):
  result = requests.get(f"{URL}&start={0*LIMIT}") #페이지 요청 
  soup = BeautifulSoup(result.text, "html.parser") # 데이터를 html에서 추출
  results = soup.find_all("a", {"class":"fs-unmask"})
  for result in results:
    title = result.find("h2", {"class": "jobTitle"}).find("span", title=True).text
    company = result.find("span", {"class" : "companyName"})
    # 여기서 company는 soup이다 
    company_anchor = company.find("a")
    if company_anchor is not None:
     company = str(company_anchor.string)# 기존의 soup을 없애고 string을 넣어줌 
    else:
     company = str(company.string)
    company = company.strip() 
    print(title, company)
  return jobs

#출력의 빈칸을 없애려면 strip을 사용해줘야한다. strip은 해당 문자열의 ()안 내용을 모두 삭제해준다. strip()은 양 옆 빈칸 삭제 

