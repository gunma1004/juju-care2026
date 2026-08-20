import os

# 1. template.html 읽기
if not os.path.exists("template.html"):
    print("오류: template.html 파일이 없습니다.")
    exit()

with open("template.html", "r", encoding="utf-8") as f:
    template_content = f.read()

# 2. 지역 데이터 (서울 / 경기 / 인천 및 주요 구·동)
regions_data = {
    "seoul": {
        "name": "서울",
        "gangnam": ["역삼동", "개포동", "청담동", "삼성동", "대치동", "신사동", "논현동", "압구정동", "세곡동", "자곡동", "율현동", "일원동", "수서동", "도곡동"],
        "gangdong": ["강일동", "상일동", "명일동", "고덕동", "암사동", "천호동", "성내동", "길동", "둔촌동"],
        "gangbuk": ["미아동", "번동", "수유동", "우이동"],
        "gangseo": ["염창동", "등촌동", "화곡동", "가양동", "마곡동", "내발산동", "외발산동", "공항동", "방화동", "개화동"],
        "seocho": ["서초동", "잠원동", "반포동", "방배동", "양재동", "우면동", "원지동", "내곡동", "염곡동", "신원동"],
        "songpa": ["잠실동", "신천동", "풍납동", "송파동", "석촌동", "삼전동", "가락동", "문정동", "장지동", "방이동", "오금동", "거여동", "마천동"],
        "mapo": ["공덕동", "아현동", "도화동", "용강동", "대흥동", "염리동", "신수동", "상수동", "서교동", "동교동", "합정동", "망원동", "연남동", "성산동", "상암동"],
        "yeongdeungpo": ["영등포동", "여의도동", "당산동", "도림동", "문래동", "양평동", "신길동", "대림동"],
        "yongsan": ["이태원동", "한남동", "한강로동", "용산동", "후암동", "원효로동"],
        "junggu": ["명동", "을지로동", "신당동", "다산동", "약수동", "청구동", "황학동", "중림동"]
    },
    "gyeonggi": {
        "name": "경기",
        "suwon": ["인계동", "매탄동", "원천동", "영통동", "망포동", "광교동", "곡반정동", "권선동", "세류동", "화서동", "정자동", "조원동", "율전동", "천천동"],
        "seongnam": ["분당동", "수내동", "정자동", "서현동", "이매동", "야탑동", "판교동", "삼평동", "백현동", "운중동", "금곡동", "구미동", "신흥동", "태평동", "상대원동"],
        "goyang": ["일산동", "주엽동", "탄현동", "대화동", "마두동", "백석동", "식사동", "풍동", "화정동", "행신동", "원흥동", "삼송동", "지축동"],
        "hwaseong": ["동탄동", "병점동", "진안동", "반월동", "기안동", "봉담읍", "향남읍", "남양읍"],
        "yongin": ["풍덕천동", "신봉동", "죽전동", "동천동", "상현동", "성복동", "기흥동", "신갈동", "구갈동", "보정동", "동백동", "처인동"],
        "bucheon": ["중동", "상동", "심곡동", "원미동", "소사동", "오정동", "송내동", "괴안동"],
        "anyang": ["안양동", "석수동", "박달동", "비산동", "관양동", "평촌동", "호계동", "범계동"]
    },
    "incheon": {
        "name": "인천",
        "yeonsu": ["송도동", "연수동", "청학동", "동춘동", "옥련동", "선학동"],
        "seogu": ["청라동", "검암동", "경서동", "연희동", "가정동", "신현동", "석남동", "가좌동", "마전동", "당하동", "원당동", "오류동", "왕길동", "루원시티"],
        "bupyeong": ["부평동", "십정동", "산곡동", "청천동", "삼산동", "갈산동", "부개동", "일신동"],
        "namdong": ["구월동", "간석동", "만수동", "논현동", "서창동", "도림동"],
        "michuhol": ["주안동", "도화동", "학익동", "용현동", "숭의동", "관교동", "문학동"],
        "junggu": ["영종동", "운서동", "중산동", "신흥동", "답동", "북성동", "신포동"]
    }
}

