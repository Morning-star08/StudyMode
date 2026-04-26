from datetime import date, timedelta


JOURNEY_TOTAL_DAYS = 180
JOURNEY_START_DATE = date(2026, 4, 27)
JOURNEY_END_DATE = JOURNEY_START_DATE + timedelta(days=JOURNEY_TOTAL_DAYS - 1)
SUBJECT_SEQUENCE = [
    "MATHEMATICS",
    "PHYSICS",
    "CHEMISTRY",
    "MATHEMATICS",
    "PHYSICS",
    "CHEMISTRY",
    "ENGLISH",
]


def block(topic, days, subtopics, resource_url, self_test_question, formula_focus, track="content"):
    return {
        "topic": topic,
        "days": days,
        "subtopics": list(subtopics),
        "resource_url": resource_url,
        "self_test_question": self_test_question,
        "formula_focus": formula_focus,
        "track": track,
    }


SUBJECT_BLOCKS = {
    "MATHEMATICS": [
        block(
            "Set, Logic and Functions",
            5,
            [
                "Set notation, real numbers, intervals, and absolute value basics",
                "Logic statements, connectives, truth values, and laws of logic",
                "Functions as mappings, domain/range, and function notation",
                "Injective, surjective, bijective functions with simple graphs",
                "Algebraic, trigonometric, exponential, logarithmic, inverse, and composite functions",
            ],
            "https://www.khanacademy.org/math/algebra-home/alg-functions",
            "How do domain, range, and one-one / onto behavior decide whether an inverse exists?",
            "Interval notation, absolute value rules, logic laws, inverse/composite function rules",
        ),
        block(
            "Algebra",
            7,
            [
                "Matrices: types, addition, multiplication, transpose, and identity matrix",
                "Determinants, minors, cofactors, inverse of a matrix, and matrix equations",
                "Complex numbers: Argand plane, modulus, argument, and operations",
                "Polynomial equations, relation between roots and coefficients, quadratic/cubic patterns",
                "Sequences and series: AP, GP, harmonic ideas, and sigma notation",
                "Permutation and combination with counting strategy and restrictions",
                "Binomial theorem with general term plus exponential and logarithmic series overview",
            ],
            "https://www.khanacademy.org/math/precalculus",
            "When should you model a problem with a matrix, a complex-number identity, or a counting formula?",
            "Determinant formulas, complex identities, AP/GP sums, nPr/nCr, binomial general term",
        ),
        block(
            "Trigonometry",
            4,
            [
                "Trigonometric identities, equations, standard angles, and general values",
                "Inverse trigonometric functions, principal values, and restricted domains",
                "Properties of triangles: sine law, cosine law, projection, and area rules",
                "Special triangle centres, solution of triangles, and mixed MCQ application",
            ],
            "https://www.khanacademy.org/math/trigonometry",
            "Which trig identity or triangle law unlocks the problem fastest, and why?",
            "Standard values, principal-value ranges, sine/cosine laws, triangle area formulas",
        ),
        block(
            "Coordinate Geometry",
            5,
            [
                "Straight line forms, slope, intercepts, and angle between lines",
                "Pair of lines and combined second-degree line equations",
                "Circle equations, centre-radius form, and family of circles",
                "Tangent, normal, and conic sections: parabola, ellipse, hyperbola",
                "3D coordinates, direction ratios, and plane equation basics",
            ],
            "https://www.khanacademy.org/math/geometry-home",
            "How do you identify the geometric object directly from its equation before solving?",
            "Line forms, circle condition, tangent-normal formulas, standard conic equations, plane equation",
        ),
        block(
            "Calculus",
            9,
            [
                "Limits, continuity, one-sided thinking, and graphical intuition",
                "Indeterminate forms and L'Hospital's rule",
                "Derivative definition, standard derivatives, and chain/product/quotient rules",
                "Higher-order derivatives and geometric meaning of derivative",
                "Tangent, normal, and rate-of-change questions",
                "Maxima and minima strategy with sign tests and critical points",
                "Integration as inverse process and standard integral forms",
                "Definite integration, area under a curve, and area between curves",
                "Differential equations: variable separable, homogeneous, linear, exact, integrating factor",
            ],
            "https://www.khanacademy.org/math/calculus-1",
            "How do you choose between differentiation, integration, or a differential-equation method for a word problem?",
            "Limit laws, derivative rules, tangent-normal forms, maxima/minima steps, standard integrals, DE forms",
        ),
        block(
            "Vectors",
            2,
            [
                "Vectors in plane and space, algebra, linear combination, dependence, and independence",
                "Scalar product, vector product, scalar triple product, and geometry meaning",
            ],
            "https://www.khanacademy.org/math/linear-algebra/vectors-and-spaces",
            "What does each vector product tell you geometrically, and when is each one useful?",
            "Vector addition, direction cosines, dot/cross/triple product formulas",
        ),
        block(
            "Statistics and Probability",
            3,
            [
                "Measures of location and dispersion with data interpretation",
                "Correlation and regression with trend meaning",
                "Conditional probability, compound events, Bayes theorem, and binomial distribution",
            ],
            "https://www.khanacademy.org/math/statistics-probability",
            "How do you decide whether a probability question is conditional, Bayes, or binomial?",
            "Mean/variance formulas, regression idea, conditional probability, Bayes rule, binomial formula",
        ),
        block(
            "Math Practice - Algebra and Trig Speed Drill",
            2,
            [
                "Timed mixed MCQs from set, functions, algebra, and trigonometry",
                "Error review and shortcut building for repeated traps",
            ],
            "https://www.youtube.com/results?search_query=IOE+entrance+math+mcq+algebra+trigonometry",
            "Which mistake pattern still repeats even when you know the formula?",
            "Top formulas from sets, algebra, and trig",
            "practice",
        ),
        block(
            "Math Practice - Coordinate Geometry",
            1,
            ["Timed MCQs on lines, circles, conics, and 3D coordinates"],
            "https://www.youtube.com/results?search_query=IOE+entrance+coordinate+geometry+mcq",
            "Can you classify the geometry type within 10 seconds before calculating?",
            "Line, circle, and conic quick checks",
            "practice",
        ),
        block(
            "Math Practice - Calculus",
            2,
            [
                "Timed MCQs on limits, derivatives, tangent-normal, and maxima-minima",
                "Timed MCQs on integration, area, and differential equations",
            ],
            "https://www.youtube.com/results?search_query=IOE+entrance+calculus+mcq",
            "Which calculus chapter gives the slowest solve time, and what shortcut fixes it?",
            "Derivative and integral standard results",
            "practice",
        ),
        block(
            "Math Practice - Vectors and Probability",
            1,
            ["Mixed timed drill on vectors, statistics, and probability"],
            "https://www.youtube.com/results?search_query=IOE+entrance+vectors+probability+mcq",
            "Can you translate the question into the correct formula family instantly?",
            "Dot/cross product and probability formulas",
            "practice",
        ),
        block(
            "Math Practice - Half Mock",
            2,
            [
                "50-minute mixed math paper under timed conditions",
                "Review every wrong answer and rebuild the formula sheet",
            ],
            "https://www.youtube.com/results?search_query=IOE+entrance+math+mock+test",
            "Which chapter is still below 70 percent accuracy after timed work?",
            "Full math formula sheet",
            "practice",
        ),
        block(
            "Math Revision - Sets and Functions Repair",
            1,
            ["Repair weak notes on sets, logic, and functions; redo 10 marked mistakes"],
            "https://www.khanacademy.org/math/algebra-home/alg-functions",
            "Can you explain domain, range, and inverse conditions without notes?",
            "Sets and function rules",
            "revision",
        ),
        block(
            "Math Revision - Algebra Repair",
            1,
            ["Redo weak algebra questions from matrix, complex, sequence, and binomial chapters"],
            "https://www.khanacademy.org/math/precalculus",
            "Which algebra identity do you still forget under pressure?",
            "Matrix, complex, AP/GP, permutation/combination, binomial formulas",
            "revision",
        ),
        block(
            "Math Revision - Trigonometry Repair",
            1,
            ["Redo trigonometric equation and triangle-centre mistakes"],
            "https://www.khanacademy.org/math/trigonometry",
            "Can you pick the right trig identity in one glance?",
            "Trig identities and triangle laws",
            "revision",
        ),
        block(
            "Math Revision - Coordinate Geometry Repair",
            1,
            ["Redo line, circle, and conic mistakes with one-page summary writing"],
            "https://www.khanacademy.org/math/geometry-home",
            "Which equation form lets you read the graph fastest?",
            "Line, circle, conic, and plane formulas",
            "revision",
        ),
        block(
            "Math Revision - Calculus Repair",
            2,
            [
                "Weak-topic repair on limits, derivatives, and maxima-minima",
                "Weak-topic repair on integration, area, and differential equations",
            ],
            "https://www.khanacademy.org/math/calculus-1",
            "Which calculus question type still breaks your time control?",
            "Limit, derivative, integration, and DE formulas",
            "revision",
        ),
        block(
            "Math Revision - Formula Sheet Sprint",
            1,
            ["Write the entire math formula sheet from memory and patch every blank"],
            "https://www.youtube.com/results?search_query=IOE+math+formula+sheet",
            "Can you rebuild the math formula sheet from memory in one sitting?",
            "Full math formula sheet",
            "revision",
        ),
        block(
            "Math Revision - Full Mock",
            1,
            ["Full 50-mark timed math mock with strict marking"],
            "https://www.youtube.com/results?search_query=IOE+entrance+math+full+mock",
            "Did your speed and accuracy reach mock-ready level on the highest-weight subject?",
            "Full math formula sheet",
            "revision",
        ),
        block(
            "Math Revision - Final Error Log",
            1,
            ["Final pass through the error log, guessed questions, and last weak formulas"],
            "https://www.youtube.com/results?search_query=IOE+entrance+math+mistake+analysis",
            "Which 5 math traps must you actively avoid on exam day?",
            "Personal error log and top formulas",
            "revision",
        ),
    ],
    "PHYSICS": [
        block(
            "Physical Quantities, Vectors and Kinematics",
            3,
            [
                "Units, dimensions, physical quantities, vector basics, and resolution of vectors",
                "1D and 2D kinematics, equations of motion, graphs, and relative motion",
                "Projectile motion, vector combination, and kinematics MCQ building",
            ],
            "https://www.khanacademy.org/science/physics/one-dimensional-motion",
            "How do dimensions, vectors, and motion graphs help you choose the right kinematics equation?",
            "Dimensions, vector resolution, equations of motion, projectile range/time formulas",
        ),
        block(
            "Newton's Laws, Friction and Momentum",
            2,
            [
                "Newton's laws, free-body diagrams, friction, and equilibrium thinking",
                "Conservation of momentum, impulse, and force-system MCQ practice",
            ],
            "https://www.khanacademy.org/science/physics/forces-newtons-laws",
            "Can you draw the force picture before solving the equation?",
            "Newton's laws, friction formula, momentum and impulse relations",
        ),
        block(
            "Work, Energy, Power and Collisions",
            2,
            [
                "Work-energy theorem, power, conservation of energy, and conservative forces",
                "Elastic and inelastic collisions with energy and momentum comparison",
            ],
            "https://www.khanacademy.org/science/physics/work-and-energy",
            "When is energy conservation enough, and when must momentum be used too?",
            "Work-energy theorem, power, collision relations",
        ),
        block(
            "Circular Motion, Gravitation and SHM",
            3,
            [
                "Circular motion, centripetal force, banking, and gravitation basics",
                "Satellite motion, escape velocity, pendulum, and resonance ideas",
                "Simple harmonic motion equations and mixed mechanics connections",
            ],
            "https://www.khanacademy.org/science/physics/circular-motion-and-gravitation",
            "What is providing the centripetal force in each motion problem?",
            "Centripetal force, gravitation, satellite formulas, SHM period relations",
        ),
        block(
            "Rotational Dynamics",
            2,
            [
                "Moment of inertia, radius of gyration, torque, and rotational equilibrium",
                "Angular momentum, rolling ideas, and rotational MCQ application",
            ],
            "https://www.youtube.com/results?search_query=rotational+dynamics+ioe+entrance+physics",
            "Which quantity controls rotation here: torque, MOI, or angular momentum?",
            "Torque, angular momentum, rotational kinetic energy, standard MOI values",
        ),
        block(
            "Elasticity and Fluid Mechanics",
            3,
            [
                "Hooke's law, Young/Bulk/Rigidity modulus, Poisson's ratio, and elastic energy",
                "Archimedes principle, pressure, viscosity, surface tension, and Reynolds number",
                "Bernoulli equation and fluid-flow MCQ practice",
            ],
            "https://www.khanacademy.org/science/physics/fluids",
            "What conservation law or material law is controlling the fluid or elasticity question?",
            "Modulus formulas, buoyancy, continuity, Bernoulli relation",
        ),
        block(
            "Heat and Thermodynamics",
            4,
            [
                "Specific heat, latent heat, Newton's law of cooling, and triple point",
                "Thermal expansion of solids and liquids, conduction, convection, and radiation",
                "Kinetic theory of gases, heat capacities, and gas-process reasoning",
                "Laws of thermodynamics, Carnot/Otto/Diesel cycles, and entropy basics",
            ],
            "https://www.khanacademy.org/science/physics/thermodynamics",
            "Which heat or thermodynamics formula fits the process described in the question?",
            "Heat equations, expansion formulas, Stefan-Boltzmann, gas relations, thermodynamic efficiencies",
        ),
        block(
            "Optics",
            4,
            [
                "Reflection, mirror formula, refraction, TIR, prism, and lens formula",
                "Lens maker formula, optical fibre, dispersion, chromatic aberration, and scattering",
                "Huygen's principle, velocity of light, and Young's double slit",
                "Diffraction, resolving power, polarization, Brewster's law, and Polaroid",
            ],
            "https://www.khanacademy.org/science/physics/geometric-optics",
            "Is the question testing image formation, wave behavior, or light-material interaction?",
            "Mirror/lens formulas, prism relations, YDSE, grating, Brewster law",
        ),
        block(
            "Waves and Sound",
            3,
            [
                "Travelling and stationary waves, wave equation, and phase ideas",
                "Sound in solids/liquids/gases, pipes, strings, resonance tube, and laws of vibration",
                "Doppler effect, ultrasonic/infrasonic waves, and intensity level",
            ],
            "https://www.khanacademy.org/science/physics/mechanical-waves-and-sound",
            "What changes frequency, what changes speed, and what changes wavelength in this wave setup?",
            "Wave equation, pipe/string frequencies, Doppler formula, intensity level",
        ),
        block(
            "Electrostatics, DC Circuits and Thermoelectricity",
            3,
            [
                "Coulomb's law, electric field, potential, Gauss law, capacitors, and dielectrics",
                "Ohm's law, Kirchhoff's law, Joule heating, and internal resistance",
                "Seebeck, Peltier, Thomson effects, and circuit-style application",
            ],
            "https://www.khanacademy.org/science/physics/circuits-topic",
            "Is this an electric-field idea, a circuit loop idea, or a thermoelectric-effect idea?",
            "Electrostatic field/potential, capacitance, Kirchhoff rules, Joule law, thermoelectric effects",
        ),
        block(
            "Magnetism, EM Induction and AC",
            3,
            [
                "Biot-Savart, Ampere law, Hall effect, magnetic torque, and magnetic properties",
                "Earth magnetism, hysteresis, permeability, Faraday law, self/mutual induction, and transformer",
                "Alternating current, RMS, phasor diagrams, quality factor, and power factor",
            ],
            "https://www.khanacademy.org/science/physics/magnetic-forces-and-magnetic-fields",
            "Which magnetic law directly connects the geometry in the question to the answer?",
            "Magnetic field formulas, Faraday law, transformer ratio, RMS and power factor",
        ),
        block(
            "Modern Physics",
            2,
            [
                "Electron discoveries, photoelectric effect, Bohr theory, De Broglie, X-rays, lasers, and semiconductors",
                "Radioactivity, fission/fusion, decay law, logic gates, recent trends, universe, telecom, nano-tech",
            ],
            "https://www.khanacademy.org/science/physics/quantum-physics",
            "Which modern-physics model explains the phenomenon fastest: particle, wave, atom, or nucleus?",
            "Photoelectric equation, Bohr radius/energy, decay law, semiconductor and logic-gate basics",
        ),
        block(
            "Physics Practice - Mechanics Drill",
            2,
            [
                "Timed mixed mechanics MCQs from vectors to fluids",
                "Mechanics error analysis and speed shortcuts",
            ],
            "https://www.youtube.com/results?search_query=IOE+physics+mechanics+mcq",
            "Which mechanics chapter is still causing most wrong answers under time pressure?",
            "Mechanics master formula list",
            "practice",
        ),
        block(
            "Physics Practice - Thermal and Optics Drill",
            2,
            [
                "Timed MCQs on heat, thermodynamics, and thermal properties",
                "Timed MCQs on mirrors, lenses, interference, diffraction, and polarization",
            ],
            "https://www.youtube.com/results?search_query=IOE+physics+optics+thermodynamics+mcq",
            "Do you lose marks more from concepts or from formula setup in thermal/optics questions?",
            "Thermal and optics formulas",
            "practice",
        ),
        block(
            "Physics Practice - Waves and Electricity Drill",
            2,
            [
                "Timed MCQs on waves, sound, and Doppler effect",
                "Timed MCQs on electrostatics, circuits, magnetism, EMI, and AC",
            ],
            "https://www.youtube.com/results?search_query=IOE+physics+electricity+magnetism+mcq",
            "Which electricity chapter still feels slow: circuits, electrostatics, or AC?",
            "Waves and electricity formulas",
            "practice",
        ),
        block(
            "Physics Practice - Modern Mixed",
            1,
            ["Mixed modern-physics timed set with decay, semiconductor, and atom questions"],
            "https://www.youtube.com/results?search_query=IOE+modern+physics+mcq+nepal",
            "Can you identify the correct modern-physics model in under 10 seconds?",
            "Modern physics formulas",
            "practice",
        ),
        block(
            "Physics Practice - Full Mixed Set",
            2,
            [
                "40-mark style mixed physics set under timed conditions",
                "Paper review with an error log and chapter ranking",
            ],
            "https://www.youtube.com/results?search_query=IOE+physics+full+paper+solution",
            "Did your timing hold across mechanics, optics, and electricity in one sitting?",
            "Physics master formula sheet",
            "practice",
        ),
        block(
            "Physics Revision - Mechanics Repair",
            2,
            [
                "Redo marked weak questions from vectors, Newton, work-energy, and circular motion",
                "Redo weak questions from rotation, elasticity, and fluids",
            ],
            "https://www.youtube.com/results?search_query=IOE+physics+mechanics+revision",
            "Which mechanics chapter still creates panic or second-guessing?",
            "Mechanics master formula list",
            "revision",
        ),
        block(
            "Physics Revision - Thermal and Optics Repair",
            2,
            [
                "Repair heat, thermodynamics, and gas-theory weak spots",
                "Repair optics weak spots and redraw ray/wave diagrams from memory",
            ],
            "https://www.youtube.com/results?search_query=IOE+physics+optics+revision",
            "Can you sketch the setup before solving the optics question?",
            "Thermal and optics formulas",
            "revision",
        ),
        block(
            "Physics Revision - Electricity Repair",
            2,
            [
                "Redo electrostatics and circuit weak questions",
                "Redo magnetism, induction, and AC weak questions",
            ],
            "https://www.youtube.com/results?search_query=IOE+physics+electricity+revision",
            "Which electricity chapter still drops accuracy below target?",
            "Electricity and magnetism formulas",
            "revision",
        ),
        block(
            "Physics Revision - Formula Sheet Sprint",
            1,
            ["Write the full physics formula sheet by hand from memory"],
            "https://www.youtube.com/results?search_query=IOE+physics+formula+sheet",
            "Can you recall the main physics formulas without opening your notes?",
            "Physics master formula sheet",
            "revision",
        ),
        block(
            "Physics Revision - Full Mock",
            1,
            ["Timed 40-mark style physics mock and strict review"],
            "https://www.youtube.com/results?search_query=IOE+physics+mock+test+nepal",
            "Did your physics score cross the target under real timing?",
            "Physics master formula sheet",
            "revision",
        ),
        block(
            "Physics Revision - Final Error Log",
            1,
            ["Final pass through guessed questions, units traps, and weak formulas"],
            "https://www.youtube.com/results?search_query=IOE+physics+mistake+analysis",
            "Which 5 physics mistakes must never repeat on exam day?",
            "Personal physics error log",
            "revision",
        ),
    ],
    "CHEMISTRY": [
        block(
            "Chemical Arithmetic",
            2,
            [
                "Mole concept, Avogadro hypothesis, stoichiometry, and equivalent mass",
                "Stoichiometric problem solving and chemical arithmetic MCQ practice",
            ],
            "https://www.khanacademy.org/science/chemistry/chemical-reactions-stoichiome",
            "Which quantity conversion breaks the problem open first: mole, mass, gas volume, or equivalent?",
            "Mole formulas, equivalent mass, stoichiometry ratios",
        ),
        block(
            "States of Matter",
            2,
            [
                "Gaseous state, gas laws, kinetic picture, and real-gas intuition",
                "Liquid and solid states, intermolecular forces, and state-change reasoning",
            ],
            "https://www.khanacademy.org/science/chemistry/states-of-matter-and-intermolecular-forces",
            "Which state-property relation explains the observation in the question?",
            "Gas laws, density and state-change relations",
        ),
        block(
            "Atomic Structure and Periodic Classification",
            3,
            [
                "Atomic models, quantum numbers, electronic configuration",
                "Periodic trends: size, ionization energy, electron affinity, electronegativity",
                "Periodic classification mixed MCQs and trend prediction",
            ],
            "https://www.khanacademy.org/science/chemistry/electronic-structure-of-atoms",
            "Which periodic trend should rise or fall here, and why?",
            "Quantum numbers, configuration order, periodic trend rules",
        ),
        block(
            "Oxidation, Reduction and Equilibrium",
            3,
            [
                "Oxidation number, balancing redox reactions, and oxidising/reducing agents",
                "Chemical equilibrium, Le Chatelier principle, and equilibrium constant",
                "Redox and equilibrium application MCQs",
            ],
            "https://www.khanacademy.org/science/chemistry/chemical-equilibrium",
            "What shifts the equilibrium, and how do oxidation numbers reveal the reaction change?",
            "Redox rules, equilibrium constant ideas",
        ),
        block(
            "Volumetric Analysis, Ionic Equilibrium, Acid, Base and Salt",
            3,
            [
                "Volumetric analysis, titration logic, normality, molarity, and equivalent concept",
                "Ionic equilibrium, pH, weak acid/base ideas, and common-ion effect",
                "Buffer idea, salt hydrolysis, and acid-base MCQ practice",
            ],
            "https://www.khanacademy.org/science/chemistry/acid-base-equilibrium",
            "Is this a titration problem, a pH problem, or a salt-hydrolysis problem?",
            "Molarity-normality, pH, ionic-equilibrium relations",
        ),
        block(
            "Electrochemistry",
            2,
            [
                "Electrolysis, galvanic cells, cell notation, and Faraday law",
                "Electrode potential, spontaneous direction, and electrochemistry MCQs",
            ],
            "https://www.khanacademy.org/science/chemistry/oxidation-reduction",
            "How do you decide the anode, cathode, and direction before calculating anything?",
            "Faraday laws, cell potential basics",
        ),
        block(
            "Energetics, Kinetics, Bonding and Molecular Shape",
            3,
            [
                "Enthalpy, reaction energetics, Hess-style thinking, and activation energy",
                "Reaction rate, collision idea, and factors affecting kinetics",
                "Chemical bonding, hybridisation, VSEPR, and molecular shape",
            ],
            "https://www.khanacademy.org/science/chemistry/chemical-bonds",
            "Is the question asking about energy change, rate change, or molecular structure?",
            "Enthalpy, rate factors, bond types, VSEPR shape rules",
        ),
        block(
            "Non-metals",
            4,
            [
                "Hydrogen, oxygen, ozone, water, and environment pollution links",
                "Nitrogen family and important compounds",
                "Halogens, carbon family, phosphorus, and sulphur compounds",
                "Noble gases, environmental chemistry, and non-metal mixed MCQs",
            ],
            "https://www.youtube.com/results?search_query=IOE+chemistry+non+metals",
            "Which family trend or compound property explains the reaction here?",
            "Key compounds and family trends of non-metals",
        ),
        block(
            "Metals and Extraction",
            3,
            [
                "Metallurgical principles, ore concentration, reduction, and refining",
                "Alkali, alkaline earth, and coinage metals with important reactions",
                "Extraction of zinc, mercury, and iron compounds",
            ],
            "https://www.youtube.com/results?search_query=IOE+chemistry+metallurgy+nepal",
            "Which extraction step or metal property is the key clue in the question?",
            "Metallurgy steps, metal reactivity, extraction flow",
        ),
        block(
            "Organic Fundamentals",
            2,
            [
                "Nomenclature, isomerism, electron movement, and organic reaction language",
                "Reaction mechanism basics and functional-group recognition",
            ],
            "https://www.khanacademy.org/science/organic-chemistry",
            "Can you identify the functional group and likely reaction type before solving?",
            "IUPAC basics, isomerism rules, mechanism keywords",
        ),
        block(
            "Hydrocarbons",
            2,
            [
                "Alkanes, alkenes, alkynes, and major reactions",
                "Aromatic hydrocarbons and substitution pattern basics",
            ],
            "https://www.khanacademy.org/science/organic-chemistry/alkanes-cycloalkanes",
            "Which hydrocarbon class is present, and what reaction does it prefer?",
            "Hydrocarbon reaction map",
        ),
        block(
            "Haloalkanes, Haloarenes, Alcohols, Phenols and Ethers",
            2,
            [
                "Haloalkanes and haloarenes with substitution and elimination logic",
                "Alcohols, phenols, ethers, and reaction trend comparison",
            ],
            "https://www.khanacademy.org/science/organic-chemistry/substitution-elimination-reactions",
            "Is the reaction more likely substitution, elimination, or functional-group conversion?",
            "Halo and alcohol/phenol/ether reactions",
        ),
        block(
            "Aldehydes, Ketones, Carboxylic Acids, Nitro Compounds and Amines",
            3,
            [
                "Aldehydes and ketones: identification tests and major reactions",
                "Carboxylic acids and derivatives with acidity and reactivity patterns",
                "Nitro compounds, amines, and final organic mixed MCQs",
            ],
            "https://www.khanacademy.org/science/organic-chemistry/aldehydes-ketones-carboxylic-acids",
            "Which functional-group test or reaction pathway is the fastest clue here?",
            "Carbonyl, acid, nitro, and amine reaction map",
        ),
        block(
            "Chemistry Practice - Physical Chemistry Drill",
            2,
            [
                "Timed MCQs on stoichiometry, states, atomic structure, equilibrium, and acid-base",
                "Redo wrong numerical questions and fix unit mistakes",
            ],
            "https://www.youtube.com/results?search_query=IOE+chemistry+physical+chemistry+mcq",
            "Which physical-chemistry calculation still costs the most time?",
            "Physical chemistry formulas",
            "practice",
        ),
        block(
            "Chemistry Practice - Inorganic Drill",
            2,
            [
                "Timed MCQs on non-metals, metals, and metallurgy",
                "Reaction-trend review and memory repair for compounds",
            ],
            "https://www.youtube.com/results?search_query=IOE+chemistry+inorganic+mcq",
            "Which compound family still feels memorised but not understood?",
            "Important inorganic reactions and trends",
            "practice",
        ),
        block(
            "Chemistry Practice - Organic Drill",
            2,
            [
                "Timed MCQs on nomenclature, hydrocarbons, and functional groups",
                "Reaction-map rebuild for weak organic chapters",
            ],
            "https://www.youtube.com/results?search_query=IOE+organic+chemistry+mcq+nepal",
            "Which functional-group conversion still confuses you under time pressure?",
            "Organic reaction map",
            "practice",
        ),
        block(
            "Chemistry Practice - Equation and Conversion Drill",
            1,
            ["Fast drill on balancing, mole conversion, pH, electrochemistry, and reaction trends"],
            "https://www.youtube.com/results?search_query=IOE+chemistry+numerical+mcq",
            "Are errors coming from chemistry concepts or from algebra/arithmetic slips?",
            "Chemistry quick formulas and reaction cues",
            "practice",
        ),
        block(
            "Chemistry Practice - Full Mixed Set",
            2,
            [
                "30-mark style mixed chemistry paper under timed conditions",
                "Review all missed questions and update the reaction/formula sheet",
            ],
            "https://www.youtube.com/results?search_query=IOE+chemistry+full+paper+mcq",
            "Did your chemistry timing hold across physical, inorganic, and organic questions?",
            "Chemistry master formula and reaction sheet",
            "practice",
        ),
        block(
            "Chemistry Revision - Physical Chemistry Repair",
            2,
            [
                "Repair stoichiometry, equilibrium, acid-base, and electrochemistry weak spots",
                "Redo the hardest physical-chemistry numericals only",
            ],
            "https://www.youtube.com/results?search_query=IOE+physical+chemistry+revision",
            "Which physical-chemistry chapter still feels least automatic?",
            "Physical chemistry formulas",
            "revision",
        ),
        block(
            "Chemistry Revision - Inorganic Repair",
            2,
            [
                "Repair weak inorganic family trends and compounds",
                "Rewrite metallurgy flow and important reactions from memory",
            ],
            "https://www.youtube.com/results?search_query=IOE+inorganic+chemistry+revision",
            "Which compound families still need active recall rather than rereading?",
            "Inorganic reactions and extraction steps",
            "revision",
        ),
        block(
            "Chemistry Revision - Organic Repair",
            2,
            [
                "Redo organic naming, mechanism, and conversion mistakes",
                "Rebuild the organic reaction map in one notebook page",
            ],
            "https://www.youtube.com/results?search_query=IOE+organic+chemistry+revision",
            "Which organic conversion still breaks your confidence?",
            "Organic reaction map",
            "revision",
        ),
        block(
            "Chemistry Revision - Reaction Sheet Sprint",
            1,
            ["Write the reaction chart and formula sheet fully from memory"],
            "https://www.youtube.com/results?search_query=IOE+chemistry+formula+sheet",
            "Can you rebuild the chemistry reaction map without opening notes?",
            "Chemistry master formula and reaction sheet",
            "revision",
        ),
        block(
            "Chemistry Revision - Final Mock Review",
            1,
            ["One final timed chemistry set and strict correction review"],
            "https://www.youtube.com/results?search_query=IOE+chemistry+mock+test+nepal",
            "Did your chemistry score clear the safe target under time pressure?",
            "Chemistry master formula and reaction sheet",
            "revision",
        ),
    ],
    "ENGLISH": [
        block(
            "Grammar I - Tense Sequence and Concord",
            2,
            [
                "Tense sequence, subject-verb agreement, and sentence correction basics",
                "Error spotting and sentence improvement on tense and concord",
            ],
            "https://www.khanacademy.org/humanities/grammar/parts-of-speech-the-verb",
            "Can you explain why the verb form is wrong instead of just guessing the answer?",
            "Tense timeline and concord rules",
        ),
        block(
            "Grammar I - Direct/Indirect and Transformation",
            2,
            [
                "Direct to indirect speech, reporting verbs, and tense back-shift",
                "Sentence transformation patterns and quick recognition rules",
            ],
            "https://www.khanacademy.org/humanities/grammar",
            "What transformation rule is being tested before you change the sentence?",
            "Reporting changes and transformation patterns",
        ),
        block(
            "Grammar II - Conditionals, Voice and Verbals",
            3,
            [
                "Zero to third conditionals and structure cues",
                "Active-passive voice conversion in common tenses",
                "Verbals, gerunds, participles, and mixed grammar MCQs",
            ],
            "https://www.khanacademy.org/humanities/grammar",
            "What grammar clue tells you the sentence structure rule being tested?",
            "Conditional patterns, passive templates, verbals",
        ),
        block(
            "Grammar II - Parts of Speech, Punctuation and Prepositions",
            3,
            [
                "Parts of speech and function words in sentence meaning",
                "Punctuation rules that change sentence clarity",
                "High-frequency prepositions and quick correction patterns",
            ],
            "https://www.khanacademy.org/humanities/grammar/punctuation",
            "Which small grammar signal changes the whole sentence meaning here?",
            "Parts-of-speech cues, punctuation rules, common prepositions",
        ),
        block(
            "Vocabulary and Idioms",
            2,
            [
                "High-yield vocabulary building with root/context method",
                "Common idioms, phrases, and elimination strategy",
            ],
            "https://www.youtube.com/results?search_query=IOE+english+vocabulary+idioms",
            "Can you eliminate wrong options by tone and context even if one word is unfamiliar?",
            "High-yield vocabulary and idiom list",
        ),
        block(
            "Phonetics",
            2,
            [
                "Phonemes, vowels, consonants, and syllable basics",
                "Word stress, sentence stress, and pronunciation-style MCQs",
            ],
            "https://www.youtube.com/results?search_query=IOE+english+phonetics+stress",
            "Where does the stress fall, and how do you spot it quickly from the word pattern?",
            "Phoneme groups and stress rules",
        ),
        block(
            "Comprehension",
            3,
            [
                "General passage reading strategy: main idea, tone, and inference",
                "Technical English passage strategy with data and process language",
                "Timed passage practice and wrong-option elimination",
            ],
            "https://www.youtube.com/results?search_query=IOE+english+reading+comprehension",
            "Can you answer from evidence in the passage instead of memory or intuition?",
            "Reading strategy checklist",
        ),
        block(
            "English Practice - Grammar Mixed",
            1,
            ["Timed mixed grammar drill covering tense, concord, voice, transformation, and prepositions"],
            "https://www.youtube.com/results?search_query=IOE+english+grammar+mcq",
            "Which grammar chapter still creates the most hesitation?",
            "Top 10 grammar rules",
            "practice",
        ),
        block(
            "English Practice - Phonetics and Vocabulary",
            1,
            ["Timed phonetics, stress, vocabulary, and idiom drill"],
            "https://www.youtube.com/results?search_query=IOE+english+phonetics+mcq",
            "Are you missing marks from knowledge gaps or from rushing the wording?",
            "Phonetics and vocabulary quick rules",
            "practice",
        ),
        block(
            "English Practice - Comprehension Timed Set",
            1,
            ["Timed comprehension set with both general and technical passages"],
            "https://www.youtube.com/results?search_query=IOE+english+comprehension+mcq",
            "Did you answer from passage evidence or from a guess?",
            "Comprehension strategy checklist",
            "practice",
        ),
        block(
            "English Practice - Mini Mock",
            1,
            ["20-mark style mixed English mini mock with rapid review"],
            "https://www.youtube.com/results?search_query=IOE+english+mock+test",
            "Did you keep English fast enough to save time for the science subjects?",
            "English fast-score checklist",
            "practice",
        ),
        block(
            "English Revision - Top 10 Grammar Rules",
            1,
            ["Rewrite the top 10 grammar rules and solve one example for each"],
            "https://www.youtube.com/results?search_query=IOE+english+grammar+rules",
            "Can you explain each rule in one line without hesitation?",
            "Top 10 grammar rules",
            "revision",
        ),
        block(
            "English Revision - Error Log",
            1,
            ["Redo all grammar and vocabulary mistakes from your error log"],
            "https://www.youtube.com/results?search_query=IOE+english+error+analysis",
            "Which careless English mistakes keep repeating even after revision?",
            "Personal English error log",
            "revision",
        ),
        block(
            "English Revision - Comprehension Tune-up",
            1,
            ["One final timed passage set with evidence-based answer checking"],
            "https://www.youtube.com/results?search_query=IOE+english+reading+practice",
            "Can you stay calm and evidence-based under passage pressure?",
            "Comprehension checklist",
            "revision",
        ),
        block(
            "English Revision - Final Sprint",
            1,
            ["Fast grammar, vocab, and phonetics sprint plus 20-minute formula-sheet review from a weak core subject"],
            "https://www.youtube.com/results?search_query=IOE+english+quick+revision",
            "Can English stay quick and clean without stealing energy from math, physics, or chemistry?",
            "English fast-score checklist",
            "revision",
        ),
    ],
}


