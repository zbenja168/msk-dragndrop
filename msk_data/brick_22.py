BRICK = {
    "brick_num": 22,
    "brick_title": "Pharmacologic Treatment of Musculoskeletal Pain",
    "games": [
        {
            "slug": "muscle_relaxants",
            "title": "Skeletal Muscle Relaxants",
            "subtitle": "Match each muscle relaxant to its mechanism, pharmacokinetics and key precaution",
            "categories": ["Mechanism / site", "Key pharmacokinetics", "Key precaution"],
            "data": {
                "Cyclobenzaprine": {
                    "Mechanism / site": "Tricyclic-related; reduces tonic motor activity in brainstem",
                    "Key pharmacokinetics": "Hepatic metabolism; long, variable half-life",
                    "Key precaution": "Contraindicated with MAO inhibitors and conduction disease"
                },
                "Methocarbamol": {
                    "Mechanism / site": "Incompletely defined; likely CNS depression",
                    "Key pharmacokinetics": "Hepatic metabolism; short half-life",
                    "Key precaution": "Short half-life does not eliminate driving impairment"
                },
                "Carisoprodol": {
                    "Mechanism / site": "Centrally acting antispasmodic; mechanism incompletely defined",
                    "Key pharmacokinetics": "Metabolized to meprobamate, a sedating active metabolite",
                    "Key precaution": "Abuse potential, dependence and withdrawal; generally avoid"
                },
                "Orphenadrine": {
                    "Mechanism / site": "Central antispasmodic with analgesic, anticholinergic properties",
                    "Key pharmacokinetics": "Spasm-relief mechanism incompletely defined",
                    "Key precaution": "Avoid in glaucoma, prostatic hypertrophy, older adults"
                },
                "Baclofen": {
                    "Mechanism / site": "Spinal GABA-B agonist",
                    "Key pharmacokinetics": "Cleared mainly unchanged by the kidneys",
                    "Key precaution": "Abrupt intrathecal interruption: rebound spasticity, hyperthermia, seizures"
                },
                "Tizanidine": {
                    "Mechanism / site": "Central alpha-2 agonist reducing input to motor neurons",
                    "Key pharmacokinetics": "Short-acting; hepatic metabolism by CYP1A2",
                    "Key precaution": "Ciprofloxacin and fluvoxamine contraindicated"
                }
            }
        },
        {
            "slug": "analgesics",
            "title": "Analgesics for Musculoskeletal Pain",
            "subtitle": "Match each analgesic to its mechanism, major adverse effect and role",
            "categories": ["Mechanism", "Major adverse effect", "Role or limit"],
            "data": {
                "Ibuprofen / naproxen": {
                    "Mechanism": "Nonselective COX-1 and COX-2 inhibition",
                    "Major adverse effect": "GI ulceration and bleeding, acute kidney injury",
                    "Role or limit": "Lowest dose, shortest duration; never two systemic NSAIDs"
                },
                "Celecoxib": {
                    "Mechanism": "Selective COX-2 inhibition at usual doses",
                    "Major adverse effect": "Renal and cardiovascular risk still present",
                    "Role or limit": "Reduces some GI toxicity, not all NSAID risk"
                },
                "Topical diclofenac": {
                    "Mechanism": "COX inhibition delivered to a superficial site",
                    "Major adverse effect": "Lower systemic exposure, though risk is not zero",
                    "Role or limit": "First-line for acute non-low back sprain or strain"
                },
                "Ketorolac": {
                    "Mechanism": "Nonselective COX inhibition, oral or parenteral",
                    "Major adverse effect": "GI, bleeding and renal risks",
                    "Role or limit": "Combined systemic use limited to 5 days in adults"
                },
                "Acetaminophen": {
                    "Mechanism": "Central modulation of prostaglandin synthesis and pain signaling",
                    "Major adverse effect": "Hepatotoxicity; antidote is N-acetylcysteine",
                    "Role or limit": "General adult ceiling 4 g/day from all products"
                },
                "Opioids (mu agonists)": {
                    "Mechanism": "Gi/o-coupled receptor; decreases adenylyl cyclase activity",
                    "Major adverse effect": "Respiratory depression, sedation, miosis, constipation",
                    "Role or limit": "Brief immediate-release course for severe acute pain"
                }
            }
        },
        {
            "slug": "clinical_situations",
            "title": "Choosing Therapy by Clinical Situation",
            "subtitle": "Match each clinical situation to its pharmacologic approach and reasoning",
            "categories": ["Pharmacologic approach", "Reasoning or caution"],
            "data": {
                "Acute non-low back injury (sprain/strain)": {
                    "Pharmacologic approach": "Topical NSAID first-line; oral NSAID or acetaminophen alternatives",
                    "Reasoning or caution": "Local relief with less systemic exposure; opioids discouraged"
                },
                "Acute nonspecific low back pain": {
                    "Pharmacologic approach": "Activity and heat; oral NSAID an option; SMRs second line",
                    "Reasoning or caution": "Acetaminophen not recommended; muscle relaxant benefit uncertain"
                },
                "Osteoarthritis": {
                    "Pharmacologic approach": "Topical NSAID for knee and hand; oral NSAID an option",
                    "Reasoning or caution": "Topical drug unlikely to reach the deep hip joint"
                },
                "Severe acute injury or postoperative pain": {
                    "Pharmacologic approach": "Brief immediate-release opioid when nonopioids insufficient",
                    "Reasoning or caution": "Combine with nonopioid measures; reassess sedation and need"
                },
                "Neurologic spasticity": {
                    "Pharmacologic approach": "Antispasticity agent guided by disorder and goals",
                    "Reasoning or caution": "Not interchangeable with ordinary strain treatment"
                }
            }
        },
        {
            "slug": "patient_factors",
            "title": "Patient Factors That Change the Choice",
            "subtitle": "Match each patient factor to its concern and the drugs implicated",
            "categories": ["Concern", "Drugs implicated"],
            "data": {
                "Kidney dysfunction or volume depletion": {
                    "Concern": "Reduced renal perfusion and impaired renal drug clearance",
                    "Drugs implicated": "NSAIDs; baclofen accumulation"
                },
                "Liver disease": {
                    "Concern": "Hepatic metabolism and drug-induced liver injury",
                    "Drugs implicated": "Acetaminophen totals; dantrolene and tizanidine"
                },
                "Older age, falls, cognitive impairment": {
                    "Concern": "Sedation and fracture risk, plus anticholinergic effects",
                    "Drugs implicated": "Cyclobenzaprine and methocarbamol generally avoided"
                },
                "Driving": {
                    "Concern": "A bedtime dose can still cause next-day sedation",
                    "Drugs implicated": "Sedating muscle relaxants such as cyclobenzaprine"
                },
                "Drug interactions": {
                    "Concern": "Additive CNS depression, serotonergic combinations, CYP inhibition",
                    "Drugs implicated": "Ciprofloxacin with tizanidine; opioids with relaxants"
                }
            }
        }
    ]
}
