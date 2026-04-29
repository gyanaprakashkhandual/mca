from reportlab.lib.pagesizes import A4 # pyright: ignore[reportMissingModuleSource]
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, PageBreak # pyright: ignore[reportMissingModuleSource]
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle # pyright: ignore[reportMissingModuleSource]
from reportlab.lib.units import inch # pyright: ignore[reportMissingModuleSource]
from reportlab.lib import colors # pyright: ignore[reportMissingModuleSource]
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY # pyright: ignore[reportMissingModuleSource]

def make_styles():
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle('CustomTitle', parent=styles['Title'],
        fontSize=16, fontName='Helvetica-Bold', alignment=TA_CENTER,
        spaceAfter=6, textColor=colors.HexColor('#1a1a6e'))
    
    subtitle_style = ParagraphStyle('Subtitle', parent=styles['Normal'],
        fontSize=11, fontName='Helvetica-Bold', alignment=TA_CENTER,
        spaceAfter=4, textColor=colors.HexColor('#1a1a6e'))
    
    info_style = ParagraphStyle('Info', parent=styles['Normal'],
        fontSize=10, fontName='Helvetica', alignment=TA_CENTER,
        spaceAfter=3, textColor=colors.HexColor('#333333'))
    
    course_header_style = ParagraphStyle('CourseHeader', parent=styles['Normal'],
        fontSize=13, fontName='Helvetica-Bold', alignment=TA_LEFT,
        spaceBefore=14, spaceAfter=4, textColor=colors.HexColor('#1a1a6e'),
        borderPad=4)
    
    q_style = ParagraphStyle('Question', parent=styles['Normal'],
        fontSize=10.5, fontName='Helvetica-Bold', alignment=TA_LEFT,
        spaceBefore=10, spaceAfter=3, textColor=colors.HexColor('#8B0000'))
    
    ans_style = ParagraphStyle('Answer', parent=styles['Normal'],
        fontSize=10, fontName='Helvetica', alignment=TA_JUSTIFY,
        spaceBefore=3, spaceAfter=4, leading=15)
    
    sub_q_style = ParagraphStyle('SubQ', parent=styles['Normal'],
        fontSize=10, fontName='Helvetica-Bold', alignment=TA_LEFT,
        spaceBefore=6, spaceAfter=2, textColor=colors.HexColor('#444444'))
    
    return title_style, subtitle_style, info_style, course_header_style, q_style, ans_style, sub_q_style

