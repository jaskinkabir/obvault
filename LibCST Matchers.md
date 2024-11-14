Based on [Working With Matchers](https://libcst.readthedocs.io/en/latest/matchers_tutorial.html) and [Matchers ](https://libcst.readthedocs.io/en/latest/matchers.html)
# Matchers:
Matchers are a way to ask if a particular LibCST node and its children match a particular **shape**. It is a much cleaner alternative to writing visitors that track attributes using the visit methods, or using manual `isinstance` checking while traversing a node's children. 

The LibCST library has matchers that correspond to each LibCST node in the documentation. Matchers default each of their attributes to the sentinel matcher [`DoNotCare()`](https://libcst.readthedocs.io/en/latest/matchers.html#libcst.matchers.DoNotCare "libcst.matchers.DoNotCare"). This means that matchers can be constructed around nodes with only the values of attributes of concern populated. The attributes set to DoNotCare() will not be compared against.

# Basic Matcher Usage
Consider a case where it must be known whether a Call node's arguments are all the literal True or False. Since Call.args is a sequence of Arg, and each Arg.value is a BaseExpression, it would be possible to loop over node.args and check `isinstance(arg.value, cst.name)` for each arg in the loop before finally checking if the value is true or false. 
```python
def is_call_with_booleans(node: cst.Call) -> bool:
    for arg in node.args:
        if not isinstance(arg.value, cst.Name):
            # This can't be the literal True/False, so bail early.
            return False
        if cst.ensure_type(arg.value, cst.Name).value not in ("True", "False"):
            # This is a Name node, but not the literal True/False, so bail.
            return False
    # We got here, so all arguments are literal boolean values.
    return True
```
**This sucks**

This can instead be implemented with a matcher. For each argument in the node's args list, call the `matchers.matches()` function with the assertion that `arg.value` should be a Name object with either "True" or "False" as its value.

```python
import libcst.matchers as m

def better_is_call_with_booleans(node: cst.Call) -> bool:
    for arg in node.args:
        if not m.matches(arg.value, m.Name("True") | m.Name("False")):
            # Oops, this isn't a True/False literal!
            return False
    # We got here, so all arguments are literal boolean values.
    return True
```
This is a lot better.

However there is even more room for improvement. This can be done with a single function call to `matchers.matches()`. We assert that the Call node matches the pattern of a Call node with `ZeroOrMore` arguments that match the pattern of a literal True or False:

```python
def best_is_call_with_booleans(node: cst.Call) -> bool:
    return m.matches(
        node,
        m.Call(
            args=(
                m.ZeroOrMore(m.Arg(m.Name("True") | m.Name("False"))),
            ),
        ),
    )
```

# Matcher Decorators
Consider the case where each boolean literal within a function call must be inverted. This can be done with a `CSTTransformer` that calls `matchers.matches()` on each `Call` node it visits. The following code checks if each call node it visits matches the pattern. If it does, it increments its internal flag to remember that it is currently walking a valid Call node and its children. 
Whenever it leaves a Call, it checks if it is a valid Call node, and then decrements the flag. Upon leaving each Name node, it first checks if it is walking a valid Call node. If it is, it will change any Name with a value of True to False and vice versa. The internal flag is to make sure that any calls within calls are accounted for and do not break the functionality. 

```python
class BoolInverter(cst.CSTTransformer):
    def __init__(self) -> None:
        self.in_call: int = 0

    def visit_Call(self, node: cst.Call) -> None:
        if m.matches(node, m.Call(args=(
            m.ZeroOrMore(m.Arg(m.Name("True") | m.Name("False"))),
        ))):
            self.in_call += 1

    def leave_Call(self, original_node: cst.Call, updated_node: cst.Call) -> cst.Call:
        if m.matches(original_node, m.Call(args=(
            m.ZeroOrMore(m.Arg(m.Name("True") | m.Name("False"))),
        ))):
            self.in_call -= 1
        return updated_node

    def leave_Name(self, original_node: cst.Name, updated_node: cst.Name) -> cst.Name:
        if self.in_call > 0:
            if updated_node.value == "True":
                return updated_node.with_changes(value="False")
            if updated_node.value == "False":
                return updated_node.with_changes(value="True")
        return updated_node
```
This works, but the class must keep track of where it is in the tree and duplicate the matching logic. This can be improved with matcher decorators. There is a decorator within the matchers module called `@matchers.call_if_inside()` that takes a matcher as an argument. We can call this decorator on our Name inverter function and never have to manually call the matcher check function. 

**Note that Matcher Decorators can only be used in Transformers that inherit from `matchers.MatcherDecoratableTransformer`**
```python
class BetterBoolInverter(m.MatcherDecoratableTransformer):
    @m.call_if_inside(m.Call(args=(
        m.ZeroOrMore(m.Arg(m.Name("True") | m.Name("False"))),
    )))
    def leave_Name(self, original_node: cst.Name, updated_node: cst.Name) -> cst.Name:
        if updated_node.value == "True":
            return updated_node.with_changes(value="False")
        if updated_node.value == "False":
            return updated_node.with_changes(value="True")
        return updated_node
```
While this is better, the leave_Name function still needs to check if the Name node matches the pattern of True or False. This can be handled by another matcher decorator called `@matchers.leave()`, which ensures that the function is only called when leaving a node that matches this matcher.
```python
class BetterBoolInverter(m.MatcherDecoratableTransformer):
    @m.call_if_inside(m.Call(args=(
        m.ZeroOrMore(m.Arg(m.Name("True") | m.Name("False"))),
    )))
    @m.leave(m.Name("True") | m.Name("False"))
    def leave_Name(self, original_node: cst.Name, updated_node: cst.Name) -> cst.Name:
        if updated_node.value == "True":
            return updated_node.with_changes(value="False")
        if updated_node.value == "False":
            return updated_node.with_changes(value="True")
```
Note that this only really creates a small performance increase and a slight improvement of readability.

Topic #LibCST