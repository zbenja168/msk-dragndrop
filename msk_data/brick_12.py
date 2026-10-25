BRICK = {
    "brick_num": 12,
    "brick_title": "Skeletal Muscle Adaptations",
    "games": [
        {
            "slug": "regeneration_stages",
            "title": "Stages of Muscle Regeneration",
            "subtitle": "Match each stage of regeneration to its order, key events, and cells or markers",
            "categories": ["Order", "Key events", "Cells or markers"],
            "data": {
                "Degeneration": {
                    "Order": "First: the triggering injury phase",
                    "Key events": "Sarcolemma dissolves and myofiber permeability rises",
                    "Cells or markers": "Creatine kinase leaks into the plasma",
                },
                "Inflammation": {
                    "Order": "Second: follows sarcolemmal breakdown",
                    "Key events": "Damaged tissue cleared; repair signals released",
                    "Cells or markers": "Neutrophils and macrophages",
                },
                "Satellite cell activation and differentiation": {
                    "Order": "Third: after inflammatory clearance",
                    "Key events": "Myoblasts fuse into multinucleated myotubes that mature",
                    "Cells or markers": "Satellite cells and myogenic progenitor myoblasts",
                },
                "Remodeling": {
                    "Order": "Final stage of regeneration",
                    "Key events": "Extracellular matrix remodeled and new fibers reinnervated",
                    "Cells or markers": "Angiogenesis restores the surrounding vasculature",
                },
            },
        },
        {
            "slug": "adaptation_signaling",
            "title": "Signals Behind Muscle Adaptation",
            "subtitle": "Match each signaling molecule to its trigger, its action, and the adaptation it serves",
            "categories": ["Activated or triggered by", "Main action", "Adaptation served"],
            "data": {
                "IGF-1": {
                    "Activated or triggered by": "Muscle contraction during exercise",
                    "Main action": "Initiates the cascade leading to Akt and mTOR",
                    "Adaptation served": "Hypertrophy with resistance training",
                },
                "Akt": {
                    "Activated or triggered by": "Upstream phosphorylation in the IGF-1 cascade",
                    "Main action": "Activates mTOR and keeps FoxO out of nucleus",
                    "Adaptation served": "Anabolism; opposes atrophy signaling",
                },
                "mTOR": {
                    "Activated or triggered by": "Akt, or mechanical pathways independent of IGF-1",
                    "Main action": "Key regulator of muscle protein synthesis",
                    "Adaptation served": "Fiber growth; weaker in sarcopenic muscle",
                },
                "AMPK": {
                    "Activated or triggered by": "Rising AMP and falling glycogen levels",
                    "Main action": "Increases transcription of Pgc1α1",
                    "Adaptation served": "Endurance metabolic adaptation",
                },
                "Pgc1α1": {
                    "Activated or triggered by": "Transcription increased by AMPK",
                    "Main action": "Master regulator of mitochondrial biogenesis",
                    "Adaptation served": "Greater aerobic capacity and fatigue resistance",
                },
                "FoxO": {
                    "Activated or triggered by": "Catabolic signals drive nuclear translocation",
                    "Main action": "Turns on E3 ligases and upregulates autophagy",
                    "Adaptation served": "None; drives muscle atrophy",
                },
            },
        },
        {
            "slug": "training_adaptations",
            "title": "Endurance vs Resistance Adaptations",
            "subtitle": "Match each adaptation to the training mode that drives it and its functional effect",
            "categories": ["Training mode", "Functional effect"],
            "data": {
                "Capillarization": {
                    "Training mode": "Endurance: primary adaptation",
                    "Functional effect": "Enhances O2 and nutrient delivery to fibers",
                },
                "Mitochondrial biogenesis": {
                    "Training mode": "Endurance: driven by AMPK and Pgc1α1",
                    "Functional effect": "More aerobic ATP via oxidative phosphorylation",
                },
                "Sarcomeres added in parallel": {
                    "Training mode": "Resistance: the basis of hypertrophy",
                    "Functional effect": "More contractile units and force output",
                },
                "Satellite cell myonuclear donation": {
                    "Training mode": "Resistance: supports growing fibers",
                    "Functional effect": "Maintains translational capacity of larger fibers",
                },
                "Neurological adaptation": {
                    "Training mode": "Resistance: possible additional contributor",
                    "Functional effect": "Improves muscle recruitment and activation",
                },
                "Hyperplasia": {
                    "Training mode": "Either mode: disputed, minimal involvement",
                    "Functional effect": "Would increase myofiber number",
                },
            },
        },
        {
            "slug": "muscle_wasting_conditions",
            "title": "Conditions of Muscle Wasting",
            "subtitle": "Match each condition to its setting, its main mechanism, and a key clinical point",
            "categories": ["Setting", "Main mechanism", "Clinical point"],
            "data": {
                "Cachexia": {
                    "Setting": "Cancer and other pathological states",
                    "Main mechanism": "Proteasome, autophagy, and IL-1, IL-6, TNF-α",
                    "Clinical point": "Added calories or protein alone cannot reverse it",
                },
                "Age-related sarcopenia": {
                    "Setting": "Older adults; contributes to frailty",
                    "Main mechanism": "Anabolic resistance with weaker mTOR activation",
                    "Clinical point": "Blunted regeneration with fat and connective tissue",
                },
                "Disuse atrophy": {
                    "Setting": "Bed rest, casting, immobilization, spaceflight",
                    "Main mechanism": "Suppressed muscle protein synthesis",
                    "Clinical point": "Reversed by remobilization and resistance exercise",
                },
                "Denervation atrophy": {
                    "Setting": "Motor neuropathies and motor neuron diseases",
                    "Main mechanism": "Lost contractile signals; satellite activation falls",
                    "Clinical point": "Stretching or splints prevent contracture",
                },
                "Duchenne muscular dystrophy": {
                    "Setting": "Loss of dystrophin protein",
                    "Main mechanism": "Fragile sarcolemma; satellite cells become exhausted",
                    "Clinical point": "Fibrofatty deposition causes pseudohypertrophy",
                },
            },
        },
    ],
}
