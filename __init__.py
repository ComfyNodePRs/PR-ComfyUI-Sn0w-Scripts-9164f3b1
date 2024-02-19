from .src.find_resolution import FindResolutionNode
from .src.lora_selector import LoraSelectorNode
from .src.lora_tester_xl import LoraTestXLNode
from .src.lora_tester import LoraTestNode
from .src.character_select import CharacterSelectNode
from .src.prompt_combine import CombineStringNode
from .src.simple_sampler_xl import SimpleSamplerXlNode
from .src.simple_sampler import SimpleSamplerNode
from .src.lora_stacker import LoraStackerNode
from .src.load_lora_xl import LoraLoraXLNode
from .src.load_lora_15 import LoraLora15Node
from .src.load_lora_character import LoadLoraCharacterNode
from .src.get_font_size import GetFontSizeNode
from .src.get_all_styles import GetStylesNode
from .src.prompt_selector import PromptSelectNode
from .src.load_lora_concept import LoadLoraConceptNode

NODE_CLASS_MAPPINGS = {
    "Find SDXL Resolution": FindResolutionNode,
    "Lora Selector": LoraSelectorNode,
    "Lora Tester XL": LoraTestXLNode,
    "Lora Tester": LoraTestNode,
    "Character Selector": CharacterSelectNode,
    "Prompt Combine": CombineStringNode,
    "Simple Sampler XL": SimpleSamplerXlNode,
    "Simple Sampler": SimpleSamplerNode,
    "Lora Stacker": LoraStackerNode,
    "Load Lora XL": LoraLoraXLNode,
    "Load Lora 1.5": LoraLora15Node,
    "Load Lora Character": LoadLoraCharacterNode,
    "Get Font Size": GetFontSizeNode,
    "Get All Styles": GetStylesNode,
    "Prompt Selector": PromptSelectNode,
    "Load Lora Concept": LoadLoraConceptNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Find SDXL Resolution": "Find SDXL Resolution",
    "Lora Selector": "Lora Selector",
    "Lora Tester XL": "Lora Tester XL",
    "Lora Tester": "Lora Tester",
    "Character Selector": "Character Selector",
    "Prompt Combine": "Prompt Combine",
    "Simple Sampler XL": "Simple Sampler XL",
    "Simple Sampler": "Simple Sampler",
    "Lora Stacker": "Lora Stacker",
    "Load Lora XL": "Load Lora XL",
    "Load Lora 1.5": "Load Lora 1.5",
    "Load Lora Character": "Load Lora Character",
    "Get Font Size": "Get Font Size",
    "Get All Styles": "Get All Styles",
    "Prompt Selector": "Prompt Selector",
    "Load Lora Concept": "Load Lora Concept",
}
