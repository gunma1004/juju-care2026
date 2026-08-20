import os

if not os.path.exists("template.html"):
    print("오류: template.html 파일이 없습니다.")
    exit()

with open("template.html", "r", encoding="utf-8") as f:
    template_content = f.read()

# 계층형 지역 데이터 정의 (구 한국어 이름 매핑 포함)
regions_data = {
    "seoul": {
        "name": "서울",
        "gus": {
            "gangnam": {"name": "강남구", "dongs": ["역삼동", "개포동", "청담동", "삼성동", "대치동", "신사동", "논현동", "압구정동", "세곡동", "자곡동", "율현동", "일원동", "수서동", "도곡동"]},
            "gangdong": {"name": "강동구", "dongs": ["강일동", "상일동", "명일동", "고덕동", "암사동", "천호동", "성내동", "길동", "둔촌동"]},
            "gangbuk": {"name": "강북구", "dongs": ["미아동", "번동", "수유동", "우이동"]},
            "gangseo": {"name": "강서구", "dongs": ["염창동", "등촌동", "화곡동", "가양동", "마곡동", "내발산동", "외발산동", "공항동", "방화동", "개화동"]},
            "seocho": {"name": "서초구", "dongs": ["서초동", "잠원동", "반포동", "방배동", "양재동", "우면동", "원지동", "내곡동", "염곡동", "신원동"]},
            "songpa": {"name": "송파구", "dongs": ["잠실동", "신천동", "풍납동", "송파동", "석촌동", "삼전동", "가락동", "문정동", "장지동", "방이동", "오금동", "거여동", "마천동"]},
            "mapo": {"name": "마포구", "dongs": ["공덕동", "아현동", "도화동", "용강동", "대흥동", "염리동", "신수동", "상수동", "서교동", "동교동", "합정동", "망원동", "연남동", "성산동", "상암동"]},
            "yeongdeungpo": {"name": "영등포구", "dongs": ["영등포동", "여의도동", "당산동", "도림동", "문래동", "양평동", "신길동", "대림동"]},
            "yongsan": {"name": "용산구", "dongs": ["이태원동", "한남동", "한강로동", "용산동", "후암동", "원효로동"]},
            "junggu": {"name": "중구", "dongs": ["명동", "을지로동", "신당동", "다산동", "약수동", "청구동", "황학동", "중림동"]}
        }
    },
    "gyeonggi": {
        "name": "경기",
        "gus": {
            "suwon": {"name": "수원시", "dongs": ["인계동", "매탄동", "원천동", "영통동", "망포동", "광교동", "곡반정동", "권선동", "세류동", "화서동", "정자동", "조원동", "율전동", "천천동"]},
            "seongnam": {"name": "성남시", "dongs": ["분당동", "수내동", "정자동", "서현동", "이매동", "야탑동", "판교동", "삼평동", "백현동", "운중동", "금곡동", "구미동", "신흥동", "태평동", "상대원동"]},
            "goyang": {"name": "고양시", "dongs": ["일산동", "주엽동", "탄현동", "대화동", "마두동", "백석동", "식사동", "풍동", "화정동", "행신동", "원흥동", "삼송동", "지축동"]},
            "hwaseong": {"name": "화성시", "dongs": ["동탄동", "병점동", "진안동", "반월동", "기안동", "봉담읍", "향남읍", "남양읍"]},
            "yongin": {"name": "용인시", "dongs": ["풍덕천동", "신봉동", "죽전동", "동천동", "상현동", "성복동", "기흥동", "신갈동", "구갈동", "보정동", "동백동", "처인동"]},
            "bucheon": {"name": "부천시", "dongs": ["중동", "상동", "심곡동", "원미동", "소사동", "오정동", "송내동", "괴안동"]},
            "anyang": {"name": "안양시", "dongs": ["안양동", "석수동", "박달동", "비산동", "관양동", "평촌동", "호계동", "범계동"]}
        }
    },
    "incheon": {
        "name": "인천",
        "gus": {
            "yeonsu": {"name": "연수구", "dongs": ["송도동", "연수동", "청학동", "동춘동", "옥련동", "선학동"]},
            "seogu": {"name": "서구", "dongs": ["청라동", "검암동", "경서동", "연희동", "가정동", "신현동", "석남동", "가좌동", "마전동", "당하동", "원당동", "오류동", "왕길동", "루원시티"]},
            "bupyeong": {"name": "부평구", "dongs": ["부평동", "십정동", "산곡동", "청천동", "삼산동", "갈산동", "부개동", "일신동"]},
            "namdong": {"name": "남동구", "dongs": ["구월동", "간석동", "만수동", "논현동", "서창동", "도림동"]},
            "michuhol": {"name": "미추홀구", "dongs": ["주안동", "도화동", "학익동", "용현동", "숭의동", "관교동", "문학동"]},
            "junggu": {"name": "중구", "dongs": ["영종동", "운서동", "중산동", "신흥동", "답동", "북성동", "신포동"]}
        }
    }
}

count = 0

