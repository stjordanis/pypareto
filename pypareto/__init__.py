from .pypareto import (
    Cmp,
    Comparison,
    ComparisonChain,
    Domination,
    MaxMin,
    MaxMinList,
    by_none,
    by_value,
    cmp_to_target,
    dominates,
    GroupNones)

__doc__ = """
# pypareto
Pypareto is a Python library for pareto front seaching.
## Usage
""" + ComparisonChain.split_by_pareto.__doc__

__all__ = [
    'Cmp',
    'Comparison',
    'GroupNones',
    'ComparisonChain',
    'Domination',
    'MaxMin',
    'MaxMinList',
    'by_none',
    'by_value',
    'cmp_to_target',
    'dominates',
    'DominanceMatrix']