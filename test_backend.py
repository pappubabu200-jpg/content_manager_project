from api_integration.content_api import generate_content

def test_generate_content():
    result = generate_content("Test prompt")
    assert "Test prompt" in result
    print("Backend test passed!")

if __name__ == "__main__":
    test_generate_content()