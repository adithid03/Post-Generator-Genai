# post_generator.py
from llm_helper import llm
from few_shot import FewShotPosts
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

few_shot = FewShotPosts()

def get_length_str(length):
    if length == "Short":
        return "1 to 5 lines"
    if length == "Medium":
        return "6 to 10 lines"
    if length == "Long":
        return "11 to 15 lines"

def generate_post(length, language, tag):
    try:
        logger.info(f"Generating post for length={length}, language={language}, tag={tag}")
        prompt = get_prompt(length, language, tag)
        logger.info("Prompt generated successfully")
        
        # Just pass the prompt string directly
        response = llm.invoke(prompt)
        logger.info("Response received from LLM")
        
        if not response or not response.content:
            raise ValueError("Empty response received from LLM")
            
        return response.content
        
    except Exception as e:
        logger.error(f"Error in generate_post: {str(e)}")
        return f"Error generating post: {str(e)}"

def get_prompt(length, language, tag):
    try:
        length_str = get_length_str(length)
        
        prompt = f'''
        Generate a LinkedIn post using the below information. No preamble.

        1) Topic: {tag}
        2) Length: {length_str}
        3) Language: {language}
        If Language is Hinglish then it means it is a mix of Hindi and English. 
        The script for the generated post should always be English.
        '''

        examples = few_shot.get_filtered_posts(length, language, tag)
        
        if len(examples) > 0:
            prompt += "4) Use the writing style as per the following examples."

        for i, post in enumerate(examples):
            post_text = post['text']
            prompt += f'\n\n Example {i+1}: \n\n {post_text}'

            if i == 1:  # Use max two samples
                break

        return prompt
        
    except Exception as e:
        logger.error(f"Error in get_prompt: {str(e)}")
        raise

if __name__ == "__main__":
    try:
        print(generate_post("Medium", "English", "Mental Health"))
    except Exception as e:
        print(f"Failed to generate post: {str(e)}")