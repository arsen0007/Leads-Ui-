# taxonomy.py
# SINGLE SOURCE OF TRUTH — FULLY RECONCILED

MAIN_CATEGORIES = [
    "Business Law",
    "Criminal Law",
    "Intellectual Property Law",
    "General Civil / Consumer Law",
    "Insurance / Insurance Law",
    "Bankruptcy",
    "Family Law",
    "Military Law",
    "Estate Planning / Elder Law",
    "Immigration Law",
    "Torts",
    "Real Estate Law",
    "Labor / Employment",
    "Mediation",
    "Taxes",
    "General Classification",
]

PRACTICE_TO_MAIN = {

    # -------------------------
    # BUSINESS LAW
    # -------------------------
    "business law": "Business Law",
    "business/ commercial": "Business Law",
    "commercial law": "Business Law",
    "corporate": "Business Law",
    "corporate law": "Business Law",
    "contracts": "Business Law",
    "banking": "Business Law",
    "banking law": "Business Law",
    "finance": "Business Law",
    "securities": "Business Law",
    "investments": "Business Law",
    "mergers & acquisitions": "Business Law",
    "government contracts": "Business Law",
    "antitrust": "Business Law",
    "antitrust & trade regulation": "Business Law",
    "antitrust and consumer protection": "Business Law",
    "cannabis": "Business Law",
    "campaign & political": "Business Law",
    "non-profit/tax exempt": "Business Law",

    # -------------------------
    # CRIMINAL LAW
    # -------------------------
    "criminal": "Criminal Law",
    "criminal law": "Criminal Law",
    "white collar crime": "Criminal Law",
    "traffic offenses": "Criminal Law",
    "juvenile": "Criminal Law",
    "forfeiture": "Criminal Law",

    # -------------------------
    # INTELLECTUAL PROPERTY
    # -------------------------
    "intellectual property": "Intellectual Property Law",
    "intellectual property law": "Intellectual Property Law",
    "patent/ trademark/ copyright": "Intellectual Property Law",
    "internet law": "Intellectual Property Law",
    "media law": "Intellectual Property Law",
    "technology & science": "Intellectual Property Law",
    "privacy law": "Intellectual Property Law",
    "privacy and data security": "Intellectual Property Law",

    # -------------------------
    # GENERAL CIVIL / CONSUMER
    # -------------------------
    "civil litigation": "General Civil / Consumer Law",
    "litigation": "General Civil / Consumer Law",
    "civil rights": "General Civil / Consumer Law",
    "consumer": "General Civil / Consumer Law",
    "class actions": "General Civil / Consumer Law",
    "collections": "General Civil / Consumer Law",
    "subrogation": "General Civil / Consumer Law",

    # -------------------------
    # INSURANCE / MALPRACTICE
    # -------------------------
    "insurance": "Insurance / Insurance Law",
    "malpractice": "Insurance / Insurance Law",
    "medical malpractice": "Insurance / Insurance Law",
    "professional liability": "Insurance / Insurance Law",

    # -------------------------
    # BANKRUPTCY
    # -------------------------
    "bankruptcy": "Bankruptcy",
    "debtor & creditor": "Bankruptcy",
    "debtor-creditor": "Bankruptcy",
    "foreclosure": "Bankruptcy",

    # -------------------------
    # FAMILY LAW
    # -------------------------
    "family": "Family Law",
    "family law": "Family Law",
    "guardianships": "Family Law",
    "disability": "Family Law",

    # -------------------------
    # ESTATE / ELDER
    # -------------------------
    "estate planning/ probate/ wills": "Estate Planning / Elder Law",
    "trusts & estates": "Estate Planning / Elder Law",
    "wills & probate": "Estate Planning / Elder Law",
    "elder": "Estate Planning / Elder Law",
    "elder law": "Estate Planning / Elder Law",

    # -------------------------
    # IMMIGRATION
    # -------------------------
    "immigration": "Immigration Law",
    "international law & immigration": "Immigration Law",

    # -------------------------
    # TORTS
    # -------------------------
    "torts": "Torts",
    "toxic torts": "Torts",
    "personal injury": "Torts",
    "products liability": "Torts",

    # -------------------------
    # REAL ESTATE
    # -------------------------
    "real estate": "Real Estate Law",
    "real property": "Real Estate Law",
    "real property law": "Real Estate Law",
    "real property/ land use": "Real Estate Law",
    "land use": "Real Estate Law",
    "planning & land use": "Real Estate Law",
    "landlord-tenant law": "Real Estate Law",
    "landlord/ tenant": "Real Estate Law",
    "homeowner association law": "Real Estate Law",
    "housing": "Real Estate Law",
    "zoning": "Real Estate Law",
    "construction": "Real Estate Law",
    "construction law": "Real Estate Law",
    "eminent domain": "Real Estate Law",

    # -------------------------
    # LABOR / EMPLOYMENT
    # -------------------------
    "labor": "Labor / Employment",
    "employment": "Labor / Employment",
    "labor & employment": "Labor / Employment",
    "employee benefits": "Labor / Employment",
    "workers compensation": "Labor / Employment",
    "workers' compensation": "Labor / Employment",
    "occupational safety & health": "Labor / Employment",

    # -------------------------
    # MEDIATION / ADR
    # -------------------------
    "alternative dispute resolution": "Mediation",
    "dispute resolution": "Mediation",

    # -------------------------
    # TAXES
    # -------------------------
    "tax": "Taxes",
    "taxation": "Taxes",

    # -------------------------
    # GENERAL CLASSIFICATION
    # -------------------------
    "administrative law": "General Classification",
    "administrative/ regulatory": "General Classification",
    "appellate": "General Classification",
    "appellate practice": "General Classification",
    "constitutional": "General Classification",
    "constitutional law": "General Classification",
    "education": "General Classification",
    "education law": "General Classification",
    "environmental": "General Classification",
    "environmental law": "General Classification",
    "health": "General Classification",
    "health care": "General Classification",
    "human rights": "General Classification",
    "lgbtq": "General Classification",
    "indian": "General Classification",
    "indians & native populations": "General Classification",
    "international": "General Classification",
    "government": "General Classification",
    "legislation": "General Classification",
    "lobbying": "General Classification",
    "judicial officer": "General Classification",
    "communications": "General Classification",
    "animal law": "General Classification",
    "agricultural": "General Classification",
    "sports": "General Classification",
    "maritime": "General Classification",
    "aviation": "General Classification",
    "military": "Military Law",
    "oil": "General Classification",
    "gas & energy": "General Classification",

    # -------------------------
    # META / IGNORE BUT MAP
    # -------------------------
    "general": "General Classification",
    "none specified": "General Classification",
    "not actively practicing law": "General Classification",
}
