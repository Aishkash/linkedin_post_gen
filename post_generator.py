from llm_help import llm
from few_shot import FewShotPosts

few_shot = FewShotPosts()


def get_length_str(length):
    if length == "Short":
        return "1 to 5 lines"
    if length == "Medium":
        return "11 to 15 lines"
    if length == "Long":
        return "20 to 30 lines"


def generate_post(length, language, tag, user_prompt=""):
    prompt = get_prompt(length, language, tag, user_prompt)
    response = llm.invoke(prompt)
    return response.content


def get_prompt(length, language, tag, user_prompt=""):
    length_str = get_length_str(length)

    prompt = f'''
    Generate a LinkedIn post using the below information. No preamble.

    1) Topic: {tag}
    2) Length: {length_str}
    3) Language: {language}
    If Language is Hinglish then it means it is a mix of Hindi and English. 
    The script for the generated post should always be English.
    '''
    

    if user_prompt.strip():
        prompt += f"\n4) Additional Context/Requirements: {user_prompt}"

    examples = few_shot.get_filtered_posts(length, language, tag)

    if len(examples) > 0:
        example_number = 5 if user_prompt.strip() else 4
        prompt += f"{example_number}) Use the writing style as per the following examples."

    for i, post in enumerate(examples):
        post_text = post['text']
        prompt += f'\n\n Example {i+1}: \n\n {post_text}'

        if i == 1: # Use max two samples
            break

    return prompt


if __name__ == "__main__":
    print(generate_post("Medium", "English", "Job Search"))