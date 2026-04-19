import json
from llm_help import llm
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException

def process_post(raw_file_path, processes_file_path="Data/processed_posts.json"):
    enriched_posts = []
    with open(raw_file_path, encoding='utf-8') as file:
        posts = json.load(file)
        for post in posts:
            metadata = extract_metadata(post['text'])
            post_with_metadata = post | metadata
            enriched_posts.append(post_with_metadata)

    unified_tags = get_unified_tags(enriched_posts)
    for post in enriched_posts:
        current_tags = post['tags']
        new_tags = {unified_tags[tag] for tag in current_tags}
        post['tags'] = list(new_tags)

    with open(processes_file_path, encoding='utf-8', mode="w") as outfile:
        json.dump(enriched_posts, outfile, indent=4)

def extract_metadata(post): 
    template = '''
    You are given a LinkedIn post. You need to extract number of lines, language of the post and tags.
    1. Return a valid JSON. No preamble. 
    2. JSON object should have exactly three keys: line_count, language and tags. 
    3. tags is an array of text tags. Extract maximum two tags.
    4. Language should be English or Hinglish (Hinglish means hindi + english)
    
    Here is the actual post on which you need to perform this task:  
    {post}
    '''

    pt = PromptTemplate.from_template(template)
    chain = pt | llm
    response = chain.invoke(input={"post": post})

    try:
        json_parser = JsonOutputParser()
        res = json_parser.parse(response.content)
    except OutputParserException:
        raise OutputParserException("Context too big. Unable to parse jobs.")
    return res


def get_unified_tags(posts_with_metadata):
    unique_tags = set()
    # Loop through each post and extract the tags
    for post in posts_with_metadata:
        unique_tags.update(post['tags'])  # Add the tags to the set

    unique_tags_list = ','.join(unique_tags)

    # 1. Initialize the parser FIRST so we can inject its instructions into the prompt
    json_parser = JsonOutputParser()

    # 2. Update the template to be much stricter about the output format
    template = '''
    You are an expert data categorizer. I will give you a list of tags. 
    You must unify similar tags into broader categories.
    
    Examples of unification:
    - "LLMs", "GPT", "GenAI" -> "Artificial Intelligence"
    - "LangGraph", "Multi-Agent" -> "AI Agents"
    - "Job Search", "Internships" -> "Career Development"
    
    CRITICAL RULES:
    1. Output ONLY a valid JSON object. 
    2. DO NOT write any Python script or code. 
    3. DO NOT include any conversational text, explanations, or preamble.
    4. The JSON keys must be the original tags, and the values must be the unified tags in Title Case.
    
    {format_instructions}
    
    Here is the list of tags: 
    {tags}
    '''
    
    # 3. Pass the format_instructions into the PromptTemplate
    pt = PromptTemplate(
        template=template,
        input_variables=["tags"],
        partial_variables={"format_instructions": json_parser.get_format_instructions()}
    )
    
    chain = pt | llm
    response = chain.invoke(input={"tags": str(unique_tags_list)})
    
    try:
        res = json_parser.parse(response.content)
    except OutputParserException:
        raise OutputParserException("Context too big or LLM failed to output JSON. Unable to parse tags.")
    
    return res

if __name__ == "__main__":
    process_post("Data/raw_post.json", "Data/processed_posts.json")