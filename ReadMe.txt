Created_By: Morgan Houston

Running cspConsistency uses arc consistency to find solutions in different ways. One being domain splitting. It will test the solution it finds with the solutions in the cspExamples test function.

Running cspSLS will use the stochastic local searcher (any-conflict) to search for a solution selecting any conflict.
It is set to only search 1000 steps for the solution. It will return 'No solution in XXXX steps X conflicts remain', if no solution is found.

Running cspSearch will use a depth-first search to look through the domain and try different values to find a solution. It also will display the cost at each step.