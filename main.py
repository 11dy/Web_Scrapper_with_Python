from indeed import extract_indeed_pages, extract_indeed_jobs 

last_indeed_page = extract_indeed_pages()

#페이지를 가져오고 마지막 페이지를 받아서 > 
extract_indeed_jobs(last_indeed_page)# 함수 실행 
# 여기까지 하면 이제 request를 수행할 수 있다. 