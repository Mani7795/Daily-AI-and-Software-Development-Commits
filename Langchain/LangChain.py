from langchain.llms import OpenAI
from langchain.chains.summarize import load_summarize_chain
from langchain.prompts import PromptTemplate
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter

# Initialize OpenAI LLM
llm = OpenAI(temperature=0, openai_api_key="6oA")

# Load the document
document_path = "Summary.txt"
loader = TextLoader(document_path)
documents = loader.load()

# Split the document into chunks
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)

# Define a custom prompt for summarization
summary_prompt = PromptTemplate(
    input_variables=["text"],
    template="Summarize the following text:\n\n{text}\n\nProvide a concise summary."
)

# Define a custom prompt for topic generation
topic_prompt = PromptTemplate(
    input_variables=["summary"],
    template="Based on the following summary, provide a topic:\n\n{summary}"
)

# Create the summarization chain
summarize_chain = load_summarize_chain(llm, chain_type="map_reduce", map_prompt=summary_prompt)

# Generate the summary
summary = summarize_chain.run(docs)

# Generate the topic
topic_chain = load_summarize_chain(llm, chain_type="stuff", map_prompt=topic_prompt)
topic = topic_chain.run([{"text": summary}])

# Output the results
print("Summary:")
print(summary)
print("\nTopic:")
print(topic)