FORMULA_SHEETS = {
    "MATHEMATICS": [
        "Set identities, interval notation, and absolute-value rules",
        "Function rules: inverse, composite, domain/range checks",
        "Matrix inverse and determinant results",
        "Complex-number identities and modulus/argument form",
        "AP/GP sums, permutation/combination, and binomial general term",
        "Trig identities, inverse-trig ranges, triangle laws",
        "Line, circle, conic, and plane equations",
        "Limit rules, derivative rules, tangent-normal, maxima-minima steps",
        "Standard integrals, area formulas, differential-equation forms",
        "Dot/cross/triple product and probability formulas",
    ],
    "PHYSICS": [
        "Units, dimensions, vector resolution, equations of motion, projectile formulas",
        "Newton's laws, friction, momentum, and collision relations",
        "Circular motion, gravitation, SHM, and rotational formulas",
        "Elasticity, fluid continuity, Bernoulli, and buoyancy formulas",
        "Heat, latent heat, thermal expansion, gas laws, and thermodynamic efficiencies",
        "Mirror/lens formulas, prism, YDSE, diffraction, and polarization relations",
        "Wave equation, pipes/strings, Doppler effect, intensity level",
        "Electrostatic field/potential, capacitance, and Kirchhoff rules",
        "Magnetic field, Faraday law, transformer, RMS, and power factor formulas",
        "Photoelectric equation, Bohr model, decay law, and semiconductor basics",
    ],
    "CHEMISTRY": [
        "Mole concept, equivalent mass, stoichiometric conversion ladder",
        "Gas laws and states-of-matter relations",
        "Electronic configuration order and periodic-trend rules",
        "Redox-number rules and equilibrium shifts",
        "Volumetric-analysis relations, pH, ionic-equilibrium patterns",
        "Faraday laws and cell-direction logic",
        "Enthalpy, rate factors, bond types, and VSEPR shapes",
        "Important non-metal compounds and environmental chemistry links",
        "Metallurgy flow, extraction steps, and metal reactivity",
        "Organic reaction map: hydrocarbons to amines",
    ],
    "ENGLISH": [
        "Tense sequence and subject-verb agreement rules",
        "Direct-indirect change rules and sentence transformation cues",
        "Conditionals, passive voice, and verbal patterns",
        "Parts of speech, punctuation, and preposition traps",
        "Phoneme groups, vowel/consonant classes, and stress rules",
        "Comprehension strategy: main idea, tone, evidence, elimination",
    ],
}

