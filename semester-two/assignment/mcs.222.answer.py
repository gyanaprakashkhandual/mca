from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY

doc = SimpleDocTemplate(
    "MCS-222_Answers.pdf",
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
code_style = ParagraphStyle('Code', parent=styles['Code'], fontSize=8.5, fontName='Courier', leading=12, leftIndent=20, spaceAfter=6, backColor=colors.HexColor('#f5f5f5'), borderPadding=6)

story = []

# Header
story.append(Paragraph("INDIRA GANDHI NATIONAL OPEN UNIVERSITY", title_style))
story.append(Paragraph("School of Computer and Information Sciences", subtitle_style))
story.append(Paragraph("Master of Computer Applications (MCA New) — Semester II", info_style))
story.append(HRFlowable(width="100%", thickness=2, color=colors.HexColor('#1a237e'), spaceAfter=8))

details = [
    ["Course Code", "MCSL-222"],
    ["Course Title", "OOAD and Web Technologies Lab"],
    ["Assignment No.", "MCA_NEW(II)/L-222/Assign/2025-26"],
    ["Maximum Marks", "100 (Section 1: 20 + Section 2: 20 + Lab Records: 40 + Viva Voce: 20)"],
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
story.append(Spacer(1, 0.3*cm))
story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#9fa8da'), spaceAfter=8))

def hr(): story.append(HRFlowable(width="100%", thickness=0.5, color=colors.grey, spaceBefore=8, spaceAfter=8))

def code_block(text):
    lines = text.strip().split('\n')
    formatted = '<br/>'.join(l.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace(' ', '&nbsp;') for l in lines)
    story.append(Paragraph(formatted, code_style))

# ═══════════════════════════════════
# SECTION 1: OOAD LAB
# ═══════════════════════════════════
story.append(Paragraph("SECTION 1: OOAD Lab", ParagraphStyle('SectionHead', parent=styles['Normal'], fontSize=13, fontName='Helvetica-Bold', textColor=colors.white, backColor=colors.HexColor('#1a237e'), spaceAfter=10, spaceBefore=10, alignment=TA_CENTER, borderPadding=6)))

# Q1 Section 1
story.append(Paragraph("Q1: Draw Use Case Diagram and Deployment Diagram for Online Shopping System. (10 Marks)", q_style))
story.append(Paragraph("<b>Answer:</b>", heading_style))

story.append(Paragraph("<b>Assumptions:</b>", heading_style))
for pt in [
    "The system supports Customer registration, browsing, ordering, payment, and order tracking.",
    "Admin can manage products, inventory, and orders.",
    "The system integrates with a Payment Gateway.",
    "Delivery Partner handles order shipping.",
    "The system has a web application tier and a database tier.",
]:
    story.append(Paragraph(f"• {pt}", bullet_style))

# Use Case Diagram
story.append(Paragraph("<b>Use Case Diagram — Online Shopping System:</b>", heading_style))
story.append(Paragraph("<b>Actors:</b> Customer, Admin, Payment Gateway, Delivery Partner", body_style))

story.append(Paragraph("<b>Use Cases and Actor Associations:</b>", heading_style))
uc_data = [
    ["Actor", "Use Cases"],
    ["Customer", "Register / Login, Browse Products, Search Products, Add to Cart, Place Order, Make Payment, Track Order, Write Review, Manage Profile, View Order History"],
    ["Admin", "Login, Manage Products (Add/Edit/Delete), Manage Inventory, View Orders, Update Order Status, Generate Reports, Manage Customers, Manage Categories"],
    ["Payment Gateway", "Process Payment, Validate Transaction, Send Payment Confirmation"],
    ["Delivery Partner", "Receive Order Details, Update Delivery Status, Confirm Delivery"],
]
uct = Table(uc_data, colWidths=[4*cm, 12.5*cm])
uct.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1a237e')),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTNAME', (0,1), (0,-1), 'Helvetica-Bold'),
    ('FONTSIZE', (0,0), (-1,-1), 9.5),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#9fa8da')),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#e8eaf6')]),
    ('TOPPADDING', (0,0), (-1,-1), 5),
    ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
]))
story.append(uct)
story.append(Spacer(1, 0.3*cm))