# 1. 광역 시·도 페이지 생성 (/seoul/, /gyeonggi/, /incheon/)
for sido_key, sido_val in regions_data.items():
    sido_dir = sido_key
    os.makedirs(sido_dir, exist_ok=True)

    # 해당 시·도의 '구/시' 목록 버튼 생성
    gu_links = []
    for gu_key, gu_info in sido_val["gus"].items():
        gu_links.append(f'<a href="/{sido_key}/{gu_key}/">{gu_info["name"]} 바로가기 ➔</a>')
    
    breadcrumbs = f'<a href="/">홈</a> <span>&gt;</span> {sido_val["name"]}'
    
    page = template_content
    page = page.replace("{{BREADCRUMBS}}", breadcrumbs)
    page = page.replace("{{PAGE_TITLE}}", f"{sido_val['name']} 출장마사지 | 퀸즈홈테라피 24시 프리미엄 케어")
    page = page.replace("{{PAGE_DESC}}", f"{sido_val['name']} 전지역 24시간 출장마사지 퀸즈홈테라피. 100% 후불제 안심 힐링 케어.")
    page = page.replace("{{REGION_NAME}}", f"{sido_val['name']} 전지역")
    page = page.replace("{{HERO_DESC}}", f"{sido_val['name']} 전지역 어디서나 머무시는 곳으로 25~35분 내에 빠르게 방문합니다.")
    page = page.replace("{{SUB_NAV_TITLE}}", f"📍 {sido_val['name']} 시·군·구 선택")
    page = page.replace("{{SUB_NAV_LINKS}}", "\n".join(gu_links))
    
    with open(f"{sido_dir}/index.html", "w", encoding="utf-8") as f:
        f.write(page)
    count += 1

# 2. 구·시 페이지 생성 (/seoul/gangnam/, /gyeonggi/suwon/ 등)
for sido_key, sido_val in regions_data.items():
    for gu_key, gu_info in sido_val["gus"].items():
        gu_dir = f"{sido_key}/{gu_key}"
        os.makedirs(gu_dir, exist_ok=True)

        # 해당 구에 속한 '동' 목록 버튼 생성
        dong_links = []
        for dong in gu_info["dongs"]:
            dong_links.append(f'<a href="/{sido_key}/{gu_key}/{dong}/">{dong}</a>')
        
        breadcrumbs = f'<a href="/">홈</a> <span>&gt;</span> <a href="/{sido_key}/">{sido_val["name"]}</a> <span>&gt;</span> {gu_info["name"]}'
        
        page = template_content
        page = page.replace("{{BREADCRUMBS}}", breadcrumbs)
        page = page.replace("{{PAGE_TITLE}}", f"{sido_val['name']} {gu_info['name']} 출장마사지 | 퀸즈홈테라피")
        page = page.replace("{{PAGE_DESC}}", f"{sido_val['name']} {gu_info['name']} 전지역 24시간 출장마사지 퀸즈홈테라피.")
        page = page.replace("{{REGION_NAME}}", f"{sido_val['name']} {gu_info['name']}")
        page = page.replace("{{HERO_DESC}}", f"{gu_info['name']} 전지역 계신 곳으로 25~35분 내에 빠르게 방문합니다.")
        page = page.replace("{{SUB_NAV_TITLE}}", f"📍 {gu_info['name']} 세부 동네 선택")
        page = page.replace("{{SUB_NAV_LINKS}}", "\n".join(dong_links))
        
        with open(f"{gu_dir}/index.html", "w", encoding="utf-8") as f:
            f.write(page)
        count += 1

# 3. 세부 동네 페이지 생성 (/seoul/gangnam/역삼동/ 등)
for sido_key, sido_val in regions_data.items():
    for gu_key, gu_info in sido_val["gus"].items():
        # 같은 구에 속한 인근 동네 버튼들
        neighbor_links = []
        for dong in gu_info["dongs"]:
            neighbor_links.append(f'<a href="/{sido_key}/{gu_key}/{dong}/">{dong}</a>')
        
        for dong in gu_info["dongs"]:
            target_dir = f"{sido_key}/{gu_key}/{dong}"
            os.makedirs(target_dir, exist_ok=True)
            
            breadcrumbs = f'<a href="/">홈</a> <span>&gt;</span> <a href="/{sido_key}/">{sido_val["name"]}</a> <span>&gt;</span> <a href="/{sido_key}/{gu_key}/">{gu_info["name"]}</a> <span>&gt;</span> {dong}'
            
            page = template_content
            page = page.replace("{{BREADCRUMBS}}", breadcrumbs)
            page = page.replace("{{PAGE_TITLE}}", f"{sido_val['name']} {dong} 출장마사지 | 퀸즈홈테라피 24시")
            page = page.replace("{{PAGE_DESC}}", f"{sido_val['name']} {gu_info['name']} {dong} 24시간 출장마사지 퀸즈홈테라피.")
            page = page.replace("{{REGION_NAME}}", f"{gu_info['name']} {dong}")
            page = page.replace("{{HERO_DESC}}", f"{dong} 어디서나 머무시는 곳으로 25~35분 내에 빠르게 방문합니다.")
            page = page.replace("{{SUB_NAV_TITLE}}", f"📍 {gu_info['name']} 인근 동네 둘러보기")
            page = page.replace("{{SUB_NAV_LINKS}}", "\n".join(neighbor_links))
            
            with open(f"{target_dir}/index.html", "w", encoding="utf-8") as f:
                f.write(page)
            count += 1

print(f">> 완료! 총 {count}개의 계층형(시/도 ➔ 구/시 ➔ 동) 페이지가 완벽하게 제작되었습니다.")