"""LOG PROCESSOR V4.7

Instructions:

Your time starts as soon as the you (the candidate) joins the pad.
Do all work inside the pad.
Your work will be graded at the 90 minute mark.
The pad will not exit itself. You should exit the pad when you are done by closing the browser tab.

You may solve in any language unless instructed otherwise, the examples are given in python3.7.
If you use another language, you don't have to re-implement all the examples, classes, tests, etc,
 just implement the four questions.
Marking focuses on the implementation of the functions, not the boilerplate.
You can also change the function signatures and data types to whatever is more appropriate for your
 language but avoid changing the given function signatures if you are using Python.
Some examples are available for other languages at the very bottom of this page.

You can use books, Google, Stack Overflow, etc, but don't ask for help from other people.
You may add helper functions and global variables to assist you.

Outline:

You are developing a log processing system, which manipulates text logs from various applications.
The system is made up of many different "steps" that process the log in different ways.
Each step is declared in advance and the system is built up by feeding the output
 of one step into the inputs of other steps.
Each step has a python function (stored in the "action" attribute) that gets
 evaluated to produce the output for that step.
The user tells the system they want the output of a particular step,
 and the system will call the action for that step (and any other actions that
 the desired step depends on) to return the processed log.

Each step is given an "output_name" attribute, which the user can use to get the output of that
 step.
The "input_names" attribute stores a list of strings that match the output_name from other steps
 so that the output value from one step can be used as an input parameter to other steps.

Read further to see examples of the system in action and begin Questions 1-4.

"""
from typing import List, Callable, Any

# typedef for logdata, just for clarity, since we use strings elsewhere
logdata = str


# action functions
def action_get_logs1(inputs: List[logdata]) -> logdata:
    return "this_is_a_log"


def action_get_logs2(inputs: List[logdata]) -> logdata:
    return "yet_another_log"


def action_combine_logs(inputs: List[logdata]) -> logdata:
    return " ".join(inputs)


def action_combine_logs_flipped(inputs: List[logdata]) -> logdata:
    return " ".join(reversed(inputs))


class StepDeclaration:
    def __init__(self, output_name: str, input_names: List[str], action: Callable):
        self.output_name = output_name
        self.input_names = input_names
        self.action = action


# an example of a system of step declarations for processing logs
example_system_1 = [
    StepDeclaration(
        output_name="output1",  # output_name could be any string
        input_names=[],
        action=action_get_logs1,  # action can be any python callable
    ),
    StepDeclaration(
        output_name="output2",
        input_names=[],
        action=action_get_logs2,
    ),
    StepDeclaration(
        output_name="output3",
        input_names=["output1", "output2"],
        # each "input_names" item corresponds to an "output_name" from another StepDeclaration.
        action=action_combine_logs,
        # when this action function is called, the parameters to "action_combine_logs()" will be the return values from the action functions "action_get_logs1()" and "action_get_logs2()"
    ),
    StepDeclaration(
        output_name="output4",
        input_names=["output3", "output2"],
        action=action_combine_logs_flipped,
    ),
]

"""
QUESTION 1:
In example_system_1, the step for "output3" takes inputs from the steps for "output1" and "output2".
Thus, if the user requests "output3", we must first evaluate the actions for "output2" and "output1"
 to get the values of these outputs so the values can be used as inputs to the action of "output3".

To determine the correct ordering of step dependencies, complete the action_evaluation_order()
 function below so that it will return a list of "output_name"s needed for the
 "order_for_output_name" parameter.
Each "output_name" item in the list should appear *after* any of its dependencies.
The ordering should not contain any duplicates.

You may assume every list of "StepDeclarations" is valid and solvable:
- each "StepDeclaration" will only have one output
- each "StepDeclaration" can have any number of inputs (including 0)
- a list of StepDeclarations will not contain duplicate "output_name"s
- a "StepDeclaration" cannot depend on its own output (directly or indirectly)

For this and the following questions assume the system is running at a large scale;
 efficiency is important.
That said, correct slow solutions will get more marks than incorrect fast ones.
You may also leave notes explaining tradeoffs between speed/space/implementation complexity
"""

# Creating a graph adjacency list
graph_adj_list = {}


def action_evaluation_order(step_declarations: List[StepDeclaration], order_for_output_name: str) -> List[str]:
    global graph_adj_list

    # Updating the graph adjacency list
    for node in step_declarations:
        graph_adj_list[node["output_name"]] = node["input_names"]

    # We need to implement topological sort of graph to solve this issue
    # Graph Topological Sort
    visited = [False for i in range(len(graph_adj_list))]
    result = []

    def DFS(node):
        if visited[node]:
            return
        visited[node] = True
        for adj in graph_adj_list[node]:
            DFS(adj)
        result.append(node)

    DFS(order_for_output_name)

    return result