story.append(Paragraph("<b>Relationships in Use Case Diagram:</b>", heading_style))
for rel in [
    "<b>&lt;&lt;include&gt;&gt;:</b> Place Order includes Make Payment (payment is always part of placing an order).",
    "<b>&lt;&lt;include&gt;&gt;:</b> Place Order includes Validate Cart.",
    "<b>&lt;&lt;extend&gt;&gt;:</b> Apply Coupon Code extends Place Order (optional step).",
    "<b>&lt;&lt;extend&gt;&gt;:</b> Write Review extends View Order History (optional).",
    "<b>Generalization:</b> Customer and Admin both generalize from 'User' (both can Login).",
]:
    story.append(Paragraph(f"• {rel}", bullet_style))

story.append(Paragraph("<b>Use Case Diagram (Textual/ASCII Representation):</b>", heading_style))
uc_ascii = """
+------------------------------------------------------------------+
|              ONLINE SHOPPING SYSTEM (System Boundary)            |
|                                                                  |
|  Customer -----> [ Register/Login ]                              |
|  Customer -----> [ Browse Products ]                             |
|  Customer -----> [ Search Products ]                             |
|  Customer -----> [ Add to Cart ]                                 |
|  Customer -----> [ Place Order ] ---<<include>>---> [Make Payment]|
|                  [ Place Order ] ---<<extend>>----> [Apply Coupon]|
|  Customer -----> [ Track Order ]                                 |
|  Customer -----> [ Write Review ]                                |
|                                                                  |
|  Admin --------> [ Manage Products ]                             |
|  Admin --------> [ Manage Orders ]                               |
|  Admin --------> [ Generate Reports ]                            |
|                                                                  |
|  Payment GW ---> [ Process Payment ]                             |
|  Delivery -----> [ Update Delivery Status ]                      |
+------------------------------------------------------------------+
"""
story.append(Paragraph(uc_ascii.replace('\n', '<br/>').replace(' ', '&nbsp;'), code_style))

# Deployment Diagram
story.append(Paragraph("<b>Deployment Diagram — Online Shopping System:</b>", heading_style))
story.append(Paragraph(
    "A Deployment Diagram shows the physical hardware nodes and how software components are deployed on them.",
    body_style))