ENGLISH_MINIMAL_STRATEGY = [
    "Keep English to Sunday plus a 15-minute nightly micro-habit on 3 weekdays.",
    "Prioritise grammar, direct-indirect, voice, prepositions, and comprehension before deep vocabulary study.",
    "Treat English as a speed-score subject: answer quickly, avoid perfectionism, and save energy for math/physics.",
    "Maintain one single-page grammar rule sheet and one single-page vocabulary/idiom list.",
]

ENGLISH_QUICK_RULES = [
    "Match the verb to the real subject, not the nearest noun.",
    "Back-shift tense in indirect speech unless the statement is still universally true.",
    "Zero conditional uses present-present; third conditional uses had + past participle.",
    "Passive voice needs the correct form of be plus past participle.",
    "Gerunds act like nouns; participles act like adjectives or verb forms.",
    "Use articles based on specificity: a/an for non-specific, the for specific.",
    "Prepositions follow meaning patterns, not literal translation habits.",
    "Comma misuse and missing punctuation often signal the right MCQ option.",
    "In comprehension, choose the option best supported by the passage, not by outside knowledge.",
    "In phonetics/stress, look for syllable pattern and common suffix rules before guessing.",
]

TOP_20_REPEATED_TOPICS = [
    "Functions and inverse/composite functions",
    "Matrices and determinants",
    "Complex numbers",
    "Permutation and combination",
    "Binomial theorem",
    "Trigonometric equations",
    "Circle and conic-section equations",
    "Limits and continuity",
    "Applications of derivatives",
    "Integration and area",
    "Physical quantities, vectors, and projectile motion",
    "Newton's laws and friction",
    "Circular motion and SHM",
    "Heat and thermodynamics",
    "Geometric optics and interference",
    "Electrostatics and DC circuits",
    "Chemical equilibrium and ionic equilibrium",
    "Electrochemistry",
    "Organic functional-group reactions",
    "English grammar transformation and comprehension",
]

