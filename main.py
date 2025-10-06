from api_integration.content_api import generate_content
from api_integration.management_api import save_content
from ai_tools.cursor_integration import assist_code

def main():
    content_request = "Write a short blog post about AI in healthcare."
    content = generate_content(content_request)
    print("Generated Content:", content)
    save_content(content)
    code_suggestion = assist_code("def hello():")
    print("Cursor AI Suggestion:", code_suggestion)

if __name__ == "__main__":
    main()