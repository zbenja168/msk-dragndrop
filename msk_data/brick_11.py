BRICK = {
    "brick_num": 11,
    "brick_title": "Muscle Metabolism",
    "games": [
        {
            "slug": "atp_energy_systems",
            "title": "Muscle ATP Energy Systems",
            "subtitle": "Match each ATP source to its fuel, yield, time window and O2 need",
            "categories": ["Fuel or reaction", "ATP yield / speed", "Dominant time window", "O2 dependence"],
            "data": {
                "Resting ATP pool": {
                    "Fuel or reaction": "Preformed ATP already stored in the fiber",
                    "ATP yield / speed": "Very small pool, used up almost instantly",
                    "Dominant time window": "Sustains contraction for only 1-2 seconds",
                    "O2 dependence": "None; ATP is simply hydrolyzed",
                },
                "Phosphagen system": {
                    "Fuel or reaction": "PCr + ADP to Cr + ATP via creatine kinase",
                    "ATP yield / speed": "Single-step reaction, fastest ATP resynthesis",
                    "Dominant time window": "First ~10 seconds of activity",
                    "O2 dependence": "Anaerobic single-step reaction",
                },
                "Glycolysis": {
                    "Fuel or reaction": "Rapid breakdown of muscle glycogen to pyruvate",
                    "ATP yield / speed": "Rapid but limited: 2 ATP per glucose",
                    "Dominant time window": "From ~10 seconds to about 2 minutes",
                    "O2 dependence": "Anaerobic; excess pyruvate becomes lactate",
                },
                "Oxidative phosphorylation": {
                    "Fuel or reaction": "Acetyl CoA through TCA cycle and ETC",
                    "ATP yield / speed": "Slow to engage but ~30-32 ATP per glucose",
                    "Dominant time window": "Sustained contraction over minutes to hours",
                    "O2 dependence": "Entirely O2-dependent; O2 is final electron acceptor",
                },
            },
        },
        {
            "slug": "fiber_type_tasks",
            "title": "Fiber Types at Work",
            "subtitle": "Match each task to its dominant fiber type, pathway and fitting feature",
            "categories": ["Dominant fiber type", "Main ATP pathway", "Feature that suits the task"],
            "data": {
                "Postural support (soleus, paraspinals)": {
                    "Dominant fiber type": "Type I slow-twitch, red",
                    "Main ATP pathway": "Oxidative phosphorylation, with high lipid stores",
                    "Feature that suits the task": "High capillary density and small diameter aid O2 diffusion",
                },
                "Elite marathon running": {
                    "Dominant fiber type": "High proportion of Type I fibers",
                    "Main ATP pathway": "Aerobic metabolism yielding 30-32 ATP per glucose",
                    "Feature that suits the task": "Prolonged low-to-moderate force without fatigue",
                },
                "Sustained power output": {
                    "Dominant fiber type": "Type IIA fast, intermediate, red",
                    "Main ATP pathway": "Dual oxidative-glycolytic capability",
                    "Feature that suits the task": "More mitochondria and myoglobin than Type IIX",
                },
                "Sprint or explosive resistance effort": {
                    "Dominant fiber type": "Type IIX fast-twitch, white",
                    "Main ATP pathway": "Glycolysis fueled by abundant glycogen",
                    "Feature that suits the task": "High ATPase and Ca2+ machinery for fast, high force",
                },
            },
        },
        {
            "slug": "metabolism_molecules",
            "title": "Key Molecules of Muscle Metabolism",
            "subtitle": "Match each molecule to its role, location and key feature",
            "categories": ["Role", "Location", "Key feature"],
            "data": {
                "Creatine kinase": {
                    "Role": "Transfers phosphate from PCr to ADP",
                    "Location": "Cytosol of the muscle cell",
                    "Key feature": "Serum level is a non-specific muscle injury marker",
                },
                "Phosphocreatine": {
                    "Role": "High-energy phosphate donor buffering early ATP drop",
                    "Location": "Readily available stores within muscle",
                    "Key feature": "Depleted within about 10 seconds of intense effort",
                },
                "Muscle glycogen": {
                    "Role": "Intracellular fuel liberated for glycolysis",
                    "Location": "Abundant in Type IIX glycolytic fibers",
                    "Key feature": "Mobilized by Ca2+-calmodulin and beta2-cAMP signaling",
                },
                "Myoglobin": {
                    "Role": "Binds, stores and releases O2 inside the fiber",
                    "Location": "Skeletal muscle only; absent from the bloodstream",
                    "Key feature": "One O2 site, high affinity, hyperbolic curve",
                },
                "Hemoglobin": {
                    "Role": "Carries O2 in blood and hands it to muscle",
                    "Location": "Red cells within capillary blood",
                    "Key feature": "Four O2 sites, lower affinity, sigmoidal curve",
                },
            },
        },
        {
            "slug": "metabolic_muscle_disorders",
            "title": "Metabolic Muscle Disorders and Fatigue",
            "subtitle": "Match each condition to its problem, clinical effect and key finding",
            "categories": ["Underlying problem", "Clinical or physiologic effect", "Key associated finding"],
            "data": {
                "Muscle glycogen storage disorder": {
                    "Underlying problem": "Variants in glycogen synthesis, degradation or regulation genes",
                    "Clinical or physiologic effect": "Cramps and pain after short moderate-intense exercise",
                    "Key associated finding": "Myoglobinuria and progressive trunk and limb weakness",
                },
                "Mitochondrial myopathy": {
                    "Underlying problem": "Impaired OXPHOS via respiratory chain complexes I-V",
                    "Clinical or physiologic effect": "Premature fatigue, myalgia, proximal muscle weakness",
                    "Key associated finding": "Elevated CK; rhabdomyolysis only less often",
                },
                "Rhabdomyolysis": {
                    "Underlying problem": "Fiber damage from crush, extreme exertion or toxins",
                    "Clinical or physiologic effect": "Tea-colored urine and risk of acute kidney injury",
                    "Key associated finding": "Heme-positive dipstick without RBCs; high serum CK",
                },
                "Intense-exercise acidosis": {
                    "Underlying problem": "H+ accumulation from glycolysis and ATP breakdown",
                    "Clinical or physiologic effect": "H+ displaces Ca2+ from troponin and slows glycolysis",
                    "Key associated finding": "Fatigue that parallels lactate accumulation",
                },
            },
        },
    ],
}