# 1) 전체 동네 링크 목록 HTML 생성
all_links = []
for sido_key, sido_val in regions_data.items():
    for gu_key, dong_list in sido_val.items():
        if gu_key == "name":
            continue
        for dong in dong_list:
            all_links.append(f'<a href="/{sido_key}/{gu_key}/{dong}/">{sido_val["name"]} {dong}</a>')

all_links_html = "\n".join(all_links)

# 2) 메인 index.html 치환 업데이트
if os.path.exists("index.html"):
    with open("index.html", "r", encoding="utf-8") as f:
        main_html = f.read()
    main_html = main_html.replace("{{REGION_LINKS}}", all_links_html)
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(main_html)
    print(">> index.html 갱신 완료")

# 3) 광역 시·도 메인 페이지 생성 (/seoul/, /gyeonggi/, /incheon/)
for sido_key, sido_val in regions_data.items():
    sido_dir = sido_key
    os.makedirs(sido_dir, exist_ok=True)
    
    # 해당 시·도 전용 동네 링크들만 추출
    sido_links = []
    for gu_key, dong_list in sido_val.items():
        if gu_key == "name":
            continue
        for dong in dong_list:
            sido_links.append(f'<a href="/{sido_key}/{gu_key}/{dong}/">{sido_val["name"]} {dong}</a>')
    sido_links_html = "\n".join(sido_links)

    sido_page = template_content
    sido_page = sido_page.replace("{{PAGE_TITLE}}", f"{sido_val['name']} 출장마사지 | 퀸즈홈테라피 24시 프리미엄 방문 케어")
    sido_page = sido_page.replace("{{PAGE_DESC}}", f"{sido_val['name']} 전지역 24시간 출장마사지 퀸즈홈테라피. 100% 후불제, 빠른 배정 안심 힐링 케어.")
    sido_page = sido_page.replace("{{REGION_NAME}}", f"{sido_val['name']} 전지역")
    sido_page = sido_page.replace("{{HERO_DESC}}", f"{sido_val['name']} 전지역 어디서나 머무시는 곳으로 25~35분 내에 빠르게 방문합니다.")
    sido_page = sido_page.replace("{{REGION_LINKS}}", sido_links_html)

    with open(f"{sido_dir}/index.html", "w", encoding="utf-8") as f:
        f.write(sido_page)

# 4) 세부 구·동 페이지 생성
for sido_key, sido_val in regions_data.items():
    for gu_key, dong_list in sido_val.items():
        if gu_key == "name":
            continue
        for dong in dong_list:
            target_dir = f"{sido_key}/{gu_key}/{dong}"
            os.makedirs(target_dir, exist_ok=True)
            
            dong_page = template_content
            dong_page = dong_page.replace("{{PAGE_TITLE}}", f"{sido_val['name']} {dong} 출장마사지 | 퀸즈홈테라피 24시 힐링 케어")
            dong_page = dong_page.replace("{{PAGE_DESC}}", f"{sido_val['name']} {dong} 전지역 24시간 출장마사지 퀸즈홈테라피. 100% 후불제, 빠른 배정 안심 케어.")
            dong_page = dong_page.replace("{{REGION_NAME}}", f"{sido_val['name']} {dong}")
            dong_page = dong_page.replace("{{HERO_DESC}}", f"{sido_val['name']} {dong} 어디서나 편안하게 계신 곳으로 30분 내 방문합니다.")
            dong_page = dong_page.replace("{{REGION_LINKS}}", all_links_html)
            
            with open(f"{target_dir}/index.html", "w", encoding="utf-8") as f:
                f.write(dong_page)

print(f">> 완료! 서울/경기/인천 광역 대문 페이지 및 총 {len(all_links)}개의 세부 동네 페이지가 모두 정상 제작되었습니다.")