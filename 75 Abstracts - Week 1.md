# 1. FPGA-Accelerated 3rd Generation DNA Sequencing
[10.1109/TBCAS.2019.2958049](https://doi.org/10.1109/TBCAS.2019.2958049)
School: York University (Toronto)
- DNA sequencing devices are becoming much smaller and more power efficient
- This means they can be used in mobile settings more easily 
- However, mapping the raw signal data from the measurement device onto the ACGT bases requires immense compute
- This paper uses an FPGA accelerator for this 'basecalling' task of DNA measurements
- The computations are ported to a custom FPGA which operates with a CPU, which leads to a 100X speed-up over CPU-only 
	- Energy efficiency is increased by 3x
# 2. FPGA Acceleration of Sequence Alignment: A Survey
School: UCSD
https://doi.org/10.48550/arXiv.2002.02394
- Generation of genetic data now outpaces the growth of computational power
	- Current machines sequence 50 genomes a day, but aligning the sequences against a reference genome and assembling the read genome takes 1300 CPU hours
- The main step in constructing the genome is alignment
- FPGA accelerators have shown great performance improvements due to the massive parallelism
- The paper discusses three main algorithms for this task and their implementations on FPGA
# 3. An optimized and low-cost FPGA-based DNA sequence alignment--a step towards personal genomics
[10.1109/EMBC.2013.6610096](https://doi.org/10.1109/embc.2013.6610096)
School: UET (Pakistan)
- FPGA accelerators for DNA sequence alignment typically ignores the performance per dollar spent metric
- This paper presents optimizations that increase the cost effectiveness of FPGA-based DNA alignment
	- The processing is set to start on a change in input value rather than clock, which eliminates the need for tight clock synchronization
	- The implementation is unrestrained by the size of the sequences to be aligned
	- The waiting time required for sequence to load into the FPGA is minimized
	- An efficient method is devised to store the output matrix
		- The diagonal elements are saved and used in the next pass in parallel with the computation of the output matrix
- This implementation achieved a 20x performance improvement 
# 4. High speed DNA sequencing accelerator using FPGA
[10.1109/ICED.2008.4786759](https://doi.org/10.1109/ICED.2008.4786759)
School: Universiti Teknologi MARA (Malaysia)
- The Smith-Waterman algorithm is a common algorithm used for DNA alignments. As the sequence database increases, it becomes much harder for CPUs to handle the workload
- A parallelized FPGA implementation of this algorithm has been developed that can align 10 sequences each clock cycle
# 5. Accelerating DNA pairwise sequence alignment using FPGA and a customized convolutional neural network
School: Mansoura University (Egypt)
[https://doi.org/10.1016/j.compeleceng.2021.107112](https://doi.org/10.1016/j.compeleceng.2021.107112 "Persistent link using digital object identifier")
- Two DNA sequence alignment algorithms based on lookup tables are illustrated
	- These algorithms are best used for identifying similar regions between sequences
- The proposed implementation relies on the complete parallelization of these algorithms
- A customized CNN is used to implement global alignment and achieve 98.3% accuracy
# 6. MEDAL: Scalable DIMM based Near Data Processing Accelerator for DNA Seeding Algorithm
[https://doi.org/10.1145/3352460.335832](https://doi.org/10.1145/3352460.3358329)
School: UCSB
- In contrast to other papers examining the use of FPGA for sequence alignment, this paper investigates the problem of DNA seeding, which is typically a memory-bound problem
	- This is why NDP (Near Data Processing) is a better solution
- Current NDP solutions for DNA seeding face two grand challenges
	- Fine-grained random memory access
	- Scalability
- This paper proposes a practical, efficient, DIMM based NDP accelerator for a DNA seeding algorithm (MEDAL) using of the shelf DRAM components
- The memory access problem is solved on small databases that can fit within a single DRAM rank with
	- An intra-rank design, together with algorithm-specific address mapping, bandwidth-aware data mapping, and Individual Chip Select
- To tackle scalability there are three proposed inter-rank designs
	- Polling-based communication
	- Interrupt-based communication
	- Non-Volatile DIMM solution
- Additionally, the paper proposes an algorithm-specific data compression technique
# Notes on DNA
- Field shows potential for improvement through FPGAs on several levels, from interpreting raw sensor data all the way up to aligning the sequences and comparing them against others
- There are even papers proposing compute-in-memory solutions
# 7. IoT Intrusion Detection Using Machine Learning with a Novel High Performing Feature Selection Method
 [https://doi.org/10.3390/app12105015](https://doi.org/10.3390/app12105015)
 Schools: 
	 - University of Idaho
	 - Princess Sumaya Uni for Tech (Jordan)
	 - Qassim Uni (Saudi Arabia)
	 - Washington State
	 - Ashland Uni (Ohio asd
 - IDS, or Intrusion Detection Systems, are important in IoT networks for security
 - The paper proposes a novel feature selection and extraction approach for anomaly-based IDS
	 - Detecting anomalies in the network traffic, system activity, etc within a network
 - The model is trained and tested on the IoT intrusion dataset, and the NSL-KDD dataset
	 - The approach scores 99.98% in accuracy, which reveals this approach to be state-of-the-art
# 8. A Lightweight Multi-Attack CAN Intrusion Detection System on Hybrid FPGAs
- DOI:[10.1109/FPL57034.2022.00070](https://doi.org/10.1109/FPL57034.2022.00070)
School: Trinity College Dublin
- Intrusion detection for in-vehicle CAN networks is important because the CAN protocol has no inherent security or authentication mechanism
- Most approaches require dedicated computing components like GPUs, which consume large amounts of power
- This paper presents a lightweight multi-attack quantised ML model that is deployed using Xilinx's DL processing unit IP
- The model detects Dos and fuzzing attacks with an accuracy above 99%
- The system consumes justs 2W with software tasks running on the ECU
- Achieves a 25% reduction in processing latency over other state-of-the-art implementations
# 9. FPL Demo: A Flexible and Scalable Quantum-Classical Interface based on FPGAs
[10.1109/FPL57034.2022.00089](https://doi.org/10.1109/FPL57034.2022.00089)
School: Osaka University
- Quantum computers require a controller to communicate with quantum devices
- FPGAs are an attractive platform for such controllers because
	- The controller requires flexibility to transmit/receive various wave shapes
	- Scalability is also required
- Challenges exist in implementing QC-IFs on FPGAs because of the restrictions of physics
- This workdemonstrates an implementation with high-bandwidth memory to treate large-volume data in high throughput
# 10. Optimized Mappings for Symmetric Range-Limited Molecular Force Calculations on FPGAs (Interesting)
[10.1109/FPL57034.2022.00026](https://doi.org/10.1109/FPL57034.2022.00026)
School: Boston University
- Simulation of molecular forces is challenging and Computing these pair-wise forces in parallel, and finding the optimal mapping of particles and computations to memories and processors is surprisingly challenging
- Mappings on FPGAs have not previously been studied
	- It was thought that the half-shell method, which is not FPGA-friendly, the preferred method
- This work shows that the Manhattan method is compatible with FPGA hardware
	- The ultra-fine-grained memory access demanded by this method can be satisfied, even though FPGA memory blocks appear not to be fine-grained enough
- The Manhattan method allows for a more efficient utilization of FPGA hardware and speeds up the simulation process in a way not explored before
# 11. SQL2FPGA: Automatic Acceleration of SQL Query Processing on Modern CPU-FPGA Platforms (Interesting)
[10.1109/FCCM57271.2023.00028](https://doi.org/10.1109/FCCM57271.2023.00028)
School: Simon Fraser University, BC Canada
- FPGA-based database acceleration has shown a promising performance improvement with good energy efficiency
- But most innovations rely on the SQL query plan generated by CPU query engines and map the query plan onto FPGA accelerators
	- Tedious and error prone
	- Do not consider the utilization of FPGA accelerators and could lose more optimization opportunities
- SQL2FPGA is an FPGA accelerator-aware compiler that automatically maps SQL queries onto the CPU-FPGA platform
- The front-end takes an optimized logical plan from the query engine and transforms it into an intermediate representation
- The IR is then fed through several compiler optimization passes to:
	- Improve acceleration coverage by FPGA
	- Eliminate redundant computation
	- Minimize data transfer between FPGA and CPU
- Finally, SQL2FPGA generates the query acceleration code for CPU-FPGA system deployment
- Achieves a speedup of up to 13.9x
# 12. FPGA-accelerated Iterative Reconstruction for Transmission Electron Tomography
[10.1109/FCCM51124.2021.00025](http://dx.doi.org/10.1109/FCCM51124.2021.00025)
School: Peking University
- TET is a biomedical imaging technique that uses iterative reconstruction to obtain reconstructed images
- The MS algorithm is accurate, but compute and memory intensive
- The algorithm can be parallelized and acccelerated on FPGA
- The paper's approach achieves a 1.87X speedup compared to GPU
# 13. Upgrade of FPGA Range-Limited Molecular Dynamics to Handle Hundreds of Processors
[10.1109/FCCM51124.2021.00024](https://doi.org/10.1109/FCCM51124.2021.00024)
School: Boston University
- Molecular Dynamics simulation plays a crucial role in drug discovery
- Current approaches to parallelization of this task using FPGA does not scale well when the number of pipelines grows from 10 to the hundreds
- This is done through 4 major contributions:
	- Address the problem of routing
	- Develop a novel asynchronous out-of-order comm mechanism
	- Invert standard particle access algorithm
	- Custom numerical format that increases precision and saves on space and logic
# 14. The Importance of Being X-Drop: High Performance Genome Alignment on Reconfigurable Hardware
[10.1109/FCCM51124.2021.00023](https://doi.org/10.1109/FCCM51124.2021.00023)
School: Polytechnic University of Milan
- The most commonly used approaches to alignment use time consuming exact alignment algorithms, while heuristic algorithms can be faster and more efficient
- State-of-the-art hardware implementations of genome alignment often lack high-level APIs that simplify their integration into commonly used genomic pipelines
	- These implementations also typically use exact alignment
- This paper presents the first high-performance FPGA implementation of the X-drop heuristic alg and an easy-to-use FPGA
- This design achieves up to 5x speed-up vs a software algorithm running on two 80-core Xeon processors
- Achieves a 1.5x speedup vs a GPU implementation of X-drop running on an Nvidia Tesla V100
# 15. FPGA-Based Real-Time Charged Particle Trajectory Reconstruction at the Large Hadron Collider (Interesting)
[10.1109/FCCM.2017.27](https://doi.org/10.1109/FCCM.2017.27)
School:
	- Cornell
	- Rutgers
	- Notre Dame
	- Ohio State
- The Compact Muon Solenoid experiment at CERN's LHC present several challenges
	- The input data rate is about 20 to 40 Tbps
	- A new batch of input data must be processed every 25ns
		- Each batch contains 10k precise position measurements of particles (stubs)
	- Pattern recognition must be performed on thhse stubs to find the trajectories
	- A list of parameters describing these trajectories must be produced within 4 $\mu s$ of input
- This paper presents a novel approach to pattern recognition and trajectory reconstruction using an all-FPGA solution
# 16. Bonded Force Computations on FPGAs
[10.1109/FCCM.2017.49](https://doi.org/10.1109/FCCM.2017.49)
School: Boston University
- Sidenote: Boston University has several papers on molecular dynamics acceleration
- Acceleration of MD has received much attention, but the bonded force calculation has not, even though this is a significan part of this application
- This paper is the first description and analysis of bonded force calculations outside of ASICs
	- The paper characterizes the computational requirements
- A naive, direct FPGA implementation requires resources out of proportion with the FPGA's portion of the workload
	- Other options such as softcores and speed/area tradeoffs are investigated
# 17. FPGA-Based Real-Time Super-Resolution System for Ultra High Definition Videos (Interesting)
[10.1109/FCCM.2018.00036](http://dx.doi.org/10.1109/FCCM.2018.00036)
School: Peking University
- The display market is deluged with UHD displays, yet most cameras can only produce FHD video, and most content available is only FHD
- Upgrading existing videos without extra storage costs can be achieved using an FPGA-based super-resolution system that allows real-time, high quality UHD upscaling
- The system balances FPGA utilization, frame rate, and image quality
- The system achieves superior throughput and quality when compared to current approaches
# 18. Hardware Acceleration of Long Read Pairwise Overlapping in Genome Sequencing: A Race Between FPGA and GPU
[10.1109/FCCM.2019.00027](https://doi.org/10.1109/FCCM.2019.00027)
- School: UCLA
- There is a problem in genome sequencing of detecting potential overlaps between any pair of input reads
	- This task, called chaining, needs to be accelerated
- The task is poorly parallelizable, but this paper proposes a method to adapt the algorithm in to a hardware-friendly form
- The GPU accelerator achieves 7x acceleration, while the FPGA achieves 28x acceleration
	- This paper also analyzes the architectural reason for the performance difference

# 19. FPGA-accelerated Automatic Alignment for Three-dimensional Tomography
[10.1109/FCCM48280.2020.00031](https://doi.org/10.1109/FCCM48280.2020.00031)
School: Peking University
- The attitude and center point of a specimen, from which the projection data is collected, can suffer from misalignment
- This paper proposes an FPGA accelerator for a state-of-the-art auto alignment algorithm
	- Modifies order of data access for easier on-chip data management
	- Using BRAMs and effective local data management
- The accelerator has a 60x speed-up with 7.8x energy reduction over an open CL implementation on Nvidia Titan V
# 20. When Apache Spark Meets FPGAs: A Case Study for Next-Generation DNA Sequencing Acceleration
[10.1109/FCCM.2016.18](https://doi.org/10.1109/FCCM.2016.18)
- School: UCLA
- This paper uses next-generation DNA sequencing as a case study to demonstrate how FPGAs can be efficiently integrated into big data frameworks
	- The question of how to integrate FPGAs into existing frameworks like Apache Spark has 'not been well studied'
	- They are able to create a 2.6x speedup with 2.4x energy efficiency improvement
- The paper conducts an in=depth analysis of challenges and solutions at several levels
	- Single thread, single node multithread, multinode
# 21. Terabyte Sort on FPGA-Accelerated Flash Storage
[10.1109/FCCM.2017.53](https://doi.org/10.1109/FCCM.2017.53)
School: MIT
- The paper examines the problem of sorting terabyte-scale datasets
- Typically, this is done by distributing the data and computation over a cluster of machines
	- This can be fast, but expensive and power hungry
- The solution proposed by this paper is based on flash storage connected to a group of FPGAs
	- These FPGAs contain sorting networks and merge trees
- This prototype has twice the power efficiency compared to the current recordholder
# 22. Emulating Mammalian Vision on Reconfigurable Hardware (Interesting)
[10.1109/FCCM.2012.33](https://doi.org/10.1109/FCCM.2012.33)
School: Penn State
- Machines with artificial vision must be able to process visual information as quickly and efficiently as the brain
- This paper identifies algorithms that model the process of attention and recognition in the mammal visual cortex
- The paper then presents an FPGA framework for generating systems that potentially emulate the visual cortex
- The paper makes comparisons against CPU, GPU, and FPGA implementations and shows high accuracy and speedup increases
# 23.  A Heterogeneous Architecture for Evaluating Real-Time One-Dimensional Computational Fluid Dynamics on FPGAs
[10.1109/FCCM.2012.31](https://doi.org/10.1109/FCCM.2012.31)
UC Berkeley
- 1D CFD isused to model the flow of fluid through a fuel pipe or any other pipe system
- The paper presents a novel framework to do this kind of calculation
- The interconnected pipes are partitioned into subvolumes tthat compute their parameters each step based on neighboring values
- The paper utilizes the reconfigurability of the FPGA to save hardware resources, rather than using it as an ASIC simulator
- No comparison against CPU/GPU, just against other FPGA implementations
# 24. Fast, Power-Efficient Biophotonic Simulations for Cancer Treatment Using FPGAs
 [10.1109/FCCM.2014.45](https://doi.org/10.1109/FCCM.2014.45)
 School: Toronto University
 - The Monte Carlo simulation of photon migration is the best method to capture tissue geometry through biphotonics
	 - Very costly algorithm
 - The paper presents the first hardware-accelerator for this task
 - Compares against a CPU for some reason
	 - Sees a 4x performance and 67x efficiency improvement
# 25. FPGA-based Acceleration for Tracking Audio Effects in Movies
[10.1109/FCCM.2012.24](https://doi.org/10.1109/FCCM.2012.24)
School: University of Piraeus, Greece
- This paper proposes an FPGA hardware platform for acceleration of audio tracking using an approach inspired by sequence alignmet
- Parallelizes the commonly used Smith-Waterson algorithm
	- Audio tracking in real time imposes stricter timing requirements than gene sequencing
- The implementation is compared agaist a 'software' implementation
# 26. Two-Hit Filter Synthesis for Genomic Database Search
[10.1109/FCCM.2016.24](https://doi.org/10.1109/FCCM.2016.24)
School: University of South Carolina
- The current search algorithm is NCBI BLAST, which transforms the query into a filter that is applied across the entire database
	- This introduces an I/O bandwidth bottleneck
- This paper proposes a variation of the algorithm that maps more suitably to FPGA implementation
- Transforms the database, instead of the query, into a filter stored as a hierarchical arrangement of three tables
- Speedups of up to 8X can be achieved when compared against NCBI BLAST
# 27. Architectures and Precision Analysis for Modelling Atmospheric Variables with Chaotic Behaviour
[10.1109/FCCM.2015.52](https://doi.org/10.1109/FCCM.2015.52)
Schools: 
	 - Imperial College of London
	 - Oxford
- Implement algorithmic improvements for atmospheric modeling to guide FPGA design
- 10% loss in accuracy, 13x speedup, 23x efficiency against a 6 core old ass Xeon
# 28. A Content Adapted FPGA Memory Architecture with Pattern Recognition Capability for L1 Track Triggering in the LHC Environment
[10.1109/FCCM.2016.52](https://doi.org/10.1109/FCCM.2016.52)
School: KIT, germany
- Compact Muon Solenoid Experiment at CERN produces an enormous amount of data every 25ns
	- The data rate is over 50Tbit/s
- The current implementation to handle this data is an ASIC with a content addressable mem architecture
- The FPGA implementation combines filtering and track finding
- There is more flexibility from the FGPA vs. ASIC
# 29. FPGA-Accelerated Decision Tree Classifier for Real-Time Supervision of Bluetooth SoC
[10.1109/ReConFig48160.2019.8994784](https://doi.org/10.1109/ReConFig48160.2019.8994784)
School: New Mexico State
- The paper proposes an FPGA-Accelerated supervisory system that classifies the operation of a bluetooth SoC
- The input supply current to the Trasceiver is monitored
- The FPGA implements a machine learning model to classify two different operation modes
- 97.4% accuracy
	- No other metrics, comparisons against GPU etc
# 30. FPGA-based Accurate Pedestrian Detection with Thermal Camera for Surveillance System
