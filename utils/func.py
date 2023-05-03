from langchain.llms import OpenAIChat
from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    HumanMessage,
    SystemMessage
)


def calc_time(email_content: str):
    model_name = "gpt-4"
    if len(email_content) > 9000:
        model_name = "gpt-4-32k"
    chat = ChatOpenAI(model_name=model_name, temperature=0)
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
    model_name = "gpt-4"
    if len(email_content) > 9000:
        model_name = "gpt-4-32k"
    chat = ChatOpenAI(model_name=model_name, temperature=0)
    email_template = """Following is meeting time discussion email thread:

    ##############
    {email_content}
    ##############
    """
    email_prompt = PromptTemplate(
        input_variables=["email_content"],
        template=email_template
    )
    messages = [
        SystemMessage(
            content="You are AI Bot which is responsible for executive assistance. You have to write down kind reply email."),
        HumanMessage(content=email_prompt.format(email_content=email_content))
    ]
    output = chat(messages).content
    return output


def check_whether_schedule(email_thread):
    model_name = "gpt-4"
    if len(email_thread) > 9000:
        model_name = "gpt-4-32k"
    chat = ChatOpenAI(model_name=model_name, temperature=0)
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


def sort_messages(thread, sender, sendtime):
    model_name = "gpt-4"
    if len(thread) > 9000:
        model_name = "gpt-4-32k"
    chat = ChatOpenAI(model_name=model_name, temperature=0)
    check_template = """It is mainly decoded in reverse order. The top message is the latest mssage but its sender {sender} and send datetime {sendtime} is not mentioned in the thread. You have to keep rule when mention about sender, for example, "On Mon, Apr 10, 2023 at 5:35 PM Denis Titov <titov.denis2@gmail.com> wrote:". Rearrange the messages in right order and mention about sender, send datetime in the latest message.
    
    ###############
    {email_thread}
    ###############
    """
    check_prompt = PromptTemplate(
        input_variables=["email_thread", "sender", "sendtime"],
        template=check_template
    )
    messages = [
        SystemMessage(
            content="You are AI Bot that rearrange the decoded message in email thread."),
        HumanMessage(content=check_prompt.format(
            email_thread=thread, sender=sender, sendtime=sendtime))
    ]
    output = chat(messages).content
    return output
