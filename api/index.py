import json
import os

def handler(request, response):
    try:
        # Load student data from file
        json_path = os.path.join(os.path.dirname(__file__), '..', 'q-vercel-python.json')

        with open(json_path, 'r') as f:
            students = json.load(f)

        # Create a dictionary for fast lookup
        student_dict = {student["name"]: student["marks"] for student in students}

        # Parse query parameters
        names = request.query.get("name")
        if not names:
            return response.json({"error": "No name provided"}, status=400)

        if isinstance(names, str):
            names = [names]  # support single name as well

        result = []
        for name in names:
            result.append({name: student_dict.get(name, None)})

        return response.json(result)

    except Exception as e:
        return response.json({"error": str(e)}, status=500)
