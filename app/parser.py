from bs4 import BeautifulSoup


def parse_result_html(html: str) -> list[dict]:
    soup = BeautifulSoup(html, "lxml")

    questions = []
    seen_question_ids = set()

    for tr in soup.select("table.table-check tbody tr"):
        tds = tr.select("td")

        if len(tds) < 5:
            continue

        question_id_tag = tds[2].select_one("a")
        if question_id_tag is None:
            continue

        question_id = question_id_tag.get_text(strip=True)

        if question_id in seen_question_ids:
            continue

        seen_question_ids.add(question_id)

        question_no = int(tds[0].get_text(strip=True))

        result_icon = tds[1].select_one("i")
        icon_classes = result_icon.get("class", []) if result_icon else []

        if "fa-circle" in icon_classes:
            result = "correct"
        elif "fa-times" in icon_classes:
            result = "incorrect"
        else:
            result = "unknown"

        title = tds[3].get_text(" ", strip=True)
        category = tds[4].get_text(strip=True)

        questions.append({
            "question_no": question_no,
            "question_id": question_id,
            "result": result,
            "title": title,
            "category": category,
        })

    return questions