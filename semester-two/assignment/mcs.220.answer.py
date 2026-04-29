from reportlab.lib.pagesizes import A4 # pyright: ignore[reportMissingModuleSource]
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, Table, TableStyle, Preformatted # pyright: ignore[reportMissingModuleSource]
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle # pyright: ignore[reportMissingModuleSource]
from reportlab.lib.units import cm # pyright: ignore[reportMissingModuleSource]
from reportlab.lib import colors # pyright: ignore[reportMissingModuleSource]
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT # pyright: ignore[reportMissingModuleSource]

doc = SimpleDocTemplate(
    "/home/claude/MCS-220_Answers.pdf",
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
code_style = ParagraphStyle('Code', parent=styles['Code'], fontSize=8.5, fontName='Courier', leading=12, leftIndent=20, spaceAfter=6, backColor=colors.HexColor('#f5f5f5'))

story = []

story.append(Paragraph("INDIRA GANDHI NATIONAL OPEN UNIVERSITY", title_style))
story.append(Paragraph("School of Computer and Information Sciences", subtitle_style))
story.append(Paragraph("Master of Computer Applications (MCA New) — Semester II", info_style))
story.append(HRFlowable(width="100%", thickness=2, color=colors.HexColor('#1a237e'), spaceAfter=8))

details = [
    ["Course Code", "MCS-220"],
    ["Course Title", "Web Technologies"],
    ["Assignment No.", "MCA_NEW(II)/220/Assign/2025-26"],
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
def code(text): story.append(Paragraph(text.replace('\n', '<br/>').replace(' ', '&nbsp;'), code_style))

# Q1a
story.append(Paragraph("Q1(a): What is a Singleton Design Pattern? Explain a scenario where it is useful in a web application and provide a Java code example. (5 Marks)", q_style))
story.append(Paragraph("<b>Answer:</b>", heading_style))
story.append(Paragraph(
    "The <b>Singleton Design Pattern</b> is a creational design pattern that ensures a class has only <b>one instance</b> throughout the application's lifecycle and provides a global point of access to that instance. It is part of the Gang of Four (GoF) design patterns.",
    body_style))
story.append(Paragraph("<b>Scenario in a Web Application:</b>", heading_style))
story.append(Paragraph(
    "A <b>Database Connection Pool</b> is a classic use case. In a web application, creating a new database connection for every request is extremely expensive (time-consuming, resource-intensive). Instead, a single ConnectionPool object is created when the application starts and is reused by all requests throughout the application's lifetime. The Singleton pattern ensures that only one pool exists, preventing multiple pools from being accidentally created.",
    body_style))
story.append(Paragraph("<b>Java Code Example:</b>", heading_style))
code_text = (
    "public class DatabaseConnectionPool {\n"
    "    // Step 1: Private static instance\n"
    "    private static DatabaseConnectionPool instance;\n\n"
    "    private String connectionString;\n\n"
    "    // Step 2: Private constructor\n"
    "    private DatabaseConnectionPool() {\n"
    "        connectionString = \"jdbc:mysql://localhost:3306/mydb\";\n"
    "        System.out.println(\"Connection Pool Initialized\");\n"
    "    }\n\n"
    "    // Step 3: Public static method (thread-safe with synchronized)\n"
    "    public static synchronized DatabaseConnectionPool getInstance() {\n"
    "        if (instance == null) {\n"
    "            instance = new DatabaseConnectionPool();\n"
    "        }\n"
    "        return instance;\n"
    "    }\n\n"
    "    public String getConnection() {\n"
    "        return \"Connection from pool: \" + connectionString;\n"
    "    }\n"
    "}\n\n"
    "// Usage in Servlet:\n"
    "DatabaseConnectionPool pool = DatabaseConnectionPool.getInstance();\n"
    "String conn = pool.getConnection();"
)
story.append(Paragraph(code_text.replace('\n', '<br/>').replace(' ', '&nbsp;'), code_style))
story.append(Paragraph(
    "The <b>synchronized</b> keyword ensures thread safety in a multi-threaded web environment where multiple requests arrive simultaneously.",
    sub_style))

# Q1b
story.append(Paragraph("Q1(b): Differentiate between Web Server and Web Container. Explain MVC architecture. (5 Marks)", q_style))
story.append(Paragraph("<b>Answer:</b>", heading_style))
diff_data = [
    ["Aspect", "Web Server", "Web Container"],
    ["Definition", "Handles HTTP requests for static content", "Manages lifecycle of Servlets/JSP (dynamic content)"],
    ["Content Type", "Static: HTML, CSS, images, JS files", "Dynamic: Servlets, JSP pages"],
    ["Examples", "Apache HTTP Server, Nginx, IIS", "Apache Tomcat, Jetty, GlassFish"],
    ["Protocol", "HTTP/HTTPS", "Extends HTTP with servlet API"],
    ["Java Support", "No native Java support", "Full Java EE/Jakarta EE support"],
    ["Request Handling", "Serves files directly from file system", "Instantiates, invokes, and destroys servlets"],
]
dt = Table(diff_data, colWidths=[3.5*cm, 6.5*cm, 6.5*cm])
dt.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1a237e')),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTNAME', (0,1), (0,-1), 'Helvetica-Bold'),
    ('FONTSIZE', (0,0), (-1,-1), 9),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#9fa8da')),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#e8eaf6')]),
    ('TOPPADDING', (0,0), (-1,-1), 4),
    ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
]))
story.append(dt)
story.append(Spacer(1, 0.3*cm))
story.append(Paragraph("<b>MVC (Model-View-Controller) Architecture:</b>", heading_style))
story.append(Paragraph(
    "MVC is a software architectural pattern that separates an application into three interconnected components:",
    body_style))
