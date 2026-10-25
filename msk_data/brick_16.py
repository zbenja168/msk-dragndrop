BRICK = {
    "brick_num": 16,
    "brick_title": "Muscular Dystrophy",
    "games": [
        {
            "slug": "dystrophy_genetics",
            "title": "Muscular Dystrophy Genetics",
            "subtitle": "Match each dystrophy to its inheritance, molecular defect and weakness pattern",
            "categories": ["Inheritance", "Molecular defect", "Weakness pattern"],
            "data": {
                "Duchenne (DMD)": {
                    "Inheritance": "X-linked recessive; ~40% de novo",
                    "Molecular defect": "Frameshift exon deletion; dystrophin absent",
                    "Weakness pattern": "Severe proximal weakness from age 3-5, Gowers sign",
                },
                "Becker (BMD)": {
                    "Inheritance": "X-linked recessive; rarer, about 1 in 20,000 males",
                    "Molecular defect": "Non-frameshift mutation; shortened, partly functional dystrophin",
                    "Weakness pattern": "Milder, slower DMD-like weakness starting in teens",
                },
                "Myotonic dystrophy type 1": {
                    "Inheritance": "Autosomal dominant with anticipation",
                    "Molecular defect": "CTG expansion in 3' UTR of DMPK",
                    "Weakness pattern": "Distal weakness, foot drop, facial weakness, ptosis",
                },
                "Myotonic dystrophy type 2": {
                    "Inheritance": "Autosomal dominant, no significant anticipation",
                    "Molecular defect": "CCTG expansion in intron 1 of CNBP",
                    "Weakness pattern": "Milder proximal shoulder, hip and thigh weakness",
                },
                "Facioscapulohumeral (FSHD)": {
                    "Inheritance": "Autosomal dominant, 1 in 8,000-20,000",
                    "Molecular defect": "Loss of epigenetic silencing; toxic DUX4 expression",
                    "Weakness pattern": "Face first, then shoulders and upper arms",
                },
                "Limb-girdle (LGMD)": {
                    "Inheritance": "Autosomal dominant and autosomal recessive forms",
                    "Molecular defect": "More than 30 genes, e.g. sarcoglycans, dysferlin",
                    "Weakness pattern": "Proximal shoulder and pelvic girdle weakness",
                },
            },
        },
        {
            "slug": "dystrophy_course",
            "title": "Course and Extramuscular Features",
            "subtitle": "Match each dystrophy to its onset, survival and signature non-muscle finding",
            "categories": ["Typical onset", "Survival / cause of death", "Signature extramuscular finding"],
            "data": {
                "Duchenne (DMD)": {
                    "Typical onset": "Ages 3-5; cannot walk unassisted by 12",
                    "Survival / cause of death": "Rarely beyond 30s; dilated cardiomyopathy in adults",
                    "Signature extramuscular finding": "Intellectual and learning disabilities",
                },
                "Becker (BMD)": {
                    "Typical onset": "Teenage years, variable",
                    "Survival / cause of death": "Often into 40s; heart failure from cardiomyopathy",
                    "Signature extramuscular finding": "Dilated cardiomyopathy leading cause of death",
                },
                "Myotonic dystrophy": {
                    "Typical onset": "20s; congenital DM1 at birth",
                    "Survival / cause of death": "Variable; DM2 often normal lifespan",
                    "Signature extramuscular finding": "Cataracts, frontal balding, insulin resistance",
                },
                "Facioscapulohumeral (FSHD)": {
                    "Typical onset": "Any age; most before age 20",
                    "Survival / cause of death": "Slow progression; most have normal lifespan",
                    "Signature extramuscular finding": "Retinal telangiectasias, sensorineural hearing loss",
                },
                "Limb-girdle (LGMD)": {
                    "Typical onset": "Adolescence or young adulthood",
                    "Survival / cause of death": "Generally live to their 50s or 60s",
                    "Signature extramuscular finding": "Dilated cardiomyopathy in about a quarter of adults",
                },
            },
        },
        {
            "slug": "membrane_proteins",
            "title": "Dystrophy Proteins and Their Jobs",
            "subtitle": "Match each muscle protein to its functional class, normal role and defect consequence",
            "categories": ["Functional class", "Normal role", "Consequence of mutation"],
            "data": {
                "Dystrophin": {
                    "Functional class": "Cytoskeletal linker / molecular shock absorber",
                    "Normal role": "Links actin to alpha- and beta-dystroglycan",
                    "Consequence of mutation": "Membrane fragility, necrosis; DMD or BMD",
                },
                "Sarcoglycans (alpha, beta, gamma, delta)": {
                    "Functional class": "Membrane stability proteins",
                    "Normal role": "Components of the dystrophin-associated glycoprotein complex",
                    "Consequence of mutation": "Fibers less stable and damaged during contraction",
                },
                "Dysferlin": {
                    "Functional class": "Muscle membrane repair protein",
                    "Normal role": "Repairs microscopic sarcolemmal tears from contraction",
                    "Consequence of mutation": "Unrepaired tears and progressive fiber degeneration",
                },
                "Caveolin-3": {
                    "Functional class": "Structural and signaling protein",
                    "Normal role": "Organizes the muscle cell membrane",
                    "Consequence of mutation": "Disrupted signaling pathways for muscle function",
                },
                "Alpha-dystroglycan glycosylation enzymes": {
                    "Functional class": "Extracellular matrix anchoring enzymes",
                    "Normal role": "Glycosylate alpha-dystroglycan for matrix binding",
                    "Consequence of mutation": "Weak fiber-matrix connection during contraction",
                },
            },
        },
        {
            "slug": "md_therapies",
            "title": "Muscular Dystrophy Therapies",
            "subtitle": "Match each therapy to the disease it treats, its mechanism and its effect",
            "categories": ["Used in", "Mechanism", "Effect"],
            "data": {
                "Mexiletine": {
                    "Used in": "Myotonic dystrophy types 1 and 2",
                    "Mechanism": "Voltage-gated sodium channel blocker",
                    "Effect": "Reduces myotonia and repetitive action potentials",
                },
                "Glucocorticoids (prednisone, deflazacort)": {
                    "Used in": "Duchenne muscular dystrophy",
                    "Mechanism": "Slow muscle degeneration",
                    "Effect": "Prolong ambulation and respiratory function",
                },
                "Exon-skipping antisense oligonucleotides": {
                    "Used in": "Duchenne, approved therapy at the RNA level",
                    "Mechanism": "Restore the reading frame of the transcript",
                    "Effect": "Shortened partly functional dystrophin; modest benefit",
                },
                "Micro-dystrophin gene therapy": {
                    "Used in": "Duchenne, gene delivered to muscle cells",
                    "Mechanism": "Supplies a micro-dystrophin gene",
                    "Effect": "Dystrophin-like protein; may slow progression, not curative",
                },
                "CRISPR-Cas9 and siRNA": {
                    "Used in": "Emerging therapies for muscular dystrophies",
                    "Mechanism": "Gene editing or gene silencing of the cause",
                    "Effect": "Potential to target underlying molecular causes",
                },
                "Pacemaker / antiarrhythmics": {
                    "Used in": "Patients with cardiac involvement",
                    "Mechanism": "Supportive cardiac rhythm management",
                    "Effect": "Manage conduction abnormalities and arrhythmias",
                },
            },
        },
    ],
}
