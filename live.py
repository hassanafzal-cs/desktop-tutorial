from pyngrok import ngrok


url = ngrok.connect(8000)
print(f"YE RAHI AAPKI LIVE LINK: {url}")
input("Band karne ke liye ENTER dabao...")