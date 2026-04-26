from modules.speech import get_input
from modules.llm import process_text
from modules.hardware import adjust_light

def main():
    user_input = get_input()
    
    response = process_text(user_input)
    light = adjust_light(user_input)
    
    print("\n--- System Output ---")
    print(response)
    print(light)

if __name__ == "__main__":
    main()