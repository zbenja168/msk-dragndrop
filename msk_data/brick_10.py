BRICK = {
    "brick_num": 10,
    "brick_title": "Neuromuscular Junction Disorders",
    "games": [
        {
            "slug": "nmj_disorders_vs_gbs",
            "title": "MG vs Lambert-Eaton vs Botulism vs GBS",
            "subtitle": "Match each disorder to its target, weakness pattern, reflexes, and association",
            "categories": ["Target", "Weakness pattern", "Reflexes", "Association or source"],
            "data": {
                "Myasthenia gravis": {
                    "Target": "Postsynaptic nicotinic ACh receptors (autoantibodies)",
                    "Weakness pattern": "Fatigable ptosis and diplopia, worse late in the day",
                    "Reflexes": "Usually normal; a single stimulus still transmits",
                    "Association or source": "Thymoma or thymic follicular hyperplasia"
                },
                "Lambert-Eaton syndrome": {
                    "Target": "Presynaptic voltage-gated Ca2+ channels (autoantibodies)",
                    "Weakness pattern": "Proximal leg weakness, trouble rising from a chair",
                    "Reflexes": "Reduced, briefly returning after muscle activation",
                    "Association or source": "Small-cell lung carcinoma (paraneoplastic)"
                },
                "Botulism": {
                    "Target": "SNARE proteins cleaved by Clostridium botulinum toxin",
                    "Weakness pattern": "Rapid descending symmetric flaccid paralysis",
                    "Reflexes": "Decreased because many NMJs fail to activate fibers",
                    "Association or source": "Preserved foods, honey in infants, injection drug use"
                },
                "Guillain-Barre syndrome": {
                    "Target": "Schwann cells and peripheral nerve myelin",
                    "Weakness pattern": "Ascending paralysis with sensory loss",
                    "Reflexes": "Areflexia from failed nerve conduction",
                    "Association or source": "Preceding Campylobacter jejuni gastroenteritis"
                }
            }
        },
        {
            "slug": "mg_diagnostic_tests",
            "title": "Myasthenia Gravis Workup",
            "subtitle": "Match each test to what it shows and its role or caveat",
            "categories": ["What it shows or does", "Role or caveat"],
            "data": {
                "AChR antibody test": {
                    "What it shows or does": "Autoantibodies against acetylcholine receptors",
                    "Role or caveat": "Preferred initial test; may be absent in ocular MG"
                },
                "MuSK antibody test": {
                    "What it shows or does": "Autoantibodies against muscle-specific kinase",
                    "Role or caveat": "Ordered when AChR antibodies are absent but suspicion high"
                },
                "Repetitive nerve stimulation": {
                    "What it shows or does": "Progressively smaller (decremental) muscle response",
                    "Role or caveat": "Electrodiagnostic test of neuromuscular transmission"
                },
                "Ice-pack test": {
                    "What it shows or does": "Cold inhibits AChE, temporarily improving ptosis",
                    "Role or caveat": "Free 2-minute bedside test, 85% sensitive"
                },
                "Edrophonium (Tensilon) test": {
                    "What it shows or does": "Short-acting AChE inhibitor transiently improves weakness",
                    "Role or caveat": "Needs cardiac monitoring; largely replaced"
                },
                "Chest CT": {
                    "What it shows or does": "Evaluates for an associated thymoma",
                    "Role or caveat": "Finding a thymoma may mandate thymectomy"
                }
            }
        },
        {
            "slug": "mg_les_treatments",
            "title": "Treating MG and Lambert-Eaton",
            "subtitle": "Match each therapy to its mechanism or rationale and when it is used",
            "categories": ["Mechanism or rationale", "When used"],
            "data": {
                "Pyridostigmine": {
                    "Mechanism or rationale": "Inhibits AChE without crossing the blood-brain barrier",
                    "When used": "First-line symptomatic MG therapy; diarrhea can limit dose"
                },
                "Azathioprine or mycophenolate": {
                    "Mechanism or rationale": "Immunosuppression, alongside glucocorticoids",
                    "When used": "MG not adequately controlled by AChE inhibitors"
                },
                "IVIG or plasma exchange": {
                    "Mechanism or rationale": "Rapid immune therapy for acute deterioration",
                    "When used": "Severe exacerbations and myasthenic crisis"
                },
                "Thymectomy": {
                    "Mechanism or rationale": "Removes thymoma or hyperplastic thymus with germinal centers",
                    "When used": "Thymoma, or selected generalized MG without thymoma"
                },
                "Amifampridine (3,4-diaminopyridine)": {
                    "Mechanism or rationale": "Blocks presynaptic K+ channels, raising Ca2+ influx",
                    "When used": "Preferred symptomatic therapy for Lambert-Eaton syndrome"
                }
            }
        },
        {
            "slug": "botulism_forms",
            "title": "Forms of Botulism",
            "subtitle": "Match each exposure to how toxin arises, its classic source, and treatment",
            "categories": ["How toxin arises", "Classic source", "Specific treatment"],
            "data": {
                "Foodborne botulism": {
                    "How toxin arises": "Preformed toxin is ingested",
                    "Classic source": "Improperly preserved foods",
                    "Specific treatment": "Equine heptavalent antitoxin (BAT), serotypes A-G"
                },
                "Infant botulism": {
                    "How toxin arises": "Ingested spores colonize the gut and make toxin",
                    "Classic source": "Honey given before age 1 year",
                    "Specific treatment": "Human hyperimmune IgG (BabyBIG), serotypes A and B"
                },
                "Wound botulism": {
                    "How toxin arises": "Spores contaminate a wound and make toxin locally",
                    "Classic source": "Injection drug use",
                    "Specific treatment": "BAT plus penicillin G (metronidazole alternative)"
                },
                "Adult who eats honey": {
                    "How toxin arises": "No toxin; mature microbiota blocks spore colonization",
                    "Classic source": "Honey in an adult diet",
                    "Specific treatment": "None needed"
                }
            }
        }
    ]
}