story.append(Paragraph("<b>Nodes and Components:</b>", heading_style))
dd_data = [
    ["Node (Hardware)", "Deployed Artifact / Component"],
    ["Client Device (PC/Mobile Browser)", "Web Browser, Mobile App (Android/iOS)"],
    ["Web Server (Apache Tomcat / Nginx)", "JSP Pages, HTML/CSS/JS files, Spring MVC Controllers, Servlets"],
    ["Application Server (JEE / Spring Boot)", "Business Logic Layer, Service Classes, DAO Layer, REST API"],
    ["Database Server (MySQL / Oracle)", "Customer DB, Product DB, Order DB, Inventory DB, Review DB"],
    ["Payment Gateway Server (External)", "Payment Processing Service, Transaction Validation API"],
    ["Mail Server (SMTP)", "Email Notification Service (Order Confirmation, Password Reset)"],
    ["CDN (Content Delivery Network)", "Static assets: Images, CSS, JS files — served globally"],
    ["Delivery Partner System (External)", "Delivery Tracking API, Shipping Management System"],
]
ddt = Table(dd_data, colWidths=[6*cm, 10.5*cm])
ddt.setStyle(TableStyle([
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
story.append(ddt)
story.append(Spacer(1, 0.3*cm))

story.append(Paragraph("<b>Communication Links:</b>", heading_style))
for link in [
    "Client Device ←—HTTPS—→ Web Server (port 443)",
    "Web Server ←—HTTP—→ Application Server (internal network)",
    "Application Server ←—JDBC/TCP—→ Database Server (port 3306)",
    "Application Server ←—HTTPS/REST API—→ Payment Gateway (external)",
    "Application Server ←—SMTP—→ Mail Server (port 587)",
    "Application Server ←—REST API—→ Delivery Partner System (external)",
    "Client Device ←—HTTPS—→ CDN (for static assets)",
]:
    story.append(Paragraph(f"• {link}", bullet_style))

story.append(Paragraph("<b>Deployment Architecture (Textual Representation):</b>", heading_style))
deploy_ascii = """
[Client: PC/Mobile]
       | HTTPS
       v
[Web Server Node: Nginx]
  <<artifact>>: HTML, CSS, JS, JSP
       | HTTP (internal)
       v
[Application Server Node: Tomcat/Spring Boot]
  <<artifact>>: Controllers, Services, DAO
  <<artifact>>: REST APIs
       |           |              |
       | JDBC      | HTTPS        | SMTP
       v           v              v
[DB Server]  [Payment GW]   [Mail Server]
  MySQL DB    (External)     (SMTP Server)
                             
[CDN] <--- Static Assets --- [Application Server]
"""
story.append(Paragraph(deploy_ascii.replace('\n', '<br/>').replace(' ', '&nbsp;'), code_style))
hr()

# Q2 Section 1
story.append(Paragraph("Q2: Draw Class Diagram for Online Shopping System. Make necessary assumptions. (10 Marks)", q_style))
story.append(Paragraph("<b>Answer:</b>", heading_style))
story.append(Paragraph("<b>Assumptions:</b> The system handles user registration, product management, cart, orders, payments, and reviews.", body_style))

story.append(Paragraph("<b>Classes with Attributes and Methods:</b>", heading_style))
classes_data = [
    ["Class", "Attributes", "Methods"],
    ["User (Abstract)", "userId, name, email, password, phone, createdAt", "login(), logout(), updateProfile()"],
    ["Customer (extends User)", "shippingAddress, loyaltyPoints, wishlist", "browseProducts(), placeOrder(), trackOrder(), writeReview()"],
    ["Admin (extends User)", "adminRole, permissions", "manageProducts(), manageOrders(), generateReport()"],
    ["Product", "productId, name, description, price, stockQty, category, imageUrl, rating", "getDetails(), checkAvailability(), updateStock()"],
    ["Category", "categoryId, name, description, parentCategory", "getProducts(), addProduct()"],
    ["Cart", "cartId, customerId, items[], totalAmount, createdAt", "addItem(), removeItem(), updateQuantity(), clearCart(), getTotal()"],
    ["CartItem", "cartItemId, productId, quantity, unitPrice, subtotal", "calculateSubtotal()"],
    ["Order", "orderId, customerId, items[], totalAmount, status, orderDate, deliveryDate", "placeOrder(), cancelOrder(), getOrderDetails(), updateStatus()"],
    ["OrderItem", "orderItemId, productId, quantity, unitPrice, subtotal", "calculateSubtotal()"],
    ["Payment", "paymentId, orderId, amount, method, status, transactionId, paymentDate", "processPayment(), verifyPayment(), refund()"],
    ["Review", "reviewId, customerId, productId, rating, comment, reviewDate", "submitReview(), editReview(), deleteReview()"],
    ["Address", "addressId, street, city, state, pincode, country, isDefault", "validate()"],
    ["Inventory", "inventoryId, productId, quantity, reorderLevel, lastUpdated", "updateStock(), checkReorderLevel(), generateAlert()"],
]
ct = Table(classes_data, colWidths=[3.5*cm, 7*cm, 6*cm])
ct.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1a237e')),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTNAME', (0,1), (0,-1), 'Helvetica-Bold'),
    ('FONTSIZE', (0,0), (-1,-1), 8.5),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#9fa8da')),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#e8eaf6')]),
    ('TOPPADDING', (0,0), (-1,-1), 4),
    ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
]))
story.append(ct)
story.append(Spacer(1, 0.3*cm))

story.append(Paragraph("<b>Relationships Between Classes:</b>", heading_style))
relationships = [
    ["Relationship", "Classes Involved", "Type", "Multiplicity"],
    ["Inheritance", "Customer extends User; Admin extends User", "Generalization", "—"],
    ["Customer places Order", "Customer — Order", "Association", "1 Customer : 0..* Orders"],
    ["Order contains OrderItems", "Order — OrderItem", "Composition", "1 Order : 1..* OrderItems"],
    ["OrderItem refers to Product", "OrderItem — Product", "Association", "1..* OrderItems : 1 Product"],
    ["Customer has Cart", "Customer — Cart", "Composition", "1 Customer : 1 Cart"],
    ["Cart has CartItems", "Cart — CartItem", "Composition", "1 Cart : 0..* CartItems"],
    ["CartItem refers to Product", "CartItem — Product", "Association", "* CartItems : 1 Product"],
    ["Order has Payment", "Order — Payment", "Association", "1 Order : 1 Payment"],
    ["Customer writes Review", "Customer — Review", "Association", "1 Customer : 0..* Reviews"],
    ["Review is for Product", "Review — Product", "Association", "0..* Reviews : 1 Product"],
    ["Product belongs to Category", "Product — Category", "Association", "* Products : 1 Category"],
    ["Admin manages Inventory", "Admin — Inventory", "Dependency", "1 Admin : * Inventory"],
    ["Inventory tracks Product", "Inventory — Product", "Association", "1 Inventory : 1 Product"],
    ["Customer has Address", "Customer — Address", "Aggregation", "1 Customer : 1..* Addresses"],
]
rt = Table(relationships, colWidths=[4*cm, 5*cm, 3.5*cm, 4*cm])
rt.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1a237e')),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTSIZE', (0,0), (-1,-1), 8.5),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#9fa8da')),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#e8eaf6')]),
    ('TOPPADDING', (0,0), (-1,-1), 4),
    ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
]))
story.append(rt)
story.append(Spacer(1, 0.2*cm))

