1. Create the following files: requirements.txt, pyproject.toml, README.md

2. Create the folder config:

    - config/config.yaml
    - config/prompts.yaml

3. Create the following folders inside src/blogforge_ai

    - constants/_init__.py
    - utils >> _init__.py, common.py
    - graph >> _init__.py, state.py, schemas.py, nodes.py, llm_factory.py, pipeline.py

4. Create the following utility method:

    - Read the yaml file
    - To create the safe_slug
    - Read the config.yaml file, prompts.yaml file

5. Define the state class of the Graph.

6. Define the schemas required based on which the llm will structure its output.

7. Define the nodes

    - router_node
    
    - research_node
    
    - orchestrator_node
    
    - worker
    
    - Sub-Graph of reducer node with following nodes

        - merge_content
        - decide_images
        - generate_and_place_images

----

### Use Tavily

- Goto tavily website which is a search engine for web.

- Create a account on tavily.

- Then we get the api key from tavily.

- place that api_key in env file.