print("Running Q1...")
order = action_evaluation_order(step_declarations=example_system_1, order_for_output_name="output1")
assert order == ["output1"], "Question 1a Error"

order = action_evaluation_order(step_declarations=example_system_1, order_for_output_name="output2")
assert order == ["output2"], "Question 1b Error"

order = action_evaluation_order(step_declarations=example_system_1, order_for_output_name="output3")
# order should be a list of strings which are in the following order
assert order in (
    ["output1", "output2", "output3"],
    ["output2", "output1", "output3"],
), "Question 1c Error"  # there are multiple valid orders for "output3"

order = action_evaluation_order(step_declarations=example_system_1, order_for_output_name="output4")
assert order in (
    ["output1", "output2", "output3", "output4"],
    ["output2", "output1", "output3", "output4"],
), "Question 1d Error"  # there are multiple valid orders for "output4"
print("Q1 OK")

"""
QUESTION 2:
Now that we know the order in which the actions have to be evaluated, complete the
 get_output_value() function below.
It must call each "action" in the correct order with the right input(s) and return the output value
 of the "action" function for the StepDeclaration where the output_name attribute
 matches the "output_name" parameter.

Hint: You can use your previous work if desired.

for example_system_1, the get_output_value(example_system_1, "output3") function will do
 the following:
1) call action_get_logs1() and store the output
2) call action_get_logs2() and store the output
3) call action_combine_logs() with the output from 1) and 2) as the input
4) return the result of 3) as the "value_for_output_name" parameter matches the
    StepDeclaration.output_name for that step
Note: as in Question 1, step 1) and 2) could happen in the reverse order.
"""


def solve(ouptut):


def get_output_value(step_declarations: List[StepDeclaration], value_for_output_name: str) -> logdata:
    """
        Candidate to implement.

        Parses the "step_declarations" parameter to call the appropriate             "actions" in the correct order.

        The input(s) to each "action" are outputs of previous "actions".

        Return the output value of the action corresponding to the                   "output_name".
    """
    for item in step_declarations:
        output = action_evaluation_order(step_declarations=step_declarations, order_for_output_name=item["input_names"])
        item["output_name"] = action_combine_logs(inputs=output)
        return item["output_name"]


print("Running Q2...")
out1 = get_output_value(step_declarations=example_system_1, value_for_output_name="output1")
assert out1 == "this_is_a_log", "Question 2a Error"

out3 = get_output_value(step_declarations=example_system_1, value_for_output_name="output3")
assert out3 == "this_is_a_log yet_another_log", "Question 2b Error"

out4 = get_output_value(step_declarations=example_system_1, value_for_output_name="output4")
assert out4 == "yet_another_log this_is_a_log yet_another_log", "Question 2c Error"
print("Q2 OK")

"""
QUESTION 3:
Our users will be calling the "get_output_value()" function frequently
 with varying "step_declarations" and "value_for_output_name"s.
As some of the "actions" might be expensive to call we should cache the output of "action" calls.
That way if an "action" is called multiple times *with the same input values*
 the output value can be reused without recomputing.
An "action" function may be used in many "StepDeclarations" within one system or within different
 systems sharing a cache.

"actions" are typically pure functions, where the output value of each function only
 changes if the input changes. In a real system, some inputs are external data
 (e.g. a text log on a file system) rather than strings like the examples given.

The `StepDeclaration` class has been updated with a `can_be_cached` attribute for Question 3 to
 show this.

Implement get_output_value_with_caching() below to use the global "cache" variable.
"""


class StepDeclaration:
    def __init__(self, output_name: str, input_names: List[str], action: Callable, can_be_cached: bool = False):
        self.output_name = output_name
        self.input_names = input_names
        self.action = action
        self.can_be_cached = can_be_cached


FILE_INDEX_READ_LAST = 0


def action_read_from_filesystem(inputs: List[logdata]) -> logdata:
    """Toggle between 2 files."""
    files_contents = ["file_contents_1", "file_contents_2"]
    global FILE_INDEX_READ_LAST
    FILE_INDEX_READ_LAST += 1
    FILE_INDEX_READ_LAST %= len(files_contents)
    return files_contents[FILE_INDEX_READ_LAST]


example_system_3 = [
    StepDeclaration(
        output_name="fixed_log",
        input_names=[],
        action=action_get_logs1,
        can_be_cached=False,
    ),
    StepDeclaration(
        output_name="filesystem_log",
        input_names=[],
        action=action_read_from_filesystem,
        can_be_cached=False,
    ),
    StepDeclaration(
        output_name="system_3_output",
        input_names=["filesystem_log", "fixed_log"],
        action=action_combine_logs,
        can_be_cached=True,
    ),
]

cache = {}  # use this variable as your cache


def get_output_value_with_caching(step_declarations: List[StepDeclaration], value_for_output_name: str) -> logdata:
    """Candidate to implement."""


