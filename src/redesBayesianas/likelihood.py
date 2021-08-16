from model import model

# Calculate probability for a given observation
#P(j,m,~a,b,~e)
probability = model.probability([["true", "false", "false", "true","true"]])

print("P(j,m,~a,b,~e)={}".format(probability))

