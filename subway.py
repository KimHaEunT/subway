import streamlit as st

# st.set_page_config(page_title="서브웨이 주문", page_icon="🥪")

st.title("🥪 서브웨이 샌드위치 주문 웹사이트")

st.write("원하는 재료를 골라 나만의 샌드위치를 만들어 보세요!")

# 1. 빵 선택
bread = st.radio("1. 빵을 선택하세요", ["화이트", "하티", "위트", "허니오트", "파마산 오레가노"])

# 2. 사이즈 선택
size = st.selectbox("2. 사이즈를 선택하세요", ["15cm", "30cm"])

# 3. 치즈 선택
cheese = st.selectbox("3. 치즈를 선택하세요", ["아메리칸 치즈", "슈레드 치즈", "모차렐라 치즈", "치즈 없음"])

# 4. 야채 선택
veggies = st.multiselect(
    "4. 원하는 야채를 선택하세요 (복수 선택 가능)",
    ["양상추", "토마토", "오이", "피망", "양파", "할라피뇨", "올리브", "피클"]
)

# 5. 소스 선택
sauces = st.multiselect(
    "5. 원하는 소스를 선택하세요 (복수 선택 가능)",
    ["마요네즈", "스위트 어니언", "허니 머스타드", "랜치", "바비큐", "핫 칠리", "머스타드"]
)

# 6. 추가 요청 사항
note = st.text_area("6. 추가 요청 사항이 있으신가요?", placeholder="예: 소스를 적게 넣어주세요.")


# 주문 버튼
if st.button("🛒 주문하기"):
    st.success("🎉 주문이 완료되었습니다!")
    st.subheader("🧾 주문 내역 요약")
    st.write(f"**빵**: {bread}")
    st.write(f"**사이즈**: {size}")
    st.write(f"**치즈**: {cheese}")
    st.write(f"**야채**: {', '.join(veggies) if veggies else '없음'}")
    st.write(f"**소스**: {', '.join(sauces) if sauces else '없음'}")
    st.write(f"**요청사항**: {note if note.strip() else '없음'}")
