import os

ANSWER = "I hired a life coach to find my purpose; after three sessions he quit to become a monk, which honestly felt like an answer."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ANSWER)

if __name__ == "__main__":
    main()
