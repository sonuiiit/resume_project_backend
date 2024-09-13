from fastapi import APIRouter, UploadFile, File, Form
from PyPDF2 import PdfReader
from io import BytesIO
import openai
from app.utils.groq_utils import get_response
from datetime import datetime, timedelta

from app.constants.prompts import pdf_to_html_prompt


pdf_router = APIRouter(prefix="/pdf_router",tags=["pdf_router"])




@pdf_router.post("/generate-html/")
async def generate_html(pdf: UploadFile = File(...), openai_api_key: str = Form(...)):
    '''
    It is the endpoint function that will be called from the streamlit frontend
    :param pdf: A pdf file
    :param openai_api_key: Open AI key
    :return: will return an html code.
    '''
    # Step 1: Read the uploaded PDF
    content = await pdf.read()

    # Step 2: Extract text from the PDF using PyPDF2
    pdf_reader = PdfReader(BytesIO(content))
    extracted_text = ""
    for page in pdf_reader.pages:
        extracted_text += page.extract_text()

    # Step 3: Use the OpenAI API key provided by the user
    openai.api_key = openai_api_key

    # Step 4: Call the OpenAI API to generate the HTML resume
    try:
        input_dict={"details":extracted_text}
        pdf_prompt=pdf_to_html_prompt.format(**input_dict)
        messages = [
            {
                "role": "system",
                "content": "You are an HTML code writer. Your task is to strictly return only html text. Kindly create a visually good resume with all thing at place. Restrict from giving anything other than the html code"
            },
            {
                "role": "user",
                "content": pdf_prompt
            }
        ]
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages
        )

        # Extract the generated HTML text from the response
        html_resume = response.choices[0].message.content


        return {"html_resume": html_resume}

    except openai.error.AuthenticationError:
        return {"error": "Invalid OpenAI API key."}

    except Exception as e:
        return {"error": str(e)}





