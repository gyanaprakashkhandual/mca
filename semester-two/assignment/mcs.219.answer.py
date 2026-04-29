from reportlab.lib.pagesizes import A4 # pyright: ignore[reportMissingModuleSource]
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, Table, TableStyle # pyright: ignore[reportMissingModuleSource]
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle # pyright: ignore[reportMissingModuleSource]
from reportlab.lib.units import cm # pyright: ignore[reportMissingModuleSource]
from reportlab.lib import colors # pyright: ignore[reportMissingModuleSource]
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY # pyright: ignore[reportMissingModuleSource]

doc = SimpleDocTemplate(
    "/home/claude/MCS-219_Answers.pdf",
    pagesize=A4,
    rightMargin=2*cm, leftMargin=2*cm,
    topMargin=2*cm, bottomMargin=2*cm
)
styles = getSampleStyleSheet()
title_style = ParagraphStyle('Title', parent=styles['Title'], fontSize=16, textColor=colors.HexColor('#1a237e'), spaceAfter=6, alignment=TA_CENTER)
subtitle_style = ParagraphStyle('Subtitle', parent=styles['Normal'], fontSize=11, textColor=colors.HexColor('#1a237e'), spaceAfter=4, alignment=TA_CENTER)
info_style = ParagraphStyle('Info', parent=styles['Normal'], fontSize=10, spaceAfter=3, alignment=TA_CENTER)
q_style = ParagraphStyle('Question', parent=styles['Normal'], fontSize=11, textColor=colors.HexColor('#b71c1c'), spaceBefore=16, spaceAfter=6, fontName='Helvetica-Bold')
body_style = ParagraphStyle('Body', parent=styles['Normal'], fontSize=10.5, spaceAfter=6, leading=16, alignment=TA_JUSTIFY)
sub_style = ParagraphStyle('Sub', parent=styles['Normal'], fontSize=10.5, spaceAfter=4, leading=15, leftIndent=20, alignment=TA_JUSTIFY)
bullet_style = ParagraphStyle('Bullet', parent=styles['Normal'], fontSize=10.5, spaceAfter=3, leading=15, leftIndent=30)
heading_style = ParagraphStyle('Heading', parent=styles['Normal'], fontSize=11, fontName='Helvetica-Bold', spaceAfter=5, spaceBefore=8, textColor=colors.HexColor('#0d47a1'))

story = []

story.append(Paragraph("INDIRA GANDHI NATIONAL OPEN UNIVERSITY", title_style))
story.append(Paragraph("School of Computer and Information Sciences", subtitle_style))
story.append(Paragraph("Master of Computer Applications (MCA New) — Semester II", info_style))
story.append(HRFlowable(width="100%", thickness=2, color=colors.HexColor('#1a237e'), spaceAfter=8))

details = [
    ["Course Code", "MCS-219"],
    ["Course Title", "Object Oriented Analysis and Design (OOAD)"],
    ["Assignment No.", "MCA_NEW(II)/219/Assign/2025-26"],
    ["Maximum Marks", "100 (80 Written + 20 Viva Voce)"],
    ["Weightage", "30%"],
    ["Last Date of Submission", "31st October, 2025 (July Session) | 15th April, 2026 (Jan Session)"],
]
t = Table(details, colWidths=[5*cm, 11*cm])
t.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (0,-1), colors.HexColor('#e8eaf6')),
    ('FONTNAME', (0,0), (0,-1), 'Helvetica-Bold'),
    ('FONTSIZE', (0,0), (-1,-1), 10),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#9fa8da')),
    ('ROWBACKGROUNDS', (1,0), (1,-1), [colors.white, colors.HexColor('#f5f5f5')]),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('TOPPADDING', (0,0), (-1,-1), 5),
    ('BOTTOMPADDING', (0,0), (-1,-1), 5),
]))
story.append(t)
story.append(Spacer(1, 0.4*cm))
story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#9fa8da'), spaceAfter=10))

def hr(): story.append(HRFlowable(width="100%", thickness=0.5, color=colors.grey, spaceBefore=8, spaceAfter=8))

# Q1
story.append(Paragraph("Q1: What is OOAD? Explain basic constructs of object orientation. (10 Marks)", q_style))
story.append(Paragraph("<b>Answer:</b>", heading_style))
story.append(Paragraph(
    "<b>Object-Oriented Analysis and Design (OOAD)</b> is a software engineering approach that uses object-oriented concepts to analyze requirements and design a system. It bridges the gap between the real-world problem domain and the software solution by modeling the system as a collection of interacting objects.",
    body_style))