LAST_7_DAYS_STRATEGY = [
    "Day -7 to -5: one full mock every other day, plus same-day error review.",
    "Day -4 to -3: formula-sheet writing for math, physics, and chemistry; grammar-rule sprint for English.",
    "Day -2: only weak-topic repair and 30-40 rapid MCQs, no new content.",
    "Day -1: light recall, document check, sleep early, and stop heavy study by evening.",
    "Exam morning: no new learning, only short formula glances and calm breathing.",
]

PHASE_RULES = [
    (1, 60, "Phase 1 - Foundation", "Month 1-2"),
    (61, 120, "Phase 2 - Core Syllabus", "Month 3-4"),
    (121, 150, "Phase 3 - Practice", "Month 5"),
    (151, 180, "Phase 4 - Revision", "Month 6"),
]

MONTH_DAY_RANGES = [
    (1, 30, "Month 1 - Foundation"),
    (31, 60, "Month 2 - Foundation"),
    (61, 90, "Month 3 - Core Syllabus"),
    (91, 120, "Month 4 - Core Syllabus"),
    (121, 150, "Month 5 - Practice"),
    (151, 180, "Month 6 - Revision"),
]


def journey_day_number(target_date=None):
    target_date = target_date or date.today()
    if target_date <= JOURNEY_START_DATE:
        return 1
    if target_date >= JOURNEY_END_DATE:
        return JOURNEY_TOTAL_DAYS
    return (target_date - JOURNEY_START_DATE).days + 1