story.append(Paragraph("<b>Class Diagram (Compact Textual UML Notation):</b>", heading_style))
class_ascii = """
                    +----------+
                    |  <<abstract>>  |
                    |    User    |
                    +----------+
                    |+userId   |
                    |+name     |
                    |+email    |
                    |+password |
                    +----------+
                    |+login()  |
                    |+logout() |
                    +----------+
                   /            \\
          <<extends>>          <<extends>>
         /                          \\
+-------------+              +----------+
|  Customer   |              |  Admin   |
+-------------+              +----------+
|+address     |              |+role     |
|+loyaltyPts  |              |+perms    |
+-------------+              +----------+
|+placeOrder()|              |+manage() |
+-------------+              +----------+
     |1                          |1
     |0..*                       |0..*
+--------+   1..*  +---------+   1    +----------+
|  Order |<>-------|OrderItem|------->| Product  |
+--------+         +---------+        +----------+
|+status |         |+qty     |        |+price    |
+--------+         |+price   |        |+stock    |
     |1            +---------+        +----------+
     |1                                    |0..*
+----------+                          +--------+
| Payment  |                          | Review |
+----------+                          +--------+
|+amount   |                          |+rating |
|+method   |                          |+comment|
+----------+                          +--------+
"""
story.append(Paragraph(class_ascii.replace('\n', '<br/>').replace(' ', '&nbsp;'), code_style))

# ═══════════════════════════════════
# SECTION 2: WEB TECHNOLOGIES LAB
# ═══════════════════════════════════
story.append(Paragraph("SECTION 2: Web Technologies Lab", ParagraphStyle('SectionHead2', parent=styles['Normal'], fontSize=13, fontName='Helvetica-Bold', textColor=colors.white, backColor=colors.HexColor('#1a237e'), spaceAfter=10, spaceBefore=10, alignment=TA_CENTER, borderPadding=6)))

# Q1 Section 2
story.append(Paragraph("Q1: Write a program using JDBC and JSP to support editing (address modification, mobile number/email update) of customers of online shopping portal. The program should take email-id or registered mobile number as input. (10 Marks)", q_style))
story.append(Paragraph("<b>Answer:</b>", heading_style))

story.append(Paragraph("<b>Assumptions:</b> MySQL database with a 'customers' table. Tomcat server with MySQL JDBC driver.", body_style))
story.append(Paragraph("<b>Database Table:</b>", heading_style))

sql_create = """CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    name        VARCHAR(100) NOT NULL,
    email       VARCHAR(100) UNIQUE NOT NULL,
    mobile      VARCHAR(15)  UNIQUE NOT NULL,
    address     TEXT,
    city        VARCHAR(50),
    pincode     VARCHAR(10)
);

-- Sample data
INSERT INTO customers VALUES (1,'Rahul Sharma','rahul@email.com','9876543210','12 MG Road','Mumbai','400001');"""
story.append(Paragraph(sql_create.replace('\n','<br/>').replace(' ','&nbsp;'), code_style))

