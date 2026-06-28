from collections import defaultdict


def analyze_by_category(exam_results: list[dict]) -> list[dict]:
    category_stats = defaultdict(lambda: {
        "total_count": 0,
        "correct_count": 0,
        "incorrect_count": 0,
    })

    for exam in exam_results:
        for question in exam["questions"]:
            category = question["category"]
            result = question["result"]

            category_stats[category]["total_count"] += 1

            if result == "correct":
                category_stats[category]["correct_count"] += 1
            elif result == "incorrect":
                category_stats[category]["incorrect_count"] += 1

    analysis = []

    for category, stats in category_stats.items():
        total = stats["total_count"]
        correct = stats["correct_count"]
        incorrect = stats["incorrect_count"]
        accuracy = round(correct / total * 100, 1) if total else 0

        analysis.append({
            "category": category,
            "total_count": total,
            "correct_count": correct,
            "incorrect_count": incorrect,
            "accuracy": accuracy,
        })

    analysis.sort(key=lambda x: x["accuracy"])

    return analysis