for comp, desc in [
    ("Model", "Represents the data and business logic. It manages data, logic, and rules. It notifies the View of data changes. Example: Java beans, Entity classes, Database interaction layer."),
    ("View", "The presentation layer — what the user sees. Displays the data provided by the Model. It does not contain business logic. Example: JSP pages, HTML/Thymeleaf templates, React components."),
    ("Controller", "Acts as an intermediary between Model and View. It receives user input (HTTP requests), processes it (calling appropriate Model methods), and selects the appropriate View to render. Example: Servlet, Spring MVC @Controller."),
]:
    story.append(Paragraph(f"<b>• {comp}:</b> {desc}", bullet_style))
story.append(Paragraph("<b>MVC Flow:</b> User sends request → Controller receives it → Controller calls Model → Model returns data → Controller passes data to View → View renders response to user.", sub_style))
hr()

# Q2a
story.append(Paragraph("Q2(a): Explain RequestDispatcher and sendRedirect with key differences. (5 Marks)", q_style))
story.append(Paragraph("<b>Answer:</b>", heading_style))
diff2 = [
    ["Feature", "RequestDispatcher (forward/include)", "sendRedirect()"],
    ["Works on", "Server side (internal forward)", "Client side (sends new HTTP request)"],
    ["URL in browser", "Does NOT change", "Changes to new URL"],
    ["Request/Response objects", "Same objects shared", "New request/response created"],
    ["Speed", "Faster (no extra round trip)", "Slower (extra HTTP request)"],
    ["Usage", "Forward to JSP/Servlet within same app", "Redirect to different app or URL"],
    ["Data sharing", "Can share request attributes", "Cannot share request attributes directly"],
    ["Method", "rd.forward(req, res) or rd.include(req,res)", "response.sendRedirect(\"url\")"],
]
dt2 = Table(diff2, colWidths=[4*cm, 6.5*cm, 6*cm])
dt2.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1a237e')),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTNAME', (0,1), (0,-1), 'Helvetica-Bold'),
    ('FONTSIZE', (0,0), (-1,-1), 9),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#9fa8da')),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#e8eaf6')]),
    ('TOPPADDING', (0,0), (-1,-1), 4),
    ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
]))
story.append(dt2)
story.append(Spacer(1, 0.2*cm))
story.append(Paragraph("<b>Example:</b>", heading_style))
story.append(Paragraph(
    "RequestDispatcher rd = request.getRequestDispatcher(\"/result.jsp\"); rd.forward(request, response); — forwards to result.jsp, browser URL stays same.\n\n"
    "response.sendRedirect(\"https://www.google.com\"); — browser URL changes to Google.",
    sub_style))

# Q2b
story.append(Paragraph("Q2(b): What is Session Management? Explain techniques used to manage sessions in Servlets. (5 Marks)", q_style))
story.append(Paragraph("<b>Answer:</b>", heading_style))
story.append(Paragraph(
    "<b>Session Management</b> is the process of maintaining state and user-specific information across multiple HTTP requests in a stateless HTTP protocol. Since HTTP is stateless (each request is independent), session management techniques are needed to remember who the user is across pages.",
    body_style))
