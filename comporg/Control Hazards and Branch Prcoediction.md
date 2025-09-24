 Continues [[Data Hazards Forwarding and Stalling]]
 Continues [[Exceptions and Interrupts]]
# Pipelined Datapath Diagram
![[Pasted image 20241028180453.png]]
# Control Hazards
- The proper instruction cannot execute in the proper clock cycle because the instruction that was fetched is not the one that is needed
	- Fetching the next instruction depends on branch outcome
	- Pipeline can't always fetch correct instruction
- In LEGv8 Pipeline
	- Registers are compared and the target is computed early in the pipeline
	- Add hardware to do this in the ID stage
- Note: For some reason the textbook pretends the B.XX conditional branch instructions do not exist
	- It only considers the CBZ and CBNZ instructions
# Flushing The Pipeline
- Consider this example
- ![[Pasted image 20241111163120.png]]
	- The ALU outputs the result of comparing X1 against 0 in CC4
		- This is always true. The result of a comparison will be available at the ALU output (EX/MEM Reg) 3 clock cycles after the comparison instruction is fetched
	- However, each of the three clock cycles after CC1 fetched a new instruction and pushed it down the pipeline
	- If the branch should have been taken, these instructions must be discarded
		- This means setting the following 3 registers to 0s
			- ID/EX
			- EX/MEM
			- MEM/WB
		- Note these are the three registers that come after IF/ID
- For a CBZ instruction, flushing the pipeline due to a false branch prediction involves emptying three registers and discarding three instructions, causing a 3 cycle delay
- For a conditional branch instruction, flushing the pipeline only discards a maximum of two instructions and causes a 2 cycle delay
	- This is because the comparison instruction is typically written after the instruction that sets the flags
- Flushing is implemented through a signal called IF.Flush that zeros the instruction field of the IF/ID register
	- This also flushes the ID/EX register
		- Sets it to 0
# Reducing Branch Delays
- Firstly, move up the calculation of the branch target from the EX stage to the ID stage
	- The PC target and immediate offset are already available in the IF/ID register, so there should be no problem
	- Move the PC Target adder and shifter into the ID stage
- The more difficult task is moving the branch decision into the ID stage
	- Checking if a value is 0 simply involves ORRing all 64 bits
	- But there needs to be additional hazard and forwarding detection involved, since the value to be tested in the ID stage may not have reached the register file yet.
		- It could either:
			- Not have been computed yet
				- This would require a stall
			- Be in the ID stage
				- No hazard
			- Be in the EX/MEM Register 
			- Or be in the MEM/WB Register
	- There are two complicating factors
		- 1. During ID, we must decode the instruction, decide if a bypass to the 0 test unit is needed, and complete the 0 test
			- Forwarding for branches was previously handled by the ALU forwarding unit, since the 0 testing was done by the ALU
			- Now, there must be a separate forwarding unit to handle forwarding to the 0-testing unit
		- 2. If the value used for the branch decision is calculated in the immediately preceding instruction, a stall is required
- By moving the branch decision logic into the ID stage, the penalty for flushing the pipeline is limited to just one instruction/cycle
	- This is because only one instruction is fetched during the time the decision is being made
- 
# Reordering/Delayed Decision
- Fill the branch delay slot with an instruction that has no dependency
# Branch Prediction
- Predict outcome of branch
	- Stall if prediction is wrong
## Static Branch Prediction
- LEGv8 just always predicts that the branch is not taken
- Simplest mode of branch prediction
	- Predict backwards branches are taken
		- Loops
	- Predict forwards branches not taken
		- If statements
## Dynamic Branch prediction
- Hardware measures and predicts actual branch behavior
### Branch Target Buffer
- Use the last 5 bits of the instruction to address a small memory
- Each memory location holds the state of the branch buffer state machine
	- Branch prediction buffer/history table
- Example 2-bit branch target buffer predictor in verilog
```verilog
module buffer_predictor(
	input wire [18:0] branch_address,
	input wire update,
	input wire taken, 
	output wire prediction); 
	
	reg [1:0] prediction_buffer [0:31];

	wire [4:0] buffer_addr = branch_address[4:0];
	assign prediction = prediction_buffer[buffer_addr][1];
	
	always (*) begin
		if  (update) begin
		if (!taken_or_not_taken) begin
			// not taken
			if prediction_buffer[buffer_addr] != 0 begin
				prediction_buffer[buffer_addr] -= 1
			end
		end
		else begin
			if (prediction_buffer[buffer_addr] != 11b) 				        prediction_buffer[buffer_addr] += 1;
		end
		end
	end
endmodule

```
### Correlating Predictor
- Combines local behavior of a particular branch and global information about the behavior of some recently executed branches
	- A typical correlating predictor may have two different 2-bit predictors for each branch.
	- The choice of which predictor to use is made based on whether the last executed branch was taken or not taken
		- Note that this can be thought of as simply adding another index bit to the buffer address
- Example of 2x2 correlating predictor
```verilog
module correlating_predictor(
	input wire [18:0] branch_address,
	input wire update,
	input wire taken, 
	output wire prediction); 
	
	reg [1:0] prediction_buffer [31:0];
	reg last_branch_taken;

	wire [5:0] buffer_addr = branch_address[4:0] << 1 + last_branch_taken;
	assign prediction = prediction_buffer[buffer_addr][1];
	
	always (*) begin
		if  (update) begin
		if (!taken_or_not_taken) begin
			// not taken
			if prediction_buffer[buffer_addr] != 0 begin
				prediction_buffer[buffer_addr] -= 1
			end
		end
		else begin
			if (prediction_buffer[buffer_addr] != 11b) 				        prediction_buffer[buffer_addr] += 1;
		end
		end
		last_branch_taken = taken;
	end
endmodule
```
### Tournament Predictor
- Also called Ensemble Predictor
- Has multiple predictors per branch address, and decides which one to use based on some selection mechanism
# FINAL CPU DIAGRAM
![[Pasted image 20241111181840.png]]

For class #comporg