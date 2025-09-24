Based on [Scope Analysis](https://libcst.readthedocs.io/en/latest/scope_tutorial.html) and [Metadata](https://libcst.readthedocs.io/en/latest/metadata.html#libcst-metadata-position)

Continues [[LibCST Metadata]]
# !TODO
Write some code to figure out if the provider in the final example must be called before the transformer visits the module. If the metadata providers listed in the dependency declaration of a visitor/transformer are resolved before the visitor walks the tree, then the providers need not be resolved separately. This is important to figure out. 

# Scope Metadata
Scopes contain and separate variables from one another. They enforce that a local variable name bound within a function is available only within that function's scope

Python is function scoped, as opposed to block-scoped languages. New scopes are created for classes, functions, and comprehensions. Conditional statements, loops, try...except constructs are block-based, and thus do not create their own scopes.

There are five different types of scopes in Python
1. [`BuiltinScope`](https://libcst.readthedocs.io/en/latest/metadata.html#libcst.metadata.BuiltinScope "libcst.metadata.BuiltinScope")
	1. **This is important.** It allows us to recognize when a function call is built in vs. user-defined.
2. [`GlobalScope`](https://libcst.readthedocs.io/en/latest/metadata.html#libcst.metadata.GlobalScope "libcst.metadata.GlobalScope")
	1. The parent scope of the global scope is the global scope
3. [`ClassScope`](https://libcst.readthedocs.io/en/latest/metadata.html#libcst.metadata.ClassScope "libcst.metadata.ClassScope")
4. [`FunctionScope`](https://libcst.readthedocs.io/en/latest/metadata.html#libcst.metadata.FunctionScope "libcst.metadata.FunctionScope")
5. [`ComprehensionScope`](https://libcst.readthedocs.io/en/latest/metadata.html#libcst.metadata.ComprehensionScope "libcst.metadata.ComprehensionScope")
LibCST allows inspection of these scopes to see what local variables are assigned and accessed within.
## Scope Creation for Imports
Import statements bring new symbols into scope that are declared in other files. As such, they are represented by the `metadata.Assignment` class for scope analysis purposes. Dotted imports generate multiple Assignment objects, one for each module. Only the most specific access is recorded when analyzing references.

For example, the above `import a.b.c` statement generates three [`Assignment`](https://libcst.readthedocs.io/en/latest/metadata.html#libcst.metadata.Assignment "libcst.metadata.Assignment") objects: one for `a`, one for `a.b`, and one for `a.b.c`. A reference for `a.b.c` records an access only for the last assignment, while a reference for `a.d` only records an access for the [`Assignment`](https://libcst.readthedocs.io/en/latest/metadata.html#libcst.metadata.Assignment "libcst.metadata.Assignment") representing `a`.

The [`ScopeProvider`](https://libcst.readthedocs.io/en/latest/metadata.html#libcst.metadata.ScopeProvider "libcst.metadata.ScopeProvider") traverses a whole module and creates the scope inheritance structure.

# Scope Analysis
Consider the following example:
```python
import a, b, c as d, e as f  # expect to keep: a, c as d
from g import h, i, j as k, l as m  # expect to keep: h, j as k
from n import o  # expect to be removed entirely

a()

def fun():
    d()

class Cls:
    att = h.something

    def __new__(self) -> "Cls":
        var = k.method()
        func_undefined(var_undefined)
```

This code contains a couple unused imports such as `f, i, m, and n`. It also references an undefined function and variable. Scope analysis can recognize these errors.

## Warn on unused import or undefined reference.
First, we must apply the [`ScopeProvider`](https://libcst.readthedocs.io/en/latest/metadata.html#libcst.metadata.ScopeProvider "libcst.metadata.ScopeProvider") to a wrapper around a parsed module by calling its resolve method. Then we can iterate through the list of `assignments` of each scope. If the assignment has no [`references`](https://libcst.readthedocs.io/en/latest/metadata.html#libcst.metadata.BaseAssignment.references "libcst.metadata.BaseAssignment.references") then it is an unused assignment/import. Then we can iterate over the accesses. If an access has no [`referents`](https://libcst.readthedocs.io/en/latest/metadata.html#libcst.metadata.Access.referents "libcst.metadata.Access.referents"), it means the access is an undefined reference. 

The following code prints warnings about each unused import or undefined reference. Note that the wrapper.resolve() method is called for each type of metadata we need to access.
```python
from collections import defaultdict
from typing import Dict, Union, Set

unused_imports: Dict[Union[cst.Import, cst.ImportFrom], Set[str]] = defaultdict(set)
undefined_references: Dict[cst.CSTNode, Set[str]] = defaultdict(set)
ranges = wrapper.resolve(cst.metadata.PositionProvider)
for scope in scopes:
    for assignment in scope.assignments:
        node = assignment.node
        if isinstance(assignment, cst.metadata.Assignment) and isinstance(
            node, (cst.Import, cst.ImportFrom)
        ):
            if len(assignment.references) == 0:
                unused_imports[node].add(assignment.name)
                location = ranges[node].start
                print(
                    f"Warning on line {location.line:2d}, column {location.column:2d}: Imported name `{assignment.name}` is unused."
                )

    for access in scope.accesses:
        if len(access.referents) == 0:
            node = access.node
            location = ranges[node].start
            print(
                f"Warning on line {location.line:2d}, column {location.column:2d}: Name reference `{node.value}` is not defined."
            )
```
## Automatically Remove Unused Imports:
By calling the wrapper's resolve function above, we have created a dictionary that maps from an unused import statement to the name of that unused module

This can be reused to automatically remove the unused imports by subclassing [`CSTTransformer`](https://libcst.readthedocs.io/en/latest/visitors.html#libcst.CSTTransformer "libcst.CSTTransformer"). To modify the import statements, we will override the `leave_Import` and `leave_ImportFrom` methods, as those two types of Import statements call different methods of the visitor/transformer. Remember that semantic differences like this are easy to miss, but extremely important to keep in mind in a project like this. Since the functionality need not be different for either type of statement, we can have both overridden methods call the same method. 

The following code shows this class implementation:
For each import statement that was not flagged by the unused import flagging function above, the transformer will scan through all of the module names imported by the statement and marks the ones that do not appear in the unused_imports map. The rest are removed from the statement and returned to the tree.
```python
class RemoveUnusedImportTransformer(cst.CSTTransformer):
    def __init__(
        self, unused_imports: Dict[Union[cst.Import, cst.ImportFrom], Set[str]]
    ) -> None:
        self.unused_imports = unused_imports

    def leave_import_alike(
        self,
        original_node: Union[cst.Import, cst.ImportFrom],
        updated_node: Union[cst.Import, cst.ImportFrom],
    ) -> Union[cst.Import, cst.ImportFrom, cst.RemovalSentinel]:
        if original_node not in self.unused_imports:
            return updated_node
        names_to_keep = []
        for name in updated_node.names:
            asname = name.asname
            if asname is not None:
                name_value = asname.name.value
            else:
                name_value = name.name.value
            if name_value not in self.unused_imports[original_node]:
                names_to_keep.append(name.with_changes(comma=cst.MaybeSentinel.DEFAULT))
        if len(names_to_keep) == 0:
            return cst.RemoveFromParent()
        else:
            return updated_node.with_changes(names=names_to_keep)

    def leave_Import(
        self, original_node: cst.Import, updated_node: cst.Import
    ) -> cst.Import:
        return self.leave_import_alike(original_node, updated_node)

    def leave_ImportFrom(
        self, original_node: cst.ImportFrom, updated_node: cst.ImportFrom
    ) -> cst.ImportFrom:
        return self.leave_import_alike(original_node, updated_node)
```

Note that import and fromimport nodes can have `ImportAlias`es in their names lists. This is to handle stuff like `from a import b as c`. This means that the function must initially check if an alias exists, and then the name_value being examined must be assigned to the true name of the module.

Additionally, if the module is not an unused import, its name is sent to the list of used names with the change `(comma=cst.MaybeSentinel.DEFAULT` to make sure the proper comma format is preserved

If there are no used imports in the entire statement, then the `cst.RemoveFromParent()` function is called to generate a `cst.RemovalSentinel`.

So you can see that 

Topic #LibCST