def subject_for_day_number(day_number):
    idx = max(1, min(JOURNEY_TOTAL_DAYS, int(day_number))) - 1
    return SUBJECT_SEQUENCE[idx % len(SUBJECT_SEQUENCE)]


def phase_for_day(day_number):
    for start, end, phase, month_group in PHASE_RULES:
        if start <= day_number <= end:
            return phase, month_group
    return PHASE_RULES[-1][2], PHASE_RULES[-1][3]


def month_for_day(day_number):
    for start, end, label in MONTH_DAY_RANGES:
        if start <= day_number <= end:
            return label
    return MONTH_DAY_RANGES[-1][2]


def difficulty_band_for_day(day_number):
    if day_number <= 14:
        return "concept-build"
    if day_number <= 30:
        return "starter-mcqs"
    if day_number <= 60:
        return "medium-mcqs"
    if day_number <= 120:
        return "hard-mixed"
    if day_number <= 150:
        return "timed-practice"
    return "revision-mock"


def mcq_targets_for_day(day_number, track, is_mock_day):
    if is_mock_day:
        return 20, 40
    if day_number <= 14:
        return 0, 0
    if day_number <= 30:
        return 5, 5
    if day_number <= 60:
        return 10, 10
    if day_number <= 120:
        return 15, 20
    if track == "practice":
        return 15, 20
    return 10, 20


