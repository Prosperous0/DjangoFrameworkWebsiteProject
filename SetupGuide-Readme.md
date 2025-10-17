# Simple Overview & Setup Guide

- 📋 What Each File Does (Simple Explanation)

## 1. models.py - The Database Structure
-What it is: Defines what data you store (like creating Excel tables) Contains:

- Subscriber table (name, email, date joined)
- Recipe table (title, ingredients, instructions, cook time)
- Category table (Italian, American, Desserts)
- Review table (ratings and comments on recipes)
- Contact Message table (messages from website visitors)

`Think of it as: Your database blueprint`

2. serializers.py - Data Translator
What it is: Converts database data to JSON (and vice versa)
Why needed: Apps communicate in JSON format
Example:

Database: Recipe object (id=1)
JSON: {"id": 1, "title": "Pasta", "cook_time": 15}

Think of it as: A translator between database and internet