story.append(Paragraph("Techniques for Session Management:", heading_style))
techs = [
    ("<b>1. Cookies:</b>", "Small text files stored on the client's browser. The server sends a Set-Cookie header; the browser sends it back with every request. Can store session ID or small data. Example: Cookie c = new Cookie(\"userId\", \"123\"); c.setMaxAge(3600); response.addCookie(c);"),
    ("<b>2. HttpSession API (Server-Side Sessions):</b>", "The most common method in Java Servlets. A session object is stored on the server; only a session ID is stored in a cookie on the client. Example: HttpSession session = request.getSession(); session.setAttribute(\"user\", userObj); String user = (String) session.getAttribute(\"user\");"),
    ("<b>3. URL Rewriting:</b>", "The session ID is appended to every URL as a query parameter. Used when cookies are disabled. Example: http://example.com/profile?jsessionid=abc123"),
    ("<b>4. Hidden Form Fields:</b>", "Session data is embedded in hidden fields of HTML forms and passed with each form submission. Example: &lt;input type='hidden' name='sessionId' value='abc123'/&gt;"),
    ("<b>5. SSL Sessions:</b>", "For secure applications, the SSL/TLS layer maintains session state, eliminating the need for application-level session management."),
]
for t, d in techs:
    story.append(Paragraph(f"{t} {d}", bullet_style))
hr()

# Q3a
story.append(Paragraph("Q3(a): What are JSP Implicit Objects? Explain request, response, session, and out objects. (5 Marks)", q_style))
story.append(Paragraph("<b>Answer:</b>", heading_style))
story.append(Paragraph(
    "JSP Implicit Objects are pre-defined objects that the JSP container makes available automatically in every JSP page. They do not need to be declared or created explicitly. There are 9 implicit objects in JSP.",
    body_style))
imp_objs = [
    ["Object", "Type", "Description & Example"],
    ["request", "HttpServletRequest", "Represents the HTTP request. Used to get form data, request parameters, headers, and attributes.\nExample: String name = request.getParameter(\"name\");"],
    ["response", "HttpServletResponse", "Represents the HTTP response. Used to set content type, send redirects, add cookies.\nExample: response.setContentType(\"text/html\");"],
    ["session", "HttpSession", "Manages user session state across multiple requests.\nExample: session.setAttribute(\"user\", userObj); Object user = session.getAttribute(\"user\");"],
    ["out", "JspWriter", "Used to send output to the client (browser).\nExample: out.println(\"Hello, \" + name);"],
    ["application", "ServletContext", "Represents the entire web application; shared across all users and sessions."],
    ["config", "ServletConfig", "Provides servlet configuration info (init parameters)."],
    ["pageContext", "PageContext", "Provides access to all other implicit objects and page-level scope."],
    ["page", "Object (this)", "Refers to the current JSP page instance."],
    ["exception", "Throwable", "Available only in error pages; holds the exception thrown by the calling page."],
]
iot = Table(imp_objs, colWidths=[3*cm, 4.5*cm, 9*cm])
iot.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1a237e')),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTNAME', (0,1), (0,-1), 'Helvetica-Bold'),
    ('FONTSIZE', (0,0), (-1,-1), 9),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#9fa8da')),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#e8eaf6')]),
    ('TOPPADDING', (0,0), (-1,-1), 4),
    ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
]))
story.append(iot)
hr()

# Q3b
story.append(Paragraph("Q3(b): Explain JSP Action Tags with examples: jsp:include, jsp:forward, jsp:useBean. (5 Marks)", q_style))
story.append(Paragraph("<b>Answer:</b>", heading_style))
story.append(Paragraph("JSP Action Tags are special XML-like tags that control the behaviour of the servlet engine. They are executed at request time.", body_style))

action_tags = [
    ("<b>&lt;jsp:include&gt;</b>",
     "Includes the output of another resource (JSP page, HTML file, or Servlet) into the current JSP page at request time (dynamic inclusion). The included resource is processed and its output is merged.\n\n"
     "Example: &lt;jsp:include page=\"header.jsp\" /&gt;\n"
     "This processes header.jsp and embeds its output here.\n"
     "Difference from <%@ include %> directive: The directive includes at compile time; jsp:include includes at request time, so the included file can be dynamic."),
    ("<b>&lt;jsp:forward&gt;</b>",
     "Forwards the request from the current JSP to another resource (JSP, Servlet, or HTML). The control is permanently transferred; the current page stops processing.\n\n"
     "Example: &lt;jsp:forward page=\"login.jsp\" /&gt;\n"
     "This forwards the request to login.jsp. The browser URL does not change (server-side forward)."),
    ("<b>&lt;jsp:useBean&gt;</b>",
     "Creates or retrieves a JavaBean object and makes it available to the JSP page. It can also set and get bean properties using jsp:setProperty and jsp:getProperty.\n\n"
     "Example:\n"
     "&lt;jsp:useBean id=\"student\" class=\"com.example.Student\" scope=\"session\" /&gt;\n"
     "&lt;jsp:setProperty name=\"student\" property=\"name\" value=\"Rahul\" /&gt;\n"
     "&lt;jsp:getProperty name=\"student\" property=\"name\" /&gt;\n\n"
     "The id attribute is the reference name; class is the fully qualified class name; scope defines where the bean lives (page, request, session, application)."),
]
for tag, content in action_tags:
    story.append(Paragraph(tag, heading_style))
    for para in content.split('\n\n'):
        story.append(Paragraph(para.strip(), sub_style))
    story.append(Spacer(1, 0.1*cm))
