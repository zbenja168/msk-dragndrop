BRICK = {
    "brick_num": 9,
    "brick_title": "Mechanics of Muscle Force Production",
    "games": [
        {
            "slug": "length_tension",
            "title": "Length-Tension Relationship",
            "subtitle": "Match each sarcomere state or tension component to its filament picture and resulting force",
            "categories": ["What happens structurally", "Resulting tension"],
            "data": {
                "Sarcomere too short": {
                    "What happens structurally": "Actin filaments overlap one another and block myosin sites",
                    "Resulting tension": "Reduced active tension from blocked cross bridges"
                },
                "Sarcomere at optimal length": {
                    "What happens structurally": "Actin-myosin overlap allows the most cross bridges",
                    "Resulting tension": "Maximal active tension for force production"
                },
                "Sarcomere overstretched": {
                    "What happens structurally": "Little actin-myosin overlap, so fewer cross bridges",
                    "Resulting tension": "Reduced active tension from too little overlap"
                },
                "Passive tension": {
                    "What happens structurally": "Titin and connective tissue resist stretch elastically",
                    "Resulting tension": "Rises non-linearly with stretch, opposing further stretch"
                },
                "Total tension": {
                    "What happens structurally": "Cross-bridge force summed with elastic stretch force",
                    "Resulting tension": "Active plus passive; passive dominates at extreme lengths"
                }
            }
        },
        {
            "slug": "isotonic_twitch_phases",
            "title": "Phases of an Isotonic Contraction",
            "subtitle": "Match each phase of a single lifting twitch to its length and force behavior",
            "categories": ["Muscle length", "Force"],
            "data": {
                "Phase 1: isometric contraction": {
                    "Muscle length": "Unchanged while force builds",
                    "Force": "Rising until it matches the weight"
                },
                "Phase 2: isotonic shortening": {
                    "Muscle length": "Shortens as the load is lifted",
                    "Force": "Constant, equal to the load"
                },
                "Phase 3: isotonic relaxation": {
                    "Muscle length": "Lengthens as the load re-extends it",
                    "Force": "Constant while still supporting the weight"
                },
                "Phase 4: isometric relaxation": {
                    "Muscle length": "Back at original length, no change",
                    "Force": "Falling once the load is set down"
                },
                "Load above maximal force": {
                    "Muscle length": "Never shortens at any point",
                    "Force": "Entire contraction isometric; velocity zero"
                }
            }
        },
        {
            "slug": "proprioceptors_motor_neurons",
            "title": "Spindles, Tendon Organs, and Motor Neurons",
            "subtitle": "Match each receptor or motor neuron to its location, fiber type, and role",
            "categories": ["Location or target", "Fiber type", "Role"],
            "data": {
                "Muscle spindle": {
                    "Location or target": "Parallel to extrafusal fibers, built of intrafusal fibers",
                    "Fiber type": "Group Ia (primary) and group II (secondary) afferents",
                    "Role": "Senses length and rate of stretch; excites alpha motor neurons"
                },
                "Golgi tendon organ": {
                    "Location or target": "Within the tendon, in series with muscle fibers",
                    "Fiber type": "Group Ib afferents",
                    "Role": "Senses tension; inhibits agonist, excites antagonist"
                },
                "Alpha motor neuron": {
                    "Location or target": "Innervates extrafusal muscle fibers",
                    "Fiber type": "Cholinergic efferent forming motor units",
                    "Role": "Drives force-producing contraction of the muscle"
                },
                "Gamma motor neuron": {
                    "Location or target": "Innervates contractile regions of intrafusal fibers",
                    "Fiber type": "Cholinergic efferent to the spindle",
                    "Role": "Keeps spindle taut and sensitive as muscle shortens"
                }
            }
        },
        {
            "slug": "nmj_drugs_toxins",
            "title": "Drugs and Toxins at the NMJ",
            "subtitle": "Match each agent or defect to its molecular target, mechanism, and muscle effect",
            "categories": ["Molecular target", "Mechanism", "Muscle effect"],
            "data": {
                "Hemicholinium": {
                    "Molecular target": "Choline uptake into the presynaptic terminal",
                    "Mechanism": "Blocks choline recycling, depleting neuronal ACh",
                    "Muscle effect": "Presynaptic transmission failure as ACh runs out"
                },
                "Botulinum toxin": {
                    "Molecular target": "SNARE vesicle-fusion proteins",
                    "Mechanism": "Prevents vesicular ACh release",
                    "Muscle effect": "Flaccid paralysis of exposed muscle"
                },
                "Curare derivatives": {
                    "Molecular target": "ACh binding sites on nicotinic receptors",
                    "Mechanism": "Block ACh binding, reducing the end-plate potential",
                    "Muscle effect": "Flaccid paralysis from postsynaptic blockade"
                },
                "Acetylcholinesterase inhibitors": {
                    "Molecular target": "Acetylcholinesterase in the synaptic cleft",
                    "Mechanism": "Prevent ACh hydrolysis so ACh accumulates",
                    "Muscle effect": "Fasciculations; therapeutic doses aid myasthenia gravis"
                },
                "Failed presynaptic Ca2+ entry": {
                    "Molecular target": "Voltage-gated Ca2+ channels of the axon terminal",
                    "Mechanism": "No Ca2+ influx, so vesicles do not fuse",
                    "Muscle effect": "No ACh release despite a normal nerve impulse"
                }
            }
        }
    ]
}
