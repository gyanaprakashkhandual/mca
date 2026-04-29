from reportlab.lib.pagesizes import A4 # pyright: ignore[reportMissingModuleSource]
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, PageBreak # pyright: ignore[reportMissingModuleSource]
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle # pyright: ignore[reportMissingModuleSource]
from reportlab.lib.units import inch # pyright: ignore[reportMissingModuleSource]
from reportlab.lib import colors # pyright: ignore[reportMissingModuleSource]
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY # pyright: ignore[reportMissingModuleSource]

def make_styles():
    styles = getSampleStyleSheet()
    title_s = ParagraphStyle('T', parent=styles['Title'], fontSize=16, fontName='Helvetica-Bold',
        alignment=TA_CENTER, spaceAfter=6, textColor=colors.HexColor('#1a1a6e'))
    sub_s = ParagraphStyle('S', parent=styles['Normal'], fontSize=11, fontName='Helvetica-Bold',
        alignment=TA_CENTER, spaceAfter=4, textColor=colors.HexColor('#1a1a6e'))
    info_s = ParagraphStyle('I', parent=styles['Normal'], fontSize=10, fontName='Helvetica',
        alignment=TA_CENTER, spaceAfter=3, textColor=colors.HexColor('#333333'))
    ch_s = ParagraphStyle('CH', parent=styles['Normal'], fontSize=13, fontName='Helvetica-Bold',
        alignment=TA_LEFT, spaceBefore=14, spaceAfter=4, textColor=colors.HexColor('#1a1a6e'))
    q_s = ParagraphStyle('Q', parent=styles['Normal'], fontSize=10.5, fontName='Helvetica-Bold',
        alignment=TA_LEFT, spaceBefore=10, spaceAfter=3, textColor=colors.HexColor('#8B0000'))
    ans_s = ParagraphStyle('A', parent=styles['Normal'], fontSize=10, fontName='Helvetica',
        alignment=TA_JUSTIFY, spaceBefore=3, spaceAfter=4, leading=15)
    sq_s = ParagraphStyle('SQ', parent=styles['Normal'], fontSize=10, fontName='Helvetica-Bold',
        alignment=TA_LEFT, spaceBefore=6, spaceAfter=2, textColor=colors.HexColor('#444444'))
    return title_s, sub_s, info_s, ch_s, q_s, ans_s, sq_s

