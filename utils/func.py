from langchain.llms import OpenAIChat
from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    HumanMessage,
    SystemMessage
)


def calc_time(email_content: str):
    chat = ChatOpenAI(model="gpt-4", temperature=0)
    email_template = """Following is meeting time discussion email thread and calculate the exact meeting date and time on this email thread:

    ##############
    {email_content}
    ##############

    Only answer date and time.
    """
    email_prompt = PromptTemplate(
        input_variables=["email_content"],
        template=email_template
    )
    messages = [
        SystemMessage(content="You are AI Bot that calculates suitable meeting time for people about given email thread. You have to determine exact meeting date and time that is as suitable as possible for everyone."),
        HumanMessage(content=email_prompt.format(email_content=email_content))
    ]
    output = chat(messages).content
    return output


def predict_reply(email_content: str):
    chat = ChatOpenAI(model="gpt-4", temperature=0)
    email_template = """Following is meeting time discussion email thread and schedule the exact meeting datetime and reply kindly to people's email:

    ##############
    {email_content}
    ##############
    """
    email_prompt = PromptTemplate(
        input_variables=["email_content"],
        template=email_template
    )
    messages = [
        SystemMessage(content="You are AI Bot which is responsible for executive assistance. You have to schedule exact meeting date and time that is as suitable as possible for everyone and reply kindly to each person's email in thread."),
        HumanMessage(content=email_prompt.format(email_content=email_content))
    ]
    output = chat(messages).content
    return output


def check_whether_schedule(email_thread):
    chat = ChatOpenAI(model_name="gpt-4", temperature=0)
    check_template = """Check whether the mail is meeting schedule discussion mail.
    
    ###############
    {email_thread}
    ###############
    
    Answer format must be True or False.
    """
    check_prompt = PromptTemplate(
        input_variables=["email_thread"],
        template=check_template
    )
    messages = [
        SystemMessage(
            content="You are AI Bot that checks email and identifies the mail is related to meeting schedule."),
        HumanMessage(content=check_prompt.format(email_thread=email_thread))
    ]
    output = chat(messages).content
    return output