hr()

# Q4
story.append(Paragraph("Q4: What is Maven? Explain pom.xml structure and Maven build lifecycle. (5 Marks)", q_style))
story.append(Paragraph("<b>Answer:</b>", heading_style))
story.append(Paragraph(
    "<b>Maven</b> is a powerful build automation and project management tool primarily used for Java projects. It was developed by Apache Software Foundation. Maven manages project builds, dependencies, documentation, and deployment through a standardized project structure and a central configuration file called <b>pom.xml</b>.",
    body_style))
story.append(Paragraph("Key features: dependency management (automatically downloads libraries from Maven Central Repository), standardized directory structure, build lifecycle management, and plugin support.", body_style))

story.append(Paragraph("<b>Structure of pom.xml (Project Object Model):</b>", heading_style))
story.append(Paragraph("The pom.xml is the heart of a Maven project. Key sections include:", body_style))
pom_sections = [
    "<b>Project Coordinates:</b> groupId (e.g., com.ignou.mca), artifactId (project name), version (e.g., 1.0.0), packaging (jar/war).",
    "<b>&lt;dependencies&gt;:</b> Lists all external libraries the project needs. Maven downloads them automatically from repositories.",
    "<b>&lt;build&gt; &amp; &lt;plugins&gt;:</b> Configure build plugins like maven-compiler-plugin (set Java version), spring-boot-maven-plugin (for Spring Boot apps).",
    "<b>&lt;properties&gt;:</b> Define project-wide properties like Java version, encoding settings.",
    "<b>&lt;repositories&gt;:</b> Specify additional Maven repositories beyond the default Maven Central.",
    "<b>&lt;parent&gt;:</b> In Spring Boot, inherits configuration from spring-boot-starter-parent, which provides dependency management defaults.",
]
for s in pom_sections:
    story.append(Paragraph(f"• {s}", bullet_style))

story.append(Paragraph("<b>Maven Build Lifecycle (Default Lifecycle — 8 Key Phases):</b>", heading_style))
lifecycle = [
    ["Phase", "Description"],
    ["validate", "Validates the project structure and pom.xml is correct."],
    ["compile", "Compiles the source code (src/main/java) into bytecode (target/classes)."],
    ["test", "Runs unit tests using a testing framework (JUnit). Tests in src/test/java."],
    ["package", "Packages compiled code into a distributable format — JAR or WAR file."],
    ["verify", "Runs integration tests to verify the package is valid and meets quality criteria."],
    ["install", "Installs the package into the local Maven repository (~/.m2) for use by other local projects."],
    ["deploy", "Copies the final package to a remote repository for sharing with other developers or environments."],
    ["clean", "(Separate lifecycle) Removes the target/ directory — cleans previous build artifacts."],
]
lt = Table(lifecycle, colWidths=[4*cm, 12.5*cm])
lt.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1a237e')),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTNAME', (0,1), (0,-1), 'Helvetica-Bold'),
    ('FONTSIZE', (0,0), (-1,-1), 9),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#9fa8da')),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#e8eaf6')]),
    ('TOPPADDING', (0,0), (-1,-1), 4),
    ('BOTTOMPADDING', (0,0), (-1,-1), 4),
]))
story.append(lt)
story.append(Spacer(1, 0.2*cm))
story.append(Paragraph("Each phase executes all preceding phases automatically. Running mvn package automatically runs validate, compile, test, and package.", sub_style))
hr()

# Q5
story.append(Paragraph("Q5: Explain IoC and Dependency Injection in Spring Framework with example. (5 Marks)", q_style))
story.append(Paragraph("<b>Answer:</b>", heading_style))
story.append(Paragraph("<b>Inversion of Control (IoC):</b>", heading_style))
story.append(Paragraph(
    "Inversion of Control is a design principle where the control of object creation and dependency management is transferred from the application code to a framework or container. Instead of an object creating its own dependencies (traditional approach), the container creates and injects the dependencies.",
    body_style))
story.append(Paragraph("Traditional approach: Service service = new Service(); — the class controls its own dependencies.", sub_style))
story.append(Paragraph("IoC approach: The Spring Container creates the Service object and injects it wherever needed.", sub_style))

story.append(Paragraph("<b>Dependency Injection (DI):</b>", heading_style))
story.append(Paragraph(
    "Dependency Injection is the implementation mechanism of IoC. The Spring IoC container injects dependencies into objects at runtime, based on configuration (XML or annotations). There are three types: Constructor Injection, Setter Injection, and Field Injection (via @Autowired).",
    body_style))