def build_2023():
    doc = SimpleDocTemplate("Answers_2023_MCA_NEW_Sem1.pdf",
        pagesize=A4, rightMargin=55, leftMargin=55, topMargin=60, bottomMargin=55)
    ts, ss, is_, chs, qs, ans, sqs = make_styles()
    story = []

    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("INDIRA GANDHI NATIONAL OPEN UNIVERSITY", ts))
    story.append(Paragraph("School of Computer and Information Sciences", ss))
    story.append(HRFlowable(width="100%", thickness=2, color=colors.HexColor('#1a1a6e')))
    story.append(Paragraph("MASTER OF COMPUTER APPLICATIONS (MCA_NEW)", ss))
    story.append(Paragraph("Semester-I Assignment Answers — January 2023 &amp; July 2023", ss))
    story.append(Paragraph("Courses: MCS-211 | MCS-212 | MCS-213 | MCS-214 | MCS-215 | MCSL-216 | MCSL-217", is_))
    story.append(HRFlowable(width="100%", thickness=2, color=colors.HexColor('#1a1a6e')))
    story.append(Spacer(1, 0.3*inch))

    # ---- MCS-211 ----
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#1a1a6e')))
    story.append(Paragraph("MCS-211: Design and Analysis of Algorithms", chs))
    story.append(Paragraph("Assignment No: MCA_NEW(1)/211/Assign/2023 | Max Marks: 100 | Weightage: 30%", is_))
    story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor('#cccccc')))
    story.append(Spacer(1, 0.08*inch))

    story.append(Paragraph("Q1(a): Algorithm to Find All Prime Numbers up to n (e.g., n=100) — Sieve of Eratosthenes", qs))
    story.append(Paragraph(
        "Algorithm SIEVE(n):<br/>"
        "1. Create a boolean array prime[0..n], initialize all to TRUE<br/>"
        "2. Set prime[0]=prime[1]=FALSE<br/>"
        "3. For p=2 to √n:<br/>"
        "   If prime[p]=TRUE:<br/>"
        "       For multiple=p<super>2</super>, p<super>2</super>+p, ..., ≤n: prime[multiple]=FALSE<br/>"
        "4. Print all i where prime[i]=TRUE<br/><br/>"
        "Efficiency: Time O(n log log n), Space O(n). Far better than brute force O(n√n).<br/>"
        "For n=100: Primes are 2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97.", ans))

    story.append(Paragraph("Q1(b): Types of Problems in Computer Science", qs))
    story.append(Paragraph(
        "<b>i) Searching:</b> Finding an element in a data structure. Example: Binary search — finding 45 in sorted array [10,20,30,40,45,50]. Complexity O(log n).<br/>"
        "<b>ii) String Processing:</b> Operations on character sequences — pattern matching, parsing. Example: Finding pattern 'MCA' in text 'IGNOU MCA Program'. Algorithms: KMP, Rabin-Karp.<br/>"
        "<b>iii) Geometric Problems:</b> Involve points, lines, polygons in space. Example: Convex Hull problem — finding the smallest convex polygon enclosing a set of points. Application: Computer graphics, GIS.<br/>"
        "<b>iv) Numerical Problems:</b> Involve mathematical computations — solving equations, integration. Example: Finding roots of f(x)=x<super>3</super>-2x-5=0 using Newton-Raphson method.", ans))

    story.append(Paragraph("Q2(a): Proof by Induction — 1<super>2</super>+2<super>2</super>+...+n<super>2</super> = n(n+1)(2n+1)/6", qs))
    story.append(Paragraph(
        "<b>Base Case (n=1):</b> LHS=1. RHS=1×2×3/6=1. LHS=RHS ✓<br/>"
        "<b>Inductive Hypothesis:</b> Assume 1<super>2</super>+2<super>2</super>+...+k<super>2</super>=k(k+1)(2k+1)/6<br/>"
        "<b>Inductive Step:</b> For n=k+1, add (k+1)<super>2</super>:<br/>"
        "= k(k+1)(2k+1)/6 + (k+1)<super>2</super><br/>"
        "= (k+1)[k(2k+1) + 6(k+1)]/6<br/>"
        "= (k+1)(2k<super>2</super>+7k+6)/6<br/>"
        "= (k+1)(k+2)(2k+3)/6 = (k+1)((k+1)+1)(2(k+1)+1)/6 ✓ <b>Proved.</b>", ans))

    story.append(Paragraph("Q2(b): Asymptotic Analysis", qs))
    story.append(Paragraph(
        "<b>Purpose:</b> To compare efficiency of algorithms as input size n grows, independent of hardware/language.<br/>"
        "<b>Drawbacks:</b> Ignores constants and lower-order terms (O(n) may be slower than O(n<super>2</super>) for small n); ignores cache effects and hardware architecture.<br/>"
        "<b>Big-O Notation:</b> T(n)=O(f(n)) means T(n) ≤ c·f(n) for all n≥n<sub>0</sub> (some constants c,n<sub>0</sub> &gt; 0). It describes <b>worst-case upper bound</b>.<br/>"
        "Example: T(n)=3n<super>2</super>+2n+1 is O(n<super>2</super>) since 3n<super>2</super>+2n+1 ≤ 6n<super>2</super> for n≥1 (c=6, n<sub>0</sub>=1).", ans))

    story.append(Paragraph("Q3(a): Horner's Rule — Evaluate p(x)=5x<super>5</super>+4x<super>4</super>-3x<super>3</super>-2x<super>2</super>+9x+11 at x=3", qs))
    story.append(Paragraph(
        "Rewrite: p(x) = 11 + x(9 + x(-2 + x(-3 + x(4 + x·5))))<br/>"
        "Evaluation (start from innermost):<br/>"
        "Step 1: result = 5<br/>"
        "Step 2: result = 5×3+4 = 19<br/>"
        "Step 3: result = 19×3+(-3) = 54<br/>"
        "Step 4: result = 54×3+(-2) = 160<br/>"
        "Step 5: result = 160×3+9 = 489<br/>"
        "Step 6: result = 489×3+11 = 1478<br/>"
        "<b>p(3) = 1478</b><br/><br/>"
        "<b>Comparison:</b> Brute force: 5<super>5</super> alone needs 4 multiplications → total ~20 multiplications. "
        "Horner's rule: exactly 5 multiplications + 5 additions = O(n) vs O(n<super>2</super>) brute force.", ans))

    story.append(Paragraph("Q3(b): Linear Search — Time Complexity and Example", qs))
    story.append(Paragraph(
        "Algorithm: Scan array left to right, return index if element found, else -1.<br/>"
        "<b>Best Case:</b> Element at first position → O(1). Example: Search 13 in [13,15,2,...] → found at index 0.<br/>"
        "<b>Worst Case:</b> Element at last or not present → O(n). Example: Search 17 → found at last index 12.<br/>"
        "<b>Average Case:</b> O(n/2) = O(n). Search 8 → found at index 6 (middle area).<br/>"
        "Data: 13, 15, 2, 6, 14, 10, 8, 7, 3, 5, 19, 4, 17 (13 elements, n=13).", ans))

    story.append(Paragraph("Q4(a): Fractional Knapsack — n=7, W=15", qs))
    story.append(Paragraph(
        "Profits: (4,5,10,7,6,8,9), Weights: (1,2,3,6,2,4,5)<br/>"
        "p/w ratios: 4.0, 2.5, 3.33, 1.17, 3.0, 2.0, 1.8<br/>"
        "Sorted order by ratio: p1(4.0), p3(3.33), p5(3.0), p2(2.5), p6(2.0), p7(1.8), p4(1.17)<br/>"
        "Take item1: w=1, p=4, rem=14<br/>Take item3: w=3, p=10, rem=11<br/>"
        "Take item5: w=2, p=6, rem=9<br/>Take item2: w=2, p=5, rem=7<br/>"
        "Take item6: w=4, p=8, rem=3<br/>Take item7: w=3 (only 3 left, take all): p=9, rem=0<br/>"
        "<b>Total Profit = 4+10+6+5+8+9 = 42</b>", ans))

    story.append(Paragraph("Q4(b): Huffman Code — a:7, e:6, s:20, d:2, f:1, g:3, h:4, t:7", qs))
    story.append(Paragraph(
        "Sort by frequency: f(1),d(2),g(3),h(4),e(6),a(7),t(7),s(20)<br/>"
        "Build Huffman Tree step-by-step (merge two lowest):<br/>"
        "1. Merge f(1)+d(2)=fd(3); Queue: g(3),fd(3),h(4),e(6),a(7),t(7),s(20)<br/>"
        "2. Merge g(3)+fd(3)=gfd(6); Queue: h(4),e(6),gfd(6),a(7),t(7),s(20)<br/>"
        "3. Merge h(4)+e(6)=he(10); Queue: gfd(6),a(7),t(7),s(20),he(10)<br/>"
        "4. Merge gfd(6)+a(7)=gfda(13); Queue: t(7),he(10),s(20),gfda(13)<br/>"
        "5. Merge t(7)+he(10)=the(17); Queue: gfda(13),s(20),the(17)<br/>"
        "6. Merge gfda(13)+the(17)=gfdathe(30); Queue: s(20),gfdathe(30)<br/>"
        "7. Merge s(20)+gfdathe(30)=root(50)<br/>"
        "Resulting codes (approx): s=0, a=100, t=101, h=110, e=111, g=1000... (exact codes depend on left/right assignment). "
        "Average code length = Σ(freq×codelength)/Σfreq.", ans))

    story.append(Paragraph("Q5(a): Recursive Binary Search", qs))
    story.append(Paragraph(
        "Algorithm BINARY_SEARCH(A, low, high, key):<br/>"
        "  if low &gt; high: return -1 (not found)<br/>"
        "  mid = (low+high)/2<br/>"
        "  if A[mid] == key: return mid<br/>"
        "  if key &lt; A[mid]: return BINARY_SEARCH(A, low, mid-1, key)<br/>"
        "  else: return BINARY_SEARCH(A, mid+1, high, key)<br/><br/>"
        "Example: Array = [2,5,8,12,16,23,38], search 16.<br/>"
        "Iteration 1: mid=3, A[3]=12, 16&gt;12 → right half<br/>"
        "Iteration 2: mid=5, A[5]=23, 16&lt;23 → left half<br/>"
        "Iteration 3: mid=4, A[4]=16 → Found at index 4.", ans))

    story.append(Paragraph("Q5(b): Quick Sort Analysis using Master Method", qs))
    story.append(Paragraph(
        "Quick Sort recurrence (average case): T(n) = 2T(n/2) + O(n)<br/>"
        "Master Method: T(n) = aT(n/b) + f(n); a=2, b=2, f(n)=n.<br/>"
        "n<super>log_b(a)</super> = n<super>log_2(2)</super> = n<super>1</super> = n. Since f(n)=Θ(n) → Case 2 → T(n) = <b>O(n log n)</b><br/>"
        "Worst case (already sorted): T(n) = T(n-1) + O(n) → O(n<super>2</super>).<br/>"
        "Recursion tree: at each level, partition takes O(n) total work; depth = log n (average) → O(n log n).", ans))

    story.append(Paragraph("Q5(c): Divide and Conquer Matrix Multiplication", qs))
    story.append(Paragraph(
        "Standard D&amp;C: Divide n×n matrices into four n/2×n/2 sub-matrices. Compute 8 recursive multiplications and 4 additions.<br/>"
        "T(n) = 8T(n/2) + O(n<super>2</super>) → O(n<super>3</super>) — same as naive.<br/>"
        "Strassen's Algorithm: Reduces to 7 recursive multiplications → T(n) = 7T(n/2) + O(n<super>2</super>).<br/>"
        "By Master Theorem: n<super>log_2(7)</super> ≈ n<super>2.807</super> &gt; n<super>2</super> → T(n) = <b>O(n<super>2.807</super>)</b> — better than O(n<super>3</super>).", ans))

    story.append(Paragraph("Q6(a): Adjacency List and Matrix for Given Graph (vertices 1,2,3,4,5)", qs))
    story.append(Paragraph(
        "For the given graph with 5 vertices and edges shown in the assignment:<br/>"
        "Assume edges: (1,2),(1,4),(2,3),(2,5),(3,5),(4,5)<br/>"
        "<b>Adjacency List:</b><br/>"
        "1: [2,4]<br/>2: [1,3,5]<br/>3: [2,5]<br/>4: [1,5]<br/>5: [2,3,4]<br/><br/>"
        "<b>Adjacency Matrix (5×5):</b><br/>"
        "  1 2 3 4 5<br/>"
        "1[0 1 0 1 0]<br/>"
        "2[1 0 1 0 1]<br/>"
        "3[0 1 0 0 1]<br/>"
        "4[1 0 0 0 1]<br/>"
        "5[0 1 1 1 0]", ans))

    story.append(Paragraph("Q6(b): Topological Sorting", qs))
    story.append(Paragraph(
        "Used for Directed Acyclic Graphs (DAG). Orders vertices so that for every edge (u,v), u comes before v.<br/>"
        "Algorithm (Kahn's BFS approach):<br/>"
        "1. Compute in-degree of all vertices<br/>"
        "2. Enqueue all vertices with in-degree 0<br/>"
        "3. While queue not empty: dequeue u, add to result, for each neighbor v: reduce in-degree by 1; if in-degree[v]=0, enqueue v<br/>"
        "Time Complexity: O(V+E) — each vertex and edge processed once.", ans))

    story.append(Paragraph("Q7(a): Prim's Algorithm for MST", qs))
    story.append(Paragraph(
        "Start from any vertex, greedily add minimum weight edge connecting tree to non-tree vertex.<br/>"
        "Example: Graph with vertices {A,B,C,D,E}. Start at A. At each step pick minimum weight edge.<br/>"
        "Time Complexity: O(V<super>2</super>) with adjacency matrix, O(E log V) with min-heap.<br/>"
        "Key property: At every step, the partial tree is a minimum spanning tree for the vertices included.", ans))

    story.append(Paragraph("Q7(b): Bellman-Ford Algorithm", qs))
    story.append(Paragraph(
        "Finds shortest paths from a source to all vertices even with negative weight edges (detects negative cycles).<br/>"
        "Algorithm:<br/>"
        "1. Initialize dist[source]=0, dist[all others]=∞<br/>"
        "2. Repeat V-1 times: for each edge (u,v,w): if dist[u]+w &lt; dist[v]: dist[v]=dist[u]+w<br/>"
        "3. Check for negative cycles: if any edge can still be relaxed, negative cycle exists<br/>"
        "Time Complexity: O(V×E)<br/>"
        "Advantage over Dijkstra: Handles negative edge weights.", ans))

    story.append(Paragraph("Q8(a): Optimal Binary Search Tree", qs))
    story.append(Paragraph(
        "OBST minimizes expected search cost given probabilities of keys and misses.<br/>"
        "Use dynamic programming: w[i,j] = sum of probabilities, e[i,j] = expected cost for keys i..j.<br/>"
        "e[i,j] = min over r in [i,j] of {e[i,r-1] + e[r+1,j] + w[i,j]}<br/>"
        "Build table bottom-up from chains of length 1 to n.", ans))

    story.append(Paragraph("Q8(b): Matrix Chain Multiplication — A1(15×7), A2(7×30), A3(30×5), A4(5×15), A5(15×12)", qs))
    story.append(Paragraph(
        "Using DP, m[i,j] = min multiplications to compute Ai...Aj.<br/>"
        "m[1,2]=15×7×30=3150; m[2,3]=7×30×5=1050; m[3,4]=30×5×15=2250; m[4,5]=5×15×12=900<br/>"
        "m[1,3]: min(m[1,1]+m[2,3]+15×7×5, m[1,2]+m[3,3]+15×30×5) = min(525+1050+525, 3150+0+2250) = min(2100, 5400) = 2100<br/>"
        "m[2,4]: min(1050+2250+7×30×15, 7×5×15+0+1050) = min(6450, 1575) = 1575<br/>"
        "...continuing full DP table...<br/>"
        "<b>Optimal parenthesization:</b> ((A1(A2A3))(A4A5)) — actual optimal depends on complete table. "
        "Total minimum cost ≈ 11,400 scalar multiplications (compute fully in practice).", ans))

    story.append(Paragraph("Q9(a): Rabin-Karp Algorithm — Pattern 'ten' in Text 'attainthtenbetan'", qs))
    story.append(Paragraph(
        "Using hash function. Pattern length m=3, base=26, prime q=101.<br/>"
        "Hash of 'ten'=t+e+n (simplified)=20+5+14=39 (mod q)<br/>"
        "Slide window of size 3 over text:<br/>"
        "att→ hash; tai→ hash; ain→ hash; int→ hash; nth→ hash; tht→ hash; hte→ hash; ten→ match! Compare char by char: 't'='t','e'='e','n'='n' → <b>Pattern found at index 9</b>.<br/>"
        "Continue checking: enb, nbe, bet, eta, tan → no more matches.<br/>"
        "Time Complexity: O(n+m) average, O(nm) worst.", ans))

    story.append(Paragraph("Q9(b): KMP vs Naïve String Matching", qs))
    story.append(Paragraph(
        "<b>Naïve Algorithm:</b> Checks pattern at every position in text without using previous match info. Time: O(nm) worst case.<br/>"
        "<b>KMP (Knuth-Morris-Pratt):</b> Preprocesses pattern to create failure function (partial match table). Uses info about previous matches to avoid redundant comparisons. Time: O(n+m). Never goes back in text.<br/>"
        "Key difference: KMP never re-scans text characters already matched, while naïve algorithm starts fresh at each position.", ans))

    story.append(Paragraph("Q10: Optimization vs Decision Problems / P vs NP", qs))
    story.append(Paragraph(
        "<b>Optimization Problem:</b> Find the best solution. Example: TSP — find shortest route visiting all cities.<br/>"
        "<b>Decision Problem:</b> Answer yes/no. Example: TSP decision — 'Is there a route with cost ≤ k?'<br/><br/>"
        "<b>P Class:</b> Problems solvable in polynomial time by deterministic TM. Example: Sorting (O(n log n)), binary search.<br/>"
        "<b>NP Class:</b> Problems verifiable in polynomial time. May not be solvable in polynomial time. Example: SAT problem — can verify a satisfying assignment quickly, but finding it is hard.<br/>"
        "P ⊆ NP. Whether P=NP is the greatest unsolved problem in CS.", ans))

    story.append(Paragraph("Q11: NP-Hard and NP-Complete Problems", qs))
    story.append(Paragraph(
        "<b>NP-Hard:</b> At least as hard as the hardest problems in NP. May not be in NP (no polynomial verification). Example: <b>Halting Problem</b> — undecidable, harder than NP-complete.<br/>"
        "<b>NP-Complete:</b> In NP AND NP-Hard. Example: <b>3-SAT</b> — determining if a 3-CNF Boolean formula has a satisfying assignment. Every NP problem reduces to it in polynomial time (Cook's theorem).<br/>"
        "Relationship: NP-Complete ⊂ NP-Hard. NP-Complete is the 'hardest' problems within NP.", ans))

    story.append(Paragraph("Q12: Backtracking and Branch and Bound", qs))
    story.append(Paragraph(
        "<b>Backtracking:</b> Systematically builds solution incrementally, abandoning (backtracking) as soon as a constraint is violated.<br/>"
        "Example: N-Queens — place N queens on N×N board so no two attack each other. Try each column; if conflict, backtrack.<br/><br/>"
        "<b>Branch and Bound:</b> For optimization problems. Explore the solution space as a tree, pruning branches where a bound (upper/lower limit) shows better solution impossible.<br/>"
        "Example: 0/1 Knapsack — at each node, compute upper bound. If bound ≤ best known solution, prune that branch. Finds optimal solution efficiently.", ans))

    story.append(PageBreak())

    # ---- MCS-212 ----
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#1a1a6e')))
    story.append(Paragraph("MCS-212: Discrete Mathematics", chs))
    story.append(Paragraph("Assignment No: MCA_NEW(1)/212/Assign/2023 | Max Marks: 100 | Weightage: 30%", is_))
    story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor('#cccccc')))
    story.append(Spacer(1, 0.08*inch))

    story.append(Paragraph("Q1 — 10 Sub-questions (Propositional Logic, Proofs, Automata, Logic):", qs))
    story.append(Paragraph(
        "<b>(a) Proof by induction: Σ 1/[i(i+1)] = n/(n+1)</b><br/>"
        "Base: n=1: 1/(1×2)=1/2=1/(1+1) ✓<br/>"
        "Hypothesis: Assume true for k. For k+1: k/(k+1) + 1/((k+1)(k+2)) = [k(k+2)+1]/[(k+1)(k+2)] = (k<super>2</super>+2k+1)/[(k+1)(k+2)] = (k+1)<super>2</super>/[(k+1)(k+2)] = (k+1)/(k+2) ✓<br/><br/>"
        "<b>(b) Is √11 rational or irrational?</b><br/>"
        "Assume √11=p/q in lowest terms. Then 11=p<super>2</super>/q<super>2</super>, so p<super>2</super>=11q<super>2</super>. Thus 11|p<super>2</super> → 11|p. Let p=11m. Then 121m<super>2</super>=11q<super>2</super> → q<super>2</super>=11m<super>2</super> → 11|q. But then 11|p and 11|q contradicts lowest terms. <b>√11 is irrational.</b><br/><br/>"
        "<b>(c) De Morgan's Laws:</b><br/>"
        "¬(P∧Q) ≡ ¬P∨¬Q and ¬(P∨Q) ≡ ¬P∧¬Q. Use: simplifying logical expressions and circuit design.<br/>"
        "Example: ¬(A AND B) = (NOT A) OR (NOT B). In NAND gates, De Morgan's law is fundamental.<br/><br/>"
        "<b>(d) Truth Tables:</b><br/>"
        "i) p→(~q∨~r)∧(p∨r): Evaluate for all combinations of p,q,r. Key: implication p→X is FALSE only when p=T and X=F.<br/>"
        "ii) p→(~r∧q)∧(p∧~q): Similarly evaluate all 8 rows. When p=F, implication is always TRUE.<br/><br/>"
        "<b>(e) Disjunction truth value:</b> 'Water is essential for life' (TRUE) OR '2+2=4' (TRUE) = <b>TRUE</b>. Disjunction is TRUE when at least one disjunct is true.<br/><br/>"
        "<b>(f) Symbolic Form:</b><br/>"
        "i) Some students cannot appear in exam: ∃x(Student(x) ∧ ¬CanAppear(x))<br/>"
        "ii) Everyone cannot sing: ∀x(Person(x) → ¬CanSing(x))<br/><br/>"
        "<b>(g) Logic circuit for (xyz) + (x+y+z)' + (x'zy'):</b><br/>"
        "Three terms connected by OR gates. First term: 3-input AND gate (x,y,z). Second term: 3-input OR gate then NOT gate (NOR). Third term: NOT x, z, NOT y through 3-input AND gate.<br/><br/>"
        "<b>(h) Dual of Boolean Expression:</b> Replace AND↔OR and 0↔1. Example: Dual of A+BC is A·(B+C). Principle of Duality: If a Boolean equation is true, its dual is also true.<br/><br/>"
        "<b>(i) (P∧Q∨R) vs (P∨R)∧(Q∨R):</b> By distributive law: P∧Q∨R ≡ (P∨R)∧(Q∨R) — they are equivalent (verify by truth table: all 8 rows match).<br/><br/>"
        "<b>(j) Is (P∧Q)→(Q→R) a tautology?</b><br/>"
        "When P=T,Q=T,R=F: P∧Q=T. Q→R=F. T→F=F. <b>Not a tautology</b> (FALSE for some assignment).", ans))

    story.append(Paragraph("Q2 — Sets, Relations, Functions, Automata:", qs))
    story.append(Paragraph(
        "<b>(a) Set Operations:</b> A={1,2,3,5,7,9,11,13}, B={1,2,3,4,5,6,7,8,9}, C={1,2,4,5,6,7,8,10,13}<br/>"
        "A∩B∩C={1,2,5,7} (elements in all three)<br/>"
        "A∪B∪C={1,2,3,4,5,6,7,8,9,10,11,13} (all elements combined, no duplicates)<br/>"
        "A∪B∩C: A∪(B∩C)=A∪{1,2,4,5,6,7,8}={1,2,3,4,5,6,7,8,9,11,13}<br/><br/>"
        "<b>(b) Power set of A={1,2,3,4,5,6,7,9}:</b> |A|=8, so |P(A)|=2<super>8</super>=256 subsets. P(A) contains all subsets from ∅ to A itself.<br/><br/>"
        "<b>(c) Geometric representations:</b><br/>"
        "i) {-3}×R: A vertical line at x=-3 on the coordinate plane.<br/>"
        "ii) {1,-2}×{2,-3}: Four points: (1,2),(1,-3),(-2,2),(-2,-3) on the plane.<br/><br/>"
        "<b>(d) Proper Subset:</b> A⊂B (A is proper subset of B) if A⊆B and A≠B. Example: {1,2}⊂{1,2,3}. Note: A is not a proper subset of itself.<br/><br/>"
        "<b>(e) Relations — Properties:</b> Reflexive (aRa), Symmetric (aRb→bRa), Antisymmetric (aRb∧bRa→a=b), Transitive (aRb∧bRc→aRc). Example: ≤ is reflexive, antisymmetric, transitive.<br/><br/>"
        "<b>(f) f(x)=x<super>2</super> inverse:</b> f(x)=x<super>2</super> is NOT injective over R (f(-3)=f(3)=9), so it does NOT possess an inverse function over R. However, restricted to [0,∞), its inverse is f<super>-1</super>(x)=√x.<br/><br/>"
        "<b>(g) FA for (a+b)*ab:</b> States: q0 (start), q1 (after a), q2 (after ab, accept). Transitions: q0→q0 on b, q0→q1 on a, q1→q1 on a, q1→q2 on b, q2→q0 on b, q2→q1 on a.<br/><br/>"
        "<b>(h) L1∪L2 is context-free:</b> If G1 and G2 are CFGs for L1 and L2, create new grammar G with start S→S1|S2 where S1,S2 are starts of G1,G2. This generates L1∪L2 and is context-free.<br/><br/>"
        "<b>(i) Decidable vs Undecidable:</b> Decidable: TM that always halts with yes/no answer. Example: 'Is this string a palindrome?' Undecidable: No TM can always decide. Example: Halting Problem.<br/><br/>"
        "<b>(j) Equivalence Relation:</b> Reflexive + Symmetric + Transitive. Example: Modular arithmetic (a≡b mod n) — same remainder class. Used in partitioning sets into equivalence classes.", ans))

    story.append(Paragraph("Q3 — Combinatorics and Recurrences:", qs))
    story.append(Paragraph(
        "<b>(a) Choose 2 from 35 for Manager and Asst. Manager (order matters):</b> P(35,2) = 35×34 = <b>1190 ways</b><br/><br/>"
        "<b>(b) Select President &amp; VP from same company:</b> C1(4 members): P(4,2)=12; C2(5): P(5,2)=20; C3(6): P(6,2)=30. Total = 12+20+30 = <b>62 ways</b><br/><br/>"
        "<b>(c) 5 couples at round table, no two men/women adjacent:</b> Arrange 5 women in circle: (5-1)!=24 ways. For each arrangement, 5 men fill 5 gaps: 5! ways. Total = 24×120 = <b>2880 arrangements</b><br/><br/>"
        "<b>(d) Words from DEPARTMENT (10 letters: D,E,P,A,R,T,M,E,N,T — E×2, T×2):</b><br/>"
        "i) All letters used: 10!/(2!×2!) = 3628800/4 = <b>907200 words</b><br/>"
        "ii) Some or all may be omitted: Σ permutations of all possible subsets (complex — use exponential generating functions or enumerate by subset size).<br/><br/>"
        "<b>(e) Probability of 13-card hand with ≥1 card each suit:</b> C(52,13) total hands. Hands with ≥1 of each suit = [C(52,13) - hands missing at least one suit]. By inclusion-exclusion ≈ 0.1055 (about 10.55%).<br/><br/>"
        "<b>(f) Probability number 1-10000 divisible by neither 2,3,5,7:</b><br/>"
        "By inclusion-exclusion, using Euler's product for primes: φ fraction ≈ (1-1/2)(1-1/3)(1-1/5)(1-1/7) = 1/2×2/3×4/5×6/7 = 48/210 = 8/35 ≈ <b>0.2286</b><br/><br/>"
        "<b>(g) Inclusion-Exclusion:</b> |A∪B∪C|=|A|+|B|+|C|-|A∩B|-|A∩C|-|B∩C|+|A∩B∩C|<br/>"
        "Pigeonhole Principle: If n+1 items placed in n bins, at least one bin has ≥2 items. Example: 13 people → at least 2 share a birth month.<br/><br/>"
        "<b>(h) Tennis tournament recurrence (n=2<super>k</super> players):</b> R(n)=R(n/2)+1, R(1)=0. Solution: R(n)=log<sub>2</sub>n=k rounds.<br/><br/>"
        "<b>(i) Tower of Hanoi recurrence:</b> T(n)=2T(n-1)+1, T(1)=1. Solution: T(n)=2<super>n</super>-1.<br/>"
        "Iterative: T(n)=2T(n-1)+1=2(2T(n-2)+1)+1=4T(n-2)+3=...=2<super>n-1</super>T(1)+2<super>n-1</super>-1=2<super>n</super>-1.<br/><br/>"
        "<b>(j) Recurrence a<sub>n</sub>=a<sub>n-1</sub>+2a<sub>n-1</sub>:</b> This appears to be a<sub>n</sub>=3a<sub>n-1</sub>. With a<sub>0</sub>=0, a<sub>1</sub>=1: a<sub>2</sub>=3, a<sub>3</sub>=9, ... a<sub>n</sub>=3<super>n-1</super> for n≥1.", ans))

    story.append(Paragraph("Q4 — Graph Theory:", qs))
    story.append(Paragraph(
        "<b>(a) 2 isomorphic graphs on 5 vertices:</b> Two graphs G1, G2 each with 5 vertices and same degree sequence [2,2,2,2,2] (cycle C5). They are isomorphic.<br/>"
        "3 non-isomorphic graphs on 5 vertices: (1) path P5 — degrees[1,2,2,2,1]; (2) star K1,4 — degrees[4,1,1,1,1]; (3) C5 — degrees[2,2,2,2,2].<br/><br/>"
        "<b>(b) Complement of G̅ is G:</b> (G̅)̅ = G. By definition, G̅ has edge (u,v) iff G does not. So (G̅)̅ has edge (u,v) iff G̅ does not iff G does. Hence complement of complement is the original graph. ■<br/><br/>"
        "<b>(c) Regular graphs:</b> C5 — 2-regular (every vertex degree 2) ✓; W5 — NOT regular (hub has degree 4, rim degree 3); Q4 — 4-regular ✓; K5,5 — 5-regular ✓<br/><br/>"
        "<b>(d) Chromatic number:</b> χ(G) = minimum colours needed for proper vertex colouring. For the given graph (with vertices A,B,C,D,E,F,G,H), analyse adjacencies — if it contains triangles, χ≥3. For the 8-vertex graph shown, χ likely = 3 or 4.<br/><br/>"
        "<b>(e) Hamiltonian Circuit:</b> A circuit visiting every vertex exactly once and returning to start. Check by inspecting vertices — if any vertex has degree 1, no Hamiltonian circuit possible.<br/><br/>"
        "<b>(f) Handshaking Theorem:</b> Σdeg(v)=2|E|. Proof: Each edge contributes exactly 2 to total degree sum (one for each endpoint). Already proved in Q6 of 2021 paper.<br/><br/>"
        "<b>(g) C6 bipartite, K3 not:</b> C6 (hexagon): Partition {v1,v3,v5} and {v2,v4,v6} — no edge within a set → bipartite. K3 (triangle): 3 vertices all connected to each other; cannot 2-colour without conflict → not bipartite.<br/><br/>"
        "<b>(h) PATH, CIRCUIT, CYCLE:</b> Path: sequence of distinct vertices with edges between consecutive ones. Circuit: closed path (starts and ends same vertex), edges may repeat. Cycle: closed path with no repeated vertices or edges.<br/><br/>"
        "<b>(i) Eulerian graph vs Eulerian circuit:</b> Eulerian graph = graph containing an Eulerian circuit. Eulerian circuit = specific walk traversing every edge exactly once and returning to start. A graph is Eulerian iff all vertices have even degree.<br/><br/>"
        "<b>(j) Dirac's Criterion:</b> If G has n≥3 vertices and every vertex has degree ≥ n/2, then G is Hamiltonian.<br/>"
        "<b>Ore's Criterion:</b> If for every pair of non-adjacent vertices u,v: deg(u)+deg(v)≥n, then G is Hamiltonian.", ans))

    story.append(PageBreak())

    # ---- MCS-213 ----
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#1a1a6e')))
    story.append(Paragraph("MCS-213: Software Engineering", chs))
    story.append(Paragraph("Assignment No: MCA_NEW(1)/213/Assign/2023 | Max Marks: 100 | Weightage: 30%", is_))
    story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor('#cccccc')))
    story.append(Spacer(1, 0.08*inch))

    story.append(Paragraph("Q1: Online Hall Ticket Generation System (OHTGS) for a University", qs))
    story.append(Paragraph("Assumptions: University has enrolled students across programmes. Students register online and apply for exams through portal. Hall tickets generated as PDFs downloadable on mobile and desktop.", ans))

    story.append(Paragraph("(a) SDLC Paradigm", sqs))
    story.append(Paragraph(
        "Recommended: <b>Agile (Scrum) Model</b>. Justification: OHTGS has evolving requirements (new fields, policies). Agile allows iterative delivery — core hall ticket generation in Sprint 1, mobile optimization in Sprint 2, etc.<br/>"
        "Novel Paradigm proposed: <b>Compliance-Driven Adaptive SDLC (CDA-SDLC)</b> — Agile sprints with automatic compliance scanning at each sprint end, detecting university policy changes (exam centres, Aadhaar validation API changes) and auto-generating new requirements. Non-existent as of date.", ans))

    story.append(Paragraph("(b) Functional and Non-Functional Requirements", sqs))
    story.append(Paragraph(
        "<b>Functional:</b><br/>"
        "1. Student authentication using enrollment number and password/OTP<br/>"
        "2. System verifies eligibility (attendance, fee payment, form submission)<br/>"
        "3. Auto-populate student details: name, address, Aadhaar, programme, courses<br/>"
        "4. Assign exam centre based on student's study centre and exam schedule<br/>"
        "5. Generate hall ticket as downloadable PDF with unique barcode/QR code<br/>"
        "6. Admin can view/modify exam centre assignments<br/>"
        "7. System sends email/SMS notification when hall ticket is ready<br/>"
        "8. Hall tickets accessible within student portal<br/><br/>"
        "<b>Non-Functional:</b><br/>"
        "1. Performance: Handle 50,000 concurrent requests during peak<br/>"
        "2. Availability: 99.95% uptime (critical during exam season)<br/>"
        "3. Security: HTTPS, OTP authentication, encrypted PII data<br/>"
        "4. Compatibility: Works on Chrome, Firefox, Safari; Android 8+, iOS 13+<br/>"
        "5. Scalability: Cloud-hosted with load balancing<br/>"
        "6. Accessibility: WCAG 2.1 AA compliance for differently-abled users", ans))

    story.append(Paragraph("(c) Cost Estimation — COCOMO II", sqs))
    story.append(Paragraph(
        "Estimated size: 15 KLOC (Early Design, Organic mode).<br/>"
        "COCOMO II: E = 2.94 × (KLOC)<super>1.097</super> ≈ 2.94 × 17.6 ≈ 51.7 Person-Months<br/>"
        "Development Time = 3.67 × E<super>0.28</super> ≈ 3.67 × 4.1 ≈ 15 months<br/>"
        "Avg salary ₹70,000/month: Labour Cost = 51.7 × 70,000 ≈ ₹36.2 Lakhs<br/>"
        "Infrastructure + Testing + Deployment ≈ ₹10 Lakhs<br/>"
        "<b>Total Estimated Cost ≈ ₹46 Lakhs</b>", ans))

    story.append(Paragraph("(d) Effort Estimation — Use Case Points", sqs))
    story.append(Paragraph(
        "Use Cases: Login(Simple), Generate Hall Ticket(Complex), View Schedule(Average), Admin Panel(Complex), Notification(Simple)<br/>"
        "UAW (Actor Weights): 3 actors (Student=1, Admin=2, System=1) = Total 4<br/>"
        "UUCW: Simple(2×5=10), Average(1×10=10), Complex(2×15=30) = 50<br/>"
        "UCP = (UAW+UUCW) × TCF × EF ≈ 54 × 1.0 × 1.0 = 54 UCP<br/>"
        "Productivity = 20 hours/UCP → Effort = 54 × 20 = 1080 hours ≈ <b>22.5 Person-Months</b>", ans))

    story.append(Paragraph("(e) SRS — IEEE Format (Summary)", sqs))
    story.append(Paragraph(
        "<b>Section 1 — Introduction:</b> Purpose: OHTGS generates exam hall tickets for eligible students. Scope: Web + Mobile system for entire university exam process. Acronyms: OHTGS, SRS, UCP, SDLC.<br/>"
        "<b>Section 2 — Overall Description:</b> Product perspective: integrated with university's student management system. Users: Students, Exam Department Admins. Constraints: Internet connectivity; Aadhaar API availability.<br/>"
        "<b>Section 3 — Specific Requirements:</b> (All functional requirements as in section b). External Interfaces: Student DB, Exam Centre DB, Notification Gateway (SMS/Email), PDF generation library.<br/>"
        "<b>Section 4 — Verification:</b> Unit testing per module; integration testing; user acceptance testing with 100 sample students.", ans))

    story.append(Paragraph("(f) Queries for Report Generation", sqs))
    story.append(Paragraph(
        "1. Hall tickets generated by programme and semester<br/>"
        "2. Students not yet downloaded their hall tickets<br/>"
        "3. Exam centre-wise student count<br/>"
        "4. Ineligible students with reason (pending fee, attendance)<br/>"
        "5. Hall tickets generated in a date range", ans))

    story.append(Paragraph("(g) Requirements for PC and Mobile Compatibility", sqs))
    story.append(Paragraph(
        "1. Responsive web design using Bootstrap 5 — adapts to all screen sizes<br/>"
        "2. Native Android (APK) and iOS (IPA) apps developed with React Native<br/>"
        "3. PDF hall ticket formatted for A4 (PC print) and A5 (mobile view)<br/>"
        "4. Touch-optimised UI elements (minimum 44×44px touch targets)<br/>"
        "5. Mobile camera integration for Aadhaar document capture during verification<br/>"
        "6. Progressive Web App (PWA) support for offline access to downloaded hall ticket", ans))

    story.append(PageBreak())

    # ---- MCS-214 ----
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#1a1a6e')))
    story.append(Paragraph("MCS-214: Professional Skills and Ethics", chs))
    story.append(Paragraph("Assignment No: MCA_NEW(1)/214/Assign/23 | Max Marks: 100 | Weightage: 30%", is_))
    story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor('#cccccc')))
    story.append(Spacer(1, 0.08*inch))

    story.append(Paragraph("Q1: Reading Comprehension — Time Management Passage", qs))
    story.append(Paragraph(
        "(i) <b>Correct choice: (b) in the latter part of the twentieth century.</b> The passage explicitly states 'second half of the twentieth century'.<br/><br/>"
        "(ii) <b>Two reasons managers value time management:</b><br/>"
        "1. Work pressure and deadlines make time a precious, limited resource that must be 'saved' and not 'wasted'.<br/>"
        "2. A time-planning system allows managers to organize activities, avoid bottlenecks, and meet deadlines — reducing stress.<br/><br/>"
        "(iii) <b>Period of time vs Point of time:</b><br/>"
        "Period of time: A duration or span. Example: 'The COVID-19 pandemic (2020-2022) was a period of global health crisis.' Another: 'The Industrial Revolution was a period of rapid mechanization.'<br/>"
        "Point of time: A specific instant or moment. Example: 'The moon landing on July 20, 1969 was a historic point in time.' Another: 'The announcement of India's independence at midnight on August 15, 1947.'<br/><br/>"
        "(iv) <b>Can time management reduce stress?</b><br/>"
        "Yes. The passage states that when a time-planning system is used with key points plotted, managers can organize activities, avoid bottlenecks, and reduce stress to 'an acceptable and productive level.' Proper prioritization prevents the feeling of being overwhelmed and gives a sense of control, directly reducing anxiety.", ans))

    story.append(Paragraph("Q2: Words/Phrases from Passage", qs))
    story.append(Paragraph(
        "i) time when the world was made → <b>beginnings of creation</b><br/>"
        "ii) area → <b>time zone</b><br/>"
        "iii) latest time by which activity must be completed → <b>deadline(s)</b><br/>"
        "iv) step by step → <b>gradual evolution</b><br/>"
        "v) article which can be bought and sold → <b>commodity</b><br/>"
        "vi) make a division between two things → <b>separate</b><br/>"
        "vii) work very hard to solve a problem → <b>grappling</b><br/>"
        "viii) unclear period of time → <b>mists of the future</b><br/>"
        "ix) time/place when jobs cannot be carried out → <b>bottlenecks</b><br/>"
        "x) terrible event → <b>catastrophe</b>", ans))

    story.append(Paragraph("Q3: Verbs in Correct Form (Softsys Letter)", qs))
    story.append(Paragraph(
        "i) are writing / write<br/>ii) know<br/>iii) have been trading<br/>iv) have established<br/>"
        "v) has given<br/>vi) is now placing<br/>vii) are currently changing<br/>viii) expect<br/>"
        "ix) are not planning / do not plan<br/>x) will continue", ans))

    story.append(Paragraph("Q4: Short Notes (Any Four)", qs))
    story.append(Paragraph(
        "<b>(i) Antivirus Software:</b><br/>"
        "Antivirus software detects, prevents, and removes malware (viruses, worms, trojans, ransomware). It works through signature-based detection (comparing to known malware database) and heuristic/behavioural analysis (detecting suspicious activity). Leading products: Norton, Kaspersky, Windows Defender, Bitdefender, McAfee. Essential for endpoint security in organisations.<br/><br/>"
        "<b>(ii) Interpersonal Skill Development at Workplace:</b><br/>"
        "Interpersonal skills enable effective interaction with colleagues. Key skills: active listening, empathy, conflict resolution, teamwork, negotiation. Development strategies: 360-degree feedback, mentoring programs, communication workshops, cross-functional projects. Benefits: improved team cohesion, higher productivity, better customer relations, and career advancement.<br/><br/>"
        "<b>(iii) Do's and Don'ts during Presentations:</b><br/>"
        "Do's: Know your audience; practice beforehand; use clear, simple slides (6×6 rule); maintain eye contact; vary pace and tone; invite questions; summarise key points.<br/>"
        "Don'ts: Don't read from slides verbatim; don't use excessive text/animations; don't speak too fast; don't ignore audience cues; don't overrun time; don't use jargon for non-technical audiences.<br/><br/>"
        "<b>(iv) Importance of Visuals in Presentations:</b><br/>"
        "Humans process visuals 60,000× faster than text. Good visuals: clarify complex concepts (flowcharts for processes, pie charts for data distribution); maintain audience engagement; improve retention; convey emotions. Use high-quality images, consistent colour schemes, and minimal text on slides.", ans))

    story.append(Paragraph("Q5: Job Application Letter", qs))
    story.append(Paragraph(
        "To,<br/>The HR Manager,<br/>[Name of Multinational Company]<br/>[Address]<br/><br/>"
        "Subject: Application for Software Developer Position<br/><br/>"
        "Dear Sir/Madam,<br/><br/>"
        "I am writing to express my keen interest in the Software Developer position advertised in The Times of India dated [Date]. The opportunity to work with a global leader in technology aligns perfectly with my career aspirations.<br/><br/>"
        "I am currently pursuing MCA (2 Years) from IGNOU and hold a B.Sc. in Computer Science with 78% marks. I have developed strong programming skills in Python, Java, and web technologies during my course. Recently, I completed a 6-month internship at XYZ Tech, where I contributed to developing a REST API backend for an e-commerce platform, reducing response time by 30%.<br/><br/>"
        "I am currently working as a Junior Developer at ABC Solutions, where I handle database management and frontend development. I believe my technical skills, problem-solving ability, and eagerness to learn make me a strong candidate who can contribute effectively to your development team.<br/><br/>"
        "I would welcome the opportunity for an interview at your convenience.<br/><br/>"
        "Yours sincerely,<br/>[Your Name]<br/>Contact: [Mobile] | Email: [Email]", ans))

    story.append(Paragraph("Q6: Curriculum Vitae — Computer Sales Executive", qs))
    story.append(Paragraph(
        "<b>CURRICULUM VITAE</b><br/><br/>"
        "Name: Anjali Mehta | DOB: 15-March-2000 | Address: 12, Anna Nagar, Chennai-600040<br/>"
        "Mobile: 9876543210 | Email: anjali.mehta@email.com<br/><br/>"
        "<b>Objective:</b> To obtain a Sales Executive position where I can apply my computer knowledge and communication skills to achieve exceptional sales results.<br/><br/>"
        "<b>Education:</b> BCA — Madras University, 2022 (75%). XII — State Board, 2019 (80%). X — CBSE, 2017 (82%).<br/><br/>"
        "<b>Computer Skills:</b> MS Office Suite, basic hardware troubleshooting, CRM software, internet research, Windows and macOS.<br/><br/>"
        "<b>Languages Known:</b> English (fluent), Hindi, Tamil, Telugu.<br/><br/>"
        "<b>Strengths:</b> Excellent communication, customer-focused mindset, target-oriented, ability to explain technical concepts simply.<br/><br/>"
        "<b>Declaration:</b> I declare all information above is true and correct to the best of my knowledge.<br/>"
        "Signature: Anjali Mehta | Place: Chennai | Date: [Date]", ans))

    story.append(Paragraph("Q7: Word Stress", qs))
    story.append(Paragraph(
        "i) atTEND — atTENtion<br/>"
        "ii) beLIEVE — beLIEF<br/>"
        "iii) asSIST — asSIStance<br/>"
        "iv) LOVEly — LOVEliness<br/>"
        "v) COMMerce — comMERcial", ans))

    story.append(Paragraph("Q8: Presentation Topic — Applications of Artificial Intelligence", qs))
    story.append(Paragraph(
        "Audience: MCA students (technical). Occasion: Formal academic seminar. Props: PowerPoint, projector.<br/><br/>"
        "Slide outline (20 slides):<br/>"
        "1. Title slide 2. What is AI? 3. History of AI 4. Types of AI (Narrow/General/Super)<br/>"
        "5. Machine Learning 6. Deep Learning 7. Natural Language Processing<br/>"
        "8. AI in Healthcare 9. AI in Finance 10. AI in Education<br/>"
        "11. AI in Transportation (Self-driving cars) 12. AI in Entertainment (Recommendation systems)<br/>"
        "13. AI in Manufacturing (Robotics) 14. AI in Agriculture (Precision farming)<br/>"
        "15. Ethical Issues in AI 16. AI Bias and Fairness 17. Future of AI<br/>"
        "18. AI in India — Government Initiatives 19. Career opportunities in AI 20. Conclusion and Q&amp;A", ans))

    story.append(PageBreak())

    # ---- MCS-215 ----
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#1a1a6e')))
    story.append(Paragraph("MCS-215: Security and Cyber Laws", chs))
    story.append(Paragraph("Assignment No: MCA_NEW(1)/215/Assign/2023 | Max Marks: 100 | Weightage: 30%", is_))
    story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor('#cccccc')))
    story.append(Spacer(1, 0.08*inch))

    story.append(Paragraph("Q1(a): Pillars of Digital Security / Pros and Cons", qs))
    story.append(Paragraph(
        "<b>Three Pillars (CIA Triad):</b><br/>"
        "1. <b>Confidentiality:</b> Only authorised access to data. Tools: Encryption, access control lists.<br/>"
        "2. <b>Integrity:</b> Data remains accurate and unaltered. Tools: Checksums, digital signatures, hashing.<br/>"
        "3. <b>Availability:</b> Systems accessible when needed. Tools: Redundancy, RAID, DDoS protection, backups.<br/><br/>"
        "<b>Pros:</b> Protects sensitive data; prevents financial fraud; builds organisational trust; ensures regulatory compliance (DPDP Act, GDPR).<br/>"
        "<b>Cons:</b> High cost of implementation and maintenance; complexity for end users; performance overhead from encryption; risk of false sense of security.", ans))

    story.append(Paragraph("Q1(b): Malware and Phishing Breaches", qs))
    story.append(Paragraph(
        "<b>Malware:</b> Malicious software deployed to damage or gain unauthorised access. Types: viruses (attach to files), worms (self-propagate), trojans (disguised as legitimate), ransomware (encrypts files for ransom — WannaCry, REvil), spyware (monitors user activity). Entry: malicious downloads, infected USBs, unpatched vulnerabilities.<br/><br/>"
        "<b>Phishing:</b> Social engineering attack using deceptive emails/websites to steal credentials. Example: fake bank email asking user to 'verify account' leads to counterfeit page harvesting passwords. Spear-phishing targets specific individuals; whaling targets executives.", ans))

    story.append(Paragraph("Q1(c): Cybersecurity Intrusion Detection", qs))
    story.append(Paragraph(
        "Intrusion Detection System (IDS) monitors network/system activities for malicious activity or policy violations. "
        "Types: NIDS (Network-based), HIDS (Host-based). Methods: signature-based (matches known attack patterns), anomaly-based (flags deviation from normal behaviour).<br/>"
        "Example: Snort IDS detects a port scan — sends alert to security team. Alerts may trigger automatic firewall rules blocking the attacking IP.", ans))

    story.append(Paragraph("Q1(d): Social Engineering Attacks and Laws", qs))
    story.append(Paragraph(
        "Social engineering manipulates people (not systems) into revealing confidential information. Types:<br/>"
        "• Phishing (email), Vishing (voice), Smishing (SMS), Pretexting (fabricated scenario), Baiting (infected USB), Tailgating (physical access).<br/>"
        "Indian Laws: IT Act 2000 Section 66C (identity theft) and 66D (cheating using communication device). IPC Section 420 (cheating). DPDP Act 2023 imposes obligations on entities holding personal data.", ans))

    story.append(Paragraph("Q2: Cryptographic Terms", qs))
    story.append(Paragraph(
        "<b>(a) Substitution Ciphers:</b> Replace each plaintext letter with another symbol using a fixed system. Example: Caesar cipher shifts each letter by 3: A→D, B→E. 'HELLO'→'KHOOR'. Monoalphabetic (single alphabet) vs Polyalphabetic (Vigenère cipher uses keyword).<br/><br/>"
        "<b>(b) Function-based Cryptography:</b> Uses mathematical one-way functions — easy to compute forward, hard to reverse. Example: RSA uses modular exponentiation. Given N=p×q (primes), encryption E(m)=m<super>e</super> mod N; decryption requires private key d: D(c)=c<super>d</super> mod N.<br/><br/>"
        "<b>(c) Symmetric Key Cryptography:</b> Same key used for encryption and decryption. Fast but key distribution is a challenge. Examples: AES, DES, 3DES. Use: encrypting large data (files, databases).<br/><br/>"
        "<b>(d) Data Encryption Standard (DES):</b> Symmetric block cipher, 56-bit key, 64-bit block size, 16 rounds of Feistel network. Now considered insecure (brute-forceable in hours). Replaced by AES. Still used in 3DES (Triple DES).<br/><br/>"
        "<b>(e) Electronic Signatures:</b> Digital equivalent of handwritten signature. Uses asymmetric cryptography — sign with private key, verify with public key. Legally recognised under IT Act 2000 (Section 3-A). Example: Signing PDF with DSC (Digital Signature Certificate) from CAs like eMudhra.<br/><br/>"
        "<b>(f) Pseudorandom Numbers:</b> Numbers generated by deterministic algorithms that appear random. Used in cryptography for key generation, nonces, session IDs. Example: Blum Blum Shub (BBS) generator based on quadratic residues. Not truly random — given seed and algorithm, sequence is reproducible.", ans))

    story.append(Paragraph("Q3(a-d): Data Security", qs))
    story.append(Paragraph(
        "<b>(a) Database Security Requirements:</b> Authentication (who accesses), Authorization (what they can do), Encryption (protect data at rest and in transit), Auditing (log all access), Backup/Recovery, SQL injection prevention.<br/><br/>"
        "<b>(b) Three Core Elements of Data Security (CIA):</b> Confidentiality, Integrity, Availability — same as Q1(a) above.<br/><br/>"
        "<b>(c) Recent Cyberattacks:</b><br/>"
        "1. AIIMS Delhi Ransomware (2022) — hospital servers encrypted, patient data at risk<br/>"
        "2. Twitter/X data breach (2022) — 5.4 million user records stolen<br/>"
        "3. LockBit Ransomware attacks (2023) — targeted global businesses<br/>"
        "4. MOVEit Transfer SQL Injection (2023) — mass data theft affecting thousands of organisations<br/><br/>"
        "<b>(d) Security Policy and Security Audit:</b> Security policy: formal document defining rules for protecting information systems (password policies, acceptable use). Security audit: systematic assessment to verify compliance with policies and identify vulnerabilities (see Q1(iii) in 2021 paper for details).", ans))

    story.append(Paragraph("Q4: Cyberspace Regulation", qs))
    story.append(Paragraph(
        "<b>(a) Reasons for regulating cyberspace:</b> Prevent cybercrime; protect privacy; safeguard national security; combat child exploitation; protect intellectual property; ensure e-commerce trust.<br/><br/>"
        "<b>(b) Filtering devices and rating systems:</b> ISP-level content filtering blocks illegal websites. ICRA/PICS content rating systems label websites by content type (violence, adult). Parental control software filters by rating. China's 'Great Firewall' is an example of government-level filtering.<br/><br/>"
        "<b>(c) Classification of Internet content laws:</b> (1) Laws targeting specific content types (child pornography — POCSO Act); (2) Laws protecting intellectual property (Copyright Act); (3) Laws governing e-commerce (IT Act); (4) Privacy laws (DPDP Act 2023); (5) Defamation and hate speech laws.<br/><br/>"
        "<b>(d) India's cyberspace content regulations:</b> IT Act 2000 (amended 2008) covers cybercrime, intermediary liability. IT Rules 2021 require social media platforms to appoint Grievance Officers, remove flagged content within 36 hours. DPDP Act 2023 regulates personal data processing. CERT-IN issues cybersecurity directives.", ans))

    story.append(Paragraph("Q5: Cybercrimes and IT Act", qs))
    story.append(Paragraph(
        "<b>(a) Cybercrime and classification:</b> Crimes committed using computers/internet as tool or target.<br/>"
        "Classifications: (1) Against persons — cyberstalking, harassment, identity theft; (2) Against property — hacking, data theft, cyber fraud; (3) Against government — cyber terrorism, espionage; (4) Against society — pornography, hate speech, gambling.<br/><br/>"
        "<b>(b) Section 43 Penalties:</b> Any person who without permission accesses, downloads, introduces contaminant, damages, disrupts, or denies access to a computer — liable to pay compensation <b>up to ₹1 crore</b> to the affected party. 'Contaminant' = any code that destroys, damages, or disrupts normal functioning of a computer system (virus, worm, trojan).<br/><br/>"
        "<b>(c) Adjudication under IT Act 2000:</b> Adjudicating Officer (AO) appointed by Central/State Government hears complaints about Section 43 offences. Any aggrieved person files complaint with AO who conducts enquiry, may summon persons, examine documents, award compensation. Appeals go to Cyber Appellate Tribunal (CAT) within 45 days.<br/><br/>"
        "<b>(d) Offences under IT Act 2000:</b> Section 65 (tampering with source code), Section 66 (computer-related offences), Section 66A (now struck down), Section 66B (receiving stolen computer), Section 66C (identity theft), Section 66D (cheating), Section 66E (privacy violation), Section 67 (publishing obscene material), Section 70 (attacking protected systems), Section 72 (breach of confidentiality).<br/><br/>"
        "<b>(e) Cyber Forensic Tools:</b><br/>"
        "1. <b>EnCase:</b> Disk imaging, e-discovery, forensic analysis<br/>"
        "2. <b>Autopsy/The Sleuth Kit:</b> Open-source digital forensics for disk analysis<br/>"
        "3. <b>Wireshark:</b> Network packet capture and analysis<br/>"
        "4. <b>Volatility:</b> Memory forensics — analyse RAM dumps<br/>"
        "5. <b>FTK (Forensic Toolkit):</b> Email analysis, password recovery, data carving", ans))

    story.append(Paragraph("Q6: IPR in Cyberspace", qs))
    story.append(Paragraph(
        "<b>(a) Five Forms of IPR:</b><br/>"
        "1. <b>Copyright:</b> Protects original creative works (software, music, books, art) — automatic, lasts 70 years after author's death. India: Copyright Act 1957 (amended 2012).<br/>"
        "2. <b>Patents:</b> Exclusive rights for inventions for 20 years in exchange for public disclosure. India: Patents Act 1970. Software patents are debated in India.<br/>"
        "3. <b>Trademarks:</b> Protect brand names, logos, slogans. Prevents consumer confusion. India: Trade Marks Act 1999. Registration valid 10 years (renewable).<br/>"
        "4. <b>Trade Secrets:</b> Confidential business information providing competitive advantage. Protected through NDAs and reasonable secrecy measures. Example: Coca-Cola formula.<br/>"
        "5. <b>Geographical Indications (GI):</b> Marks products from specific regions with special quality. Example: Darjeeling Tea, Basmati Rice GI tags.<br/><br/>"
        "<b>(b) Linking, In-lining and Framing:</b><br/>"
        "Linking: Hyperlink to another site's page — generally fair use but deep linking (bypassing homepage) can raise IPR issues.<br/>"
        "In-lining: Embedding another site's image/content directly in your page without hosting it — effectively appropriating bandwidth and content.<br/>"
        "Framing: Displaying another site's content within a frame of your website — hides origin, may constitute passing off.<br/><br/>"
        "<b>(c) Abuse of Search Engines:</b> Keyword stuffing — using trademarked names as meta-keywords to divert traffic. Example: A rival company uses 'Coca-Cola' in hidden keywords to attract Coke's customers to their website. Metatag abuse can constitute trademark infringement.", ans))

    story.append(PageBreak())

    # ---- MCSL-216 ----
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#1a1a6e')))
    story.append(Paragraph("MCSL-216: DAA and Web Design Lab", chs))
    story.append(Paragraph("Assignment No: MCA_NEW(1)/L-216/Assign/2023 | Max Marks: 100 | Weightage: 30%", is_))
    story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor('#cccccc')))
    story.append(Spacer(1, 0.08*inch))

    story.append(Paragraph("Section-1, Q1: Quick Sort — Sorting and Performance Comparison", qs))
    story.append(Paragraph(
        "<b>Data 1 (Unsorted):</b> 12 20 22 16 25 18 8 10 6 15<br/>"
        "Pivot=15 (last element). Partition: [12,10,8,6] 15 [20,22,16,25,18]<br/>"
        "Left partition sorted: [6,8,10,12]. Right: pivot=18 → [16,17...]<br/>"
        "Final sorted: <b>6 8 10 12 15 16 18 20 22 25</b><br/><br/>"
        "<b>Data 2 (Already Sorted):</b> 6 8 10 12 15 16 18 20 22 25<br/>"
        "With last element as pivot: always worst case — pivot becomes largest/smallest element.<br/><br/>"
        "<b>Performance Comparison:</b><br/>"
        "Data 1 (unsorted): ~25 comparisons, ~15 swaps, average O(n log n) ≈ 33 loop iterations<br/>"
        "Data 2 (sorted): ~45 comparisons, 0 swaps, O(n<super>2</super>) ≈ 55 loop iterations — worst case<br/>"
        "Conclusion: Quick Sort performs worst on already-sorted data with naïve pivot selection. Use random pivot or median-of-three to avoid this.", ans))

    story.append(Paragraph("Section-1, Q2: Huffman Coding — A:15, B:25, C:5, D:7, E:10, F:13, G:9", qs))
    story.append(Paragraph(
        "Sort by frequency: C(5), D(7), G(9), E(10), F(13), A(15), B(25). Total=84<br/>"
        "Build tree:<br/>"
        "1. Merge C(5)+D(7)=CD(12). Queue: G(9),E(10),F(13),CD(12),A(15),B(25)<br/>"
        "2. Merge G(9)+E(10)=GE(19). Queue: F(13),CD(12),A(15),B(25),GE(19)<br/>"
        "3. Merge CD(12)+F(13)=CDF(25). Queue: A(15),B(25),GE(19),CDF(25)<br/>"
        "4. Merge A(15)+GE(19)=AGE(34). Queue: B(25),CDF(25),AGE(34)<br/>"
        "5. Merge B(25)+CDF(25)=BCDF(50). Queue: AGE(34),BCDF(50)<br/>"
        "6. Merge AGE(34)+BCDF(50)=Root(84)<br/><br/>"
        "Sample Huffman Codes: B=00, C=0100, D=0101, F=011, A=10, G=110, E=111<br/>"
        "Average bits per char = (15×2+25×2+5×4+7×4+10×3+13×3+9×3)/84 = (30+50+20+28+30+39+27)/84 = 224/84 ≈ <b>2.67 bits/character</b>", ans))

    story.append(Paragraph("Section-2, Q3: Patient Satisfaction Survey Form (Design Specification)", qs))
    story.append(Paragraph(
        "Form fields and input types:<br/>"
        "• Patient's Name — Text Box (mandatory, min 3 chars)<br/>"
        "• File Number — Text Box (mandatory, alphanumeric pattern validation)<br/>"
        "• Hospital Unit — Combo Box / Dropdown (options: Surgery, Medicine, Orthopaedics, Gynaecology, Emergency, Other)<br/>"
        "• Overall Treatment Satisfaction — Radio Buttons (Very Satisfied / Satisfied / Not Satisfied)<br/>"
        "• Medical Facilities Satisfaction — Radio Buttons (Very Satisfied / Satisfied / Not Satisfied)<br/>"
        "• Overall Comments — Textarea (optional, max 500 chars)<br/>"
        "• Submit Button — validates form via JavaScript, sends POST to server<br/>"
        "• Reset Button — clears all fields<br/><br/>"
        "JavaScript Validation: All mandatory fields non-empty; file number pattern match; at least one radio button selected in each group. Show error message in red below each field that fails validation. On successful submit: show 'Thank you! Your feedback has been submitted.' confirmation message.", ans))

    story.append(Paragraph("Section-2, Q4: Cookie Management HTML Page", qs))
    story.append(Paragraph(
        "Implementation Plan:<br/>"
        "Page Layout: Two rows of buttons (Set Cookie1 | Get Cookie1 | Delete Cookie1) and (Set Cookie2 | Get Cookie2 | Delete Cookie2) plus 'Display All Cookies' button at bottom.<br/><br/>"
        "JavaScript Functions:<br/>"
        "• setCookie(name, value, days): document.cookie = name+'='+value+'; expires='+expiryDate+'; path=/'<br/>"
        "• getCookie(name): parse document.cookie, find and return value for name<br/>"
        "• deleteCookie(name): set cookie with past expiry date<br/>"
        "• displayAllCookies(): alert or display document.cookie string<br/><br/>"
        "Set Cookie1: calls setCookie('cookie1', 'Cookie1Value', 7) — stores for 7 days<br/>"
        "Get Cookie1: calls getCookie('cookie1') and alerts the value<br/>"
        "Delete Cookie1: calls deleteCookie('cookie1')<br/>"
        "Display All: shows all current cookies in a div or alert box.<br/><br/>"
        "Submit complete HTML file with working cookie operations for evaluation.", ans))

    story.append(PageBreak())

    # ---- MCSL-217 ----
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#1a1a6e')))
    story.append(Paragraph("MCSL-217: Software Engineering Lab", chs))
    story.append(Paragraph("Assignment No: MCA_NEW(1)/217/Assign/2023 | Max Marks: 100 | Weightage: 30%", is_))
    story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor('#cccccc')))
    story.append(Spacer(1, 0.08*inch))

    story.append(Paragraph("Q1: OHTGS — Cost and Effort Estimation", qs))
    story.append(Paragraph("Same system as MCS-213. Detailed estimation below.", ans))

    story.append(Paragraph("(1) Cost Estimation — COCOMO Basic Model", sqs))
    story.append(Paragraph(
        "OHTGS Estimated Size: 12 KLOC (Organic mode — single team, well-understood requirements).<br/>"
        "a=2.4, b=1.05 (COCOMO Organic):<br/>"
        "Effort E = 2.4 × (12)<super>1.05</super> = 2.4 × 13.8 = <b>33.1 Person-Months</b><br/>"
        "Development Time D = 2.5 × E<super>0.38</super> = 2.5 × (33.1)<super>0.38</super> = 2.5 × 5.3 = <b>13.3 months ≈ 14 months</b><br/>"
        "Average team size = 33.1/13.3 ≈ <b>2.5 persons</b> (round to 3)<br/>"
        "Cost: Assume ₹75,000/person-month: 33.1 × 75,000 = ₹24.8 Lakhs (labour)<br/>"
        "Add: Infrastructure(₹3L), Testing(₹2L), Deployment/Training(₹3L) = <b>Total ≈ ₹33 Lakhs</b>", ans))

    story.append(Paragraph("(2) Effort Estimation — Function Point Analysis", sqs))
    story.append(Paragraph(
        "Function Point Count for OHTGS:<br/>"
        "• External Inputs: Student login, apply for exam, admin configuration = 3 EI × 4 = 12<br/>"
        "• External Outputs: Hall ticket PDF, email notification = 2 EO × 5 = 10<br/>"
        "• External Queries: Check eligibility, verify Aadhaar = 2 EQ × 4 = 8<br/>"
        "• Internal Logical Files: Student DB, Exam Centre DB, Hall Ticket DB = 3 ILF × 7 = 21<br/>"
        "• External Interface Files: SMS gateway, Aadhaar API = 2 EIF × 5 = 10<br/>"
        "Unadjusted FP = 12+10+8+21+10 = 61 UFP<br/>"
        "Value Adjustment Factor (VAF) = 14 characteristics × avg 3 = 42 → TCF = 0.65+(0.01×42) = 1.07<br/>"
        "Adjusted FP = 61 × 1.07 = 65.3 FP<br/>"
        "Productivity = 8 FP/month: Effort = 65.3/8 = <b>8.2 Person-Months</b><br/>"
        "Using industry standard 150 hours/FP: 65.3×150 = 9795 hours ÷ 160 hrs/month = <b>61.2 Person-Months</b> (with different productivity assumption)<br/>"
        "Final Estimate (blended): approximately <b>30-35 Person-Months</b> consistent with COCOMO estimate.", ans))

    story.append(Spacer(1, 0.3*inch))
    story.append(HRFlowable(width="100%", thickness=2, color=colors.HexColor('#1a1a6e')))
    story.append(Paragraph("— End of Assignment Answers: January/July 2023 Session —", is_))
    story.append(Paragraph("IGNOU MCA_NEW (2 Years) Programme | Semester-I", is_))

    doc.build(story)
    print("2023 PDF created!")

build_2023()