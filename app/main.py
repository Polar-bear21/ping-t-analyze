import sys
from pathlib import Path
from wcwidth import wcswidth

from parser import parse_result_html
from storage import save_questions_to_json, load_all_exam_results
from analyzer import analyze_by_category


def parse_command(html_file: str):
    html_path = Path(html_file)

    if not html_path.exists():
        print(f"ファイルが見つかりません: {html_path}")
        return

    html = html_path.read_text(encoding="utf-8")
    questions = parse_result_html(html)

    saved_path = save_questions_to_json(questions)

    print(f"抽出件数: {len(questions)}")
    print(f"JSONに保存しました: {saved_path}")


def analyze_command():
    exam_results = load_all_exam_results()

    if not exam_results:
        print("解析対象のJSONがありません")
        return

    analysis = analyze_by_category(exam_results)

    print()
    print("分野別成績")
    print("=" * 70)

    for item in analysis:
        category = item["category"]
        result = (
            f"{item['correct_count']}/{item['total_count']} "
            f"({item['accuracy']:.1f}%)"
        )

        print(f"{ljust_display(category, 54)} {result:>14}")

    print("=" * 70)
    
def ljust_display(text: str, width: int) -> str:
    text_width = wcswidth(text)
    padding = max(width - text_width, 0)
    return text + " " * padding

def main():
    if len(sys.argv) < 2:
        print("コマンドを指定してください")
        print("例:")
        print("  python app/main.py parse data/raw_html/result.html")
        print("  python app/main.py analyze")
        return

    command = sys.argv[1]

    if command == "parse":
        if len(sys.argv) < 3:
            print("HTMLファイルを指定してください")
            return

        parse_command(sys.argv[2])

    elif command == "analyze":
        analyze_command()

    else:
        print(f"未対応のコマンドです: {command}")


if __name__ == "__main__":
    main()