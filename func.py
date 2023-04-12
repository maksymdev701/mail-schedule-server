from langchain.llms import OpenAI
from langchain import PromptTemplate


def calc_time(email_content: str):
    llm = OpenAI(model_name="text-davinci-003")
    email_template = """You are AI Bot that determines scheduled suitable meeting time for people. Below is meeting time discussion email thread chat log in the same channel. Based on following, determine exact date and time that is as suitable as possible for everyone.

    ##############
    {email_content}
    ##############
    """
    email_prompt = PromptTemplate(
        input_variables=["email_content"],
        template=email_template
    )
    output = llm(email_prompt.format(email_content=email_content))
    return output


def check_whether_schedule(email_thread):
    llm = OpenAI(model_name="text-davinci-003")
    check_template = """You are AI Bot that checks email and identifies the mail is related to meeting schedule. Below is email thread chat log in the same channel. Base on that check the mail is whether meeting schedule discussion mail.
    
    ###############
    {email_thread}
    ###############
    
    Just answer as 'Yes' or 'No'."""
    check_prompt = PromptTemplate(
        input_variables=["email_thread"],
        template=check_template
    )
    output = llm(check_prompt.format(email_thread=email_thread))
    return output