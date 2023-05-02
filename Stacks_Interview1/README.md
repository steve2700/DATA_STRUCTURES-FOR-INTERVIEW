<h2You have an empty sequence, and you will be given  queries. Each query is one of these three types:</h3>

<h2 1 x  -Push the element x into the stack.</h3>
<h2 2    -Delete the element present at the top of the stack.<h/3>
<h1   3    -Print the maximum element in the stack.<h/2>
<h1 Function Description<h1/1

#Complete the getMax function in the editor below.

#getMax has the following parameters:
- string operations[n]: operations as strings

#Returns
- int[]: the answers to each type 3 query

Input Format

The first line of input contains an integer, . The next  lines each contain an above mentioned query.

Constraints

Constraints



All queries are valid.

Sample Input

STDIN   Function
-----   --------
10      operations[] size n = 10
1 97    operations = ['1 97', '2', '1 20', ....]
2
1 20
2
1 26
1 20
2
3
1 91
3
Sample Output

26
91
Language

