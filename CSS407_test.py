# test_style.py
import pytest
from bs4 import BeautifulSoup

def test_css_properties():
    html_content = open("index.html", "r", encoding="utf-8").read()
    soup = BeautifulSoup(html_content, "html.parser")
    
    container = soup.find(class_="container")
    assert container is not None, "A .container elem nem található."
    
    h1 = soup.find("h1")
    assert h1 is not None, "A h1 elem nem található."
    
    h2 = soup.find("h2")
    assert h2 is not None, "A h2 elem nem található."
    
    aside1 = soup.find(class_="note1")
    aside2 = soup.find(class_="note2")
    assert aside1 is not None, "A .note1 elem nem található."
    assert aside2 is not None, "A .note2 elem nem található."
    
    quae = soup.find(class_="quae")
    modi = soup.find(class_="modi")
    assert quae is not None, "A .quae elem nem található."
    assert modi is not None, "A .modi elem nem található."

    print("Minden HTML elem megfelelően definiálva van.")

if __name__ == "__main__":
    pytest.main()