def subtopic_for_day(block_data, topic_day_index):
    items = block_data["subtopics"]
    index = min(max(1, topic_day_index), len(items)) - 1
    return items[index]


def session_blocks_for_day(entry):
    subject = entry["subject"]
    subtopic = entry["subtopic"]
    topic = entry["topic"]
    morning_mcq = entry["mcq_target_morning"]
    evening_mcq = entry["mcq_target_evening"]
    is_first = entry["topic_day_index"] == 1
    is_second = entry["topic_day_index"] == 2
    is_final = entry["topic_day_index"] == entry["topic_day_total"]
    is_mock = entry["is_mock_day"]

    if is_mock:
        return (
            [
                "0-5 min: Review formula sheet and mock strategy only",
                "5-30 min: Solve timed mixed mock questions with no pausing",
                f"30-45 min: Check {morning_mcq} rapid MCQs and mark weak spots",
                "45-50 min: Write 3 mistakes to avoid in the evening mock block",
            ],
            [
                "0-10 min: Warm up with the morning error list",
                "10-50 min: Solve the main timed mixed set under strict exam conditions",
                "50-70 min: Review wrong answers and classify them by chapter",
                "70-85 min: Rewrite weak formulas and fastest solving shortcuts",
                "85-90 min: Decide tomorrow's repair target before closing",
            ],
        )

    morning = [
        "0-5 min: Review yesterday's notes only",
        f"5-30 min: Learn '{subtopic}' from the linked resource",
        (
            "30-45 min: No new MCQs yet - translate the concept into your own words"
            if morning_mcq == 0
            else f"30-45 min: Solve {morning_mcq} focused MCQs on today's subtopic"
        ),
        f"45-50 min: Write 3 key formulas or points from {topic}",
    ]
    evening = [
        "0-10 min: Warm up by reviewing the morning notes",
        (
            "10-50 min: Re-explain the concept aloud and rebuild examples without notes"
            if evening_mcq == 0
            else f"10-50 min: Solve {evening_mcq} MCQs on {topic} and mark every mistake"
        ),
        f"50-70 min: Advance to the next layer of '{topic}' through '{subtopic}'",
        "70-85 min: Write clean notes and one-page summary lines",
        "85-90 min: Plan tomorrow's focus before stopping",
    ]

    if is_first:
        morning[1] = f"5-30 min: Start '{topic}' from zero using '{subtopic}'"
        evening[2] = f"50-70 min: Preview tomorrow's part of '{topic}' so it feels familiar"
    elif is_second:
        evening[0] = "0-10 min: Warm up with yesterday's notes and one mini recap aloud"
        evening[2] = f"50-70 min: Advance into the next part of '{topic}' and compare it with Day 1"
    elif is_final:
        morning[2] = (
            "30-45 min: Do a self-check instead of fresh MCQs if Week 1-2 pacing applies"
            if morning_mcq == 0
            else f"30-45 min: Solve {morning_mcq} final-check MCQs and flag any last confusion"
        )
        evening[1] = (
            "10-50 min: Run the full self-test and explain every answer aloud"
            if evening_mcq == 0
            else f"10-50 min: Solve {evening_mcq} mixed MCQs and finish the topic with confidence"
        )
        evening[2] = f"50-70 min: Answer the self-test question: {entry['self_test_question']}"
        evening[3] = f"70-85 min: Final formula memorisation for {topic}"
        evening[4] = f"85-90 min: Mark '{topic}' complete and note the next topic"

    if subject == "ENGLISH":
        evening[2] = "50-70 min: Keep English light, then review one weak formula sheet from Math/Physics/Chemistry"

    return morning, evening