story.append(Paragraph("<b>OOAD consists of two phases:</b>", body_style))
for pt in [
    "<b>Object-Oriented Analysis (OOA):</b> Focuses on understanding what the system should do. It identifies the key objects, their attributes, relationships, and behaviours from the problem domain.",
    "<b>Object-Oriented Design (OOD):</b> Focuses on how the system will be implemented. It defines the software objects and their collaborations to fulfil the requirements identified during OOA.",
]:
    story.append(Paragraph(f"• {pt}", bullet_style))

story.append(Paragraph("<b>Basic Constructs of Object Orientation</b>", heading_style))

constructs = [
    ("1. Object",
     "An object is a real-world entity that has a state (attributes/data) and behaviour (methods/functions). For example, a 'Car' object has attributes like colour, speed, brand and behaviours like start(), stop(), accelerate()."),
    ("2. Class",
     "A class is a blueprint or template for creating objects. It defines the attributes and methods that all objects of that class will have. Example: class BankAccount { String accountNumber; double balance; void deposit(double amount); void withdraw(double amount); }"),
    ("3. Encapsulation",
     "Encapsulation is the mechanism of bundling data (attributes) and the methods that operate on that data within a single unit (class), and restricting direct access to some of the object's components. This is achieved through access modifiers (private, protected, public). It promotes data hiding and protects the integrity of the object's state."),
    ("4. Abstraction",
     "Abstraction means representing only the essential features of an entity and hiding unnecessary implementation details. For example, when driving a car, you use the steering wheel and pedals without knowing the internal workings of the engine. In OO programming, abstract classes and interfaces implement abstraction."),
    ("5. Inheritance",
     "Inheritance is a mechanism whereby a new class (subclass/derived class) acquires the properties and behaviours of an existing class (superclass/base class). It supports code reuse and establishes an 'IS-A' relationship. Example: class Dog extends Animal — Dog inherits attributes and methods of Animal and can add its own."),
    ("6. Polymorphism",
     "Polymorphism means 'many forms'. It allows objects of different classes to be treated as objects of a common superclass, and for the same operation to behave differently based on the object. Types: Compile-time (method overloading — same method name, different parameters) and Runtime polymorphism (method overriding — subclass provides a specific implementation of a method defined in the superclass)."),
    ("7. Association, Aggregation, and Composition",
     "Association: A general relationship between two classes (e.g., Teacher teaches Student). Aggregation: A 'HAS-A' relationship where the child can exist independently of the parent (e.g., Department HAS-A Professor — Professor can exist without a Department). Composition: A strong 'HAS-A' relationship where the child cannot exist without the parent (e.g., House HAS-A Room — Room cannot exist without a House)."),
    ("8. Message Passing",
     "Objects communicate with each other by sending messages (method calls). When object A calls a method of object B, it passes a message to B. This forms the basis of interaction in OO systems."),
]
for title, content in constructs:
    story.append(Paragraph(f"<b>{title}</b>", heading_style))
    story.append(Paragraph(content, sub_style))
hr()

# Q2
story.append(Paragraph("Q2: Draw class diagram for Online Banking System. Make necessary assumptions. (10 Marks)", q_style))
story.append(Paragraph("<b>Answer:</b>", heading_style))
story.append(Paragraph("<b>Assumptions:</b> The Online Banking System supports customer registration, account management (savings/current), fund transfers, loans, and transaction history.", body_style))
story.append(Paragraph("<b>Class Diagram Description (Textual UML Representation):</b>", heading_style))