story.append(Paragraph("<b>Example Using Annotations:</b>", heading_style))
example_code = (
    "// Service Interface\n"
    "public interface EmailService {\n"
    "    void sendEmail(String to, String message);\n"
    "}\n\n"
    "// Service Implementation\n"
    "@Service  // marks this as a Spring-managed bean\n"
    "public class EmailServiceImpl implements EmailService {\n"
    "    public void sendEmail(String to, String message) {\n"
    "        System.out.println(\"Sending email to \" + to + \": \" + message);\n"
    "    }\n"
    "}\n\n"
    "// Controller using Dependency Injection\n"
    "@RestController\n"
    "public class UserController {\n"
    "\n"
    "    @Autowired  // Spring injects EmailServiceImpl here automatically\n"
    "    private EmailService emailService;\n"
    "\n"
    "    @GetMapping(\"/register\")\n"
    "    public String registerUser() {\n"
    "        emailService.sendEmail(\"user@example.com\", \"Welcome!\");\n"
    "        return \"User registered successfully!\";\n"
    "    }\n"
    "}"
)
story.append(Paragraph(example_code.replace('\n', '<br/>').replace(' ', '&nbsp;'), code_style))
story.append(Paragraph(
    "<b>Benefits of IoC &amp; DI:</b> Loose coupling between classes; Easier unit testing (mock dependencies can be injected); Better code maintainability; Follows Open/Closed and Dependency Inversion SOLID principles.",
    body_style))
hr()

# Q6a
story.append(Paragraph("Q6(a): Explain Update and Delete operations in Spring Boot + Hibernate with code snippets. (5 Marks)", q_style))
story.append(Paragraph("<b>Answer:</b>", heading_style))
story.append(Paragraph("<b>Entity Class:</b>", heading_style))
story.append(Paragraph(
    "@Entity @Table(name=\"students\") public class Student { @Id @GeneratedValue(strategy=GenerationType.IDENTITY) private Long id; private String name; private String email; // getters and setters }",
    sub_style))
story.append(Paragraph("<b>Repository Layer:</b>", heading_style))
story.append(Paragraph(
    "@Repository public interface StudentRepository extends JpaRepository&lt;Student, Long&gt; { } — JpaRepository provides built-in save(), findById(), deleteById(), findAll() methods.",
    sub_style))
story.append(Paragraph("<b>Service Layer — Update Operation:</b>", heading_style))
story.append(Paragraph(
    "@Service public class StudentService { @Autowired StudentRepository repo;\n\n"
    "public Student updateStudent(Long id, Student updatedData) {\n"
    "   Student existing = repo.findById(id).orElseThrow(() -&gt; new RuntimeException(\"Student not found\"));\n"
    "   existing.setName(updatedData.getName());\n"
    "   existing.setEmail(updatedData.getEmail());\n"
    "   return repo.save(existing); // save() performs INSERT or UPDATE based on whether ID exists\n"
    "} }",
    sub_style))
story.append(Paragraph("<b>Service Layer — Delete Operation:</b>", heading_style))
story.append(Paragraph(
    "public void deleteStudent(Long id) {\n"
    "   if (!repo.existsById(id)) throw new RuntimeException(\"Student not found\");\n"
    "   repo.deleteById(id); // Hibernate generates DELETE SQL automatically\n"
    "}",
    sub_style))
story.append(Paragraph("<b>Controller Layer:</b>", heading_style))
story.append(Paragraph(
    "@PutMapping(\"/students/{id}\") public ResponseEntity&lt;Student&gt; update(@PathVariable Long id, @RequestBody Student s) { return ResponseEntity.ok(service.updateStudent(id, s)); }\n\n"
    "@DeleteMapping(\"/students/{id}\") public ResponseEntity&lt;String&gt; delete(@PathVariable Long id) { service.deleteStudent(id); return ResponseEntity.ok(\"Deleted successfully\"); }",
    sub_style))

# Q6b
story.append(Paragraph("Q6(b): Explain form validation in Spring MVC with example. (5 Marks)", q_style))
story.append(Paragraph("<b>Answer:</b>", heading_style))
story.append(Paragraph(
    "Spring MVC supports Bean Validation (JSR-380) using annotations from the javax.validation / jakarta.validation package. The @Valid annotation on a controller method parameter triggers validation, and errors are captured in a BindingResult object.",
    body_style))
story.append(Paragraph("<b>Model Class with Validation Annotations:</b>", heading_style))
story.append(Paragraph(
    "public class UserRegistration {\n\n"
    "   @NotBlank(message = \"Name is required\")\n"
    "   @Size(min=2, max=50, message = \"Name must be 2-50 chars\")\n"
    "   private String name;\n\n"
    "   @NotBlank(message = \"Email is required\")\n"
    "   @Email(message = \"Invalid email format\")\n"
    "   private String email;\n\n"
    "   @NotBlank(message = \"Password is required\")\n"
    "   @Size(min=8, message = \"Password must be at least 8 characters\")\n"
    "   private String password;\n\n"
    "   @Min(value=18, message = \"Age must be at least 18\")\n"
    "   @Max(value=100, message = \"Age must be at most 100\")\n"
    "   private int age;\n"
    "   // getters and setters\n"
    "}",
    sub_style))