def build_subject_entries(subject, blocks):
    entries = []
    for block_index, block_data in enumerate(blocks, start=1):
        for topic_day in range(1, block_data["days"] + 1):
            entries.append(
                {
                    "subject": subject,
                    "topic": block_data["topic"],
                    "subtopic": subtopic_for_day(block_data, topic_day),
                    "topic_day_index": topic_day,
                    "topic_day_total": block_data["days"],
                    "resource_url": block_data["resource_url"],
                    "self_test_question": block_data["self_test_question"],
                    "formula_focus": block_data["formula_focus"],
                    "track": block_data["track"],
                    "block_index": block_index,
                }
            )
    return entries


def build_weekly_targets(plan):
    weekly = {}
    total_weeks = (JOURNEY_TOTAL_DAYS + 6) // 7
    for week_number in range(1, total_weeks + 1):
        week_entries = [entry for entry in plan if entry["week_number"] == week_number]
        phase = week_entries[0]["phase"]
        finished_topics = []
        for entry in week_entries:
            if entry["topic_day_index"] == entry["topic_day_total"]:
                finished_topics.append(f"{entry['subject']}: {entry['topic']}")
        if phase == "Phase 1 - Foundation":
            self_test = "Untimed weekly recall check: explain each topic aloud, then solve a 15-question mixed quiz."
            target_score = "Aim for 60% and clear understanding."
        elif phase == "Phase 2 - Core Syllabus":
            self_test = "20-25 mixed MCQs from the week's subjects with an error log."
            target_score = "Aim for 65-70% before moving on confidently."
        elif phase == "Phase 3 - Practice":
            self_test = "35-40 timed MCQs plus one short mixed mini-mock."
            target_score = "Aim for 75% with improving speed."
        else:
            self_test = "Revision week: one half/full mock plus formula-sheet recall."
            target_score = "Aim for 80%+ and identify only small weak pockets."
        weekly_id = f"W{week_number:02d}"
        weekly[weekly_id] = {
            "id": weekly_id,
            "week_number": week_number,
            "phase": phase,
            "topics_to_finish": finished_topics or ["Hold the current topics and finish every pending self-test."],
            "weekly_mcq_target": sum(entry["mcq_target_morning"] + entry["mcq_target_evening"] for entry in week_entries),
            "weekly_self_test": self_test,
            "score_target": target_score,
            "catch_up_rule": "If behind, keep the same subject on the next due day, cut note-making to one clean page, and use Sunday review to close backlog.",
        }
    return weekly


