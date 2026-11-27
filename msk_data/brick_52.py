BRICK = {
    "brick_num": 52,
    "brick_title": "Cutaneous T cell Lymphoma",
    "games": [
        {
            "slug": "mf_clinical_stages",
            "images": {"Patch stage": "pic_img/msk-52-027.jpg", "Tumor stage": "pic_img/msk-52-028.jpg"},
            "title": "Mycosis Fungoides Clinical Stages",
            "subtitle": "Match each MF stage to its appearance and its place in the sequence",
            "categories": ["Clinical appearance", "Place in progression"],
            "data": {
                "Patch stage": {
                    "Clinical appearance": "Flat, red, scaly lesions, often annular or kidney-shaped",
                    "Place in progression": "Earliest stage; mimics eczema, tinea, or psoriasis",
                },
                "Plaque stage": {
                    "Clinical appearance": "Raised, thick, scaly red lesions",
                    "Place in progression": "Second stage; more advanced than flat lesions",
                },
                "Tumor stage": {
                    "Clinical appearance": "Nodules of lymphoma cells growing on the skin",
                    "Place in progression": "Third stage; larger, more diffuse dermal infiltrate",
                },
                "Erythrodermic stage": {
                    "Clinical appearance": "Red, scaly skin from head to toe",
                    "Place in progression": "Final stage; malignant cells take over entire skin",
                },
            },
        },
        {
            "slug": "ctcl_path_and_lab_findings",
            "images": {"Pautrier microabscess": "pic_img/msk-52-030.jpg", "Sezary cell": "pic_img/msk-52-029.jpg"},
            "title": "CTCL Pathology and Laboratory Findings",
            "subtitle": "Match each finding to what it is and how it is detected",
            "categories": ["What it is", "How it is found"],
            "data": {
                "Epidermotropism": {
                    "What it is": "Lymphoma cells extending from upper dermis into epidermis",
                    "How it is found": "Skin biopsy of a patch-stage lesion",
                },
                "Pautrier microabscess": {
                    "What it is": "Small intraepidermal clusters of lymphoma cells, not neutrophils",
                    "How it is found": "Skin biopsy showing epidermal clusters",
                },
                "Cerebriform nucleus": {
                    "What it is": "Convoluted nuclear contour resembling brain sulci and gyri",
                    "How it is found": "Microscopy of the malignant T cell",
                },
                "Sezary cell": {
                    "What it is": "Malignant lymphoma cell once it is in the circulation",
                    "How it is found": "Peripheral blood smear",
                },
                "Monoclonal infiltrate": {
                    "What it is": "Cells of a single lineage, indicating a neoplasm",
                    "How it is found": "T-cell receptor gene rearrangement test",
                },
                "Loss of CD7": {
                    "What it is": "Abnormal T-cell population missing a normal marker",
                    "How it is found": "Flow cytometry of the blood",
                },
            },
        },
        {
            "slug": "mf_treatment_ladder",
            "title": "Mycosis Fungoides Treatment Ladder",
            "subtitle": "Match each treatment to the disease it targets and its role",
            "categories": ["Disease targeted", "Role"],
            "data": {
                "High-potency topical corticosteroids": {
                    "Disease targeted": "Mild disease confined to a limited skin area",
                    "Role": "Minimize inflammation; first step for most cases",
                },
                "Topical nitrogen mustard": {
                    "Disease targeted": "Limited patches and plaques, applied to lesions",
                    "Role": "Topical chemotherapy that kills cancer cells",
                },
                "UVB phototherapy": {
                    "Disease targeted": "Stubborn or widespread patch-stage disease",
                    "Role": "Highly effective light therapy given in the office",
                },
                "Total skin electron beam radiotherapy": {
                    "Disease targeted": "Thicker plaques and tumors",
                    "Role": "Radiation delivered to the whole skin surface",
                },
                "Systemic chemotherapy or immunotherapy": {
                    "Disease targeted": "Disseminated disease with internal involvement",
                    "Role": "Considered only once disease spreads beyond skin",
                },
            },
        },
        {
            "slug": "ctcl_prognosis_groups",
            "title": "CTCL Prognosis by Presentation",
            "subtitle": "Match each group to its prognosis and defining feature",
            "categories": ["Prognosis", "Defining feature"],
            "data": {
                "Limited cutaneous MF": {
                    "Prognosis": "Normal life expectancy for most patients",
                    "Defining feature": "Under 10% BSA; staging imaging not needed",
                },
                "Advanced MF": {
                    "Prognosis": "Progression in a small minority of patients",
                    "Defining feature": "Lymphadenopathy, hepatosplenomegaly, marrow failure",
                },
                "Sezary syndrome": {
                    "Prognosis": "Only 20-60% alive at 5 years; infection deaths",
                    "Defining feature": "Over 1000 Sezary cells per mL; erythroderma over 80% BSA",
                },
                "MF in Black patients": {
                    "Prognosis": "Worse survival regardless of age and stage",
                    "Defining feature": "Median diagnosis age 53; more advanced at presentation",
                },
            },
        },
    ],
}
