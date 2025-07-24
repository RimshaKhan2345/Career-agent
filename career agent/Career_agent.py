from agents import function_tool

@function_tool
def get_career_roadmap(field: str) -> str:
    maps = {
        "software engineer": "Learn programming languages, data structures, algorithms, web dev, Github, Projects.",
        "data scientist": "Learn statistics, data analysis, machine learning, Python, ML, Pandas, and real-world datasets.",
        "graphic designer": "Learn Figma, Photoshop, Adobe Creative Suite, typography, color theory, Projects.",
        "ai": "Learn AI concepts, machine learning, Deep learning, Python, Transformers, PyTorch, and AI tools."
    }
    return maps.get(field.lower(), "No roadmap available for this field.")