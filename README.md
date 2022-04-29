# school.py
쉽게 사용하는 데 초점을 맞춘 파이썬 나이스 API 모듈

## Requirements
requests

## school.School(학교이름)
학교 이름으로 교육청 코드와 학교 코드 찾아줌, 변수 2개 필요

## school.Meal(학교이름, 급식코드, 날짜)
급식, 학교이름 = 문자열로 학교이름, 급식코드 = (조식:1)(중식:2)(석식:3), 날짜 = YYYYMMDD

## school.Class(학교이름, 학년, 반, 교시, 날짜)
시간표, 위와 동일

## school.ClassAll(학교이름, 학년, 반, 날짜)
전체 시간표, 위와 동일
