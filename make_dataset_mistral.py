from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage
from langchain_mistralai.chat_models import ChatMistralAI
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
import csv

load_dotenv(".env")

model = ChatMistralAI(model='open-mistral-7b', max_tokens=100)


#lyrics_dataset = 'lyrics.csv'
lyrics_csv_path = 'Sweet_Trip.csv'


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
        prompt = PromptTemplate(input_variables=['question1', 'question2', 'lyric'], template=template)

        # create and run a chain
        chain = LLMChain(prompt=prompt, llm=model)
        question = "What are the 3 main moods related to lyrics?"

        out = chain.invoke({'question': question, 'lyric' : lyric})
        print(out['text'])


