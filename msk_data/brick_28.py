BRICK = {
    "brick_num": 28,
    "brick_title": "MSK: Bone Tumors",
    "games": [
        {
            "slug": "benign_bone_tumors",
            "title": "Benign Primary Bone Tumors",
            "subtitle": "Match each benign bone tumor to its typical patient, location and treatment",
            "categories": ["Typical patient", "Typical location", "Treatment"],
            "data": {
                "Osteochondroma": {
                    "Typical patient": "Teenage boys or young men; painless mass",
                    "Typical location": "Metaphyseal surface exostosis near knee or shoulder",
                    "Treatment": "Monitor; remove if it enlarges or becomes painful",
                },
                "Osteoid osteoma": {
                    "Typical patient": "Teens and twenties; night pain relieved by NSAIDs",
                    "Typical location": "Shaft of long bones, especially the femur",
                    "Treatment": "NSAIDs; radiofrequency ablation if needed",
                },
                "Osteoblastoma": {
                    "Typical patient": "Teens and twenties, similar to osteoid osteoma",
                    "Typical location": "Posterior elements of the vertebrae; over 2 cm",
                    "Treatment": "Curettage or en bloc excision",
                },
                "Enchondroma": {
                    "Typical patient": "Ages 20-50; often incidental, may fracture",
                    "Typical location": "Medullary cavity of hand and foot tubular bones",
                    "Treatment": "Observe if small; curettage and grafting if symptomatic",
                },
                "Giant cell tumor of bone": {
                    "Typical patient": "3rd-5th decades; pain, swelling, limited joint motion",
                    "Typical location": "Epiphysis extending into metaphysis, around the knee",
                    "Treatment": "Curettage (40-60% recur); denosumab if resection morbid",
                },
                "Chondroblastoma": {
                    "Typical patient": "Teenagers with open growth plates; joint pain",
                    "Typical location": "Epiphysis of proximal humerus, distal femur, proximal tibia",
                    "Treatment": "Curettage and bone grafting",
                },
            },
        },
        {
            "slug": "malignant_bone_lesions",
            "title": "Malignant Bone Tumors: Primary and Metastatic",
            "subtitle": "Match each malignant tumor to its typical patient, sites, treatment and outlook",
            "categories": ["Typical patient", "Favored sites", "Treatment", "Outlook"],
            "data": {
                "Metastatic bone cancer": {
                    "Typical patient": "Adult with a known primary (prostate, breast, lung...)",
                    "Favored sites": "Vertebral column, sacrum, pelvis, proximal femurs",
                    "Treatment": "Chemotherapy; radiation to spine or hip to prevent fracture",
                    "Outlook": "Poor prognostic finding for any cancer",
                },
                "Osteosarcoma": {
                    "Typical patient": "Teens, with a second peak over age 60",
                    "Favored sites": "Femur, tibia and humerus",
                    "Treatment": "Neoadjuvant MAP, surgery, adjuvant chemotherapy",
                    "Outlook": "About 70% 5-year survival; 20% with metastases",
                },
                "Ewing sarcoma": {
                    "Typical patient": "Boys under 15 with fever and weight loss",
                    "Favored sites": "Diaphysis of femur; flat bones of the pelvis",
                    "Treatment": "Neoadjuvant VDC/IE, excision, adjuvant chemo +/- radiation",
                    "Outlook": "About 75% 5-year survival; chemo necrosis is favorable",
                },
                "Chondrosarcoma": {
                    "Typical patient": "Older adults with progressive pain and a mass",
                    "Favored sites": "Pelvis, proximal femur, shoulder girdle",
                    "Treatment": "Surgical excision; resistant to chemo and radiation",
                    "Outlook": "About 50% 5-year survival, varies with grade",
                },
            },
        },
        {
            "slug": "imaging_and_histology",
            "title": "Bone Tumor Imaging and Histology",
            "subtitle": "Match each tumor to its classic x-ray sign and microscopic hallmark",
            "categories": ["Classic imaging", "Histology hallmark"],
            "data": {
                "Osteosarcoma": {
                    "Classic imaging": "Sunburst pattern with Codman triangle",
                    "Histology hallmark": "Anaplastic cells producing malignant osteoid",
                },
                "Ewing sarcoma": {
                    "Classic imaging": "Layered onion-skin periosteal reaction",
                    "Histology hallmark": "Small blue malignant cells with hemorrhage",
                },
                "Giant cell tumor of bone": {
                    "Classic imaging": "Lytic, expansile soap-bubble lesion with cortical destruction",
                    "Histology hallmark": "Oval mononuclear cells with 100-nucleus giant cells",
                },
                "Chondroblastoma": {
                    "Classic imaging": "Epiphyseal lesion that can cross the growth plate",
                    "Histology hallmark": "Polyhedral chondroblasts with chicken-wire calcification",
                },
                "Osteoid osteoma": {
                    "Classic imaging": "Well-demarcated lesion under 2 cm with radiolucent core",
                    "Histology hallmark": "Woven bone trabeculae rimmed by osteoblasts",
                },
                "Langerhans cell histiocytosis": {
                    "Classic imaging": "Multiple well-defined lytic skull lesions",
                    "Histology hallmark": "Grooved-nucleus cells with eosinophils; Birbeck granules",
                },
            },
        },
        {
            "slug": "molecular_drivers",
            "title": "Molecular Drivers in Bone Lesions",
            "subtitle": "Match each molecular change to the lesion it drives and what it means",
            "categories": ["Associated lesion", "Key point"],
            "data": {
                "Germline EXT1 or EXT2 mutation": {
                    "Associated lesion": "Multiple hereditary exostosis (osteochondromas)",
                    "Key point": "Autosomal dominant; accounts for ~15% of osteochondromas",
                },
                "Somatic IDH1 or IDH2 mutation": {
                    "Associated lesion": "Enchondromas; Ollier disease and Maffucci syndrome",
                    "Key point": "Maffucci adds hemangiomas of the skin",
                },
                "RANKL overexpression by stromal cells": {
                    "Associated lesion": "Giant cell tumor of bone",
                    "Key point": "Recruits osteoclast-like giant cells; targeted by denosumab",
                },
                "t(11;22) EWSR1-FLI1 translocation": {
                    "Associated lesion": "Ewing sarcoma",
                    "Key point": "Fusion of nonhomologous chromosomes yields abnormal protein",
                },
                "BRAF V600E mutation": {
                    "Associated lesion": "Langerhans cell histiocytosis",
                    "Key point": "Present in 40-60% of cases; cells are S-100 and CD1a positive",
                },
                "Tumor-secreted PTHrP and TGF-beta": {
                    "Associated lesion": "Osteolytic metastases (lung, breast, thyroid, kidney, myeloma)",
                    "Key point": "Activate osteoclasts; weakened bone and pathologic fracture",
                },
            },
        },
    ],
}
