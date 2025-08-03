from decouple import config
from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain_huggingface import HuggingFaceEndpoint

HUGGINGFACEHUB_API_TOKEN = config('HUGGINGFACEHUB_API_TOKEN')
repo_id = "Qwen/Qwen3-Coder-480B-A35B-Instruct"

def askProblem(problem):
    
    llm = HuggingFaceEndpoint(
        repo_id=repo_id,
        huggingfacehub_api_token=HUGGINGFACEHUB_API_TOKEN,
    )


    systemMessagePrompt = SystemMessagePromptTemplate.from_template(
        "You are a highly skilled AI coding assistant. Your task is to analyze the given query and provide accurate, detailed, and optimized coding solutions. Always ensure your response aligns with best practices, is efficient, and considers edge cases. Introduce yourself as a coding assistant."
    )
    humanMessagePrompt = HumanMessagePromptTemplate.from_template("{problem}")

    chatPrompt = ChatPromptTemplate.from_messages([
        systemMessagePrompt, humanMessagePrompt
    ])

   
    formattedPrompt = chatPrompt.format_messages(problem=problem)
    full_prompt_text = "\n".join([msg.content for msg in formattedPrompt])


    response = llm.invoke(full_prompt_text)
    return response