story.append(Paragraph("<b>File 1: search.html — Search Form</b>", heading_style))
html1 = """<!DOCTYPE html>
<html>
<head>
  <title>Customer Search</title>
  <style>
    body { font-family: Arial; max-width: 500px; margin: 50px auto; }
    input, select { width: 100%; padding: 8px; margin: 8px 0; box-sizing: border-box; }
    button { background: #1a237e; color: white; padding: 10px 20px; border: none; cursor: pointer; width: 100%; }
  </style>
</head>
<body>
  <h2>Customer Profile Update</h2>
  <form action="SearchCustomer.jsp" method="post">
    <label>Search By:</label>
    <select name="searchType">
      <option value="email">Email ID</option>
      <option value="mobile">Mobile Number</option>
    </select>
    <label>Enter Value:</label>
    <input type="text" name="searchValue" placeholder="Enter email or mobile" required/>
    <button type="submit">Find Customer</button>
  </form>
</body>
</html>"""
story.append(Paragraph(html1.replace('\n','<br/>').replace(' ','&nbsp;').replace('<','&lt;').replace('>','&gt;'), code_style))

story.append(Paragraph("<b>File 2: SearchCustomer.jsp — Fetch and Display Edit Form</b>", heading_style))
jsp1 = """<%@ page import="java.sql.*" %>
<%
  String searchType  = request.getParameter("searchType");
  String searchValue = request.getParameter("searchValue");
  String sql = searchType.equals("email")
             ? "SELECT * FROM customers WHERE email = ?"
             : "SELECT * FROM customers WHERE mobile = ?";

  String dbURL  = "jdbc:mysql://localhost:3306/shoppingdb";
  String dbUser = "root";
  String dbPass = "password";

  Class.forName("com.mysql.cj.jdbc.Driver");
  Connection conn = DriverManager.getConnection(dbURL, dbUser, dbPass);
  PreparedStatement ps = conn.prepareStatement(sql);
  ps.setString(1, searchValue);
  ResultSet rs = ps.executeQuery();

  if (rs.next()) {
    int    custId  = rs.getInt("customer_id");
    String name    = rs.getString("name");
    String email   = rs.getString("email");
    String mobile  = rs.getString("mobile");
    String address = rs.getString("address");
    String city    = rs.getString("city");
    String pincode = rs.getString("pincode");
%>
<!DOCTYPE html>
<html>
<head>
  <title>Edit Customer</title>
  <style>
    body { font-family: Arial; max-width: 550px; margin: 30px auto; }
    input { width: 100%; padding: 8px; margin: 6px 0; box-sizing: border-box; }
    .btn { background: #1a237e; color: white; padding: 10px; border: none; cursor: pointer; width: 100%; }
    .info { background: #e8eaf6; padding: 10px; border-radius: 4px; margin-bottom: 15px; }
  </style>
</head>
<body>
  <h2>Edit Customer Profile</h2>
  <div class="info"><b>Customer:</b> <%=name%> | <b>ID:</b> <%=custId%></div>
  <form action="UpdateCustomer.jsp" method="post">
    <input type="hidden" name="customerId" value="<%=custId%>"/>
    <label>Email ID:</label>
    <input type="email" name="email" value="<%=email%>" required/>
    <label>Mobile Number:</label>
    <input type="text" name="mobile" value="<%=mobile%>" maxlength="10" required/>
    <label>Address:</label>
    <input type="text" name="address" value="<%=address%>"/>
    <label>City:</label>
    <input type="text" name="city" value="<%=city%>"/>
    <label>Pincode:</label>
    <input type="text" name="pincode" value="<%=pincode%>" maxlength="6"/>
    <button type="submit" class="btn">Update Profile</button>
  </form>
</body>
</html>
<%
  } else {
    out.println("<h3 style='color:red;'>No customer found with the given " + searchType + "!</h3>");
    out.println("<a href='search.html'>Go Back</a>");
  }
  rs.close(); ps.close(); conn.close();
%>"""
story.append(Paragraph(jsp1.replace('\n','<br/>').replace(' ','&nbsp;').replace('<','&lt;').replace('>','&gt;'), code_style))

