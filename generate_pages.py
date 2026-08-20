import os

# 1. 템플릿 파일 읽기
with open("template.html", "r", encoding="utf-8") as f:
    template_content = f.read()

# 2. 지역 데이터 (예시 구조 - 기존 파일의 데이터를 그대로 사용하시면 됩니다)
# 서울, 경기, 인천 전체 구/동 목록
regions_data = {
    "seoul": {
        "name": "서울",
        "gangnam": ["역삼동", "개포동", "청담동", "삼성동", "대치동", "신사동", "논현동", "압구정동", "세곡동", "자곡동", "율현동", "일원동", "수서동", "도곡동"],
        "gangdong": ["강일동", "상일동", "명일동", "고덕동", "암사동", "천호동", "성내동", "길동", "둔촌동"],
        "gangbuk": ["미아동", "번동", "수유동", "우이동"],
        "gangseo": ["염창동", "등촌동", "화곡동", "가양동", "마곡동", "내발산동", "외발산동", "공항동", "방화동", "개화동"],
        "seocho": ["서초동", "잠원동", "반포동", "방배동", "양재동", "우면동", "원지동", "내곡동", "염곡동", "신원동"],
        "songpa": ["잠실동", "신천동", "풍납동", "송파동", "석촌동", "삼전동", "가락동", "문정동", "장지동", "방이드동", "오금동", "거여동", "마천동"],
        "mapo": ["공덕동", "아현동", "도화동", "용강동", "대흥동", "염리동", "노고산동", "신수동", "현석동", "구수동", "창전동", "상수동", "하중동", "신정동", "당인동", "서교동", "동교동", "합정동", "망원동", "연남동", "성산동", "중동", "상암동"],
        "yeongdeungpo": ["영등포동", "여의도동", "당산동", "도림동", "문래동", "양평동", "신길동", "대림동"],
        # ... 추가 구/동
    },
    "gyeonggi": {
        "name": "경기",
        "suwon": ["인계동", "매탄동", "원천동", "영통동", "망포동", "광교동", "곡반정동", "권선동", "세류동", "고등동", "화서동", "정자동", "조원동", "율전동", "천천동"],
        "seongnam": ["분당동", "수내동", "정자동", "서현동", "이매동", "야탑동", "판교동", "삼평동", "백현동", "운중동", "금곡동", "구미동", "신흥동", "태평동", "상대원동", "중원동"],
        "goyang": ["일산동", "주엽동", "탄현동", "대화동", "마두동", "백석동", "식사동", "풍동", "화정동", "행신동", "원흥동", "삼송동", "지축동"],
        "hwaseong": ["동탄동", "병점동", "진안동", "반월동", "기안동", "봉담읍", "향남읍", "남양읍"],
        # ... 추가 시/구/동
    },
    "incheon": {
        "name": "인천",
        "yeonsu": ["송도동", "연수동", "청학동", "동춘동", "옥련동", "선학동"],
        "seogu": ["청라동", "검암동", "경서동", "연희동", "가정동", "신현동", "석남동", "가좌동", "마전동", "당하동", "원당동", "오류동", "왕길동"],
        "bupyeong": ["부평동", "십정동", "산곡동", "청천동", "삼산동", "갈산동", "부개동", "일신동"],
        "namdong": ["구월동", "간석동", "만수동", "논현동", "서창동"],
        # ... 추가 구/동
    }
}

# 전체 동네 링크 태그 문자열 미리 생성
all_links = []
for sido_key, sido_val in regions_data.items():
    for gu_key, dong_list in sido_val.items():
        if gu_key == "name": continue
        for dong in dong_list:
            all_links.append(f'<a href="/{sido_key}/{gu_key}/{dong}/">{sido_val["name"]} {dong}</a>')

all_links_html = "\n".join(all_links)

# 메인 index.html에도 전체 링크 반영
if os.path.exists("index.html"):
    with open("index.html", "r", encoding="utf-8") as f:
        main_html = f.read()
    main_html = main_html.replace("{{REGION_LINKS}}", all_links_html)
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(main_html)

# 동네별 HTML 파일 생성
for sido_key, sido_val in regions_data.items():
    for gu_key, dong_list in sido_val.items():
        if gu_key == "name": continue
        for dong in dong_list:
            target_dir = f"{sido_key}/{gu_key}/{dong}"
            os.makedirs(target_dir, exist_ok=True)
            
            page_content = template_content
            page_content = page_content.replace("{{PAGE_TITLE}}", f"{sido_val['name']} {dong} 출장마사지 | 퀸즈홈테라피 24시 프리미엄 케어")
            page_content = page_content.replace("{{PAGE_DESC}}", f"{sido_val['name']} {dong} 전지역 24시간 출장마사지 퀸즈홈테라피. 100% 후불제, 30분 내 빠른 방문 안심 힐링 케어.")
            page_content = page_content.replace("{{REGION_NAME}}", f"{sido_val['name']} {dong}")
            page_content = page_content.replace("{{HERO_DESC}}", f"{sido_val['name']} {dong} 어디서나 편안하게 계신 곳으로 30분 내 방문합니다.")
            page_content = page_content.replace("{{REGION_LINKS}}", all_links_html)
            
            with open(f"{target_dir}/index.html", "w", encoding="utf-8") as f:
                f.write(page_content)

print(f">> 완료! 총 {len(all_links)}개의 모든 동네 링크가 포함된 페이지들이 정상 생성되었습니다.")