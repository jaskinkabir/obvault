- Static testing unrealistic, human testing slow and low in test case coverage
- Create an agent that is a synthetic user to test the agent you are developing
# Scenario Building
- Scenarios built from
	- Profiles built from
		- Demographic attributes
		- Personality attributes
		- Target customer attributes
	- And User Goals
		- Knowledge
		- Agent capabilities
# How to Evaluate Simulation Quality
## Coverage
- Tool-calling Transition Entropy:
	- How different are the sequences of tool calls to each other?
- Tool-calling Distribution Entropy
	- How many different tools are called?
- Trajectory Distance
## Realism
- Ensure the user looks like a real user
## Cost
## Agent Failure Identification

## Example Metrics
- Customer needs completion rate:
	- How often does the agent do what it's supposed to
- Customer needs completion efficiency
	- How many tokens consume to fulfill user needs
- Call to action completion rate
	- How often does the user do what the agent says
# Self-Improving with Simulation
- Prompt optimization
- Tool updates
- Post-training with new data from simulation logs
# Simulation for Workflow Agents?
- No chat, just tool calls
## Mortgage Problem
- Mortgage decisions depend on multiple documents
- Most errors come from cross-document inconsistencies
- Today's models are rarely trained on complete, realistic cases
- Real data is restricted and hard to scale (for privacy reasons)
- Borrower stories are fragmented across documents
- Edge cases and real-world complexity are not controllable
### Persona-Based Document Synthesis
- Generate synthetic borrower profiles that produce complete, internally consistent mortgage application documents for training and testing cross-document underwriting systems
- Add noise, dark lighting, and motion blur to images of documents to train/test OCR
