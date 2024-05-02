narrative_options = "Bills, Groceries, Entertainment, Rent, Shopping"

graph_schema = f"""
Node properties are the following:\n
Person {{name: STRING, birth_date: DATE}},
Transaction {{transaction_id: INTEGER, transaction_date: DATE, narrative: STRING, type: STRING, amount: INTEGER, balance: INTEGER}}, "date format is 2024-02-15" "narrative can only be one of the following: {narrative_options}"
Account {{account_number: INTEGER, sort_code: INTEGER, account_type: STRING}},
Shop {{merchant_name: STRING, account_number: INTEGER, sort_code: INTEGER}},
Category {{transaction_category: STRING}} "This category can either be: {{online shopping, in-store}}"

The relationships between the nodes are the following:\n
(:Person)-[:MADE]->(:Transaction),
(:Person)-[:HAS]->(:Account),
(:Transaction)-[:PAID_TO]->(:Shop),
(:Transaction)-[:CLASSIFIED_AS]->(:Category),
(:Transaction)-[:PAID_BY]->(:Account)
"""
