BRICK = {
    "brick_num": 54,
    "brick_title": "Acne, Rosacea, and Other Follicular Disorders",
    "games": [
        {
            "slug": "acne_treatments",
            "title": "Acne Treatments and How They Work",
            "subtitle": "Match each acne treatment to its mechanism, the factor it targets, and when it is used",
            "categories": ["Mechanism", "Pathogenic factor targeted", "Typical use"],
            "data": {
                "Topical retinoids": {
                    "Mechanism": "Bind keratinocyte nuclear receptors to normalize growth",
                    "Pathogenic factor targeted": "Follicular hyperkeratosis (declog pores)",
                    "Typical use": "Comedonal acne; drying, so build up slowly",
                },
                "Salicylic acid": {
                    "Mechanism": "Lipophilic; strips dead cells and sebum from pores",
                    "Pathogenic factor targeted": "Follicular clogging, plus mild anti-inflammation",
                    "Typical use": "Over-the-counter control of hyperkeratosis",
                },
                "Oral isotretinoin": {
                    "Mechanism": "Shrinks sebaceous glands",
                    "Pathogenic factor targeted": "Increased sebum production",
                    "Typical use": "Most severe acne; two forms of birth control",
                },
                "Doxycycline or minocycline": {
                    "Mechanism": "Reduce bacteria and are intrinsically anti-inflammatory",
                    "Pathogenic factor targeted": "C. acnes and inflammation",
                    "Typical use": "More severe inflammatory acne; not in pregnancy",
                },
                "Spironolactone": {
                    "Mechanism": "Oral anti-androgen (also a diuretic)",
                    "Pathogenic factor targeted": "Androgen-driven oil production and inflammation",
                    "Typical use": "Long-term suppression of adult hormonal acne in women",
                },
                "Oral contraceptive pills": {
                    "Mechanism": "Feedback inhibition of the ovaries",
                    "Pathogenic factor targeted": "Ovarian androgen output (more estrogen, less oil)",
                    "Typical use": "Women with hormonal cystic acne",
                },
            },
        },
        {
            "slug": "rosacea_subtypes",
            "images": {"Papulopustular": "pic_img/msk-54-030.jpg", "Phymatous": "pic_img/msk-54-031.jpg"},
            "title": "The Four Rosacea Subtypes",
            "subtitle": "Match each rosacea subtype to its hallmark findings, distinguishing clue, and treatment",
            "categories": ["Hallmark findings", "Distinguishing clue", "Treatment"],
            "data": {
                "Erythematotelangiectatic": {
                    "Hallmark findings": "Flushing and persistent facial erythema",
                    "Distinguishing clue": "May show roughness or scaling; no papules",
                    "Treatment": "Topical brimonidine or oxymetazoline (vasoconstriction)",
                },
                "Papulopustular": {
                    "Hallmark findings": "Erythema and telangiectases with papules or pustules",
                    "Distinguishing clue": "Pinpoint pustules or follicular spines suggest Demodex",
                    "Treatment": "Topical metronidazole or ivermectin; oral tetracyclines",
                },
                "Phymatous": {
                    "Hallmark findings": "Thickened skin with irregular nodules",
                    "Distinguishing clue": "Nose and chin most affected (rhinophyma)",
                    "Treatment": "Electrosurgery, laser, cryotherapy, or hot scalpel",
                },
                "Ocular": {
                    "Hallmark findings": "Red, swollen eyelid margins with pustules and dryness",
                    "Distinguishing clue": "Foreign body sensation, photophobia; rare keratitis",
                    "Treatment": "Artificial tears, lid cleansing, cyclosporine drops",
                },
            },
        },
        {
            "slug": "follicular_mediators",
            "title": "Inflammatory Mediators of Follicular Disease",
            "subtitle": "Match each mediator to its disorder, where it comes from, and what it does",
            "categories": ["Disorder", "Source or trigger", "Effect"],
            "data": {
                "IL-1β": {
                    "Disorder": "Acne vulgaris (also named in hidradenitis)",
                    "Source or trigger": "Cleaved by the NLRP3 inflammasome after C. acnes growth",
                    "Effect": "Amplifies pain, redness, and swelling",
                },
                "IL-8 and IL-12": {
                    "Disorder": "Acne vulgaris",
                    "Source or trigger": "Macrophage toll-like receptor activation",
                    "Effect": "Recruit neutrophils to the ruptured follicle",
                },
                "Kallikrein-5 (KLK5)": {
                    "Disorder": "Rosacea",
                    "Source or trigger": "Raised by TLR2 overexpression on keratinocytes",
                    "Effect": "Cleaves the 18-kDa precursor hCAP18",
                },
                "LL-37 (cathelicidin)": {
                    "Disorder": "Rosacea",
                    "Source or trigger": "Fragment released from hCAP18 by protease cleavage",
                    "Effect": "VEGF-driven angiogenesis and leukocyte recruitment",
                },
                "IL-17A/F": {
                    "Disorder": "Hidradenitis suppurativa",
                    "Source or trigger": "Th17 cells driven by IL-23",
                    "Effect": "Recruits neutrophils and drives tunnel formation",
                },
            },
        },
        {
            "slug": "follicular_drug_effects",
            "title": "Follicular Disease Drugs: Adverse Effects",
            "subtitle": "Match each drug to the disorders it treats, its notable adverse effects, and its key interaction or caution",
            "categories": ["Used for", "Notable adverse effects", "Interaction or caution"],
            "data": {
                "Doxycycline": {
                    "Used for": "Acne and moderate-severe papulopustular rosacea",
                    "Notable adverse effects": "Sun sensitivity, nausea, esophageal irritation",
                    "Interaction or caution": "Can lessen oral contraceptive efficacy",
                },
                "Minocycline": {
                    "Used for": "Inflammatory acne and more severe hidradenitis",
                    "Notable adverse effects": "Headache, vertigo, urticaria, DRESS syndrome",
                    "Interaction or caution": "Preferred over doxycycline in hidradenitis",
                },
                "Clindamycin": {
                    "Used for": "Topical for acne; oral with rifampin for hidradenitis",
                    "Notable adverse effects": "Diarrhea",
                    "Interaction or caution": "Topical form is a mainstay in pregnancy",
                },
                "Rifampin": {
                    "Used for": "Combined with oral clindamycin for hidradenitis",
                    "Notable adverse effects": "Red urine",
                    "Interaction or caution": "Speeds metabolism of oral contraceptives",
                },
                "Isotretinoin": {
                    "Used for": "Most severe acne; refractory hidradenitis",
                    "Notable adverse effects": "Birth defects, hypertriglyceridemia, depression, dryness",
                    "Interaction or caution": "Tetracycline co-use risks pseudotumor cerebri",
                },
            },
        },
    ],
}