classes = [
    ["Class", "Attributes", "Methods"],
    ["Customer", "customerId, name, email, phone, address, dateOfBirth", "register(), login(), updateProfile(), viewAccounts()"],
    ["Account (Abstract)", "accountId, balance, openDate, status", "deposit(), withdraw(), checkBalance(), getStatement()"],
    ["SavingsAccount", "interestRate, minimumBalance", "calculateInterest(), applyInterest()"],
    ["CurrentAccount", "overdraftLimit, charges", "applyOverdraft()"],
    ["Transaction", "transactionId, amount, date, type, description", "getDetails()"],
    ["FundTransfer", "transferId, fromAccount, toAccount, amount, date", "initiateTransfer(), verifyTransfer()"],
    ["Loan", "loanId, amount, interestRate, tenure, status", "applyLoan(), calculateEMI(), approveLoan()"],
    ["Bank", "bankId, name, ifscCode, branch", "addCustomer(), removeCustomer(), generateReport()"],
    ["Admin", "adminId, name, role", "manageCustomers(), viewAllAccounts(), generateReports()"],
]
ct = Table(classes, colWidths=[4*cm, 7*cm, 5.5*cm])
ct.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1a237e')),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTSIZE', (0,0), (-1,-1), 8.5),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#9fa8da')),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#e8eaf6')]),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('TOPPADDING', (0,0), (-1,-1), 4),
    ('BOTTOMPADDING', (0,0), (-1,-1), 4),
]))
story.append(ct)
story.append(Spacer(1, 0.3*cm))

story.append(Paragraph("<b>Relationships:</b>", heading_style))
rels = [
    "Customer has a 1-to-many relationship with Account (one customer can hold multiple accounts).",
    "Account (abstract) is the parent class; SavingsAccount and CurrentAccount are subclasses (Generalization/Inheritance).",
    "Account has a 1-to-many relationship with Transaction (each account can have many transactions).",
    "FundTransfer is associated with two Account objects (fromAccount and toAccount).",
    "Customer has a 0-to-many relationship with Loan (a customer may take zero or more loans).",
    "Bank has a 1-to-many relationship with Customer.",
    "Admin manages the Bank system and has access to all entities.",
]
for r in rels:
    story.append(Paragraph(f"• {r}", bullet_style))
hr()

# Q3
story.append(Paragraph("Q3: What is object modeling, dynamic modeling and functional modeling? Briefly explain the diagrams used. (10 Marks)", q_style))
story.append(Paragraph("<b>Answer:</b>", heading_style))

modelings = [
    ("1. Object Modeling",
     "Object modeling describes the static structure of a system — the objects that exist, their attributes, and their relationships at any given moment. It focuses on the 'things' in the system.\n\n"
     "Diagrams Used:\n"
     "• Class Diagram: Shows classes, their attributes, methods, and relationships (association, aggregation, composition, inheritance). It is the primary diagram of object modeling.\n"
     "• Object Diagram: Shows a snapshot of the system at a specific point in time — instances of classes and their current attribute values and links."),
    ("2. Dynamic Modeling",
     "Dynamic modeling captures the time-dependent behaviour of the system — how objects interact and change state over time in response to events.\n\n"
     "Diagrams Used:\n"
     "• State Diagram (State Machine Diagram): Shows the different states an object can be in and the transitions between states triggered by events. Useful for objects with complex life cycles (e.g., an Order object going from 'Placed' → 'Confirmed' → 'Shipped' → 'Delivered').\n"
     "• Sequence Diagram: Shows how objects interact with each other in a time-ordered sequence of messages. The vertical axis represents time and horizontal axis represents objects.\n"
     "• Collaboration (Communication) Diagram: Shows the structural organization of objects that send and receive messages, with numbered messages indicating sequence.\n"
     "• Activity Diagram: Represents the flow of activities or workflow of a system. Shows parallel and sequential activities."),
    ("3. Functional Modeling",
     "Functional modeling describes what the system does — the computations and transformations performed on data as it flows through the system.\n\n"
     "Diagrams Used:\n"
     "• Data Flow Diagram (DFD): Shows the flow of data through the system — from inputs to processes to outputs to data stores. Has four components: External Entities, Processes, Data Stores, and Data Flows.\n"
     "• Use Case Diagram: Shows the functional requirements of the system from the user's perspective. Actors (users or external systems) interact with Use Cases (system functions). It captures WHAT the system does without detailing HOW.\n"
     "• Interaction Overview Diagram: Combines elements of activity and sequence diagrams to show a high-level overview of interactions."),
]
for title, content in modelings:
    story.append(Paragraph(f"<b>{title}</b>", heading_style))
    for para in content.split('\n\n'):
        story.append(Paragraph(para.strip(), sub_style))
    story.append(Spacer(1, 0.1*cm))
hr()

# Q4
story.append(Paragraph("Q4: Draw state diagrams for: (i) Online Banking System (ii) Online Examination System (10 Marks)", q_style))
story.append(Paragraph("<b>Answer:</b>", heading_style))

