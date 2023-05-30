# FastAPI
- [Python Docs](https://docs.python.org/ko/3/)
- [FastAPI Docs](https://fastapi.tiangolo.com/ko/tutorial/first-steps/)
- [Python설치](https://www.python.org/downloads/)

## Installing
- Fast api
```zsh
pip install fastapi
```
- 실시간 미리보기
```zsh
pip install uvicorn[standart]
```

## Run Server
- In project root directory
- main: 파일 main.py (파이썬 "모듈").
- app: main.py 내부의 app = FastAPI() 줄에서 생성한 오브젝트.
-  --reload: 코드 변경 후 서버 재시작. 개발에만 사용.
```zsh
uvicorn main:app --reload
```

## Swagger UI
- Default
```URL
http://localhost:8000/docs
```
- Custom Docs
```URL
http://localhost:8000/redoc
```