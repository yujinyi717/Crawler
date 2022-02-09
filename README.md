# Crawler

## 1. Naver_Blog

1. HOW TO USE
```
get_post_info(keyword, start_date, end_date, pages)
```

2. 데이터 수집 항목 

* 게시글 내용
  * 키워드에 해당하는 블로그 URL
  * 블로그 제목
  * 블로그 작성자 아이디
  * 블로그 작성자 닉네임
  * 블로그 게시일
  * 페이지 본 횟수
  * 좋아요 수
  * 싫어요 수
  * 블로그 게시글 내용
  * 팔로우 유저 수 
  * 유저 미디어 수 
* 댓글 내용
  * 작성자 닉네임
  * 댓글 작성일
  * 댓글 내용
  * 좋아요 수 
![image](https://user-images.githubusercontent.com/77731783/153235736-a2a1c053-5187-4985-9ad9-ef2ff4e6cda4.png)


## 2. Naver_Kin

1. HOW TO USE

```
get_post_info(keyword, start_date, end_date, pages)
```

2. 데이터 수집 항목

* 키워드에 해당하는 지식인 질문 URL 
* 요약문
* 글 작성일
* 글 제목
* 질문
* 답변 


## 3. Youtube

1. HOW TO USE
```
driver.get("https://www.youtube.com/watch?v=lAPAO3qK3_w") # URL 주소 입력 
```

2. 데이터 수집 항목 

* 아이디
* 댓글 내용