def build_2021():
    doc = SimpleDocTemplate(
        "Answers_2021_MCA_NEW_Sem1.pdf",
        pagesize=A4,
        rightMargin=55, leftMargin=55, topMargin=60, bottomMargin=55
    )
    
    title_s, subtitle_s, info_s, course_h_s, q_s, ans_s, sub_q_s = make_styles()
    story = []
    
    # Cover / Header
    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("INDIRA GANDHI NATIONAL OPEN UNIVERSITY", title_s))
    story.append(Paragraph("School of Computer and Information Sciences", subtitle_s))
    story.append(Spacer(1, 0.1*inch))
    story.append(HRFlowable(width="100%", thickness=2, color=colors.HexColor('#1a1a6e')))
    story.append(Spacer(1, 0.08*inch))
    story.append(Paragraph("MASTER OF COMPUTER APPLICATIONS (MCA_NEW)", subtitle_s))
    story.append(Paragraph("Semester-I Assignment Answers", subtitle_s))
    story.append(Paragraph("Session: January 2021 &amp; July 2021", info_s))
    story.append(Spacer(1, 0.08*inch))
    story.append(HRFlowable(width="100%", thickness=2, color=colors.HexColor('#1a1a6e')))
    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph("Courses Covered: MCS-211 | MCS-212 | MCS-213 | MCS-214 | MCS-215 | MCSL-216 | MCSL-217", info_s))
    story.append(Spacer(1, 0.3*inch))

    # ====================== MCS-211 ======================
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#1a1a6e')))
    story.append(Paragraph("MCS-211: Design and Analysis of Algorithms", course_h_s))
    story.append(Paragraph("Assignment Number: MCA(1)/211/Assign/21 | Maximum Marks: 100 | Weightage: 30%", info_s))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#cccccc')))
    story.append(Spacer(1, 0.1*inch))

    story.append(Paragraph("Q1(a): Brute Force and Horner's Algorithm for Polynomial Evaluation", q_s))
    story.append(Paragraph(
        "<b>Brute Force Method:</b> In the brute force approach, each term a<sub>i</sub>x<super>i</super> is computed independently. "
        "For a polynomial of degree n, computing x<super>i</super> requires i multiplications, so total multiplications = 0+1+2+...+n = n(n+1)/2 = O(n<super>2</super>). "
        "Addition operations = n. So total complexity is <b>O(n<super>2</super>)</b>.", ans_s))
    story.append(Paragraph(
        "<b>Horner's Rule / Algorithm:</b> Horner's rule rewrites the polynomial as nested multiplications: "
        "P(x) = a0 + x(a1 + x(a2 + ... + x(an-1 + x*an)...)). "
        "This requires exactly n multiplications and n additions, giving time complexity <b>O(n)</b> — much better than brute force.", ans_s))
    story.append(Paragraph("Pseudocode for Horner's Rule:", sub_q_s))
    story.append(Paragraph(
        "HORNER(a[], n, x):<br/>"
        "    result = a[n]<br/>"
        "    for i = n-1 downto 0:<br/>"
        "        result = result * x + a[i]<br/>"
        "    return result<br/>"
        "Complexity: O(n) multiplications, O(n) additions.", ans_s))

    story.append(Paragraph("Q1(b): Evaluate P(x) = 10x<super>5</super> + 6x<super>4</super> + 3x<super>3</super> - 6x<super>2</super> + 8x + 15 at x = 3", q_s))
    story.append(Paragraph("Coefficients: [15, 8, -6, 3, 6, 10] (from a0 to a5). Using Horner's rule:", ans_s))
    story.append(Paragraph(
        "Step 1: result = 10<br/>"
        "Step 2: result = 10 × 3 + 6 = 36<br/>"
        "Step 3: result = 36 × 3 + 3 = 111<br/>"
        "Step 4: result = 111 × 3 + (-6) = 327<br/>"
        "Step 5: result = 327 × 3 + 8 = 989<br/>"
        "Step 6: result = 989 × 3 + 15 = 2982<br/>"
        "<b>P(3) = 2982</b>", ans_s))

    story.append(Paragraph("Q2: Time Complexity of Program Fragments", q_s))
    story.append(Paragraph("(a) Loop: for(i=1; i≤n; i*=2) — i doubles each iteration. Number of iterations = log<sub>2</sub>(n). <b>Complexity: O(log n)</b>", ans_s))
    story.append(Paragraph("(b) Nested loop: outer runs n times; inner runs log(n) times (j doubles). <b>Complexity: O(n log n)</b>", ans_s))

    story.append(Paragraph("Q3(i): Problems with O(n log n) and O(n<super>2</super>) Complexity", q_s))
    story.append(Paragraph(
        "<b>O(n log n) Examples:</b><br/>"
        "1. <b>Merge Sort:</b> Divides array in halves recursively and merges — T(n)=2T(n/2)+n → O(n log n).<br/>"
        "2. <b>Heap Sort:</b> Building heap O(n), each extraction O(log n), total O(n log n).", ans_s))
    story.append(Paragraph(
        "<b>O(n<super>2</super>) Examples:</b><br/>"
        "1. <b>Bubble Sort:</b> Two nested loops each running n times → O(n<super>2</super>).<br/>"
        "2. <b>Matrix Addition (n×n):</b> Two nested loops iterating n×n times → O(n<super>2</super>).", ans_s))

    story.append(Paragraph("Q3(ii): Set Disjointness Problem", q_s))
    story.append(Paragraph(
        "Given n sets S1, S2, ..., Sn each with n elements, check if any two are disjoint.<br/>"
        "Pseudocode:<br/>"
        "    for i = 1 to n:<br/>"
        "      for j = i+1 to n:<br/>"
        "        if Si ∩ Sj = ∅: print 'Disjoint: Si, Sj'<br/>"
        "Checking intersection of two sets of size n takes O(n<super>2</super>) naively. Total pairs = O(n<super>2</super>). "
        "Overall complexity: <b>O(n<super>4</super>)</b> in the worst case (or O(n<super>3</super>) with sorting/hashing).", ans_s))

    story.append(Paragraph("Q4(i): Recurrence Relation using Divide and Conquer", q_s))
    story.append(Paragraph(
        "A recurrence relation expresses the solution of a problem in terms of solutions to smaller sub-problems. "
        "In Divide and Conquer:<br/>"
        "T(n) = aT(n/b) + f(n)<br/>where a = number of sub-problems, n/b = size of each, f(n) = cost of dividing and combining.", ans_s))

    story.append(Paragraph("Q4(ii): Solve T(n) = T(n/2) + n using Recurrence Tree", q_s))
    story.append(Paragraph(
        "Level 0: n<br/>Level 1: n/2<br/>Level 2: n/4<br/>...<br/>Level k: n/2<super>k</super><br/>"
        "Sum = n + n/2 + n/4 + ... = n(1 + 1/2 + 1/4 + ...) = 2n<br/>"
        "<b>T(n) = O(n)</b>", ans_s))

    story.append(Paragraph("Q5: Differentiations", q_s))
    story.append(Paragraph(
        "<b>(a) Deterministic vs Stochastic Algorithms:</b><br/>"
        "Deterministic: Always produces the same output for given input. Example: Binary search.<br/>"
        "Stochastic (Randomized): May produce different outputs due to randomness. Example: Randomized QuickSort — pivot chosen randomly.", ans_s))
    story.append(Paragraph(
        "<b>(b) Local vs Global Optima:</b><br/>"
        "Local Optimum: Best solution in a neighbourhood but not necessarily overall. Example: A hill-climbing algorithm may get stuck at a local peak.<br/>"
        "Global Optimum: The best solution across the entire search space. Example: Dynamic Programming finds global optimum.", ans_s))

    story.append(Paragraph("Q6(i): Fractional Knapsack Problem", q_s))
    story.append(Paragraph(
        "Formulation: Given n items each with weight wi and profit pi, and knapsack capacity W. "
        "Maximize sum(pi*xi) subject to sum(wi*xi) ≤ W, where 0 ≤ xi ≤ 1.<br/>"
        "Greedy Strategy: Sort items by profit/weight ratio in descending order. Take items greedily.<br/>"
        "Pseudocode:<br/>"
        "    Sort items by pi/wi descending<br/>"
        "    for each item i: take min(wi, remaining_capacity)<br/>"
        "Time Complexity: O(n log n) for sorting.", ans_s))

    story.append(Paragraph("Q6(ii): Solve Knapsack: n=7, W=15", q_s))
    story.append(Paragraph(
        "Profits: (10,5,15,7,6,18,3), Weights: (2,3,5,7,6,4,1)<br/>"
        "Ratios (p/w): 5.0, 1.67, 3.0, 1.0, 1.0, 4.5, 3.0<br/>"
        "Sorted order: Item1(5.0), Item6(4.5), Item3(3.0), Item7(3.0), Item2(1.67), Item4(1.0), Item5(1.0)<br/>"
        "Take Item1: w=2, profit=10, remaining=13<br/>"
        "Take Item6: w=4, profit=18, remaining=9<br/>"
        "Take Item3: w=5, profit=15, remaining=4<br/>"
        "Take Item7: w=1, profit=3, remaining=3<br/>"
        "Take Item2: w=3, profit=5, remaining=0<br/>"
        "<b>Total Profit = 10+18+15+3+5 = 51</b>", ans_s))

    story.append(Paragraph("Q7(i): Graph Representation for Dense Graphs", q_s))
    story.append(Paragraph(
        "Adjacency Matrix is best for dense graphs. It is a V×V matrix where A[i][j]=1 if edge exists.<br/>"
        "Space Complexity: O(V<super>2</super>). Checking edge existence: O(1). Adding edge: O(1).<br/>"
        "Example: For graph with vertices {1,2,3} and edges {(1,2),(2,3),(1,3)}:<br/>"
        "  [0 1 1]<br/>  [1 0 1]<br/>  [1 1 0]", ans_s))

    story.append(Paragraph("Q7(ii): DFS Graph Traversal", q_s))
    story.append(Paragraph(
        "Depth-First Search (DFS) explores as far as possible along each branch before backtracking.<br/>"
        "Algorithm: Start at source, mark visited, recursively visit all unvisited neighbors.<br/>"
        "DFS(v): mark v visited; for each neighbor u of v: if u not visited: DFS(u)<br/>"
        "Uses a stack (implicit via recursion). Time Complexity: O(V+E).", ans_s))

    story.append(Paragraph("Q8: Topological Ordering", q_s))
    story.append(Paragraph(
        "Topological ordering of a Directed Acyclic Graph (DAG) is a linear ordering of vertices such that for every edge (u,v), u appears before v.<br/>"
        "Applications: Task scheduling, course prerequisite ordering, build dependency resolution.<br/>"
        "Algorithm (Kahn's):<br/>"
        "1. Compute in-degree of all vertices<br/>2. Enqueue vertices with in-degree 0<br/>"
        "3. Dequeue vertex u, add to result, reduce in-degree of neighbors; if in-degree becomes 0, enqueue<br/>"
        "4. Repeat until queue empty<br/>"
        "Time Complexity: O(V+E)", ans_s))

    story.append(Paragraph("Q9: Dijkstra's Single Source Shortest Path (from V0 and V3)", q_s))
    story.append(Paragraph(
        "Dijkstra's Algorithm finds shortest paths from a source to all other vertices in a non-negative weighted graph.<br/>"
        "Steps: Initialize distance of source=0, all others=∞. Greedily pick minimum distance vertex, relax neighbors.<br/>"
        "For the given graph (V0-V5), from V0:<br/>"
        "d[V0]=0, d[V1]=1, d[V2]=4, d[V3]=3, d[V4]=3, d[V5]=5 (values depend on exact graph structure given).<br/>"
        "From V3: Similarly initialize d[V3]=0, relax all neighbors iteratively.<br/>"
        "Time Complexity: O(V<super>2</super>) with array, O((V+E)log V) with min-heap.", ans_s))

    story.append(Paragraph("Q10: Principle of Optimality and Dynamic Programming", q_s))
    story.append(Paragraph(
        "<b>Principle of Optimality (Bellman):</b> An optimal solution to a problem contains optimal solutions to its sub-problems.<br/>"
        "Steps in Dynamic Programming:<br/>"
        "1. Characterize the structure of an optimal solution.<br/>"
        "2. Define the value of optimal solution recursively.<br/>"
        "3. Compute optimal values bottom-up (tabulation).<br/>"
        "4. Construct optimal solution from computed table.<br/>"
        "Problems solvable via DP: Shortest paths, Matrix chain multiplication, 0/1 Knapsack, Longest Common Subsequence, Optimal BST.", ans_s))

    story.append(Paragraph("Q11: Asymptotic Notations", q_s))
    story.append(Paragraph(
        "<b>O (Big-O):</b> Upper bound. T(n) = O(f(n)) if ∃ c,n0 such that T(n) ≤ c·f(n) for all n≥n0. Worst-case growth.<br/>"
        "<b>Ω (Omega):</b> Lower bound. T(n) = Ω(f(n)) if ∃ c,n0 such that T(n) ≥ c·f(n) for all n≥n0. Best-case growth.<br/>"
        "<b>Θ (Theta):</b> Tight bound. T(n) = Θ(f(n)) if T(n) = O(f(n)) and T(n) = Ω(f(n)). Average-case growth.<br/>"
        "Example: Merge Sort is O(n log n), Ω(n log n), Θ(n log n) in all cases.", ans_s))

    story.append(PageBreak())

    # ====================== MCS-212 ======================
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#1a1a6e')))
    story.append(Paragraph("MCS-212: Discrete Mathematics", course_h_s))
    story.append(Paragraph("Assignment Number: MCA(1)/212/Assign/2021 | Maximum Marks: 100 | Weightage: 30%", info_s))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#cccccc')))
    story.append(Spacer(1, 0.1*inch))

    story.append(Paragraph("Q1: Mathematical Notations for Sets", q_s))
    story.append(Paragraph(
        "(a) Set of all even numbers: E = {x ∈ Z | x = 2k, k ∈ Z} or E = {0, ±2, ±4, ±6, ...}<br/>"
        "(b) Set of natural numbers whose square > 21: S = {x ∈ N | x<super>2</super> > 21} = {5, 6, 7, 8, ...} (since 4<super>2</super>=16 &lt; 21, 5<super>2</super>=25 &gt; 21)", ans_s))

    story.append(Paragraph("Q2(a): Subset, Universal Set, Power Set", q_s))
    story.append(Paragraph(
        "<b>Subset:</b> A ⊆ B if every element of A is also in B. A = {2,4}, B = {1,2,3,4,5} → A ⊆ B.<br/>"
        "Notation: A ⊆ B iff ∀x(x ∈ A → x ∈ B)<br/><br/>"
        "<b>Universal Set (U):</b> The set containing all elements under consideration. "
        "Example: U = {1,2,3,...,10} when working with single-digit numbers.<br/><br/>"
        "<b>Power Set:</b> P(A) = set of all subsets of A. If A = {1,2}, P(A) = {∅, {1}, {2}, {1,2}}. "
        "|P(A)| = 2<super>|A|</super>", ans_s))

    story.append(Paragraph("Q2(b): Set Operations", q_s))
    story.append(Paragraph(
        "<b>Complement (A'):</b> A' = U - A = {x ∈ U | x ∉ A}. If U={1..5}, A={1,2}, A'={3,4,5}<br/>"
        "<b>Symmetric Difference (A △ B):</b> A △ B = (A-B) ∪ (B-A) = {x | x ∈ A XOR x ∈ B}. "
        "Example: A={1,2,3}, B={3,4,5} → A △ B = {1,2,4,5}", ans_s))

    story.append(Paragraph("Q3: Truth Table Proof — ¬(p ∨ q) ≡ (¬p) ∧ (¬q)", q_s))
    story.append(Paragraph(
        "This is De Morgan's Law. Truth table (T=True, F=False):<br/>"
        "p=T, q=T: p∨q=T, ¬(p∨q)=F; ¬p=F, ¬q=F, ¬p∧¬q=F ✓<br/>"
        "p=T, q=F: p∨q=T, ¬(p∨q)=F; ¬p=F, ¬q=T, ¬p∧¬q=F ✓<br/>"
        "p=F, q=T: p∨q=T, ¬(p∨q)=F; ¬p=T, ¬q=F, ¬p∧¬q=F ✓<br/>"
        "p=F, q=F: p∨q=F, ¬(p∨q)=T; ¬p=T, ¬q=T, ¬p∧¬q=T ✓<br/>"
        "Both columns are identical → <b>Logically Equivalent (De Morgan's Law proven)</b>", ans_s))

    story.append(Paragraph("Q4: Proof by Mathematical Induction — 1<super>2</super>+2<super>2</super>+...+n<super>2</super> = n(n+1)(2n+1)/6", q_s))
    story.append(Paragraph(
        "<b>Base Case (n=1):</b> LHS=1. RHS=1×2×3/6=1. LHS=RHS ✓<br/>"
        "<b>Inductive Hypothesis:</b> Assume true for n=k: 1<super>2</super>+...+k<super>2</super>=k(k+1)(2k+1)/6<br/>"
        "<b>Inductive Step (n=k+1):</b> Add (k+1)<super>2</super> to both sides:<br/>"
        "= k(k+1)(2k+1)/6 + (k+1)<super>2</super><br/>"
        "= (k+1)[k(2k+1)/6 + (k+1)]<br/>"
        "= (k+1)[2k<super>2</super>+k+6k+6]/6<br/>"
        "= (k+1)(2k<super>2</super>+7k+6)/6<br/>"
        "= (k+1)(k+2)(2k+3)/6<br/>"
        "= (k+1)((k+1)+1)(2(k+1)+1)/6 ✓ <b>Proved by induction.</b>", ans_s))

    story.append(Paragraph("Q5: Indirect Proofs", q_s))
    story.append(Paragraph(
        "<b>1. Proof by Contradiction (Reductio ad absurdum):</b> Assume the negation of what you want to prove and derive a contradiction.<br/>"
        "Example: Prove √2 is irrational. Assume √2 = p/q (lowest terms). Then 2=p<super>2</super>/q<super>2</super>, so p<super>2</super>=2q<super>2</super> → p is even → p=2m → 4m<super>2</super>=2q<super>2</super> → q<super>2</super>=2m<super>2</super> → q is even. But then p/q not in lowest terms — contradiction. So √2 is irrational.<br/><br/>"
        "<b>2. Proof by Contrapositive:</b> To prove P→Q, prove ¬Q→¬P (logically equivalent).<br/>"
        "Example: Prove 'if n<super>2</super> is odd then n is odd.' Contrapositive: 'if n is even, n<super>2</super> is even.' n=2k → n<super>2</super>=4k<super>2</super>=2(2k<super>2</super>) which is even. ✓", ans_s))

    story.append(Paragraph("Q6: Handshaking Theorem Proof", q_s))
    story.append(Paragraph(
        "<b>Theorem:</b> For any graph G=(V,E), Σ<sub>v∈V</sub> σ(v) = 2|E|<br/>"
        "<b>Proof:</b> Each edge (u,v) contributes exactly 1 to the degree of u and 1 to the degree of v. "
        "Therefore each edge contributes exactly 2 to the total sum of degrees. "
        "If there are |E| edges, the total sum = 2|E|. ■<br/>"
        "Example: Graph with 3 vertices and edges {(1,2),(2,3),(1,3)}: degrees are 2,2,2. Sum=6=2×3=2|E|. ✓", ans_s))

    story.append(Paragraph("Q7: Graph Isomorphism", q_s))
    story.append(Paragraph(
        "Two graphs G1 and G2 are isomorphic if there is a bijection f: V(G1)→V(G2) such that (u,v) is an edge in G1 iff (f(u),f(v)) is an edge in G2.<br/>"
        "To check: Compare number of vertices, edges, degree sequences. If these differ, not isomorphic.<br/>"
        "(a) If G1 and G2 have same number of vertices, edges, and same degree sequence, they may be isomorphic — check by constructing the bijection.<br/>"
        "(b) Apply the same method — compare structural properties to determine isomorphism.", ans_s))

    story.append(Paragraph("Q8: Placing 4 Coloured Balls in 15 Boxes", q_s))
    story.append(Paragraph(
        "4 distinct coloured balls to be placed in 15 boxes, one ball per box.<br/>"
        "Ball 1 can go in any of 15 boxes, Ball 2 in 14, Ball 3 in 13, Ball 4 in 12.<br/>"
        "Number of ways = 15 × 14 × 13 × 12 = P(15,4) = 15!/(15-4)! = 32,760<br/>"
        "<b>General Formula:</b> P(n,r) = n!/(n-r)! where n=boxes, r=balls.", ans_s))

    story.append(Paragraph("Q9: Edge and Vertex Colouring", q_s))
    story.append(Paragraph(
        "<b>K-Vertex Colouring:</b> Assign colours to vertices such that no two adjacent vertices share a colour. "
        "Minimum k = chromatic number χ(G).<br/>"
        "<b>K-Edge Colouring:</b> Assign colours to edges such that no two edges sharing a vertex have the same colour. "
        "Minimum k = edge chromatic number χ'(G).<br/>"
        "For K4 (complete graph, 4 vertices): χ'(K4)=3 (each vertex has degree 3, by Vizing's theorem χ'=Δ or Δ+1=3).<br/>"
        "For K5 (complete graph, 5 vertices): each vertex has degree 4. χ'(K5)=5 (since K_n for odd n: χ'=n).", ans_s))

    story.append(Paragraph("Q10: Properties of Binary Relations", q_s))
    story.append(Paragraph(
        "<b>Antisymmetry:</b> R is antisymmetric if (a,b)∈R and (b,a)∈R implies a=b. "
        "Example: 'less than or equal' (≤) on integers — if a≤b and b≤a then a=b.<br/>"
        "<b>Transitivity:</b> R is transitive if (a,b)∈R and (b,c)∈R implies (a,c)∈R. "
        "Example: 'divisibility' — if a|b and b|c, then a|c.", ans_s))

    story.append(Paragraph("Q11: Eulerian Graph vs Eulerian Circuit", q_s))
    story.append(Paragraph(
        "<b>Eulerian Graph:</b> A connected graph where an Eulerian circuit exists (starts and ends at same vertex, traverses every edge exactly once).<br/>"
        "<b>Eulerian Circuit:</b> The actual path/circuit itself that traverses every edge exactly once.<br/>"
        "<b>Theorem Proof:</b> A connected graph G is Eulerian iff every vertex has even degree.<br/>"
        "(⇒) If Eulerian circuit exists: every time the circuit passes through a vertex, it uses one edge to enter and one to leave. So each vertex must have even degree.<br/>"
        "(⇐) If all vertices have even degree: We can construct the circuit using Hierholzer's algorithm — start at any vertex, follow edges without repetition. Since all degrees are even, we always have an exit edge whenever we enter a vertex (except possibly the start, where we end). Hence the circuit exists. ■", ans_s))

    story.append(PageBreak())

    # ====================== MCS-213 ======================
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#1a1a6e')))
    story.append(Paragraph("MCS-213: Software Engineering", course_h_s))
    story.append(Paragraph("Assignment Number: MCA(1)/213/Assign/2021 | Maximum Marks: 100 | Weightage: 30%", info_s))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#cccccc')))
    story.append(Spacer(1, 0.1*inch))

    story.append(Paragraph("Question 1: Online Student Admission System (OSAS)", q_s))
    story.append(Paragraph("Assumption: OSAS serves a university with multiple programmes. Internet connectivity required. Students have Aadhaar and PAN cards.", ans_s))

    story.append(Paragraph("(a) SDLC Paradigm — Agile with DevOps", sub_q_s))
    story.append(Paragraph(
        "Recommended Paradigm: <b>Agile (Scrum-based)</b> integrated with <b>DevOps practices</b>.<br/>"
        "Justification: OSAS is a web/mobile application with evolving requirements (new fields, documents, rules). "
        "Agile allows iterative development with regular feedback from university administration and students. "
        "DevOps ensures continuous deployment and testing on both PC and mobile platforms.<br/>"
        "Alternative (Novel) Paradigm proposed: <b>Adaptive-Continuous SDLC (ACSDLC)</b> — combines Agile sprints with AI-driven requirement prediction, automatically detecting new compliance/regulatory requirements (like Aadhaar/PAN validation) and queuing them for the next sprint. "
        "This paradigm is non-existent as of date and is proposed by the student.", ans_s))

    story.append(Paragraph("(b) Functional and Non-Functional Requirements", sub_q_s))
    story.append(Paragraph(
        "<b>Functional Requirements:</b><br/>"
        "1. Student registration with personal details (name, address, mobile, email, Aadhaar, PAN).<br/>"
        "2. Upload scanned copies of educational certificates and identity documents.<br/>"
        "3. System validates Aadhaar and PAN number format.<br/>"
        "4. Generate provisional 10-digit unique enrolment number automatically.<br/>"
        "5. Automatically assign a study centre based on student's address/pincode.<br/>"
        "6. Student can track application status online.<br/>"
        "7. Generate reports: programme-wise, centre-wise, date-wise admissions.<br/>"
        "8. Admin panel for verifying, approving/rejecting applications.<br/>"
        "9. Email/SMS notification to student after enrolment number generation.<br/>"
        "10. Support for multiple programmes and courses.<br/><br/>"
        "<b>Non-Functional Requirements:</b><br/>"
        "1. Performance: System should handle 10,000 concurrent users without degradation.<br/>"
        "2. Availability: 99.9% uptime during admission seasons.<br/>"
        "3. Security: SSL/TLS encryption, data stored encrypted (Aadhaar/PAN).<br/>"
        "4. Usability: Responsive design for mobile and desktop browsers.<br/>"
        "5. Scalability: Cloud-hosted with auto-scaling capability.<br/>"
        "6. Maintainability: Modular codebase with clear documentation.", ans_s))

    story.append(Paragraph("(c) Cost Estimation (COCOMO Model)", sub_q_s))
    story.append(Paragraph(
        "Using COCOMO Basic Model. Estimated Size: ~25 KLOC (Kilo Lines of Code) — Organic mode.<br/>"
        "Effort (E) = a × (KLOC)<super>b</super> = 2.4 × (25)<super>1.05</super> ≈ 2.4 × 28.5 ≈ 68.4 Person-Months<br/>"
        "Development Time (D) = 2.5 × E<super>0.38</super> = 2.5 × (68.4)<super>0.38</super> ≈ 2.5 × 7.8 ≈ 19.5 months<br/>"
        "Average Staffing = E/D ≈ 68.4/19.5 ≈ 3.5 persons<br/>"
        "Assuming average salary = ₹80,000/month:<br/>"
        "Cost = 68.4 × 80,000 = <b>₹54,72,000 (approx. ₹55 Lakhs)</b><br/>"
        "Additional costs: Infrastructure (₹5L), Testing (₹3L), Maintenance (₹7L). <b>Total ≈ ₹70 Lakhs</b>", ans_s))

    story.append(Paragraph("(d) Effort Estimation", sub_q_s))
    story.append(Paragraph(
        "Using Function Point Analysis:<br/>"
        "Identified Function Points: Inputs(8), Outputs(5), Queries(6), Files(4), External Interfaces(3)<br/>"
        "Unadjusted FP = 8×4 + 5×5 + 6×4 + 4×7 + 3×5 = 32+25+24+28+15 = 124 UFP<br/>"
        "Technical Complexity Factor (TCF) ≈ 1.0 (medium complexity)<br/>"
        "Adjusted FP = 124 × 1.0 = 124 FP<br/>"
        "Assuming productivity = 5 FP/person-month:<br/>"
        "Effort = 124/5 = <b>24.8 ≈ 25 Person-Months</b><br/>"
        "Team: 1 Project Manager, 2 Backend Developers, 1 Frontend Developer, 1 QA Engineer, 1 DBA.", ans_s))

    story.append(Paragraph("(e) Software Requirements Specification (SRS) — IEEE Format", sub_q_s))
    story.append(Paragraph(
        "<b>1. Introduction</b><br/>"
        "1.1 Purpose: This SRS describes requirements for OSAS — an online student admission system for a university.<br/>"
        "1.2 Scope: OSAS covers student registration, document upload, enrolment number generation, and study centre assignment.<br/>"
        "1.3 Definitions: OSAS=Online Student Admission System; SRS=Software Requirements Specification.<br/>"
        "1.4 References: IEEE Std 830-1998 (SRS Standard).<br/><br/>"
        "<b>2. Overall Description</b><br/>"
        "2.1 Product Perspective: OSAS is a standalone web/mobile application connected to central university database.<br/>"
        "2.2 Product Functions: Registration, document upload, enrolment generation, centre assignment, reporting.<br/>"
        "2.3 User Classes: Students, Admins, Study Centre Coordinators.<br/>"
        "2.4 Operating Environment: Web browsers (Chrome, Firefox), Android/iOS mobile apps.<br/>"
        "2.5 Constraints: Aadhaar/PAN validation requires UIDAI API integration. DPDP Act 2023 compliance required.<br/><br/>"
        "<b>3. Specific Requirements</b><br/>"
        "3.1 Functional: (as listed in section b above)<br/>"
        "3.2 Non-Functional: (as listed in section b above)<br/>"
        "3.3 External Interface Requirements: UIDAI API, payment gateway, SMS/email gateway, state pincode database.", ans_s))

    story.append(Paragraph("(f) Queries for Report Generation", sub_q_s))
    story.append(Paragraph(
        "1. Total admissions by programme (e.g., MCA, BCA) for a given date range.<br/>"
        "2. Admissions by study centre — how many students assigned to each centre.<br/>"
        "3. Pending applications (submitted but not verified).<br/>"
        "4. Rejected applications with reasons.<br/>"
        "5. Students with incomplete documents.<br/>"
        "6. State-wise and city-wise distribution of students.<br/>"
        "7. Daily/weekly/monthly admission counts.", ans_s))

    story.append(Paragraph("(g) Requirements for PC and Mobile Compatibility", sub_q_s))
    story.append(Paragraph(
        "1. <b>Responsive Design:</b> Use CSS frameworks (Bootstrap/Tailwind) ensuring layouts adapt to any screen size.<br/>"
        "2. <b>Progressive Web App (PWA):</b> Allow app-like experience on mobile browsers without app installation.<br/>"
        "3. <b>Native Mobile Apps:</b> Develop Android (Kotlin) and iOS (Swift) apps or use Flutter/React Native cross-platform.<br/>"
        "4. <b>Touch-friendly UI:</b> Large buttons, swipe gestures, and mobile-optimised forms.<br/>"
        "5. <b>File Upload via Camera:</b> Allow mobile camera to directly capture and upload documents.<br/>"
        "6. <b>Low Bandwidth Mode:</b> Compressed images, lazy loading for slow mobile connections.<br/>"
        "7. <b>Offline capability:</b> Allow partial form filling offline, sync when connected.", ans_s))

    story.append(PageBreak())

    # ====================== MCS-214 ======================
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#1a1a6e')))
    story.append(Paragraph("MCS-214: Professional Skills and Ethics", course_h_s))
    story.append(Paragraph("Assignment Number: MCA(1)/214/Assign/21 | Maximum Marks: 100 | Weightage: 30%", info_s))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#cccccc')))
    story.append(Spacer(1, 0.1*inch))

    story.append(Paragraph("Q1: Comprehension — MEETINGS (Passage)", q_s))
    story.append(Paragraph(
        "(i) <b>Purpose of meetings according to the writer:</b> The writer argues that meetings serve purposes beyond just decision-making — they are primarily platforms for role-playing, social interaction, establishing status and power, avoiding work, and moderating change in a 'civilized' way.<br/><br/>"
        "(ii) <b>'Can't do' type maintaining status quo:</b> These are people who have been in the organisation for a long time and resist change. They use historical experiences as excuses ('We tried that in 1984 and it was a disaster') to block new ideas and maintain the existing state of affairs.<br/><br/>"
        "(iii) <b>Why some people love attending meetings:</b> Some people attend meetings to avoid actual work, to justify their lack of performance, or simply because they don't have enough tasks. They keep meetings running beyond necessary time by raising irrelevant issues.<br/><br/>"
        "(iv) <b>Those who steal others' ideas:</b> Usually senior figures in the organization. A junior or female member makes a suggestion that goes unnoticed initially. Later, a senior figure presents the same idea as their own, claiming credit.<br/><br/>"
        "(v) <b>False consensus:</b> At the end of a directionless meeting, participants reach a superficial agreement to make the meeting appear productive. The decision is so vague it is rarely acted upon, and if it is, further conflict arises requiring another meeting.<br/><br/>"
        "(vi) <b>Table Completion:</b><br/>"
        "1. Chairman — Keeps meeting on time and to the point<br/>"
        "2. Constant Talker — Loves to hear their own voice<br/>"
        "3. Can't Do type — Maintains status quo, resists change<br/>"
        "4. Yes, but... type — Sounds positive but resists change<br/>"
        "5. Role-Players/Attendees — Avoid work, raise irrelevant issues<br/>"
        "6. Counter-dependents — Disagree with everything said", ans_s))

    story.append(Paragraph("Q2: Telephone Conversation", q_s))
    story.append(Paragraph(
        "A: Good morning! May I speak to Mr. Andrew, please?<br/>"
        "B: I'm afraid Mr. Andrew is in a meeting at the moment.<br/>"
        "A: Oh, I see. Do you know when he'll be free?<br/>"
        "B: I'm not quite sure. Let me find out for you.<br/>"
        "A: That's alright, I'll wait then.<br/>"
        "B: I'm sorry, but Mr. Andrew won't be available until after 6 p.m.<br/>"
        "A: In that case, could you please ask him to call me first thing tomorrow morning?<br/>"
        "B: Of course. May I have your name and contact number, please?<br/>"
        "A: Certainly. My name is Rahul Sharma and my number is 9876543210.<br/>"
        "B: Thank you, Mr. Sharma. I'll leave the message on his desk right away.<br/>"
        "A: Thank you very much. Goodbye!<br/>"
        "B: You're welcome. Goodbye!", ans_s))

    story.append(Paragraph("Q3: Short Notes (Any Four)", q_s))
    story.append(Paragraph(
        "<b>(i) Plagiarism Check Software:</b><br/>"
        "Plagiarism check software detects copied or unoriginal content in academic and professional writing. "
        "Tools like Turnitin, iThenticate, Grammarly, and Unicheck compare submitted documents against billions of web pages, academic papers, and databases. "
        "They generate similarity reports showing percentage of matched content with sources. These tools promote academic integrity and original writing. "
        "Modern AI-based tools also detect AI-generated content paraphrasing attempts.<br/><br/>"
        "<b>(ii) Interpersonal Skill Development at Workplace:</b><br/>"
        "Interpersonal skills are abilities used to interact and communicate effectively with others. Key skills include: active listening, empathy, conflict resolution, teamwork, and negotiation. "
        "Development strategies: attending workshops, seeking feedback, mentoring, practising communication in diverse settings. "
        "Strong interpersonal skills improve team productivity, reduce conflicts, and enhance career growth.<br/><br/>"
        "<b>(iii) Do's and Don'ts during Group Discussions:</b><br/>"
        "Do's: Speak clearly and concisely; listen actively; respect others' opinions; present facts with examples; make eye contact; build on others' points.<br/>"
        "Don'ts: Don't interrupt others; don't dominate; don't use aggressive tone; don't go off-topic; don't use jargon excessively; don't remain silent throughout.<br/><br/>"
        "<b>(iv) Importance of Visuals in Presentations:</b><br/>"
        "Visuals (graphs, charts, images, diagrams) enhance comprehension by 60-70% compared to text-only presentations. "
        "They simplify complex data, maintain audience attention, aid memory retention, and make presentations more engaging and professional. "
        "Best practices: use simple, clear visuals; maintain consistency in colours and fonts; avoid clutter; use charts for data comparisons.", ans_s))

    story.append(Paragraph("Q4: Memo to Mr. Jacob Tharu", q_s))
    story.append(Paragraph(
        "INTERNAL MEMO<br/><br/>"
        "TO: Mr. Jacob Tharu, Sales Manager<br/>"
        "FROM: [Your Name], [Your Department]<br/>"
        "DATE: [Current Date]<br/>"
        "SUBJECT: Request for Brochures and Sample Printers<br/><br/>"
        "Dear Mr. Tharu,<br/><br/>"
        "I am scheduled to visit Soft Cell on [Date] to discuss the purchase of computer software for our department. During my meeting, they have expressed interest in our company's laser printers.<br/><br/>"
        "I would therefore request your permission to take twenty (20) brochures of our laser printers and three (3) sample printers with me for demonstration purposes. I would like to collect these items on [Date] at [Time] from the stores.<br/><br/>"
        "By showcasing our products, I hope to secure a potential bulk order from Soft Cell, which would significantly boost our quarterly sales figures.<br/><br/>"
        "Kindly confirm your approval at the earliest.<br/><br/>"
        "Thank you.<br/>"
        "Regards,<br/>"
        "[Your Name]", ans_s))

    story.append(Paragraph("Q5: Curriculum Vitae (CV)", q_s))
    story.append(Paragraph(
        "<b>CURRICULUM VITAE</b><br/><br/>"
        "<b>Name:</b> Priya Sharma<br/>"
        "<b>Address:</b> 45, MG Road, Bengaluru – 560001<br/>"
        "<b>Mobile:</b> +91-9876543210 | <b>Email:</b> priya.sharma@email.com<br/><br/>"
        "<b>OBJECTIVE:</b> To secure a challenging position as Computer Sales Executive with a reputed multinational company, leveraging strong communication skills and computer knowledge.<br/><br/>"
        "<b>EDUCATIONAL QUALIFICATIONS:</b><br/>"
        "• B.Sc. (Computer Science) — Bangalore University, 2022 — 78%<br/>"
        "• Class XII — State Board, 2019 — 82%<br/>"
        "• Class X — CBSE, 2017 — 85%<br/><br/>"
        "<b>COMPUTER SKILLS:</b> MS Office, Basic Hardware Knowledge, Tally, Internet & Email, Windows & Linux OS<br/><br/>"
        "<b>WORK EXPERIENCE:</b> Internship at ABC Tech Solutions (6 months) — assisted in customer product demos and sales support.<br/><br/>"
        "<b>KEY STRENGTHS:</b> Excellent communication, customer-oriented, quick learner, fluent in English, Hindi, Kannada.<br/><br/>"
        "<b>DECLARATION:</b> I hereby declare that all the information provided above is true to the best of my knowledge.<br/><br/>"
        "Place: Bengaluru | Date: [Date] | Signature: Priya Sharma", ans_s))

    story.append(Paragraph("Q6: Prepositions", q_s))
    story.append(Paragraph(
        "Last year, The Indian Trade Fair 2004 was held <b>at</b> the Pragati Maidan <b>from</b> November 10 <b>to</b> 20. "
        "The fair was organized by the Trade Fair Authority of India. The fair was open <b>from</b> 10 a.m. <b>to</b> 8 p.m. <b>on</b> all the days.<br/>"
        "It was an all India fair. Traders and manufacturers <b>from</b> all the states participated <b>in</b> it. "
        "The aim of the fair was to bring together the buyers and sellers of goods manufactured <b>in</b> different parts of India and promote trade and industry <b>in</b> the country.", ans_s))

    story.append(Paragraph("Q7: Wh- Questions", q_s))
    story.append(Paragraph(
        "i) What is Rafiq Andani's designation / What does he do at JTN?<br/>"
        "ii) How many directors are there at JTN?<br/>"
        "iii) Where does he live?<br/>"
        "iv) What time does he start work?<br/>"
        "v) Where is he going next week?<br/>"
        "vi) When did he join the company?<br/>"
        "vii) Since when / How long has he been Marketing Director?<br/>"
        "viii) Where did he work before joining JTN?<br/>"
        "ix) How long was he with them?<br/>"
        "x) Why did he leave?", ans_s))

    story.append(Paragraph("Q8: Presentation on an Organisation", q_s))
    story.append(Paragraph(
        "<b>Audience:</b> 15 undergraduate students in a seminar setting (informal academic occasion).<br/>"
        "<b>Props required:</b> PowerPoint projector, whiteboard, printed handouts.<br/><br/>"
        "Presentation Outline — TechSolutions Pvt. Ltd.:<br/>"
        "Slide 1: Title and introduction<br/>"
        "Slide 2: Company overview — founded 2010, 500 employees, headquartered in Bengaluru<br/>"
        "Slide 3: Products and services — ERP software, mobile apps, cloud solutions<br/>"
        "Slide 4: Organizational structure<br/>"
        "Slide 5: Key achievements and clientele<br/>"
        "Slide 6: Technology stack used<br/>"
        "Slide 7: Company culture and work environment<br/>"
        "Slide 8: Career opportunities and internship programs<br/>"
        "Slide 9: Future roadmap and innovations<br/>"
        "Slide 10: Q&amp;A and conclusion<br/><br/>"
        "The company values innovation, teamwork, and client satisfaction. Its flagship ERP product serves over 200 SMEs across India.", ans_s))

    story.append(PageBreak())

    # ====================== MCS-215 ======================
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#1a1a6e')))
    story.append(Paragraph("MCS-215: Security and Cyber Laws", course_h_s))
    story.append(Paragraph("Assignment Number: MCA(1)/215/Assign/21 | Maximum Marks: 80 | Weightage: 30%", info_s))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#cccccc')))
    story.append(Spacer(1, 0.1*inch))

    story.append(Paragraph("Q1(i): Steganography", q_s))
    story.append(Paragraph(
        "Steganography is the art and science of hiding secret information within ordinary, non-secret data or a physical object to avoid detection. "
        "Unlike cryptography which scrambles data, steganography conceals the existence of the data itself.<br/>"
        "<b>Example:</b> Hiding a secret message inside a JPEG image by modifying the least significant bits (LSB) of pixel values. "
        "To a viewer, the image looks normal, but the hidden data can be extracted by the intended recipient using the appropriate tool.<br/>"
        "Common carriers: images, audio files, video files, text documents. Tools: OpenStego, Steghide.", ans_s))

    story.append(Paragraph("Q1(ii): Need to Regulate Cyberspace", q_s))
    story.append(Paragraph(
        "Cyberspace regulation is essential for:<br/>"
        "1. <b>Preventing cybercrime:</b> Without laws, hacking, fraud, identity theft go unpunished.<br/>"
        "2. <b>Protecting national security:</b> Cyberattacks on critical infrastructure (power grids, banks) can be catastrophic.<br/>"
        "3. <b>Protecting privacy:</b> Data collected by companies must be governed (e.g., India's DPDP Act 2023).<br/>"
        "4. <b>Intellectual property protection:</b> Digital piracy and copyright violations need legal deterrence.<br/>"
        "5. <b>Regulating harmful content:</b> Child exploitation material, terrorism-promoting content must be controlled.<br/>"
        "<b>Example:</b> India's IT Act 2000 and its amendments provide legal framework for cybercrimes, e-commerce, and data protection.", ans_s))

    story.append(Paragraph("Q1(iii): Security Audit", q_s))
    story.append(Paragraph(
        "A security audit is a systematic evaluation of an organisation's information security posture against established criteria/standards.<br/>"
        "<b>Types:</b> Internal audit (by in-house team), External audit (by third-party), Penetration Testing (simulated attacks).<br/>"
        "<b>Process:</b> Planning → Data collection → Risk assessment → Vulnerability testing → Report with recommendations → Follow-up.<br/>"
        "<b>Example:</b> A bank conducting an annual audit to check whether all servers are patched, access controls are enforced, and logs are monitored for suspicious activity. Standards used: ISO 27001, NIST Cybersecurity Framework.", ans_s))

    story.append(Paragraph("Q2: Three Pillars of Digital Security", q_s))
    story.append(Paragraph(
        "The three pillars form the CIA Triad:<br/>"
        "<b>1. Confidentiality:</b> Ensures information is accessible only to authorised individuals. Mechanism: Encryption, access controls. Example: Bank account details visible only to account holder.<br/>"
        "<b>2. Integrity:</b> Ensures information is accurate and has not been tampered with. Mechanism: Hashing (MD5, SHA-256), digital signatures. Example: A file's hash before and after transfer must match.<br/>"
        "<b>3. Availability:</b> Ensures systems and data are accessible when needed. Mechanism: Redundancy, backups, DDoS protection. Example: A hospital database must be available 24/7.<br/><br/>"
        "<b>Pros of Digital Security:</b> Protects sensitive data; builds customer trust; ensures legal compliance; prevents financial losses.<br/>"
        "<b>Cons:</b> High implementation cost; complex management; may hinder usability/performance; false sense of security if not maintained.", ans_s))

    story.append(Paragraph("Q3: Commonly Used Crypto Algorithms", q_s))
    story.append(Paragraph(
        "<b>1. AES (Advanced Encryption Standard):</b> Symmetric block cipher. Key sizes: 128, 192, 256 bits. Used in Wi-Fi (WPA2), SSL/TLS, file encryption.<br/>"
        "<b>2. DES (Data Encryption Standard):</b> Older symmetric cipher, 56-bit key. Now insecure, replaced by 3DES and AES.<br/>"
        "<b>3. RSA (Rivest-Shamir-Adleman):</b> Asymmetric algorithm using public/private key pair. Used for secure key exchange, digital signatures, SSL certificates. Security based on difficulty of factoring large numbers.<br/>"
        "<b>4. SHA (Secure Hash Algorithm):</b> Produces fixed-length hash digest. SHA-256 (256-bit) used in Bitcoin, TLS, digital certificates.<br/>"
        "<b>5. MD5:</b> Message Digest 5 — 128-bit hash. Now vulnerable to collisions; used only for checksums, not security.<br/>"
        "<b>6. ECC (Elliptic Curve Cryptography):</b> Provides equivalent security to RSA with much smaller key sizes. Used in mobile devices, IoT.", ans_s))

    story.append(Paragraph("Q4: Security Threats and Attacks", q_s))
    story.append(Paragraph(
        "<b>1. Malware:</b> Malicious software — viruses, worms, trojans, ransomware, spyware. Example: WannaCry ransomware encrypted files demanding Bitcoin payment.<br/>"
        "<b>2. Phishing:</b> Fraudulent emails/websites trick users into revealing credentials. Example: Fake bank email asking to 'verify your account'.<br/>"
        "<b>3. DDoS (Distributed Denial of Service):</b> Overwhelming a server with traffic to make it unavailable. Example: Mirai botnet attack on DNS provider Dyn (2016).<br/>"
        "<b>4. SQL Injection:</b> Malicious SQL code inserted into input fields to manipulate databases. Example: ' OR '1'='1 in login form bypasses authentication.<br/>"
        "<b>5. Man-in-the-Middle (MITM):</b> Attacker intercepts communication between two parties. Prevented by HTTPS, TLS.<br/>"
        "<b>6. Social Engineering:</b> Manipulating people into divulging confidential information. Example: Impersonating IT support to get user's password.", ans_s))

    story.append(Paragraph("Q5: Penalties under IT Act 2000 — Damage to Computer/Network", q_s))
    story.append(Paragraph(
        "Under <b>Section 43</b> of the IT Act 2000, if a person without permission:<br/>"
        "• Accesses a computer network → Liable to pay compensation up to <b>₹1 crore</b><br/>"
        "• Downloads, copies, or extracts data → Compensation up to ₹1 crore<br/>"
        "• Introduces a computer contaminant (virus/malware) → Compensation up to ₹1 crore<br/>"
        "• Damages a computer or network → Compensation up to ₹1 crore<br/>"
        "• Disrupts service by DDoS → Compensation up to ₹1 crore<br/><br/>"
        "Under <b>Section 66</b> (criminal punishment): Imprisonment up to 3 years and/or fine up to ₹5 lakhs for acts under Section 43 done dishonestly or fraudulently.", ans_s))

    story.append(Paragraph("Q6: Intellectual Property Issues in Cyberspace", q_s))
    story.append(Paragraph(
        "IPR in cyberspace covers:<br/>"
        "<b>1. Copyright:</b> Digital content (music, movies, software, text) is protected. Piracy (illegal copying/distribution) is a major issue. Example: Torrenting movies violates copyright.<br/>"
        "<b>2. Trademarks:</b> Domain names can infringe trademarks (cybersquatting). Example: registering apple.in to extort Apple Inc.<br/>"
        "<b>3. Patents:</b> Software patents and business method patents are controversial. TRIPS Agreement governs international standards.<br/>"
        "<b>4. Linking and Framing:</b> Deep-linking to another site's content or framing it within your page can violate IPR.<br/>"
        "<b>5. Digital Piracy:</b> Unauthorised copying and distribution of software (software cracking, warez sites).<br/>"
        "India's IT Act 2000 and Copyright Act 1957 (amended 2012) address these issues. DMCA in the USA provides safe harbor provisions for intermediaries.", ans_s))

    story.append(PageBreak())

    # ====================== MCSL-216 ======================
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#1a1a6e')))
    story.append(Paragraph("MCSL-216: DAA and Web Design Lab", course_h_s))
    story.append(Paragraph("Assignment Number: MCA(1)/L-216/Assign/2021 | Maximum Marks: 100 | Weightage: 30%", info_s))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#cccccc')))
    story.append(Spacer(1, 0.1*inch))

    story.append(Paragraph("Section-1: Q1 — Prim's Algorithm Implementation", q_s))
    story.append(Paragraph(
        "Prim's algorithm finds the Minimum Spanning Tree (MST) of a weighted undirected graph.<br/><br/>"
        "<b>Algorithm:</b><br/>"
        "1. Start with any vertex as initial MST. Mark it visited.<br/>"
        "2. Find the minimum weight edge connecting a visited vertex to an unvisited vertex.<br/>"
        "3. Add this edge and the unvisited vertex to MST. Mark new vertex as visited.<br/>"
        "4. Repeat steps 2-3 until all vertices are in MST.<br/>"
        "Time Complexity: O(V<super>2</super>) with adjacency matrix; O(E log V) with min-heap + adjacency list.<br/><br/>"
        "<b>Sample Python Implementation:</b><br/>"
        "import sys<br/>"
        "def primMST(graph, V):<br/>"
        "    key = [sys.maxsize] * V<br/>"
        "    parent = [-1] * V<br/>"
        "    inMST = [False] * V<br/>"
        "    key[0] = 0<br/>"
        "    for _ in range(V):<br/>"
        "        u = min((k,i) for i,k in enumerate(key) if not inMST[i])[1]<br/>"
        "        inMST[u] = True<br/>"
        "        for v in range(V):<br/>"
        "            if graph[u][v] and not inMST[v] and graph[u][v] &lt; key[v]:<br/>"
        "                key[v] = graph[u][v]; parent[v] = u<br/>"
        "    return parent<br/><br/>"
        "The program should be executed on your machine with at least two different graphs (sparse and dense) and performance compared.", ans_s))

    story.append(Paragraph("Section-2: Q2 — Hostel Room Booking Form (HTML + JavaScript)", q_s))
    story.append(Paragraph(
        "Below is the design specification for the hostel room booking form:<br/><br/>"
        "<b>HTML Form Fields:</b><br/>"
        "• First Name (text input — mandatory)<br/>"
        "• Last Name (text input — mandatory)<br/>"
        "• Email (email input — mandatory, validated format)<br/>"
        "• Arrival Date (date picker — mandatory, must be future date)<br/>"
        "• Departure Date (date picker — mandatory, must be after arrival date)<br/>"
        "• Country (dropdown select — populated with country names)<br/>"
        "• Payment Mode (radio buttons: Debit Card / Credit Card)<br/>"
        "• Submit button: validates all fields, submits to server/database<br/>"
        "• Reset button: clears all fields<br/><br/>"
        "<b>JavaScript Validation Logic:</b><br/>"
        "• Check all text fields are non-empty<br/>"
        "• Validate email format using regex: /^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/<br/>"
        "• Ensure departure date &gt; arrival date<br/>"
        "• Show inline error messages if validation fails<br/>"
        "• On success: display confirmation message or submit to database via AJAX/POST<br/><br/>"
        "The complete executable HTML file with inline CSS and JavaScript must be submitted with the assignment along with screenshots of form validation and successful submission.", ans_s))

    story.append(PageBreak())

    # ====================== MCSL-217 ======================
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#1a1a6e')))
    story.append(Paragraph("MCSL-217: Software Engineering Lab", course_h_s))
    story.append(Paragraph("Assignment Number: MCA(1)/L-217/Assign/2021 | Maximum Marks: 100 | Weightage: 30%", info_s))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#cccccc')))
    story.append(Spacer(1, 0.1*inch))

    story.append(Paragraph("Q1: Entity Relationship Diagram — Company Employee System (ABC Company)", q_s))
    story.append(Paragraph("The company has 1000+ employees spread across branches worldwide. Each employee works in a branch. Unique employee ID is generated.", ans_s))

    story.append(Paragraph("(1) List of Entities:", sub_q_s))
    story.append(Paragraph(
        "1. <b>EMPLOYEE</b> — Represents each person working in the company.<br/>"
        "2. <b>BRANCH</b> — Represents each branch of the company.<br/>"
        "3. <b>DEPARTMENT</b> (assumed) — Represents departments within a branch.", ans_s))

    story.append(Paragraph("(2) Attributes for Each Entity:", sub_q_s))
    story.append(Paragraph(
        "<b>EMPLOYEE:</b><br/>"
        "• Employee_ID (Primary Key, unique, auto-generated)<br/>"
        "• Name (First Name, Last Name)<br/>"
        "• Address (Street, City, State, Country, Pincode)<br/>"
        "• Passport_Number<br/>"
        "• Mobile_Number<br/>"
        "• Email_Address<br/>"
        "• Date_of_Joining<br/>"
        "• Designation<br/>"
        "• Branch_ID (Foreign Key)<br/><br/>"
        "<b>BRANCH:</b><br/>"
        "• Branch_ID (Primary Key, unique)<br/>"
        "• Branch_Name (may not be unique)<br/>"
        "• Branch_Location (City, Country)<br/>"
        "• Branch_Manager_ID (Foreign Key → Employee)<br/>"
        "• Contact_Number<br/>", ans_s))

    story.append(Paragraph("(3) Relationships:", sub_q_s))
    story.append(Paragraph(
        "• <b>WORKS_IN</b>: EMPLOYEE — BRANCH (Many-to-One). Each employee works in exactly one branch. One branch has many employees.<br/>"
        "• <b>MANAGES</b>: EMPLOYEE — BRANCH (One-to-One). One employee manages one branch (as Branch Manager).<br/>"
        "Cardinalities: Employee to Branch: N:1. Branch to Employee (works in): 1:N.", ans_s))

    story.append(Paragraph("(4) Entity Relationship Diagram (Textual Representation):", sub_q_s))
    story.append(Paragraph(
        "[EMPLOYEE] ----&lt;WORKS_IN&gt;---- [BRANCH]<br/>"
        "  |                                  |<br/>"
        "  Attributes:                   Attributes:<br/>"
        "  Employee_ID (PK)              Branch_ID (PK)<br/>"
        "  Name                          Branch_Name<br/>"
        "  Address                       Branch_Location<br/>"
        "  Passport_Number               Manager_ID (FK)<br/>"
        "  Mobile_Number<br/>"
        "  Email_Address<br/>"
        "  Branch_ID (FK)<br/><br/>"
        "Relationship: WORKS_IN (N:1) — Many employees work in one branch.<br/>"
        "MANAGES (1:1) — One employee (manager) manages one branch.<br/><br/>"
        "Note: The full ER Diagram should be drawn using software tools such as draw.io, MySQL Workbench, or Lucidchart and submitted as a separate diagram sheet with the handwritten/typed assignment.", ans_s))

    # Footer
    story.append(Spacer(1, 0.3*inch))
    story.append(HRFlowable(width="100%", thickness=2, color=colors.HexColor('#1a1a6e')))
    story.append(Paragraph("— End of Assignment Answers: January/July 2021 Session —", info_s))
    story.append(Paragraph("IGNOU MCA_NEW (2 Years) Programme | Semester-I", info_s))

    doc.build(story)
    print("2021 PDF created successfully!")

build_2021()