story.append(Paragraph("<b>(i) State Diagram for Online Banking System (Account Object):</b>", heading_style))
states_bank = [
    ["State", "Triggered By (Event)", "Transitions To"],
    ["Initial State", "Customer applies for account", "Application Submitted"],
    ["Application Submitted", "Admin reviews application", "Under Review"],
    ["Under Review", "Application approved", "Active"],
    ["Under Review", "Application rejected", "Rejected (Final State)"],
    ["Active", "Customer deposits/withdraws", "Active (self-loop)"],
    ["Active", "Balance falls below minimum", "Dormant"],
    ["Dormant", "Customer makes transaction", "Active"],
    ["Active", "Customer requests closure", "Closure Requested"],
    ["Closure Requested", "Admin approves closure", "Closed (Final State)"],
    ["Active", "Fraud detected", "Suspended"],
    ["Suspended", "Issue resolved by Admin", "Active"],
]
st = Table(states_bank, colWidths=[4.5*cm, 6*cm, 5*cm])
st.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1a237e')),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTSIZE', (0,0), (-1,-1), 9),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#9fa8da')),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#e8eaf6')]),
    ('TOPPADDING', (0,0), (-1,-1), 4),
    ('BOTTOMPADDING', (0,0), (-1,-1), 4),
]))
story.append(st)
story.append(Spacer(1, 0.3*cm))

story.append(Paragraph("<b>States Summary (Banking):</b> Initial → Application Submitted → Under Review → Active ↔ Dormant → Closure Requested → Closed. Active → Suspended → Active.", sub_style))
story.append(Spacer(1, 0.3*cm))

story.append(Paragraph("<b>(ii) State Diagram for Online Examination System (Exam Object):</b>", heading_style))
states_exam = [
    ["State", "Triggered By (Event)", "Transitions To"],
    ["Initial State", "Admin creates exam", "Exam Created"],
    ["Exam Created", "Admin publishes exam", "Published"],
    ["Published", "Student registers for exam", "Registration Open"],
    ["Registration Open", "Registration deadline passes", "Registration Closed"],
    ["Registration Closed", "Exam start time reached", "In Progress"],
    ["In Progress", "Student submits answers", "Submitted"],
    ["In Progress", "Time limit expires", "Auto-Submitted"],
    ["Submitted / Auto-Submitted", "System evaluates answers", "Under Evaluation"],
    ["Under Evaluation", "Results computed", "Results Declared"],
    ["Results Declared", "Student views result", "Completed (Final State)"],
    ["In Progress", "Technical issue occurs", "Paused"],
    ["Paused", "Issue resolved", "In Progress"],
]
st2 = Table(states_exam, colWidths=[4.5*cm, 6*cm, 5*cm])
st2.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1a237e')),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTSIZE', (0,0), (-1,-1), 9),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#9fa8da')),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#e8eaf6')]),
    ('TOPPADDING', (0,0), (-1,-1), 4),
    ('BOTTOMPADDING', (0,0), (-1,-1), 4),
]))
story.append(st2)
story.append(Spacer(1, 0.2*cm))
story.append(Paragraph("<b>States Summary (Exam):</b> Exam Created → Published → Registration Open → Registration Closed → In Progress ↔ Paused → Submitted/Auto-Submitted → Under Evaluation → Results Declared → Completed.", sub_style))
hr()

# Q5
story.append(Paragraph("Q5: What is an abstract class? Explain aggregation, generalization and specialization with suitable examples. (10 Marks)", q_style))
story.append(Paragraph("<b>Answer:</b>", heading_style))

story.append(Paragraph("<b>Abstract Class</b>", heading_style))
story.append(Paragraph(
    "An abstract class is a class that cannot be instantiated directly — you cannot create objects from it. It serves as a blueprint for other classes (subclasses) that extend it. An abstract class may contain abstract methods (methods without a body/implementation) that must be overridden by all concrete subclasses, as well as non-abstract methods with full implementations.\n\n"
    "Example: abstract class Shape { abstract double area(); abstract double perimeter(); void display() { System.out.println(\"This is a shape\"); } } — Classes like Circle, Rectangle extend Shape and provide implementations for area() and perimeter().\n\n"
    "Purpose: Enforces a common interface/contract across all subclasses while allowing shared code in the abstract class itself.",
    sub_style))

