prompts = {
    "what": "what is the stanley cup?",
    "named": "who was the stanley cup named after? ",
    "most": "what team has won the most stanley cups ever?",
    "who": "who won the most recent stanley cup?",
    "when": "when was the stanley cup first used"

}
responses = {
    "what": "The Stanley Cup (French: La Coupe Stanley) is the championship trophy awarded annually to the National Hockey League (NHL) playoff winner.",
    "named": "It is named after Lord Stanley of Preston, the Governor General of Canada who donated it as an award to Canada's top-ranking amateur ice hockey club.",
    "most": "The Montreal Canadiens",
    "who": "The St. Louis Blues",
    "when": "1893"
}

def process_input(userInput):
    print("Hello")

def main():
    print("Welcome to the Stanley cup Journal\n")
    print("You can ask me anything about the Stanley Cup or type quit\n")

    user_input = ""

    while user_input != "quit":
        user_input = input("What's your question? ").lower()
        #print(user_input)
        if user_input != "quit":
            response = process_input(user_input)
            print(response)
    
    print("It was good talking to you.\nGood-bye!")


main()