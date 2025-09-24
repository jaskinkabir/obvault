Based on [Working with metadata](https://libcst.readthedocs.io/en/latest/metadata_tutorial.html#Working-with-Metadata) and [Metadata](https://libcst.readthedocs.io/en/latest/metadata.html#libcst-metadata-position)

Continued by [[LibCST Scope Analysis]]
# Usefulness
From what I understand, this would be useful for marking the function definition node that any call node points to. 
# Metadata
Nodes in the tree all have metadata. For example, they'll have line numbers and column numbers, parent nodes, etc. This is handled in the library in a wacky way to preserve the immutability of the tree. This interface is designed to be declarative and type safe.
# Providing Metadata
Visitors can gather metadata from a tree, but the provider interface allows for dependency declaration to be used to automatically run these providers in other visitors. It also provides type safety. 
Most providers should extend from `BatchableMetadataProvider`

This example marks `Name` nodes that are function parameters
```python
import libcst as cst

class IsParamProvider(cst.BatchableMetadataProvider[bool]):
    """
    Marks Name nodes found as a parameter to a function.
    """
    def __init__(self) -> None:
        super().__init__()
        self.is_param = False

    def visit_Param(self, node: cst.Param) -> None:
        # Mark the child Name node as a parameter
        self.set_metadata(node.name, True)

    def visit_Name(self, node: cst.Name) -> None:
        # Mark all other Name nodes as not parameters
        if not self.get_metadata(type(self), node, False):
            self.set_metadata(node, False)
```

# Accessing Metadata
The two ways to work with providers given by the metadata interface is by resolving methods provided by `MetadataWrapper` and through declaring metadata dependencies on a visitor or transformer

## Using the `MetadataWrapper`
The `MetadataWrapper` is a wrapper around a `Module` that stores its associated metadata. When a wrapper is constructed around a module, it stores a deep copy of the original module, which means `MetadataWrapper(module).module == module` is `False`. This copying ensures a node with a given identity will never appear twice in the same tree. This means metadata for a node can be looked up based on a node's unique identity.

If it is known that there are no duplicate nodes in the tree (eg if the module came from the parser,), then a small performance benefit can be had by setting the `unsafe_skip_copy` argument to `True`

To use this method, instantiate the wrapper, and call its resolve function and pass the provider class to it. The resolve function will return a map from node to the metadata value. For example:
```python
module = cst.parse_module("x")
wrapper = cst.MetadataWrapper(module)

isparam = wrapper.resolve(IsParamProvider)
x_name_node = wrapper.module.body[0].body[0].value

print(isparam[x_name_node])  # should print False
```
## Using Dependency Declaration
Visitors and Transformers can declare a tuple of `METADATA_DEPENDENCIES` as a class variable. For a visitor or transformer to utilize these provided metadata dependency providers, the visit function must be called from a metadata wrapper formed around a module. You cannot call the module's visit function

```Python
from libcst.metadata import PositionProvider

class ParamPrinter(cst.CSTVisitor):
    METADATA_DEPENDENCIES = (IsParamProvider, PositionProvider,)

    def visit_Name(self, node: cst.Name) -> None:
        # Only print out names that are parameters
        if self.get_metadata(IsParamProvider, node):
            pos = self.get_metadata(PositionProvider, node).start
            print(f"{node.value} found at line {pos.line}, column {pos.column}")

module = cst.parse_module("def foo(x):\n    y = 1\n    return x + y")
wrapper = cst.MetadataWrapper(module)
result = wrapper.visit(ParamPrinter())  # NB: wrapper.visit not module.visit
```










Topic #LibCST