story.append(Paragraph("<b>File 3: UpdateCustomer.jsp — Process Update</b>", heading_style))
jsp2 = """<%@ page import="java.sql.*" %>
<%
  int    custId  = Integer.parseInt(request.getParameter("customerId"));
  String email   = request.getParameter("email");
  String mobile  = request.getParameter("mobile");
  String address = request.getParameter("address");
  String city    = request.getParameter("city");
  String pincode = request.getParameter("pincode");

  String dbURL  = "jdbc:mysql://localhost:3306/shoppingdb";
  String dbUser = "root";
  String dbPass = "password";

  Class.forName("com.mysql.cj.jdbc.Driver");
  Connection conn = DriverManager.getConnection(dbURL, dbUser, dbPass);

  String sql = "UPDATE customers SET email=?, mobile=?, address=?, city=?, pincode=? "
             + "WHERE customer_id=?";
  PreparedStatement ps = conn.prepareStatement(sql);
  ps.setString(1, email);
  ps.setString(2, mobile);
  ps.setString(3, address);
  ps.setString(4, city);
  ps.setString(5, pincode);
  ps.setInt(6, custId);

  int rows = ps.executeUpdate();
  ps.close(); conn.close();
%>
<!DOCTYPE html>
<html>
<head><title>Update Result</title></head>
<body style="font-family:Arial; max-width:500px; margin:50px auto;">
  <% if (rows > 0) { %>
    <h2 style="color:green;">Profile Updated Successfully!</h2>
    <p><b>Email:</b> <%=email%></p>
    <p><b>Mobile:</b> <%=mobile%></p>
    <p><b>Address:</b> <%=address%>, <%=city%> - <%=pincode%></p>
  <% } else { %>
    <h2 style="color:red;">Update Failed! Please try again.</h2>
  <% } %>
  <a href="search.html">Back to Search</a>
</body>
</html>"""
story.append(Paragraph(jsp2.replace('\n','<br/>').replace(' ','&nbsp;').replace('<','&lt;').replace('>','&gt;'), code_style))

story.append(Paragraph("<b>Sample Input/Output:</b>", heading_style))
io_data = [
    ["Step", "Input", "Output"],
    ["1. Search", "Search by: Email | Value: rahul@email.com", "Edit form displayed with current details"],
    ["2. Edit", "Update mobile to: 9998887776, Address: 45 Park Street", "Form submitted to UpdateCustomer.jsp"],
    ["3. Result", "—", "'Profile Updated Successfully!' with updated values shown"],
]
iot = Table(io_data, colWidths=[3*cm, 7*cm, 6.5*cm])
iot.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1a237e')),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTSIZE', (0,0), (-1,-1), 9),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#9fa8da')),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#e8eaf6')]),
    ('TOPPADDING', (0,0), (-1,-1), 5),
    ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
]))
story.append(iot)
hr()

# Q2 Section 2
story.append(Paragraph("Q2: Write a program to create simple CRUD application using Spring Boot and Hibernate for Online Examination Registration System. (10 Marks)", q_style))
story.append(Paragraph("<b>Answer:</b>", heading_style))
story.append(Paragraph("<b>Assumptions:</b> Spring Boot 3.x, Java 17+, MySQL database, Spring Data JPA with Hibernate, Maven project.", body_style))

story.append(Paragraph("<b>Project Structure:</b>", heading_style))
structure = """
exam-registration/
├── pom.xml
└── src/main/
    ├── java/com/ignou/exam/
    │   ├── ExamRegistrationApplication.java
    │   ├── entity/ExamRegistration.java
    │   ├── repository/ExamRegistrationRepository.java
    │   ├── service/ExamRegistrationService.java
    │   └── controller/ExamRegistrationController.java
    └── resources/
        └── application.properties
"""
story.append(Paragraph(structure.replace('\n','<br/>').replace(' ','&nbsp;'), code_style))

story.append(Paragraph("<b>Step 1: pom.xml — Key Dependencies</b>", heading_style))
pom = """<dependencies>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-data-jpa</artifactId>
    </dependency>
    <dependency>
        <groupId>com.mysql</groupId>
        <artifactId>mysql-connector-j</artifactId>
        <scope>runtime</scope>
    </dependency>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-validation</artifactId>
    </dependency>
</dependencies>"""
story.append(Paragraph(pom.replace('\n','<br/>').replace(' ','&nbsp;').replace('<','&lt;').replace('>','&gt;'), code_style))

story.append(Paragraph("<b>Step 2: application.properties</b>", heading_style))
props = """spring.datasource.url=jdbc:mysql://localhost:3306/examdb
spring.datasource.username=root
spring.datasource.password=password
spring.jpa.hibernate.ddl-auto=update
spring.jpa.show-sql=true
spring.jpa.properties.hibernate.dialect=org.hibernate.dialect.MySQL8Dialect
server.port=8080"""
story.append(Paragraph(props.replace('\n','<br/>').replace(' ','&nbsp;'), code_style))

