# Crawler

## 1. Naver_Blog

1. HOW TO USE
```
get_post_info(keyword, start_date, end_date, pages)

# num = int(input("몇 페이지 까지 크롤링 할까요? \n => "))
# keyword = input("검색하실 키워드를 입력해주세요 \n =>")
# start_date = input("검색 시작일을 입력해주세요 ex) 2000-01-01 \n =>")
# end_date = input("검색 종료일을 입력해주세요 ex) 2000-01-01 \n =>")

```

2. 데이터 수집 항목 

* 게시글 내용
  * 키워드에 해당하는 블로그 URL, 블로그 제목, 블로그 작성자 아이디, 블로그 작성자 닉네임, 블로그 게시일, 페이지 본 횟수, 좋아요 수, 싫어요 수, 블로그 게시글 내용, 팔로우 유저 수, 유저 미디어 수 

  ![image](https://user-images.githubusercontent.com/77731783/153236100-7fa4e4cd-ba35-40d4-8576-d6aa295772b3.png)

 
* 댓글 내용
  * 작성자 닉네임, 댓글 작성일, 댓글 내용, 좋아요 수 
  ![image](https://user-images.githubusercontent.com/77731783/153235736-a2a1c053-5187-4985-9ad9-ef2ff4e6cda4.png)


## 2. Naver_Kin

1. HOW TO USE

```
get_post_info(keyword, start_date, end_date, pages)

# num = int(input("몇 페이지 까지 크롤링 할까요? \n => "))
# keyword = input("검색하실 키워드를 입력해주세요 \n =>")
# start_date = input("검색 시작일을 입력해주세요 ex) 2000-01-01 \n =>")
# end_date = input("검색 종료일을 입력해주세요 ex) 2000-01-01 \n =>")
```

2. 데이터 수집 항목

* 키워드에 해당하는 지식인 질문 URL, 요약문, 글 작성일, 글 제목, 질문, 답변 
  ![image](https://user-images.githubusercontent.com/77731783/153235931-2af0de31-a910-4800-92ab-0fc91f0a1494.png)


## 3. Youtube

1. HOW TO USE
```
driver.get("https://www.youtube.com/watch?v=lAPAO3qK3_w") # URL 주소 입력 
```

2. 데이터 수집 항목 

* 아이디, 댓글 내용

  ![image](https://user-images.githubusercontent.com/77731783/153235845-01e2f4d1-c6df-4cd7-b763-cee68a515c47.png)
  
  
## 4. Naver_Shopping

1. HOW TO USE
```
driver.get("https://search.shopping.naver.com/catalog/29938164618?query=lg%20tv&NaPm=ct%3Dl1w5iim8%7Cci%3Dc809d139f2ae38d6cbb5fb2c91d2965c9ec4fbf7%7Ctr%3Dslsl%7Csn%3D95694%7Chk%3Dbaa6d0cf44172f61736be61218f8cbfb1baf16fa") # URL 주소 입력 
```

2. 데이터 수집 항목 

* 리뷰 제목, 내용, 평점, 구매처, 닉네임, 작성일자
