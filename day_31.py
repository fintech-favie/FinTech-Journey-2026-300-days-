company = {
    "engineering": {
        "lead": "anshika",
        "target": "45lpa",
        "language": "python"
    },
    "design": {
        "lead": "alex",
        "target": "30lpa",
        "tool": "alightmotion"
    }
}

print(f"Engineering Lead: {company['engineering']['lead']}")

company["engineering"]["target"] = "50lpa"
company["engineering"]["status"] = "senior developer"

print(company["engineering"])
