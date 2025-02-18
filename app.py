import streamlit as st

# Title of the app
st.title("Computer Organization & Design Quiz")
st.write("Test your understanding of CPU design, MIPS datapath, and control signals!")

# Initialize session state variables if they don’t exist
if "score" not in st.session_state:
    st.session_state.score = 0

if "question_index" not in st.session_state:
    st.session_state.question_index = 0

if "answer_submitted" not in st.session_state:
    st.session_state.answer_submitted = False

# Questions and answers
quiz = [
    # CPU Basics
    {"question": "Which of the following is NOT a CPU performance factor?",
     "options": ["Instruction count", "CPI", "Clock speed", "Cache size"],
     "answer": "Cache size"},

    {"question": "What determines the instruction count of a program?",
     "options": ["Compiler and ISA", "CPU hardware", "Cache memory", "Bus architecture"],
     "answer": "Compiler and ISA"},

    {"question": "Which of the following is NOT a component of a CPU?",
     "options": ["Registers", "ALU", "Cache", "Hard drive"],
     "answer": "Hard drive"},

    {"question": "What is the function of the Control Unit?",
     "options": ["Performs arithmetic operations", "Manages instruction execution", "Stores data", "Manages cache memory"],
     "answer": "Manages instruction execution"},

    {"question": "What does the ALU do?",
     "options": ["Controls instruction flow", "Performs arithmetic and logic operations", "Fetches instructions", "Manages memory"],
     "answer": "Performs arithmetic and logic operations"},

    # Instruction Execution
    {"question": "How many stages are in the MIPS instruction execution cycle?",
     "options": ["2", "3", "5", "7"],
     "answer": "5"},

    {"question": "What is the first stage of instruction execution?",
     "options": ["Decode", "Execute", "Write-back", "Fetch"],
     "answer": "Fetch"},

    {"question": "What happens during the decode stage?",
     "options": ["ALU processes data", "Registers fetch values", "Instruction is broken into opcode and operands", "Instruction writes results to memory"],
     "answer": "Instruction is broken into opcode and operands"},

    {"question": "Which instruction type performs arithmetic operations?",
     "options": ["R-type", "I-type", "J-type", "Branch"],
     "answer": "R-type"},

    {"question": "Which instruction type is used for memory access?",
     "options": ["R-type", "I-type", "J-type", "Branch"],
     "answer": "I-type"},

    # Datapath
    {"question": "Which component stores temporary data in a CPU?",
     "options": ["Memory", "Registers", "ALU", "Cache"],
     "answer": "Registers"},

    {"question": "What is the role of multiplexers in a datapath?",
     "options": ["Execute instructions", "Store data", "Select between different inputs", "Fetch data from memory"],
     "answer": "Select between different inputs"},

    {"question": "Which component increments the Program Counter?",
     "options": ["Registers", "ALU", "Control Unit", "Instruction Memory"],
     "answer": "ALU"},

    {"question": "What is the role of the Memory Data Register (MDR)?",
     "options": ["Fetch instructions", "Hold data from memory", "Control instruction execution", "Store arithmetic results"],
     "answer": "Hold data from memory"},

    {"question": "How is the Program Counter updated in a jump instruction?",
     "options": ["PC is incremented by 1", "PC is updated with an address", "PC remains unchanged", "PC is decremented"],
     "answer": "PC is updated with an address"},

    # Control Signals
    {"question": "What does the 'RegWrite' signal control?",
     "options": ["Determines register destination", "Enables/disables register writing", "Controls ALU operations", "Manages memory access"],
     "answer": "Enables/disables register writing"},

    {"question": "Which control signal activates memory read operations?",
     "options": ["MemWrite", "MemRead", "ALUOp", "RegWrite"],
     "answer": "MemRead"},

    {"question": "What determines ALU behavior?",
     "options": ["Opcode", "Clock speed", "Memory size", "Bus width"],
     "answer": "Opcode"},

    {"question": "What does the 'Zero' signal indicate in ALU operations?",
     "options": ["Arithmetic overflow", "Equality of operands", "Control unit error", "Instruction completion"],
     "answer": "Equality of operands"},

    {"question": "What is the function of the ALUOp signal?",
     "options": ["Fetches data", "Selects ALU operation", "Controls memory access", "Manages cache"],
     "answer": "Selects ALU operation"},

    # ALU Operations
    {"question": "Which ALU control signal is used for subtraction?",
     "options": ["0000", "0010", "0110", "1001"],
     "answer": "0110"},

    {"question": "Which ALU operation is performed when the control signal is '0000'?",
     "options": ["Addition", "AND", "Subtraction", "OR"],
     "answer": "AND"},

    {"question": "What operation does the ALU perform in branch comparison?",
     "options": ["Addition", "Multiplication", "Subtraction", "Bitwise OR"],
     "answer": "Subtraction"},

    # Performance and Optimization
    {"question": "What is the main factor limiting CPU clock speed?",
     "options": ["Cache size", "Longest delay path", "Instruction count", "ALU operations"],
     "answer": "Longest delay path"},

    {"question": "What is the purpose of pipelining?",
     "options": ["Increase ALU speed", "Process multiple instructions simultaneously", "Reduce instruction count", "Increase memory size"],
     "answer": "Process multiple instructions simultaneously"},

    {"question": "Which stage in pipelining is most affected by a branch instruction?",
     "options": ["Fetch", "Decode", "Execute", "Write-back"],
     "answer": "Fetch"},

    {"question": "What is a pipeline hazard?",
     "options": ["An incorrect ALU result", "A delay in instruction execution", "A memory overflow", "A broken control signal"],
     "answer": "A delay in instruction execution"},

    {"question": "How does forwarding improve pipelining?",
     "options": ["Prevents clock delays", "Reduces register dependencies", "Minimizes instruction count", "Increases memory access speed"],
     "answer": "Reduces register dependencies"},

    {"question": "Which hazard occurs when an instruction depends on the result of a previous instruction?",
     "options": ["Structural", "Data", "Control", "Memory"],
     "answer": "Data"},

    {"question": "What technique is used to predict branch outcomes?",
     "options": ["Instruction pipelining", "Branch prediction", "Multiplexing", "Forwarding"],
     "answer": "Branch prediction"},

    {"question": "What is the biggest advantage of pipelining?",
     "options": ["Reduces ALU size", "Increases instruction throughput", "Eliminates memory stalls", "Reduces CPU power consumption"],
     "answer": "Increases instruction throughput"},

    {"question": "What is the impact of increasing CPI?",
     "options": ["Improves CPU efficiency", "Slows down instruction execution", "Reduces power consumption", "Improves memory access"],
     "answer": "Slows down instruction execution"},
]

# Display the current question
current_question = quiz[st.session_state.question_index]
st.write(f"**Question {st.session_state.question_index + 1}: {current_question['question']}**")

# Multiple-choice options
selected_option = st.radio("Select your answer:", current_question["options"], key=f"question_{st.session_state.question_index}")

# Submit button to evaluate the selected answer
if st.button("Submit Answer") and not st.session_state.answer_submitted:
    if selected_option == current_question["answer"]:
        st.success("Correct!")
        st.session_state.score += 1
    else:
        st.error(f"Incorrect. The correct answer is: {current_question['answer']}")
    st.session_state.answer_submitted = True

# Next button (enabled only after an answer is submitted)
if st.session_state.answer_submitted:
    if st.button("Next Question"):
        if st.session_state.question_index < len(quiz) - 1:
            st.session_state.question_index += 1
            st.session_state.answer_submitted = False
            # Force rerun to display the next question immediately
            st.rerun()
        else:
            st.write("### Quiz Completed!")
            st.write(f"Your final score is {st.session_state.score}/{len(quiz)}")
            st.session_state.question_index = 0
            st.session_state.score = 0
            st.session_state.answer_submitted = False

st.write(f"**Current Score:** {st.session_state.score}")