story.append(Paragraph("<b>Aggregation</b>", heading_style))
story.append(Paragraph(
    "Aggregation is a special type of association that represents a 'HAS-A' (whole-part) relationship where the child object can exist independently of the parent object. It is a weak relationship.\n\n"
    "Example: A University HAS Departments, and a Department HAS Professors. If the University is dissolved, Professors still exist (they can work elsewhere). In UML, aggregation is shown with an open (hollow) diamond at the parent end of the association line.\n\n"
    "Class Notation: University ◇——— Department ◇——— Professor",
    sub_style))

story.append(Paragraph("<b>Generalization</b>", heading_style))
story.append(Paragraph(
    "Generalization is the process of extracting shared characteristics from multiple specific classes to create a more general superclass. It represents an 'IS-A' relationship and is the foundation of inheritance. It moves from specific to general.\n\n"
    "Example: We observe that Dog, Cat, and Bird all have attributes (name, age) and methods (eat(), sleep()). We generalize these into a superclass Animal. Dog IS-A Animal, Cat IS-A Animal, Bird IS-A Animal.\n\n"
    "In UML: Shown with an arrow from the subclass to the superclass (inheritance arrow). Dog → Animal.",
    sub_style))

story.append(Paragraph("<b>Specialization</b>", heading_style))
story.append(Paragraph(
    "Specialization is the reverse process of generalization — creating new specialized subclasses from an existing general superclass by adding more specific attributes and behaviours. It moves from general to specific.\n\n"
    "Example: Starting from a general class Employee, we specialize into Manager (with attributes like teamSize, managementLevel and methods like conductAppraisal()), Developer (with programmingLanguages, projectsAssigned), and HRManager (with recruitmentTarget, trainingBudget).\n\n"
    "Relationship: Manager IS-A Employee. Developer IS-A Employee. Each specialized class inherits all Employee attributes and adds its own.",
    sub_style))
hr()

# Q6
story.append(Paragraph("Q6: Explain design optimization and need of design documentation. What are features of a good design document? (10 Marks)", q_style))
story.append(Paragraph("<b>Answer:</b>", heading_style))

story.append(Paragraph("<b>Design Optimization</b>", heading_style))
story.append(Paragraph(
    "Design optimization is the process of improving the design of a system to make it more efficient, maintainable, and scalable without changing its external functionality. After an initial design is created (which is correct but may not be optimal), optimization techniques are applied.",
    body_style))
story.append(Paragraph("Key Design Optimization Techniques:", body_style))
opt = [
    "<b>Reuse of Common Code:</b> Identify repeated code patterns and extract them into reusable methods, classes, or libraries. Reduces duplication and maintenance cost.",
    "<b>Collapsing Trivial Classes:</b> If a class has very few responsibilities and attributes, it may be merged with another related class to reduce complexity.",
    "<b>Delaying Expensive Operations:</b> Use lazy initialization — create expensive objects only when needed, not at startup.",
    "<b>Caching:</b> Store results of expensive computations for reuse (memoization, database query caching).",
    "<b>Increasing Cohesion:</b> Each class/module should have a single, well-defined responsibility (Single Responsibility Principle). High cohesion improves clarity and maintainability.",
    "<b>Reducing Coupling:</b> Minimize dependencies between classes/modules. Loosely coupled systems are easier to modify and test.",
    "<b>Choosing Efficient Data Structures and Algorithms:</b> Use appropriate data structures (e.g., HashMap over ArrayList for lookups) to improve time and space complexity.",
    "<b>Design Patterns:</b> Apply proven design patterns (Singleton, Factory, Observer, etc.) to common design problems for well-optimized solutions.",
]
for o in opt:
    story.append(Paragraph(f"• {o}", bullet_style))

story.append(Paragraph("<b>Need for Design Documentation</b>", heading_style))
needs = [
    "Serves as a reference for developers during implementation, ensuring all team members have a common understanding of the system.",
    "Facilitates communication between stakeholders (clients, analysts, developers, testers).",
    "Helps in onboarding new team members quickly.",
    "Provides a baseline for testing — testers use design documents to verify that implementation matches the design.",
    "Supports maintenance and future enhancement — developers can understand the original intent of the design.",
    "Acts as legal and contractual documentation between client and development organization.",
    "Enables design reviews and quality assurance.",
]
for n in needs:
    story.append(Paragraph(f"• {n}", bullet_style))

