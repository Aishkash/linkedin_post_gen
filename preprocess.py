import json

def process_post(raw_file_path, processes_file_path="Data/processed_posts.json"):
    with open(raw_file_path, encoding='utf-8') as file:
        posts=json.load(file)
        for post in posts:
            metadata=extract_metadata(post['text'])
            post={tex}

def extract_metadata(post): 
    return{
        'lineCount':10,
        "language":"English",
        'tags':["LLMs","Building in public"],
    }

if __name__=="__main__":
    # import os
    # import sys
    # from preprocess import preprocess

    # if len(sys.argv) != 3:
    #     print("Usage: python preprocess.py <input_dir> <output_dir>")
    #     sys.exit(1)

    # input_dir = sys.argv[1]
    # output_dir = sys.argv[2]

    # if not os.path.exists(output_dir):
    #     os.makedirs(output_dir)

    # preprocess(input_dir, output_dir)
    process_post("Data/raw_post.json","Data/processed_post.json")