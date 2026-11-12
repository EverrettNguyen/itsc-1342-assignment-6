# [Everrett Nguyen] - Assignment 6 Unit Tests
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'code')))
from solution import filter_critical_scores

# Test 1: Standard threshold filter (strictly greater than default 70)
scores1 = [45, 70, 85, 92, 60]
# Remember: strictly greater than 70 means 70 is NOT included
assert filter_critical_scores(scores1) == [85, 92], "Failed Test 1: Check whether the threshold itself is included"

# Test 2: Custom threshold with values over 100 capped
scores2 = [50, 75, 105, 80]
assert filter_critical_scores(scores2, 75) == [100, 80], "Failed Test 2: Check value capping or threshold strictly greater"

# Test 3: No scores meet threshold
scores3 = [10, 20, 30]
# Look closely at the function call or expected list here:
assert filter_critical_scores(scores3, min_severity=70) == [], "Failed Test 3: Empty results check"

print("ALL UNIT TESTS PASSED - ASSIGNMENT 6")