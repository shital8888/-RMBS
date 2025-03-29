import json

def calculate_credit_rating(mortgages):
    total_risk_score = 0
    total_credit_score = 0
    num_mortgages = len(mortgages)

    for mortgage in mortgages:
        risk_score = 0

        # Loan-to-Value (LTV) Ratio
        ltv = mortgage["loan_amount"] / mortgage["property_value"]
        if ltv > 0.9:
            risk_score += 2
        elif ltv > 0.8:
            risk_score += 1

        # Debt-to-Income (DTI) Ratio
        dti = mortgage["debt_amount"] / mortgage["annual_income"]
        if dti > 0.5:
            risk_score += 2
        elif dti > 0.4:
            risk_score += 1

        # Credit Score
        credit_score = mortgage["credit_score"]
        total_credit_score += credit_score
        if credit_score >= 700:
            risk_score -= 1
        elif credit_score < 650:
            risk_score += 1

        # Loan Type
        if mortgage["loan_type"] == "fixed":
            risk_score -= 1
        elif mortgage["loan_type"] == "adjustable":
            risk_score += 1

        # Property Type
        if mortgage["property_type"] == "condo":
            risk_score += 1

        total_risk_score += risk_score

    # Adjust based on average credit score
    avg_credit_score = total_credit_score / num_mortgages
    if avg_credit_score >= 700:
        total_risk_score -= 1
    elif avg_credit_score < 650:
        total_risk_score += 1

    # Determine credit rating
    if total_risk_score <= 2:
        return "AAA"
    elif 3 <= total_risk_score <= 5:
        return "BBB"
    else:
        return "C"

if __name__ == "__main__":
    # Example input
    input_json = '''{
        "mortgages": [
            {
                "credit_score": 750,
                "loan_amount": 200000,
                "property_value": 250000,
                "annual_income": 60000,
                "debt_amount": 20000,
                "loan_type": "fixed",
                "property_type": "single_family"
            },
            {
                "credit_score": 680,
                "loan_amount": 150000,
                "property_value": 175000,
                "annual_income": 45000,
                "debt_amount": 10000,
                "loan_type": "adjustable",
                "property_type": "condo"
            }
        ]
    }'''

    data = json.loads(input_json)
    rating = calculate_credit_rating(data["mortgages"])
    print("Credit Rating:", rating)
