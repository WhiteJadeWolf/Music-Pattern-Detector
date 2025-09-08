from graphviz import Digraph

dot = Digraph()

# states added
dot.node("0", "root")
dot.node("1", "I")
dot.node("2", "IV")
dot.node("3", "V")
dot.node("4", "I* (P1)")
dot.node("5", "ii")
dot.node("6", "V")
dot.node("7", "I* (P2)")

# transitions added
dot.edge("0", "1", "I")
dot.edge("1", "2", "IV")
dot.edge("2", "3", "V")
dot.edge("3", "4", "I")
dot.edge("0", "5", "ii")
dot.edge("5", "6", "V")
dot.edge("6", "7", "I")

dot.render("automaton", format="png")