story.append(Paragraph("<b>Controller Method:</b>", heading_style))
story.append(Paragraph(
    "@PostMapping(\"/register\")\n"
    "public String register(@Valid @ModelAttribute UserRegistration user, BindingResult result, Model model) {\n"
    "   if (result.hasErrors()) {\n"
    "      return \"registration-form\"; // return to form view with errors\n"
    "   }\n"
    "   userService.save(user);\n"
    "   return \"redirect:/success\";\n"
    "}",
    sub_style))
story.append(Paragraph("<b>In the JSP/Thymeleaf View, display errors:</b> &lt;form:errors path=\"name\" cssClass=\"error\" /&gt; — this displays the validation error message next to the input field.", sub_style))
hr()

# Q7
story.append(Paragraph("Q7: Explain request processing workflow in Spring MVC. Describe DispatcherServlet, Controller, and ViewResolver. (5 Marks)", q_style))
story.append(Paragraph("<b>Answer:</b>", heading_style))
story.append(Paragraph(
    "Spring MVC follows a well-defined request processing workflow centered around the <b>DispatcherServlet</b> (Front Controller pattern).",
    body_style))
story.append(Paragraph("<b>Step-by-Step Workflow:</b>", heading_style))
steps = [
    "Client sends HTTP request (e.g., GET /students) to the web server.",
    "DispatcherServlet (Front Controller) receives all requests — it is configured in web.xml or via @SpringBootApplication. It acts as the central dispatcher for all Spring MVC requests.",
    "DispatcherServlet consults the HandlerMapping to find which Controller method handles this request (based on @RequestMapping, @GetMapping, etc.).",
    "DispatcherServlet invokes the appropriate Controller method.",
    "Controller processes the request (calls service/repository layers, builds model data), then returns a ModelAndView object containing: the view name (logical name like 'studentList') and model data (key-value pairs of data to display).",
    "DispatcherServlet consults the ViewResolver to map the logical view name to an actual view template (e.g., 'studentList' → /WEB-INF/views/studentList.jsp or studentList.html).",
    "ViewResolver resolves the view and the View renders the HTML response using the model data.",
    "DispatcherServlet sends the final HTML response back to the client.",
]
for i, s in enumerate(steps, 1):
    story.append(Paragraph(f"<b>Step {i}:</b> {s}", bullet_style))

story.append(Paragraph("<b>Key Components:</b>", heading_style))
comps = [
    ("<b>DispatcherServlet:</b>", "The Front Controller. Single entry point for all requests. Coordinates all other components (HandlerMapping, Controller, ViewResolver)."),
    ("<b>HandlerMapping:</b>", "Maps incoming requests to the appropriate Controller method based on URL patterns and HTTP method type."),
    ("<b>Controller:</b>", "Annotated with @Controller or @RestController. Contains handler methods annotated with @GetMapping, @PostMapping, etc. Contains business logic orchestration."),
    ("<b>ViewResolver:</b>", "Translates logical view names returned by Controller into actual view implementations. Common resolvers: InternalResourceViewResolver (for JSP), ThymeleafViewResolver (for Thymeleaf templates)."),
    ("<b>Model:</b>", "A Map that holds data to be passed from Controller to the View for rendering."),
]
for name, desc in comps:
    story.append(Paragraph(f"• {name} {desc}", bullet_style))
hr()

# Q8a
story.append(Paragraph("Q8(a): Describe Spring Security configuration in Spring Boot using Java-based configuration. (5 Marks)", q_style))
story.append(Paragraph("<b>Answer:</b>", heading_style))
story.append(Paragraph("Spring Security is a powerful authentication and access-control framework for Spring applications. In Spring Boot, it auto-configures basic security. We override it with a custom Java configuration class.", body_style))
story.append(Paragraph("<b>Steps to Configure Spring Security:</b>", heading_style))
for step in [
    "<b>Step 1 — Add Dependency:</b> In pom.xml: &lt;dependency&gt;&lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;&lt;artifactId&gt;spring-boot-starter-security&lt;/artifactId&gt;&lt;/dependency&gt;",
    "<b>Step 2 — Create Security Configuration Class:</b>",
]:
    story.append(Paragraph(f"• {step}", bullet_style))
