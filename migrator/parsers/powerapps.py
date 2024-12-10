import os
from typing import List
import base64
import pandas as pd
import jsonify
from openai import OpenAI

from besser.BUML.metamodel.structural import *
from besser.BUML.notations.structuralPlantUML import plantuml_to_buml

def openai_request(image_path: str, csv_paths: List[str], openai_token: str):
    # Load local image
    with open(image_path, "rb") as image_file:
        image_base64 = base64.b64encode(image_file.read()).decode("utf-8")
    
    # Load CSV files
    csv_contents = {}
    for csv_file in csv_paths:
        csv_path = os.path.join(os.getcwd(), csv_file)
        if os.path.exists(csv_path):
            csv_data = pd.read_csv(csv_path)
            csv_contents[csv_file] = csv_data.to_csv(index=False)
        else:
            print(f"File {csv_file} not found.")
            return jsonify({"error": f"{csv_file} not found"}), 400

    # Prepare text data (modify as needed)
    text = "Can you turn this image of a data model into the corresponding class diagram in PlantUML notation? The image contains the graphical overview of the classes and a lot of redundant classes. The csv files contain the concrete attributes, yet only copy the attributes unique to the classes. Add attributes using the notation 'attribute: type' and follow python type names."

    # Set up OpenAI client
    client = OpenAI(api_key=openai_token)  # Replace with your actual API key

    # Prepare the payload
    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": f"{text}",
                },
                {
                    "type": "image_url",
                    "image_url": {"url": f"data:image/jpeg;base64,{image_base64}"},
                },
            ],
        }
    ]

    for file_name, file_content in csv_contents.items():
        messages.append({
            "role": "user",
            "content": {
                "type": "file",
                "file": {
                    "name": file_name,
                    "content": file_content,
                },
            },
        })

    # Send to ChatGPT
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
    )

    # Process the response
    messages = [choice.message for choice in response.choices]
    message = messages[0].content

    # Extract UML chunk
    start_position = message.find("@startuml")
    end_position = message.find("@enduml", start_position)
    uml_chunk = message[start_position:end_position + len("@enduml")]


    # Save UML chunk to file
    file_name = "plantuml.txt"
    with open(file_name, 'w') as file:
        file.write(uml_chunk)

    return uml_chunk


def powerapps_to_buml(image_path: str, csv_paths: str, openai_token: str, encoding: str = "utf-16") -> DomainModel:
    """Converts a Powerapps model to a B-UML domain model."""
    if not os.path.exists(image_path) or os.path.getsize(image_path) == 0:
        print("The image is empty or does not exist.")
        return None
    
    for csv in csv_paths:
        if not os.path.exists(csv) or os.path.getsize(csv) == 0:
            print(f"The csv file called {csv} is empty or does not exist.")
            return None  

    openai_request(image_path=image_path, csv_paths=csv_paths, openai_token=openai_token)
    
    b_uml_model: DomainModel = plantuml_to_buml(plantUML_model_path="plantuml.txt")

    return b_uml_model