story.append(Paragraph("<b>Features of a Good Design Document</b>", heading_style))
features = [
    "<b>Complete:</b> Covers all aspects of the system — architecture, class design, interface design, database design, security considerations.",
    "<b>Consistent:</b> No contradictions between different parts of the document. Terminology is used uniformly throughout.",
    "<b>Clear and Unambiguous:</b> Written in simple, precise language. Diagrams supplement text to enhance understanding.",
    "<b>Modifiable:</b> Structured so that changes can be made easily without affecting other parts.",
    "<b>Traceable:</b> Every design decision can be traced back to a specific requirement from the SRS.",
    "<b>Correct:</b> Accurately reflects the actual system design that will be implemented.",
    "<b>Well-Structured:</b> Has a clear table of contents, numbered sections, and logical organization.",
    "<b>Version Controlled:</b> Maintains a history of changes with dates and authors.",
]
for f in features:
    story.append(Paragraph(f"• {f}", bullet_style))
hr()

# Q7
story.append(Paragraph("Q7: Map the object classes created in Q2 (Online Banking System) into database tables. (10 Marks)", q_style))
story.append(Paragraph("<b>Answer:</b>", heading_style))
story.append(Paragraph("Each class maps to a database table. Attributes become columns. Relationships are represented using foreign keys.", body_style))

db_tables = [
    ("CUSTOMER Table",
     [["Column", "Data Type", "Constraint"],
      ["customer_id", "INT", "PRIMARY KEY, AUTO_INCREMENT"],
      ["name", "VARCHAR(100)", "NOT NULL"],
      ["email", "VARCHAR(100)", "UNIQUE, NOT NULL"],
      ["phone", "VARCHAR(15)", "UNIQUE"],
      ["address", "TEXT", ""],
      ["date_of_birth", "DATE", "NOT NULL"],
      ["password_hash", "VARCHAR(255)", "NOT NULL"]]),
    ("ACCOUNT Table",
     [["Column", "Data Type", "Constraint"],
      ["account_id", "INT", "PRIMARY KEY, AUTO_INCREMENT"],
      ["customer_id", "INT", "FOREIGN KEY → CUSTOMER(customer_id)"],
      ["account_type", "ENUM('SAVINGS','CURRENT')", "NOT NULL"],
      ["balance", "DECIMAL(15,2)", "DEFAULT 0.00"],
      ["open_date", "DATE", "NOT NULL"],
      ["status", "ENUM('ACTIVE','DORMANT','CLOSED','SUSPENDED')", "DEFAULT 'ACTIVE'"],
      ["interest_rate", "DECIMAL(5,2)", "NULL (for savings)"],
      ["overdraft_limit", "DECIMAL(10,2)", "NULL (for current)"]]),
    ("TRANSACTION Table",
     [["Column", "Data Type", "Constraint"],
      ["transaction_id", "INT", "PRIMARY KEY, AUTO_INCREMENT"],
      ["account_id", "INT", "FOREIGN KEY → ACCOUNT(account_id)"],
      ["amount", "DECIMAL(15,2)", "NOT NULL"],
      ["transaction_date", "DATETIME", "NOT NULL"],
      ["type", "ENUM('CREDIT','DEBIT','TRANSFER')", "NOT NULL"],
      ["description", "VARCHAR(255)", ""]]),
    ("FUND_TRANSFER Table",
     [["Column", "Data Type", "Constraint"],
      ["transfer_id", "INT", "PRIMARY KEY, AUTO_INCREMENT"],
      ["from_account_id", "INT", "FOREIGN KEY → ACCOUNT(account_id)"],
      ["to_account_id", "INT", "FOREIGN KEY → ACCOUNT(account_id)"],
      ["amount", "DECIMAL(15,2)", "NOT NULL"],
      ["transfer_date", "DATETIME", "NOT NULL"],
      ["status", "ENUM('PENDING','COMPLETED','FAILED')", "DEFAULT 'PENDING'"]]),
    ("LOAN Table",
     [["Column", "Data Type", "Constraint"],
      ["loan_id", "INT", "PRIMARY KEY, AUTO_INCREMENT"],
      ["customer_id", "INT", "FOREIGN KEY → CUSTOMER(customer_id)"],
      ["amount", "DECIMAL(15,2)", "NOT NULL"],
      ["interest_rate", "DECIMAL(5,2)", "NOT NULL"],
      ["tenure_months", "INT", "NOT NULL"],
      ["status", "ENUM('PENDING','APPROVED','REJECTED','CLOSED')", "DEFAULT 'PENDING'"],
      ["emi_amount", "DECIMAL(10,2)", ""]]),
]
for table_name, data in db_tables:
    story.append(Paragraph(f"<b>{table_name}:</b>", heading_style))
    t = Table(data, colWidths=[5*cm, 5*cm, 6.5*cm])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0d47a1')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 9),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#9fa8da')),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#e8eaf6')]),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t)
    story.append(Spacer(1, 0.25*cm))
