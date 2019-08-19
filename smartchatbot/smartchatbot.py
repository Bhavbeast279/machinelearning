import requests

responses = {
 "what": "The Stanley Cup (French: La Coupe Stanley) is the championship trophy awarded annually to the National Hockey League (NHL) playoff winner.",
 "named": "It is named after Lord Stanley of Preston, the Governor General of Canada who donated it as an award to Canada's top-ranking amateur ice hockey club.",
 "most": "The Montreal Canadiens",
 "who": "The St. Louis Blues",
 "when": "1893"
}

def process_intent(intent):
    key = intent["class_name"].lower()
    confidence = intent["confidence"]
    if confidence < 30:
        return "I don't know that"
    if key in responses: 
        return responses[key]
    else:
        return "I don't know that"


# This function will pass your text to the machine learning model
# and return the top result with the highest confidence
def classify(text):
    key = "c9d1e700-c2b0-11e9-a971-e3949585133e784e5636-0e81-4a2f-9d49-f0a5d288844a"
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"

    response = requests.get(url, params={ "data" : text })

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()

#response = classify("What is the stanley cup?")
#print(response)
def main():
    print("Welcome to the Stanley cup Journal\n")
    print("You can ask me anything about the Stanley Cup or type quit\n")

    user_input = ""

    while user_input != "quit":
        user_input = input("What's your question? ").lower()
        #print(user_input)
        if user_input != "quit":
            intent = classify(user_input)
            response = process_intent(intent)
            print(response)
    
    print("It was good talking to you.\nGood-bye!")


main()