def build_milestones(plan):
    milestone_specs = [
        (30, "M1", "Month 1 checkpoint", "Mini mock from sets/functions, mechanics basics, chemical arithmetic/states, and core grammar", "35+/140 feels on track for a zero-base start."),
        (60, "M2", "Month 2 checkpoint", "Mini mock from all foundation topics completed by Day 60", "45+/140 means the base is stabilising."),
        (90, "M3", "Month 3 checkpoint", "Mini mock from foundation plus first half of the core syllabus", "60+/140 means the core build is working."),
        (120, "M4", "Month 4 checkpoint", "Syllabus-completion mock covering all core chapters once", "70+/140 means the full syllabus is in play."),
        (150, "M5", "Month 5 checkpoint", "Timed mixed paper built from month-5 drills and full-paper practice", "80+/140 means Krish is entering competitive range."),
        (180, "M6", "Final checkpoint", "Final full mock and last weak-topic repair only", "90+/140 is the competitive target."),
    ]
    milestones = {}
    for cutoff_day, milestone_id, title, mock_scope, score_target in milestone_specs:
        completed = []
        seen = set()
        for entry in plan:
            if entry["day_number"] > cutoff_day:
                break
            if entry["track"] == "content" and entry["topic_day_index"] == entry["topic_day_total"]:
                key = (entry["subject"], entry["topic"])
                if key not in seen:
                    seen.add(key)
                    completed.append(f"{entry['subject']}: {entry['topic']}")
        milestones[milestone_id] = {
            "id": milestone_id,
            "title": title,
            "cutoff_day": cutoff_day,
            "expected_completed": completed,
            "mini_mock_scope": mock_scope,
            "score_target": score_target,
            "catch_up_plan": "If behind, freeze new content for one week, finish only overdue topics, and convert every Sunday into review + error-log repair.",
        }
    return milestones


def load_study_plan():
    if hasattr(load_study_plan, "_cache"):
        return load_study_plan._cache

    subject_entries = {subject: build_subject_entries(subject, blocks) for subject, blocks in SUBJECT_BLOCKS.items()}
    subject_pointers = {subject: 0 for subject in subject_entries}
    plan = []
    for day_number in range(1, JOURNEY_TOTAL_DAYS + 1):
        subject = subject_for_day_number(day_number)
        entry = dict(subject_entries[subject][subject_pointers[subject]])
        subject_pointers[subject] += 1

        phase, month_group = phase_for_day(day_number)
        month_label = month_for_day(day_number)
        weekly_target_ref = f"W{((day_number - 1) // 7) + 1:02d}"
        milestone_ref = f"M{((day_number - 1) // 30) + 1}"
        is_revision_day = day_number >= 151 or entry["track"] == "revision"
        is_mock_day = "Mock" in entry["topic"] or "mock" in entry["topic"].lower()
        mcq_target_morning, mcq_target_evening = mcq_targets_for_day(day_number, entry["track"], is_mock_day)

        entry.update(
            {
                "day_number": day_number,
                "date_offset": day_number - 1,
                "date": JOURNEY_START_DATE + timedelta(days=day_number - 1),
                "phase": phase,
                "month_group": month_group,
                "month_label": month_label,
                "week_number": ((day_number - 1) // 7) + 1,
                "difficulty_band": difficulty_band_for_day(day_number),
                "weekly_target_ref": weekly_target_ref,
                "milestone_ref": milestone_ref,
                "is_revision_day": is_revision_day,
                "is_mock_day": is_mock_day,
                "mcq_target_morning": mcq_target_morning,
                "mcq_target_evening": mcq_target_evening,
            }
        )
        morning_plan, evening_plan = session_blocks_for_day(entry)
        entry["morning_plan"] = morning_plan
        entry["evening_plan"] = evening_plan
        plan.append(entry)

    weekly_targets = build_weekly_targets(plan)
    milestones = build_milestones(plan)
    references = {
        "formula_sheets": FORMULA_SHEETS,
        "english_strategy": ENGLISH_MINIMAL_STRATEGY,
        "english_rules": ENGLISH_QUICK_RULES,
        "top_20_topics": TOP_20_REPEATED_TOPICS,
        "last_7_days": LAST_7_DAYS_STRATEGY,
    }
    load_study_plan._cache = {
        "plan": plan,
        "weekly_targets": weekly_targets,
        "milestones": milestones,
        "references": references,
    }
    return load_study_plan._cache


def current_day_entry(target_date=None):
    study_plan = load_study_plan()["plan"]
    return study_plan[journey_day_number(target_date) - 1]


def subject_entries(plan, subject):
    return [entry for entry in plan if entry["subject"] == subject]


def derive_subject_progress(plan, day_progress):
    day_progress = max(0, min(int(day_progress), len(plan)))
    completed = plan[:day_progress]
    subject_counts = {}
    topic_counts = {}
    for subject in SUBJECT_BLOCKS:
        subject_counts[subject] = len([entry for entry in completed if entry["subject"] == subject])
        finished = []
        seen = set()
        for entry in completed:
            if entry["subject"] != subject:
                continue
            if entry["topic_day_index"] != entry["topic_day_total"]:
                continue
            key = entry["topic"]
            if key not in seen:
                seen.add(key)
                finished.append(key)
        topic_counts[subject] = finished
    return {"subject_days": subject_counts, "subject_topics": topic_counts}


def actual_day_entry(progress_state, target_date=None):
    progress = max(0, min(int(progress_state.get("day_progress", 0)), JOURNEY_TOTAL_DAYS - 1))
    return load_study_plan()["plan"][progress]


def subject_context(subject, progress_state, target_date=None):
    target_date = target_date or date.today()
    study_plan = load_study_plan()["plan"]
    expected_day = journey_day_number(target_date)
    day_progress = max(0, min(int(progress_state.get("day_progress", 0)), JOURNEY_TOTAL_DAYS - 1))
    subject_plan = subject_entries(study_plan, subject)
    scheduled_items = [entry for entry in subject_plan if entry["day_number"] <= expected_day]
    scheduled = dict(scheduled_items[-1] if scheduled_items else subject_plan[0])
    actual_count = len([entry for entry in study_plan[:day_progress] if entry["subject"] == subject])
    actual_index = min(actual_count, len(subject_plan) - 1)
    actual = dict(subject_plan[actual_index])
    scheduled_index = max(0, len(scheduled_items) - 1)
    behind_days = max(0, scheduled_index - actual_index)
    ahead_days = max(0, actual_index - scheduled_index)
    display = actual if day_progress != expected_day - 1 else scheduled
    return {
        "scheduled": scheduled,
        "actual": actual,
        "display": display,
        "behind_days": behind_days,
        "ahead_days": ahead_days,
        "expected_day": expected_day,
        "day_progress": day_progress,
    }


def weekly_target_for_day(entry):
    return load_study_plan()["weekly_targets"][entry["weekly_target_ref"]]


def milestone_for_day(entry):
    return load_study_plan()["milestones"][entry["milestone_ref"]]


def formula_sheet_for_subject(subject):
    return FORMULA_SHEETS.get(subject, [])


def english_quick_rules():
    return list(ENGLISH_QUICK_RULES)
