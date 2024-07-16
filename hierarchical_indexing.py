import json

class TreeNode:
    def __init__(self, node_id, parent_id=None, node_type=None, content=None, page_start=None, page_end=None):
        self.node_id = node_id
        self.parent_id = parent_id
        self.node_type = node_type
        self.content = content
        self.page_start = page_start
        self.page_end = page_end
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

def build_hierarchical_index():
    # Root node
    root = TreeNode(node_id=0, parent_id=None, node_type='root', content='General Navigation')

    # Chapters
    chapters = [
        {"title": "Chapter 1: Form of the Earth", "page_start": 1, "page_end": 10},
        {"title": "Chapter 2: Time", "page_start": 11, "page_end": 28},
        {"title": "Chapter 3: Direction", "page_start": 29, "page_end": 52},
        {"title": "Chapter 4: Speed, Distance and Time", "page_start": 53, "page_end": 66},
        {"title": "Chapter 5: Aeronautical Charts and Chart-Making", "page_start": 67, "page_end": 80},
        {"title": "Chapter 6: Features on Aeronautical Charts", "page_start": 81, "page_end": 92},
        {"title": "Chapter 7: Measuring Track Angle and Track Distance", "page_start": 93, "page_end": 102},
        {"title": "Chapter 8: Map Reading", "page_start": 103, "page_end": 122},
        {"title": "Chapter 9: Principles of Dead Reckoning Air Navigation", "page_start": 123, "page_end": 148},
        {"title": "Chapter 10: Altimeter Settings", "page_start": 149, "page_end": 172},
        {"title": "Chapter 11: The Navigation Computer", "page_start": 173, "page_end": 204},
        {"title": "Chapter 12: Flight Planning", "page_start": 205, "page_end": 232},
        {"title": "Chapter 13: Practical Navigation", "page_start": 233, "page_end": 252},
        {"title": "Chapter 14: The Lost Procedure", "page_start": 253, "page_end": 266},
        {"title": "Chapter 15: VHF Direction Finding (VDF)", "page_start": 267, "page_end": 278},
        {"title": "Chapter 16: Automatic Direction Finding (ADF)", "page_start": 279, "page_end": 302},
        {"title": "Chapter 17: VHF Omni-Directional Range (VOR)", "page_start": 303, "page_end": 330},
        {"title": "Chapter 18: Distance Measuring Equipment (DME)", "page_start": 331, "page_end": 338},
        {"title": "Chapter 19: Ground Radar", "page_start": 339, "page_end": 352},
        {"title": "Chapter 20: Secondary Surveillance Radar (SSR)", "page_start": 353, "page_end": 362},
        {"title": "Chapter 21: Global Positioning System (GPS)", "page_start": 363, "page_end": 370},
    ]

    # Appendices, Syllabus, and Answers
    appendices = [
        {"title": "Appendix A: The Flight Information Service (FIS)", "page_start": 371, "page_end": 378},
        {"title": "Appendix 1: Practical Navigation Test Route", "page_start": 379, "page_end": 382},
        {"title": "Appendix 2: Solutions for Questions on Practical Navigation", "page_start": 383, "page_end": 386},
        {"title": "Appendix 3: Aerodrome Plans", "page_start": 387, "page_end": 390},
    ]

    syllabus = {"title": "Navigation and Radio Aids Syllabus", "page_start": 391, "page_end": 394}

    answers = {"title": "Answers to Navigation and Radio Aids Questions", "page_start": 395}

    # Adding chapters to root
    for chapter_data in chapters:
        chapter_node = TreeNode(
            node_id=chapter_data['page_start'],
            parent_id=0,
            node_type='chapter',
            content=chapter_data['title'],
            page_start=chapter_data['page_start'],
            page_end=chapter_data['page_end']
        )
        root.add_child(chapter_node)

    # Adding appendices to root
    for appendix_data in appendices:
        appendix_node = TreeNode(
            node_id=appendix_data['page_start'],
            parent_id=0,
            node_type='appendix',
            content=appendix_data['title'],
            page_start=appendix_data['page_start'],
            page_end=appendix_data['page_end']
        )
        root.add_child(appendix_node)

    # Adding syllabus to root
    syllabus_node = TreeNode(
        node_id=syllabus['page_start'],
        parent_id=0,
        node_type='syllabus',
        content=syllabus['title'],
        page_start=syllabus['page_start'],
        page_end=syllabus['page_end']
    )
    root.add_child(syllabus_node)

    # Adding answers to root
    answers_node = TreeNode(
        node_id=answers['page_start'],
        parent_id=0,
        node_type='answers',
        content=answers['title'],
        page_start=answers['page_start']
    )
    root.add_child(answers_node)

    return root

def save_to_json(tree, filename):
    def serialize(node):
        serialized_node = {
            "node_id": node.node_id,
            "parent_id": node.parent_id,
            "node_type": node.node_type,
            "content": node.content,
            "page_start": node.page_start,
            "page_end": node.page_end,
            "children": []
        }
        for child in node.children:
            serialized_node["children"].append(serialize(child))
        return serialized_node
    
    serialized_tree = serialize(tree)
    
    with open(filename, 'w') as f:
        json.dump(serialized_tree, f, indent=2)

if __name__ == "__main__":
    hierarchical_tree = build_hierarchical_index()
    save_to_json(hierarchical_tree, 'hierarchical_index.json')
