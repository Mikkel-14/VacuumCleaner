from pomegranate import *

# Robo has no parents
robo = Node(DiscreteDistribution({
    "true": 0.001,
    "false": 0.999
    }),name="robo")
#Terremoto has no parents
terremoto = Node(DiscreteDistribution({
    "true":0.002,
    "false":0.998
    }), name="terremoto")

# Alarma is conditional to robo and terremoto
alarma = Node(
    ConditionalProbabilityTable([
        ["true","true","true",0.95],
        ["true","false","true",0.94],
        ["false","true","true",0.29],
        ["false","false","true",0.001],
        ["true","true","false",0.05],
        ["true","false","false",0.06],
        ["false","true","false",0.71],
        ["false","false","false",0.999]
    ], [robo.distribution, terremoto.distribution]), name="alarma")

# JohnLlama nodo is conditional on alarma
johnLlama = Node(ConditionalProbabilityTable([
    ["true","true",0.90],
    ["false","true",0.05],
    ["true","false",0.10],
    ["false","false",0.95]
], [alarma.distribution]),name="j")

# MaryLlama node is conditional on alarma
maryLlama = Node(ConditionalProbabilityTable([
    ["true","true",0.70],
    ["false","true",0.01],
    ["true","false",0.30],
    ["false","false",0.99]
], [alarma.distribution]),name="m")

# Create a Bayesian Network and add states
model = BayesianNetwork()
model.add_states(robo, terremoto, alarma, johnLlama,maryLlama)

# Add edges connecting nodes
model.add_edge(robo, alarma)
model.add_edge(terremoto, alarma)
model.add_edge(alarma, johnLlama)
model.add_edge(alarma, maryLlama)

# Finalize model
model.bake()

#segundo modelo
rained = Node(DiscreteDistribution({
    "true":0.2,
    "false":0.8
}),name="rained")

sprinklers = Node(DiscreteDistribution({
    "true":0.6,
    "false":0.4
}),name="sprinklers")

#conditionals on R 
vecino = Node(ConditionalProbabilityTable([
    ["true","true",0.3],
    ["false","true",0.4],
    ["true","false",0.7],
    ["false","false",0.6]
],[rained.distribution]),name="vecino")

#conditionals on R and S
grass = Node(ConditionalProbabilityTable([
    ["true","true","true",0.9],
    ["true","false","true",0.7],
    ["false","true","true",0.8],
    ["false","false","true",0.2],
    ["true","true","false",0.1],
    ["true","false","false",0.3],
    ["false","true","false",0.2],
    ["false","false","false",0.8]
],[rained.distribution,sprinklers.distribution]),name="grass")

#conditionals on V and G
dog = Node(ConditionalProbabilityTable([
    ["true","true","true",0.9],
    ["true","false","true",0.4],
    ["false","true","true",0.5],
    ["false","false","true",0.3],
    ["true","true","false",0.1],
    ["true","false","false",0.6],
    ["false","true","false",0.5],
    ["false","false","false",0.7]
],[vecino.distribution,grass.distribution]),name="dog")

# Create a Bayesian Network and add states
model2 = BayesianNetwork()
model2.add_states(rained, sprinklers, vecino, grass, dog)

# Add edges connecting nodes
model2.add_edge(rained, vecino)
model2.add_edge(rained, grass)
model2.add_edge(sprinklers, grass)
model2.add_edge(vecino, dog)
model2.add_edge(grass, dog)

# Finalize model
model2.bake()