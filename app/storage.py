import json
from pathlib import Path
from datetime import datetime


def save_questions_to_json(questions: list[dict], output_dir: str = "data/json") -> Path:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    now = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = output_path / f"exam_{now}.json"

    data = {
        "created_at": datetime.now().isoformat(timespec="seconds"),
        "total_count": len(questions),
        "correct_count": sum(1 for q in questions if q["result"] == "correct"),
        "incorrect_count": sum(1 for q in questions if q["result"] == "incorrect"),
        "questions": questions,
    }

    with file_path.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    return file_path


def load_all_exam_results(input_dir: str = "data/json") -> list[dict]:
    input_path = Path(input_dir)

    if not input_path.exists():
        return []

    results = []

    for json_file in sorted(input_path.glob("*.json")):
        with json_file.open("r", encoding="utf-8") as f:
            data = json.load(f)
            data["source_file"] = str(json_file)
            results.append(data)

    return results