print("Running Q3...")
# cache is empty to start
get_output_value_with_caching(step_declarations=example_system_3, value_for_output_name="system_3_output")
# values added to the cache during the call above, all 3 action functions should be called
get_output_value_with_caching(step_declarations=example_system_3, value_for_output_name="system_3_output")
# need to run again because action_read_from_filesystem() toggles between 2 files
# values added to the cache during the call above, all 3 action functions should be called

get_output_value_with_caching(step_declarations=example_system_3, value_for_output_name="system_3_output")
# the 2 StepDeclaration with can_be_cached=False should be called
# the 3rd with action function `action_combine_logs` should not be called, the result should be in the cache

"""
QUESTION 4:
Another performance upgrade would be to add concurrency/parallelism
 where possible to increase the performance of the system.
An example of parallelism in example_system_1: a single-threaded system
 will wait for the result of action_get_logs1() before calling action_get_logs2() (or vice versa).
These functions are independent of each other and could be executed in parallel to
 speed up the system.

Complete the "get_output_value_with_parallelism" below, using concurrency/parallelism
 *anywhere possible* to increase the performance of the system.

Your selection of parallelism primitive or library does not affect your score
 (e.g. you may use multithreading, multiprocessing, asyncio, etc)

You can assume that there is no performance overhead for additional workers
 (e.g. you have unlimited CPUs) and that all action functions are IO-bound.
You do not have to carry over your caching implementation from Question 3.

Extra for experts: limit the number of CPU cores you have to N and assume each action can utilize
 a fixed number of CPUs from 1 to N. Then schedule parallel actions such that CPU cores
 are optimally utilized but not oversaturated.
"""
import multiprocessing

print("Running Q4...")


def get_output_value_with_parallelism(step_declarations: List[StepDeclaration], value_for_output_name: str) -> logdata:
    for item in step_declarations:
        action_evaluation_order(step_declarations=step_declarations, order_for_output_name=item["input_names"])
        count = 1
        while output:
            pname = "p{}".format(count)
            pname = multiprocessing.Process(action_combine_logs(inputs=[output.pop(), output.pop()]))
            output.append(pname)
            count += 1

        return item["output_name"]


"""
*** OTHER LANGAUGE EXAMPLES ***

*** Java (11) ***
// functions are not first-class objects in java
// but we can use lambdas and interfaces instead.
import java.io.*;
import java.util.*;

interface ActionFunction {
    public String run(List<String> inputs);
}

class Step {
    public String output;
    public List<String> inputs;
    public ActionFunction action;
    public Step(String out, List<String> in, ActionFunction a) {
        inputs = in;
        output = out;
        action = a;
    }
}

class Solution {
  public static void main(String[] args) {

    ActionFunction joiner = (inputs) -> {
      return String.join(" ", inputs);
    };

    Step a_step = new Step(
      "output",
      List.of("input1", "input2"),
      joiner
    );

    var out = a_step.action.run(List.of("this_is_a_log", "another_log"));
    System.out.println(out);
  }
}

*** Rust ***
/// fairly straight forward.
/// however note the extra parentheses here around the
/// "action" member of the step struct to call the
/// function properly.

// typedef for clarity
type LogData = String;

fn action_get_logs1(inputs: Vec<LogData>) -> LogData {
    "this_is_a_log".to_string()
}

fn action_get_logs2(inputs: Vec<LogData>) -> LogData {
    "yet_another_log".to_string()
}

fn action_combine_logs(inputs: Vec<LogData>) -> LogData {
    inputs.join(" ")
}

fn action_combine_logs_flipped(inputs: Vec<LogData>) -> LogData {
    inputs.reverse();
    inputs.join(" ")
}

type Action = fn(Vec<String>) -> String;

pub struct Step {
    output_name: String,
    input_names: Vec<String>,
    action: Action,
}

let example_system_1 = vec![
    StepDeclaration {
        output_name: "output1",
        input_names: vec![],
        action: action_get_logs1,
    },
    StepDeclaration {
        output_name: "output2",
        input_names: vec![],
        action: action_get_logs2,
    },
    StepDeclaration {
        output_name: "output3",
        input_names: vec!["output1".to_string(), "output2".to_string()],
        action: action_combine_logs,
    },
    StepDeclaration {
        output_name: "output4",
        input_names: vec!["output3".to_string(), "output2".to_string()],
        action: action_combine_logs_flipped,
    },
]

fn main() {
    let a_step = Step {
        input_names: vec![
            "in1".to_string(),
            "in2".to_string(),
        ],
        output_name: "out1".to_string(),
        action: action_join,
    };

    // note the extra parentheses here around the struct member.
    let result = (a_step.action)(vec![
        "lifetimes".to_string(),
        "are".to_string(),
        "fun".to_string(),
    ]);

    println!("{}", result);
}

"""
