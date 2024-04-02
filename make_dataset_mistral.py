from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage
from langchain_mistralai.chat_models import ChatMistralAI
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
import csv

load_dotenv(".env")

model = ChatMistralAI(model='open-mistral-7b', max_tokens=10)


#lyrics_dataset = 'lyrics.csv'
lyrics_csv_path = 'lyrics.csv'

analysis = []

with open(lyrics_csv_path, mode='r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)

    

    for row in csv_reader:
        lyric = row['lyrics']
        # create a prompt template

        template = """Question: {question}

        Lyrics: 
        {lyric}

        Answer in ONLY 3 words, separated by comma.
        Never explain. No need to provide explanation.
        """
        prompt = PromptTemplate(input_variables=['question'], template=template)

        # create and run a chain
        chain = LLMChain(prompt=prompt, llm=model)
        question = "What is the style and formality level of whole text, in three words separated by comma?"

        out = chain.invoke({'question': question, 'lyric' : lyric})
        row['moods'] = out['text']
        print(row['index'] + "\n")
        print(out['text'] + "\n")
        analysis.append(row)


augmented_csv_path = 'augmented_lyrics_style.csv'

with open(augmented_csv_path, mode='w', encoding='utf-8') as file:
    fieldnames = analysis[0].keys()
    print(fieldnames)
    csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
    csv_writer.writeheader()

    for row in analysis:
        csv_writer.writerow(row)


