"""
Comparative Weights

Suppose you had n basketballs, all of them seemingly identical. You are
given a balance scale and told that one of the n balls is slightly
heavier than the others. What’s the fewest number of times you have to
use the scale to find the outlier? You can assume that the scale is
very large and able to fit all n balls on each side. Write a
scale_of_truth_n() function that takes in the number of basketballs and
determines the minimum number of weighs that you’ll need to find the
outlier.

For example, if you have 3 balls, you can compare 2 of them to see if
they are of equal weight. If they are, then you know the ball that you
didn’t weigh is the outlier. On the other hand, if they aren’t of equal
weight, then the heavier ball is the outlier. Therefore,
scale_of_truth_n(3) should return 1.

This challenge was reported to have been asked in interviews at many
top companies, including Microsoft. If you’ve covered the material in
Pass the Technical Interview with Python or an equivalent, you should
be able to solve this challenge. If you have trouble, try refreshing
your knowledge with its Algorithmic Complexity content.
"""


def scale_of_truth_n(n):
    """
    Return the minimum number of times you would need to weigh 'n'
    basketballs to find the one that is heavier than the others.
    """
    count = 0
    while n > 1:
        while n % 3 != 0:
            n += 1
            
        n //= 3
        count += 1

    return count


for i in range(29):
    print(f"{i}: {scale_of_truth_n(i)}")
