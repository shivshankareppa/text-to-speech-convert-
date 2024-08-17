import pyttsx3

# Initialize the text-to-speech engine
text_speech = pyttsx3.init()

def handle_case(case):
    if case == '1':  # Check if the case is '1' (string comparison)
        while True:
            text = input("Enter text to speak (or type 'exit' to quit): ")
            if text.lower() == 'exit':
                break  # Exit the loop if the user types 'exit'
            text_speech.say(text)
            text_speech.runAndWait()
    elif case == '2':  # Check if the case is '2' (string comparison)
        while True:
            # Open and read the content of a text file
            file_path = input("Enter the file path (or type 'exit' to quit):")  # Get the path to the text file
            if file_path.lower() == 'exit':
                break  # Exit the loop if the user types 'exit'
            try:
                with open(file_path, 'r') as file:
                    answer = file.read()  # Read the entire content of the file
                    print("File content:")
                    print(answer)
                    text_speech.say(answer)  # Speak the content
                    text_speech.runAndWait()
            except FileNotFoundError:
                print(f"The file {file_path} was not found.")
            except Exception as e:
                print(f"An error occurred: {e}")
    else:
        print("Invalid option. Please enter '1' or '2'.")

while True:
    # Get user choice
    print("Please enter the type of text (or type 'exit' to quit):")
    case = input("1. Enter text directly\n2. Enter the file path:\n")
    if case.lower() == 'exit':
        break
    else:
     handle_case(case)
