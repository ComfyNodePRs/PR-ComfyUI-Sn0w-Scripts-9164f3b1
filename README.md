<h1 align="center">
    sn0w-scripts
</h1>

A collection of nodes and improvements created mainly for testing loras and general ease 

# Get Started

## Install

1. Install [ComfyUi](https://github.com/comfyanonymous/ComfyUI).
2. Clone this repo into `custom_nodes`:
    ```
    cd ComfyUI/custom_nodes
    git clone https://github.com/sn0w12/ComfyUI-Sn0w-Scripts
    ```
3. Start up ComfyUI.

# Important Note
Many of the nodes require these paths to be in your extra_model_paths.yaml (with your real directories of course).

- loras_xl: C:/path/XL
- loras_15: C:/path/1.5

![Example](./imgs/lora_paths_example.png)

# Nodes

## Find Resolution
> An easy way to select a width and height.
> <details>
>    <summary>ℹ️ <i>See More Information</i></summary>
>
>    - Enable flip if you want to swap the resolutions
>
>    ![Find Resolution](./imgs/find_res.png)
>    </details>

## Lora Selector
> Automatically selects X amount of loras between two numbers.
> <details>
>    <summary>ℹ️ <i>See More Information</i></summary>
>
>    - Loras have to be formatted like the default kohya_ss outputs. (lora_name-000001)
>    - Select the first lora.
>    - Select the number of the highest lora you want to test.
>    - Select the amount of loras you want to test.
>    - Outputs list of loras like this: \<lora:name:strength>
>    - Add default generation adds an extra "nothing" at the end of the list, used in Lora Tester to generate an image without the lora.
> 
>    ![Lora Selector](./imgs/lora_selector.png)
>    </details>

## Lora Tester (XL)
> Automatically generates X amount of images with provided loras.
> <details>
>    <summary>ℹ️ <i>See More Information</i></summary>
>
>    - I recommend making lora_info and add_default_generation inputs and using the outputs from the Lora Selector.
>    - Takes normal KSampler input but takes positive and negative inputs as text.
>    - Outputs a batch of images.
> 
>    ![Lora Tester](./imgs/lora_tester.png)
>    </details>

## Character Selector
> Outputs a character name and prompt.
> <details>
>    <summary>ℹ️ <i>See More Information</i></summary>
>
>    - Loads characters.json and outputs prompt based on it.
>    - Note: Currently very small list, feel free to add your own to the json file.
> 
>    ![Character Selector](./imgs/character_selector.png)
>    </details>

## Prompt Combine
> Combines 4 string to a single string.
> <details>
>    <summary>ℹ️ <i>See More Information</i></summary>
>
>    - Combines 4 strings into one with a seperator, but only adds the seperator of there isnt one already at the end of the string.
>    - Removes any duplicate words.
> 
>    ![Prompt Combine](./imgs/prompt_combine.png)
>    </details>

## Lora Stacker
> Outputs a list of loras for Lora Tester.
> <details>
>    <summary>ℹ️ <i>See More Information</i></summary>
>
>    - Basically Lora Selector but manual.
>    - Specifically for the lora testers.
> 
>    ![Lora Stacker](./imgs/lora_stacker.png)
>    </details>

## Load Lora XL/1.5
> Normal load lora but from another folder.
> <details>
>    <summary>ℹ️ <i>See More Information</i></summary>
>
>    - Add these to your extra_model_paths.yaml (for example):
>    - loras_xl: C:/path/XL
>    - loras_15: C:/path/1.5
>    - Shows an alphabetically sorted list.
>    ![Load Lora](./imgs/load_lora.png)
>    ![Example](./imgs/lora_paths_example.png)
>    </details>

## Load Lora Character
> Finds and applies the closest matching Lora model to a character based on name similarity.
> <details>
>    <summary>ℹ️ <i>See More Information</i></summary>
>
>    - The process begins by cleaning the input character string for comparison. It then searches a JSON file for a matching character name. If a match is found, it proceeds to select the appropriate folder based on the `xl` boolean flag.
>    - To find the closest Lora model, it calculates the Levenshtein distance between the character name (in full and in parts) and the filenames of available Lora models. This ensures a case-insensitive match with the best possible model.
>    - If no lora is found it just returns the input model and the workflow can continue.
>
>
>    ![Load Lora Character](./imgs/load_lora_character.png)
>    </details>

# Example Workflows