story.append(Paragraph("<b>Step 3: Entity Class — ExamRegistration.java</b>", heading_style))
entity = """package com.ignou.exam.entity;

import jakarta.persistence.*;
import jakarta.validation.constraints.*;

@Entity
@Table(name = "exam_registrations")
public class ExamRegistration {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long registrationId;

    @NotBlank(message = "Student name is required")
    private String studentName;

    @NotBlank(message = "Email is required")
    @Email(message = "Invalid email format")
    @Column(unique = true)
    private String email;

    @NotBlank(message = "Enrollment number is required")
    @Column(unique = true)
    private String enrollmentNo;

    @NotBlank(message = "Exam name is required")
    private String examName;

    private String examDate;
    private String examCenter;

    @Enumerated(EnumType.STRING)
    private RegistrationStatus status = RegistrationStatus.PENDING;

    public enum RegistrationStatus { PENDING, CONFIRMED, CANCELLED }

    // ---- Getters and Setters ----
    public Long getRegistrationId()          { return registrationId; }
    public void setRegistrationId(Long id)   { this.registrationId = id; }
    public String getStudentName()           { return studentName; }
    public void setStudentName(String n)     { this.studentName = n; }
    public String getEmail()                 { return email; }
    public void setEmail(String e)           { this.email = e; }
    public String getEnrollmentNo()          { return enrollmentNo; }
    public void setEnrollmentNo(String en)   { this.enrollmentNo = en; }
    public String getExamName()              { return examName; }
    public void setExamName(String ex)       { this.examName = ex; }
    public String getExamDate()              { return examDate; }
    public void setExamDate(String d)        { this.examDate = d; }
    public String getExamCenter()            { return examCenter; }
    public void setExamCenter(String c)      { this.examCenter = c; }
    public RegistrationStatus getStatus()    { return status; }
    public void setStatus(RegistrationStatus s) { this.status = s; }
}"""
story.append(Paragraph(entity.replace('\n','<br/>').replace(' ','&nbsp;'), code_style))

story.append(Paragraph("<b>Step 4: Repository Interface</b>", heading_style))
repo = """package com.ignou.exam.repository;

import com.ignou.exam.entity.ExamRegistration;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import java.util.Optional;

@Repository
public interface ExamRegistrationRepository
        extends JpaRepository<ExamRegistration, Long> {

    Optional<ExamRegistration> findByEmail(String email);
    Optional<ExamRegistration> findByEnrollmentNo(String enrollmentNo);
}"""
story.append(Paragraph(repo.replace('\n','<br/>').replace(' ','&nbsp;').replace('<','&lt;').replace('>','&gt;'), code_style))

story.append(Paragraph("<b>Step 5: Service Class</b>", heading_style))
service = """package com.ignou.exam.service;

import com.ignou.exam.entity.ExamRegistration;
import com.ignou.exam.repository.ExamRegistrationRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import java.util.List;

@Service
public class ExamRegistrationService {

    @Autowired
    private ExamRegistrationRepository repository;

    // CREATE
    public ExamRegistration register(ExamRegistration reg) {
        return repository.save(reg);
    }

    // READ ALL
    public List<ExamRegistration> getAllRegistrations() {
        return repository.findAll();
    }

    // READ BY ID
    public ExamRegistration getById(Long id) {
        return repository.findById(id)
               .orElseThrow(() -> new RuntimeException("Registration not found: " + id));
    }

    // UPDATE
    public ExamRegistration update(Long id, ExamRegistration updatedReg) {
        ExamRegistration existing = getById(id);
        existing.setStudentName(updatedReg.getStudentName());
        existing.setEmail(updatedReg.getEmail());
        existing.setExamName(updatedReg.getExamName());
        existing.setExamDate(updatedReg.getExamDate());
        existing.setExamCenter(updatedReg.getExamCenter());
        existing.setStatus(updatedReg.getStatus());
        return repository.save(existing);
    }

    // DELETE
    public String delete(Long id) {
        if (!repository.existsById(id)) {
            throw new RuntimeException("Registration not found: " + id);
        }
        repository.deleteById(id);
        return "Registration " + id + " deleted successfully.";
    }
}"""
story.append(Paragraph(service.replace('\n','<br/>').replace(' ','&nbsp;').replace('<','&lt;').replace('>','&gt;'), code_style))