story.append(Paragraph(
    "@Configuration\n"
    "@EnableWebSecurity\n"
    "public class SecurityConfig {\n\n"
    "   @Bean\n"
    "   public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {\n"
    "      http\n"
    "         .authorizeHttpRequests(auth -&gt; auth\n"
    "            .requestMatchers(\"/public/**\", \"/login\", \"/register\").permitAll()\n"
    "            .requestMatchers(\"/admin/**\").hasRole(\"ADMIN\")\n"
    "            .anyRequest().authenticated()\n"
    "         )\n"
    "         .formLogin(form -&gt; form\n"
    "            .loginPage(\"/login\")\n"
    "            .defaultSuccessUrl(\"/dashboard\")\n"
    "            .permitAll()\n"
    "         )\n"
    "         .logout(logout -&gt; logout.logoutUrl(\"/logout\").permitAll())\n"
    "         .csrf(csrf -&gt; csrf.disable()); // disable CSRF for REST APIs\n"
    "      return http.build();\n"
    "   }\n\n"
    "   @Bean\n"
    "   public PasswordEncoder passwordEncoder() {\n"
    "      return new BCryptPasswordEncoder(); // secure password hashing\n"
    "   }\n"
    "}",
    sub_style))
story.append(Paragraph("This configuration: allows unauthenticated access to /public/**, /login, /register; requires ADMIN role for /admin/**; requires authentication for all other endpoints; configures custom login page and logout; uses BCrypt for password hashing.", sub_style))

# Q8b
story.append(Paragraph("Q8(b): Write a complete Servlet program that retrieves user data from HTML form and inserts into database using JDBC. (5 Marks)", q_style))
story.append(Paragraph("<b>Answer:</b>", heading_style))
story.append(Paragraph("<b>HTML Form (index.html):</b>", heading_style))
story.append(Paragraph(
    "&lt;form action=\"RegisterServlet\" method=\"POST\"&gt;\n"
    "   Name: &lt;input type=\"text\" name=\"name\" required&gt;&lt;br&gt;\n"
    "   Email: &lt;input type=\"email\" name=\"email\" required&gt;&lt;br&gt;\n"
    "   &lt;input type=\"submit\" value=\"Register\"&gt;\n"
    "&lt;/form&gt;",
    sub_style))
story.append(Paragraph("<b>Servlet (RegisterServlet.java):</b>", heading_style))
story.append(Paragraph(
    "@WebServlet(\"/RegisterServlet\")\n"
    "public class RegisterServlet extends HttpServlet {\n\n"
    "   private static final String DB_URL = \"jdbc:mysql://localhost:3306/userdb\";\n"
    "   private static final String DB_USER = \"root\";\n"
    "   private static final String DB_PASS = \"password\";\n\n"
    "   protected void doPost(HttpServletRequest request, HttpServletResponse response)\n"
    "         throws ServletException, IOException {\n\n"
    "      // Step 1: Get form parameters\n"
    "      String name = request.getParameter(\"name\");\n"
    "      String email = request.getParameter(\"email\");\n\n"
    "      response.setContentType(\"text/html\");\n"
    "      PrintWriter out = response.getWriter();\n\n"
    "      // Step 2: Establish JDBC connection and insert data\n"
    "      try {\n"
    "         Class.forName(\"com.mysql.cj.jdbc.Driver\");\n"
    "         Connection conn = DriverManager.getConnection(DB_URL, DB_USER, DB_PASS);\n\n"
    "         // Step 3: Use PreparedStatement (prevents SQL injection)\n"
    "         String sql = \"INSERT INTO users (name, email) VALUES (?, ?)\";\n"
    "         PreparedStatement ps = conn.prepareStatement(sql);\n"
    "         ps.setString(1, name);\n"
    "         ps.setString(2, email);\n\n"
    "         int rowsInserted = ps.executeUpdate();\n\n"
    "         if (rowsInserted > 0) {\n"
    "            out.println(\"&lt;h3&gt;User registered successfully!&lt;/h3&gt;\");\n"
    "         } else {\n"
    "            out.println(\"&lt;h3&gt;Registration failed!&lt;/h3&gt;\");\n"
    "         }\n"
    "         ps.close(); conn.close();\n\n"
    "      } catch (Exception e) {\n"
    "         out.println(\"Error: \" + e.getMessage());\n"
    "      }\n"
    "   }\n"
    "}",
    sub_style))
story.append(Paragraph("<b>Database Table:</b> CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100) NOT NULL, email VARCHAR(100) UNIQUE NOT NULL);", sub_style))
hr()

# Q9
story.append(Paragraph("Q9: Write short notes on: (a) Hibernate ORM Framework (b) JSP Directives (c) Spring Boot Actuator (15 Marks)", q_style))
story.append(Paragraph("<b>Answer:</b>", heading_style))