hr()

# Q8
story.append(Paragraph("Q8: Write short notes on: (i) Associations and its Implementation (ii) Implementation of Controls (10 Marks)", q_style))
story.append(Paragraph("<b>Answer:</b>", heading_style))

story.append(Paragraph("<b>(i) Associations and its Implementation</b>", heading_style))
story.append(Paragraph(
    "An <b>association</b> in OO design represents a structural relationship between two or more classes indicating that objects of one class are connected to objects of another. Associations define how objects interact and navigate to each other.",
    body_style))
story.append(Paragraph("Types of Associations:", body_style))
assoc = [
    "<b>Unidirectional Association:</b> Navigation is possible in only one direction. Class A knows about Class B, but B does not know about A. Implemented by including an instance variable of type B in class A.",
    "<b>Bidirectional Association:</b> Both classes know about each other. Each class holds a reference to the other. Example: Order and Customer — Order knows which Customer placed it, and Customer can access all Orders.",
    "<b>Multiplicity:</b> Specifies how many instances of a class can be associated with an instance of another (1:1, 1:many, many:many).",
    "<b>Many-to-many Implementation:</b> Requires a join/association class. Example: Student-Course relationship needs an Enrollment class with studentId, courseId, enrollmentDate, grade.",
    "<b>Reflexive Association:</b> A class is associated with itself. Example: Employee class where one employee is the Manager of another employee (manager is also an Employee).",
]
for a in assoc:
    story.append(Paragraph(f"• {a}", bullet_style))

story.append(Paragraph("Implementation in Java:", heading_style))
story.append(Paragraph(
    "One-to-one: private Address address; in Customer class. One-to-many: private List&lt;Order&gt; orders; in Customer class. Many-to-many: Create an Enrollment class: private Student student; private Course course; — each Enrollment object represents one enrollment record.",
    sub_style))

story.append(Paragraph("<b>(ii) Implementation of Controls</b>", heading_style))
story.append(Paragraph(
    "In OOAD, <b>control classes</b> (also called Controller classes) manage the flow of information between boundary classes (UI) and entity classes (data). They implement the use case logic and coordinate interactions.",
    body_style))
story.append(Paragraph("Key aspects of control implementation:", body_style))
ctrl = [
    "<b>Control Objects/Classes:</b> Identified during OOA for each use case. They contain the business logic and orchestrate how other objects interact. Example: TransferController handles the logic for a bank transfer — it validates input, checks balance, updates accounts, and records the transaction.",
    "<b>Event Handling:</b> Controls respond to events (user actions, system events). In GUI systems, event listeners (ActionListener, MouseListener) implement this. In web apps, controllers (in MVC framework — Spring MVC Controller, Servlet) handle HTTP requests.",
    "<b>MVC Pattern:</b> The Model-View-Controller pattern is the most common way to implement controls. The Controller class receives input from the View (boundary), processes it using Model (entity), and returns output back to the View.",
    "<b>Stateful vs Stateless Controllers:</b> Some controls maintain state across interactions (session-based); others are stateless (process each request independently, like RESTful API controllers).",
    "<b>Design Patterns for Controls:</b> Command Pattern — encapsulates a request as an object; Strategy Pattern — defines a family of algorithms and makes them interchangeable; Observer Pattern — controller notifies observers (views) of state changes.",
    "<b>Implementation Steps:</b> (1) Identify use cases. (2) Create a controller class for each use case or related group of use cases. (3) Define methods corresponding to each step of the use case. (4) Implement business logic within these methods. (5) Use dependency injection to connect controllers with entity classes and services.",
]
for c in ctrl:
    story.append(Paragraph(f"• {c}", bullet_style))

doc.build(story)
print("MCS-219 PDF created successfully.")