story.append(Paragraph("<b>Step 6: REST Controller — All CRUD Endpoints</b>", heading_style))
controller = """package com.ignou.exam.controller;

import com.ignou.exam.entity.ExamRegistration;
import com.ignou.exam.service.ExamRegistrationService;
import jakarta.validation.Valid;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import java.util.List;

@RestController
@RequestMapping("/api/exam-registrations")
public class ExamRegistrationController {

    @Autowired
    private ExamRegistrationService service;

    // CREATE — POST /api/exam-registrations
    @PostMapping
    public ResponseEntity<ExamRegistration> create(
            @Valid @RequestBody ExamRegistration reg) {
        return ResponseEntity.ok(service.register(reg));
    }

    // READ ALL — GET /api/exam-registrations
    @GetMapping
    public ResponseEntity<List<ExamRegistration>> getAll() {
        return ResponseEntity.ok(service.getAllRegistrations());
    }

    // READ BY ID — GET /api/exam-registrations/{id}
    @GetMapping("/{id}")
    public ResponseEntity<ExamRegistration> getById(@PathVariable Long id) {
        return ResponseEntity.ok(service.getById(id));
    }

    // UPDATE — PUT /api/exam-registrations/{id}
    @PutMapping("/{id}")
    public ResponseEntity<ExamRegistration> update(
            @PathVariable Long id,
            @Valid @RequestBody ExamRegistration updatedReg) {
        return ResponseEntity.ok(service.update(id, updatedReg));
    }

    // DELETE — DELETE /api/exam-registrations/{id}
    @DeleteMapping("/{id}")
    public ResponseEntity<String> delete(@PathVariable Long id) {
        return ResponseEntity.ok(service.delete(id));
    }
}"""
story.append(Paragraph(controller.replace('\n','<br/>').replace(' ','&nbsp;').replace('<','&lt;').replace('>','&gt;'), code_style))

story.append(Paragraph("<b>Step 7: Main Application Class</b>", heading_style))
main_cls = """package com.ignou.exam;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class ExamRegistrationApplication {
    public static void main(String[] args) {
        SpringApplication.run(ExamRegistrationApplication.class, args);
    }
}"""
story.append(Paragraph(main_cls.replace('\n','<br/>').replace(' ','&nbsp;'), code_style))

story.append(Paragraph("<b>Sample API Calls (with Input/Output):</b>", heading_style))
api_data = [
    ["Operation", "HTTP Method & URL", "Sample Request Body / Response"],
    ["CREATE", "POST /api/exam-registrations", '{ "studentName":"Rahul", "email":"rahul@ignou.ac.in", "enrollmentNo":"MCA2401", "examName":"MCS-218", "examDate":"2025-11-15", "examCenter":"Delhi-01" }'],
    ["READ ALL", "GET /api/exam-registrations", "Returns JSON array of all registrations with their IDs and status"],
    ["READ ONE", "GET /api/exam-registrations/1", "Returns JSON of registration with ID=1"],
    ["UPDATE", "PUT /api/exam-registrations/1", '{ "examCenter":"Mumbai-02", "status":"CONFIRMED" } — Updates center and status'],
    ["DELETE", "DELETE /api/exam-registrations/1", '"Registration 1 deleted successfully."'],
]
apt = Table(api_data, colWidths=[2.5*cm, 5*cm, 9*cm])
apt.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1a237e')),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTNAME', (0,1), (0,-1), 'Helvetica-Bold'),
    ('FONTSIZE', (0,0), (-1,-1), 9),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#9fa8da')),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#e8eaf6')]),
    ('TOPPADDING', (0,0), (-1,-1), 5),
    ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
]))
story.append(apt)
story.append(Spacer(1, 0.3*cm))
story.append(Paragraph(
    "<b>How Hibernate Works Here:</b> The @Entity annotation tells Hibernate to map the ExamRegistration class to the 'exam_registrations' table. With spring.jpa.hibernate.ddl-auto=update, Hibernate automatically creates/updates the table schema. The JpaRepository provides built-in implementations of save() (INSERT/UPDATE), findById() (SELECT), findAll() (SELECT *), and deleteById() (DELETE) — all translated to appropriate SQL by Hibernate.",
    body_style))

doc.build(story)
print("MCSL-222 PDF created successfully.")