story.append(Paragraph("<b>(a) Hibernate ORM Framework</b>", heading_style))
story.append(Paragraph(
    "Hibernate is an open-source Object-Relational Mapping (ORM) framework for Java that simplifies database interactions by mapping Java objects (POJOs) to database tables. It eliminates the need to write verbose JDBC code and generates SQL queries automatically.",
    body_style))
for pt in [
    "<b>ORM Mapping:</b> Java classes (entities) are mapped to database tables using annotations (@Entity, @Table, @Column) or XML mapping files.",
    "<b>Session and SessionFactory:</b> SessionFactory is a heavyweight object created once per application; Session is a lightweight object used for actual database operations (save, update, delete, get).",
    "<b>HQL (Hibernate Query Language):</b> An object-oriented query language similar to SQL but operates on entity objects instead of database tables.",
    "<b>Automatic SQL Generation:</b> Hibernate generates INSERT, UPDATE, DELETE, SELECT statements based on operations performed on entity objects.",
    "<b>Caching:</b> First-level cache (session-level, mandatory) and Second-level cache (SessionFactory-level, optional) improve performance.",
    "<b>Lazy Loading:</b> Related objects are loaded from database only when accessed, not immediately, improving performance.",
    "<b>Transaction Management:</b> Integrates with JTA and Spring's @Transactional for declarative transaction management.",
    "<b>JPA Integration:</b> Hibernate is the most popular JPA (Java Persistence API) implementation. Spring Boot uses Spring Data JPA with Hibernate as the default provider.",
]:
    story.append(Paragraph(f"• {pt}", bullet_style))

story.append(Paragraph("<b>(b) JSP Directives</b>", heading_style))
story.append(Paragraph(
    "JSP Directives are instructions to the JSP container that affect the overall structure and behaviour of the compiled servlet. They are processed at compile time (not request time) and use the syntax: &lt;%@ directive_name attribute=\"value\" %&gt;",
    body_style))

directives = [
    ("<b>1. Page Directive:</b>", "&lt;%@ page language=\"java\" contentType=\"text/html; charset=UTF-8\" import=\"java.util.*\" session=\"true\" errorPage=\"error.jsp\" %&gt; — Defines page-level attributes: programming language, content type, character encoding, imported packages, session usage, and error page. Key attributes: language, contentType, import, session, errorPage, isErrorPage."),
    ("<b>2. Include Directive:</b>", "&lt;%@ include file=\"header.jsp\" %&gt; — Statically includes the content of another file (JSP, HTML) at compile time. The included file's content is merged into the current JSP before compilation. Since it's compile-time inclusion, the included file cannot be dynamic per request. Used for static elements like headers, footers, nav bars."),
    ("<b>3. Taglib Directive:</b>", "&lt;%@ taglib uri=\"http://java.sun.com/jsp/jstl/core\" prefix=\"c\" %&gt; — Declares a custom tag library to be used in the JSP page. uri identifies the tag library; prefix is the shorthand used in the page (e.g., &lt;c:forEach&gt;, &lt;c:if&gt;). JSTL (JavaServer Pages Standard Tag Library) tags are the most commonly used."),
]
for name, content in directives:
    story.append(Paragraph(f"{name} {content}", bullet_style))

story.append(Paragraph("<b>(c) Spring Boot Actuator</b>", heading_style))
story.append(Paragraph(
    "Spring Boot Actuator is a sub-project of Spring Boot that provides production-ready monitoring and management features for Spring Boot applications. It exposes a set of built-in endpoints (over HTTP or JMX) that provide operational information about the running application.",
    body_style))
for pt in [
    "<b>Dependency:</b> spring-boot-starter-actuator — add this to pom.xml.",
    "<b>Built-in Endpoints:</b> /actuator/health — application health status (UP/DOWN); /actuator/info — application info (version, build details); /actuator/metrics — performance metrics (JVM memory, CPU usage, request counts); /actuator/env — environment properties; /actuator/beans — list of all Spring beans; /actuator/loggers — view and change log levels at runtime; /actuator/httptrace — recent HTTP request/response traces.",
    "<b>Health Indicators:</b> Automatically checks health of database, disk space, Redis, RabbitMQ, etc. and reports UP/DOWN status.",
    "<b>Security:</b> Sensitive endpoints are secured by default. Configure access in application.properties: management.endpoints.web.exposure.include=health,info,metrics",
    "<b>Custom Endpoints:</b> You can create custom actuator endpoints by annotating a class with @Endpoint and methods with @ReadOperation, @WriteOperation.",
    "<b>Use Cases:</b> DevOps teams use Actuator for monitoring deployment health, CI/CD pipeline health checks, performance dashboards (integrated with Prometheus + Grafana), and runtime configuration changes.",
]:
    story.append(Paragraph(f"• {pt}", bullet_style))

doc.build(story)
print("MCS-220 PDF created successfully.")