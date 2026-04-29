from reportlab.lib.pagesizes import A4 # pyright: ignore[reportMissingModuleSource]
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, Table, TableStyle # pyright: ignore[reportMissingModuleSource]
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle # pyright: ignore[reportMissingModuleSource]
from reportlab.lib.units import cm # type: ignore
from reportlab.lib import colors # pyright: ignore[reportMissingModuleSource]
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY # pyright: ignore[reportMissingModuleSource]

doc = SimpleDocTemplate(
    "MCS-221_Answers.pdf",
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
    ["Course Code", "MCS-221"],
    ["Course Title", "Data Warehousing and Data Mining"],
    ["Assignment No.", "MCA_NEW(II)/221/Assign/2025-26"],
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
story.append(Paragraph("Q1: Critically evaluate top-down and bottom-up approaches to data warehouse design, highlighting scenarios where one may outperform the other. (8 Marks)", q_style))
story.append(Paragraph("<b>Answer:</b>", heading_style))
story.append(Paragraph(
    "Data warehouse design follows two primary architectural approaches, each with distinct philosophies, strengths, and limitations.",
    body_style))

story.append(Paragraph("<b>Top-Down Approach (Bill Inmon's Architecture):</b>", heading_style))
story.append(Paragraph(
    "In the top-down approach, a centralized, enterprise-wide data warehouse (EDW) is built first. It stores integrated, normalized data for the entire organization. Departmental data marts are then derived from this central warehouse.",
    body_style))
for pt in [
    "<b>Advantages:</b> Highly integrated and consistent data across the enterprise; single source of truth; strong data quality and governance; supports complex cross-functional analysis.",
    "<b>Disadvantages:</b> Takes very long to implement (months to years); expensive; requires extensive upfront planning; delayed ROI (Return on Investment).",
    "<b>Best Scenario:</b> Large enterprises (e.g., banks, insurance companies) where cross-departmental data consistency is critical; regulated industries requiring strict governance; organizations willing to invest long-term.",
]:
    story.append(Paragraph(f"• {pt}", bullet_style))

story.append(Paragraph("<b>Bottom-Up Approach (Ralph Kimball's Architecture):</b>", heading_style))
story.append(Paragraph(
    "In the bottom-up approach, the project begins with building individual departmental data marts first (e.g., Sales mart, HR mart). The integrated data warehouse emerges over time as multiple data marts are connected using a 'bus architecture' with conformed dimensions.",
    body_style))
for pt in [
    "<b>Advantages:</b> Faster implementation; quicker ROI; easier to manage in phases; each data mart delivers immediate business value; more flexible to changing requirements.",
    "<b>Disadvantages:</b> Risk of data inconsistency across marts if conformed dimensions are not properly managed; may lead to data silos; harder to enforce enterprise-wide governance.",
    "<b>Best Scenario:</b> Startups or SMEs with limited budgets; departments needing quick analytical capabilities; agile organizations; when business requirements evolve frequently.",
]:
    story.append(Paragraph(f"• {pt}", bullet_style))

story.append(Paragraph("<b>Critical Evaluation:</b>", heading_style))
comp = [
    ["Criterion", "Top-Down (Inmon)", "Bottom-Up (Kimball)"],
    ["Development Time", "Long (months/years)", "Short (weeks/months)"],
    ["Cost", "Very High initially", "Lower, phased investment"],
    ["Data Consistency", "Excellent (normalized EDW)", "Good (if conformed dims used)"],
    ["Flexibility", "Low (rigid architecture)", "High (agile approach)"],
    ["ROI", "Delayed", "Quick"],
    ["Scalability", "High", "Moderate"],
    ["Best For", "Large enterprises, regulated industries", "Agile teams, dept-level needs"],
]
ct = Table(comp, colWidths=[4.5*cm, 6*cm, 6*cm])
ct.setStyle(TableStyle([
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
story.append(ct)
story.append(Spacer(1, 0.2*cm))
story.append(Paragraph("<b>Conclusion:</b> Neither approach is universally superior. Modern enterprises often adopt a hybrid approach — start with bottom-up data marts for quick wins, then progressively build towards an enterprise-wide integrated warehouse following top-down principles.", sub_style))
hr()

# Q2
story.append(Paragraph("Q2: Analyze the role of OLAP operations (Roll-up, Drill-down, Slice, Dice, Pivot) in multidimensional data analysis with a business intelligence scenario. (8 Marks)", q_style))
story.append(Paragraph("<b>Answer:</b>", heading_style))
story.append(Paragraph(
    "OLAP (Online Analytical Processing) operations allow analysts to interactively explore multidimensional data stored in data cubes for business intelligence and decision-making.",
    body_style))
story.append(Paragraph("<b>Business Scenario:</b> A retail chain (like BigBazaar) analyses sales data across dimensions: Time (Day → Month → Quarter → Year), Product (SKU → Category → Department), and Location (Store → City → State → Region).", body_style))

olap_ops = [
    ("1. Roll-Up (Aggregation / Drill-Up)",
     "Moves up the hierarchy by aggregating (summarizing) data. Reduces detail.\n"
     "Example: From monthly sales data, roll up to quarterly sales → then to annual sales. The analyst sees 'Total Sales by Quarter' instead of 'Sales per Day'.\n"
     "Business Value: Helps management see big-picture performance and annual trends without granular details."),
    ("2. Drill-Down (Disaggregation)",
     "The reverse of roll-up — navigates from a higher level of aggregation to more detailed (lower level) data.\n"
     "Example: From Q3 sales figures, drill down to September → drill down further to individual store sales in September.\n"
     "Business Value: When a regional manager notices a sales dip in Q3, they drill down to identify which specific store or week caused the decline."),
    ("3. Slice",
     "Selects a single value for one dimension, creating a 2D sub-cube (a 'slice') from the multidimensional cube.\n"
     "Example: Slice on Time = 'January 2025' — this shows sales data for all products in all locations for only January 2025.\n"
     "Business Value: Helps analysts focus on a specific time period, product, or location for targeted analysis."),
    ("4. Dice",
     "Selects specific values for two or more dimensions, creating a smaller sub-cube.\n"
     "Example: Dice on Time = {Q1, Q2} AND Location = {Mumbai, Pune} AND Product = {Electronics} — this shows electronics sales in Mumbai and Pune for Q1 and Q2.\n"
     "Business Value: Enables targeted multi-dimensional analysis — e.g., comparing performance of a specific product category across selected cities."),
    ("5. Pivot (Rotate)",
     "Rotates the data cube to view it from a different perspective — changes the rows and columns of the data view.\n"
     "Example: An analyst currently views a table showing Products as rows and Time periods as columns. After pivoting, Time becomes rows and Products become columns.\n"
     "Business Value: Provides different perspectives of the same data without changing the data itself, helping analysts spot patterns that may not be visible from the original orientation."),
]
for title, content in olap_ops:
    story.append(Paragraph(f"<b>{title}</b>", heading_style))
    for para in content.split('\n'):
        if para.strip():
            story.append(Paragraph(para.strip(), sub_style))
    story.append(Spacer(1, 0.1*cm))
story.append(Paragraph("<b>Conclusion:</b> These OLAP operations collectively enable analysts to navigate a multidimensional data space dynamically — zooming in and out, filtering, and rotating data — supporting informed, data-driven business decisions at all organizational levels.", body_style))
hr()

# Q3
story.append(Paragraph("Q3: Discuss the impact of data granularity on query performance, storage, and decision-making accuracy in a data warehouse. (8 Marks)", q_style))
story.append(Paragraph("<b>Answer:</b>", heading_style))
story.append(Paragraph(
    "<b>Data granularity</b> refers to the level of detail at which data is stored in a data warehouse. Fine-grained data has more detail (e.g., individual transactions), while coarse-grained data is more summarized (e.g., monthly totals).",
    body_style))

story.append(Paragraph("<b>Impact on Query Performance:</b>", heading_style))
for pt in [
    "<b>Fine-Grained:</b> Queries on detailed data require scanning millions of records, resulting in slower query performance. For example, querying all individual sales transactions for a year may take minutes.",
    "<b>Coarse-Grained:</b> Pre-aggregated, summarized data allows queries to run much faster. A query for 'annual total sales by region' on a summary table finishes in seconds.",
    "<b>Mitigation:</b> Data warehouses typically store both detailed and summarized data, and use indexing, partitioning, and materialized views to optimize query performance across granularity levels.",
]:
    story.append(Paragraph(f"• {pt}", bullet_style))

story.append(Paragraph("<b>Impact on Storage:</b>", heading_style))
for pt in [
    "<b>Fine-Grained:</b> Requires significantly more storage space. For example, a retail chain with 1 million daily transactions over 10 years needs billions of rows.",
    "<b>Coarse-Grained:</b> Highly compressed, much less storage required. Monthly summaries might represent 10 years of data in just thousands of rows.",
    "<b>Trade-off:</b> More detail = more storage cost but more analytical flexibility. Data archiving strategies and tiered storage (hot/cold data) help manage costs.",
]:
    story.append(Paragraph(f"• {pt}", bullet_style))

story.append(Paragraph("<b>Impact on Decision-Making Accuracy:</b>", heading_style))
for pt in [
    "<b>Fine-Grained:</b> Enables highly accurate and detailed analysis. Analysts can identify specific transactions, detect fraud at the individual transaction level, and perform precise customer segmentation.",
    "<b>Coarse-Grained:</b> Suitable for high-level strategic decisions but may hide important patterns. Monthly summaries might miss a sudden mid-month sales spike caused by a marketing campaign.",
    "<b>Business Example — Fine-Grained:</b> A bank storing each individual ATM transaction can detect fraud patterns like multiple small withdrawals from different locations within minutes.",
    "<b>Business Example — Coarse-Grained:</b> A retail company storing only monthly sales totals per region can quickly compare regional performance but cannot investigate which specific products drove a sales increase.",
]:
    story.append(Paragraph(f"• {pt}", bullet_style))

gran_table = [
    ["Aspect", "Fine-Grained (Detailed)", "Coarse-Grained (Summarized)"],
    ["Query Speed", "Slow", "Fast"],
    ["Storage Space", "Large", "Small"],
    ["Decision Accuracy", "High (detailed insights)", "Moderate (big picture)"],
    ["Flexibility", "High (supports any analysis)", "Low (fixed aggregations)"],
    ["Cost", "High", "Low"],
    ["Use Case", "Operational analysis, fraud detection", "Strategic planning, dashboards"],
]
gt = Table(gran_table, colWidths=[4*cm, 6.5*cm, 6*cm])
gt.setStyle(TableStyle([
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
story.append(gt)
story.append(Paragraph("<b>Conclusion:</b> The optimal granularity depends on the business use case. A best practice is to store fine-grained data in the warehouse while maintaining pre-computed aggregates (materialized views) for faster querying.", sub_style))
hr()

# Q4
story.append(Paragraph("Q4: Explain how ETL processes influence data accuracy, consistency, and timeliness. Suggest strategies for handling common ETL challenges. (8 Marks)", q_style))
story.append(Paragraph("<b>Answer:</b>", heading_style))
story.append(Paragraph(
    "<b>ETL (Extract, Transform, Load)</b> is the process of extracting data from multiple source systems, transforming it to meet quality and structural requirements, and loading it into the data warehouse. ETL is the backbone of any data warehouse.",
    body_style))

story.append(Paragraph("<b>Three ETL Phases:</b>", heading_style))
for phase, desc in [
    ("Extract", "Data is pulled from multiple heterogeneous sources — databases, flat files, APIs, CRM systems, ERP systems. Full extraction (all data) or incremental extraction (only changed/new data since last run)."),
    ("Transform", "Raw extracted data is cleaned, standardized, validated, and restructured. Includes: data type conversion, deduplication, handling missing values, business rule application, and aggregation."),
    ("Load", "Transformed data is loaded into the data warehouse tables. Full load (replace all data) or incremental load (append/update changed records)."),
]:
    story.append(Paragraph(f"<b>• {phase}:</b> {desc}", bullet_style))

story.append(Paragraph("<b>Impact on Data Quality Dimensions:</b>", heading_style))
for dim, desc in [
    ("Accuracy", "ETL transformations validate data against business rules, correct errors, and enforce referential integrity. Poor ETL = inaccurate warehouse data leading to wrong business decisions. Example: Converting all currency values to USD using the correct exchange rate at time of transaction."),
    ("Consistency", "ETL standardizes data from different source systems that may use different formats (date formats: DD/MM/YYYY vs YYYY-MM-DD; gender: M/F vs Male/Female). Consistent data enables meaningful cross-system analysis."),
    ("Timeliness", "ETL frequency (real-time, hourly, daily, weekly) determines how current the warehouse data is. Delayed ETL = stale data. Real-time streaming ETL (using Kafka + Spark) provides near-real-time data for operational dashboards."),
]:
    story.append(Paragraph(f"<b>• {dim}:</b> {desc}", bullet_style))

story.append(Paragraph("<b>Common ETL Challenges and Strategies:</b>", heading_style))
challenges = [
    ("Missing Values",
     "Strategy: Define imputation rules. Replace numeric nulls with mean/median; use 'Unknown' or 'N/A' for categorical nulls; flag records with missing critical fields for manual review; reject records missing mandatory fields and log them in an error table."),
    ("Inconsistent Data Formats",
     "Strategy: Create standardization lookup tables (e.g., mapping 'M', 'Male', 'male', '1' all to 'MALE'). Apply regular expressions for format standardization (phone numbers, dates). Use master data management (MDM) systems."),
    ("Duplicate Records",
     "Strategy: Apply deduplication logic — compare on multiple fields (name + email + phone), use fuzzy matching for near-duplicates, assign surrogate keys to uniquely identify records regardless of source system IDs."),
    ("ETL Performance / Large Data Volume",
     "Strategy: Use incremental/delta loads instead of full loads; parallelize ETL pipelines; use bulk loading utilities; apply pushdown optimization (perform transformations in the source database where possible)."),
    ("Schema Changes in Source Systems",
     "Strategy: Implement ETL pipeline monitoring and alerting; use schema evolution patterns; maintain ETL version history; test ETL pipelines in staging environments before production deployment."),
]
for challenge, strategy in challenges:
    story.append(Paragraph(f"<b>• Challenge — {challenge}:</b> {strategy}", bullet_style))
hr()

# Q5
story.append(Paragraph("Q5: Compare star schema, snowflake schema, and fact constellation with respect to query performance, ease of maintenance, and user accessibility. (8 Marks)", q_style))
story.append(Paragraph("<b>Answer:</b>", heading_style))

schemas = [
    ("Star Schema",
     "Structure: One central fact table surrounded by denormalized dimension tables. Each dimension is a single table. Resembles a star shape.\n"
     "Query Performance: Excellent — fewer joins (only between fact and dimension tables); optimized for OLAP queries.\n"
     "Ease of Maintenance: Easier to understand and maintain; data redundancy in dimension tables but simplifies ETL.\n"
     "User Accessibility: Very high — simple structure is easy for business users and BI tools to query.\n"
     "Example: Sales_Fact connected to Product_Dim, Customer_Dim, Time_Dim, Store_Dim."),
    ("Snowflake Schema",
     "Structure: Star schema with normalized dimension tables — dimensions are split into multiple related tables. Reduces data redundancy.\n"
     "Query Performance: Slower than star schema — more joins required due to normalized dimensions; however, saves storage.\n"
     "Ease of Maintenance: More complex — more tables, more complex ETL; but better data integrity with less redundancy.\n"
     "User Accessibility: Lower — complex structure is harder for business users; BI tools can abstract this complexity.\n"
     "Example: Product_Dim is split into Product, Product_Category, and Product_Subcategory tables."),
    ("Fact Constellation (Galaxy Schema)",
     "Structure: Multiple fact tables sharing dimension tables. A collection of star schemas that share common dimensions.\n"
     "Query Performance: Good for individual queries; more complex for cross-fact queries requiring multiple fact tables.\n"
     "Ease of Maintenance: Most complex — managing multiple fact tables and shared dimensions requires careful design.\n"
     "User Accessibility: Low — complex for casual users; suited for advanced analysts and data scientists.\n"
     "Example: Sales_Fact and Returns_Fact both connected to shared Product_Dim, Customer_Dim, and Time_Dim."),
]
for name, content in schemas:
    story.append(Paragraph(f"<b>{name}</b>", heading_style))
    for line in content.split('\n'):
        if line.strip():
            story.append(Paragraph(line.strip(), sub_style))
    story.append(Spacer(1, 0.1*cm))

comp_schema = [
    ["Criteria", "Star Schema", "Snowflake Schema", "Fact Constellation"],
    ["Query Performance", "Best (fewest joins)", "Moderate (more joins)", "Good (per fact table)"],
    ["Storage Efficiency", "Low (redundancy)", "High (normalized)", "Moderate"],
    ["Maintenance", "Easy", "Moderate-Complex", "Complex"],
    ["User Friendliness", "High", "Moderate", "Low"],
    ["ETL Complexity", "Low", "Moderate", "High"],
    ["Best Use Case", "OLAP, Dashboards", "Storage-constrained", "Multi-subject analysis"],
]
cs = Table(comp_schema, colWidths=[3.5*cm, 4.5*cm, 4.5*cm, 4*cm])
cs.setStyle(TableStyle([
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
story.append(cs)
story.append(Paragraph("<b>Recommendation:</b> For most BI applications, the star schema is the preferred choice due to its simplicity and query performance. Snowflake is preferred when storage is a major concern. Fact constellation is used in enterprise data warehouses with multiple business processes.", sub_style))
hr()

# Q6
story.append(Paragraph("Q6: Analyze the significance of data preprocessing — handling missing data, noise removal, and normalization — in improving classification algorithm performance. (8 Marks)", q_style))
story.append(Paragraph("<b>Answer:</b>", heading_style))
story.append(Paragraph(
    "Data preprocessing is a critical first step in the data mining pipeline. Raw real-world data is often incomplete, noisy, and inconsistent. The quality of classification results depends heavily on the quality of input data — 'garbage in, garbage out.'",
    body_style))

pp_steps = [
    ("1. Handling Missing Data",
     "Missing data occurs when values are absent for one or more attributes in a dataset. This can be due to data entry errors, sensor failures, or non-applicable fields.\n\n"
     "Impact on Classification: Many classification algorithms (like SVM, Logistic Regression) cannot handle missing values and either throw errors or produce incorrect classifications. Decision trees may create biased splits.\n\n"
     "Handling Techniques:\n"
     "• Deletion: Remove records with missing values (only if &lt;5% are missing to avoid losing significant data).\n"
     "• Mean/Median Imputation: Replace missing numeric values with the column mean or median. Use mean for symmetric distributions; median for skewed distributions.\n"
     "• Mode Imputation: Replace missing categorical values with the most frequent category.\n"
     "• Predictive Imputation: Use a regression or KNN model to predict and fill missing values based on other attributes.\n"
     "• Flagging: Add a binary indicator column (1=missing, 0=present) to let the model learn from the missingness pattern itself.\n\n"
     "Result: Proper imputation increases the effective dataset size and prevents biased models that would result from systematically excluding records with missing values."),
    ("2. Noise Removal",
     "Noise refers to random error or variance in measured variables. It includes outliers (abnormal values) and incorrect measurements.\n\n"
     "Impact on Classification: Noisy data causes classifiers to fit the noise instead of the true underlying pattern (overfitting), reducing generalization accuracy on new data.\n\n"
     "Noise Handling Techniques:\n"
     "• Binning: Sort data into bins (buckets); smooth bin values by replacing them with bin mean or boundary values.\n"
     "• Regression Smoothing: Fit data to a regression function to smooth out random variation.\n"
     "• Outlier Detection: Use statistical methods (Z-score, IQR method) or clustering to identify and remove/correct outliers. Example: In a dataset of student ages, an age of 150 is a noise outlier.\n"
     "• Cross-validation: Detect mislabeled training instances using ensemble methods.\n\n"
     "Result: Noise removal prevents classifiers from learning incorrect decision boundaries and improves classification accuracy on unseen data."),
    ("3. Normalization / Standardization",
     "Normalization scales features to a consistent range. Different attributes may have vastly different scales (age: 18-80, salary: 20,000-500,000), which biases distance-based and gradient-based algorithms.\n\n"
     "Impact on Classification: Distance-based classifiers (KNN, SVM) and gradient descent-based algorithms (Neural Networks, Logistic Regression) are heavily affected by feature scale. Without normalization, high-magnitude features dominate the model.\n\n"
     "Normalization Techniques:\n"
     "• Min-Max Normalization: Scales values to [0,1]. Formula: x' = (x - min)/(max - min). Use when data does not have extreme outliers.\n"
     "• Z-score Standardization (Zero-mean normalization): Transforms to mean=0, std=1. Formula: x' = (x - mean)/std_dev. Use when data has outliers or is Gaussian distributed.\n"
     "• Decimal Scaling: Divide values by a power of 10 to bring them within [-1, 1].\n\n"
     "Result: After normalization, all features contribute equally to the model, improving convergence speed of gradient descent and fairness of distance calculations."),
]
for title, content in pp_steps:
    story.append(Paragraph(f"<b>{title}</b>", heading_style))
    for para in content.split('\n\n'):
        if para.strip():
            for line in para.split('\n'):
                l = line.strip()
                if l.startswith('•'):
                    story.append(Paragraph(l, bullet_style))
                elif l:
                    story.append(Paragraph(l, sub_style))
    story.append(Spacer(1, 0.1*cm))
story.append(Paragraph("<b>Conclusion:</b> Data preprocessing is not optional — it is the foundation of successful data mining. Well-preprocessed data consistently leads to more accurate, faster-converging, and more generalizable classification models.", body_style))
hr()

# Q7
story.append(Paragraph("Q7: Compare classification and clustering in data mining — objectives, algorithms, and real-world use cases with complementary examples. (8 Marks)", q_style))
story.append(Paragraph("<b>Answer:</b>", heading_style))

comp_data = [
    ["Aspect", "Classification", "Clustering"],
    ["Learning Type", "Supervised (uses labeled data)", "Unsupervised (no labels needed)"],
    ["Objective", "Predict class label of new instance", "Discover natural groups/patterns"],
    ["Training Data", "Requires labeled training dataset", "No labeled data required"],
    ["Output", "Predefined class labels", "Cluster IDs (discovered groups)"],
    ["Evaluation", "Accuracy, Precision, Recall, F1-Score", "Silhouette score, Davies-Bouldin index"],
    ["Algorithms", "Decision Tree, SVM, KNN, Naive Bayes, Neural Networks, Random Forest", "K-Means, DBSCAN, Hierarchical, EM Algorithm"],
    ["Example", "Email: Spam or Not Spam", "Customer segmentation by behaviour"],
]
ct2 = Table(comp_data, colWidths=[4*cm, 7*cm, 5.5*cm])
ct2.setStyle(TableStyle([
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
story.append(ct2)
story.append(Spacer(1, 0.3*cm))

story.append(Paragraph("<b>Complementary Application Example — Healthcare:</b>", heading_style))
for pt in [
    "<b>Step 1 (Clustering):</b> Apply K-Means clustering on patient health records (age, BMI, blood pressure, glucose, cholesterol) to discover distinct patient groups (e.g., 'Healthy Adults', 'At-Risk Middle-Aged', 'High-Risk Elderly').",
    "<b>Step 2 (Classification):</b> Use the cluster-labeled data to train a Decision Tree classifier. Now the classifier can predict which cluster (health risk category) a new incoming patient belongs to, enabling personalized treatment protocols.",
    "<b>Outcome:</b> Clustering discovers meaningful patterns without prior knowledge; classification then operationalizes those patterns for real-time decision support. Both techniques are stronger together.",
]:
    story.append(Paragraph(f"• {pt}", bullet_style))

story.append(Paragraph("<b>Real-World Use Cases:</b>", heading_style))
use_cases = [
    ["Domain", "Classification Use Case", "Clustering Use Case"],
    ["Banking", "Credit risk: Approve/Reject loan application", "Customer segmentation for targeted products"],
    ["E-commerce", "Product recommendation: Buy or Not", "Group customers by purchase behaviour"],
    ["Healthcare", "Diagnose: Diabetic / Non-Diabetic", "Identify patient subgroups for clinical trials"],
    ["Cybersecurity", "Classify: Intrusion / Normal traffic", "Detect unknown attack patterns (anomaly clusters)"],
    ["Retail", "Churn prediction: Will customer leave?", "Store cluster analysis for inventory optimization"],
]
ut = Table(use_cases, colWidths=[3*cm, 6.5*cm, 7*cm])
ut.setStyle(TableStyle([
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
story.append(ut)
hr()

# Q8
story.append(Paragraph("Q8: Evaluate the importance of frequent pattern mining in retail. How do Apriori and FP-Growth help in mining association rules, and what are the trade-offs? (8 Marks)", q_style))
story.append(Paragraph("<b>Answer:</b>", heading_style))
story.append(Paragraph(
    "Frequent Pattern Mining discovers items, subsequences, or substructures that appear frequently in a dataset. In the retail industry, this translates to discovering which products are frequently purchased together — the basis of <b>Market Basket Analysis</b>.",
    body_style))
story.append(Paragraph("<b>Importance in Retail:</b>", heading_style))
for pt in [
    "Cross-selling and upselling strategies: 'Customers who bought X also bought Y.'",
    "Store layout optimization: Place frequently co-purchased items (diapers and beer, chips and salsa) near each other.",
    "Inventory management: Stock items that are often bought together in sufficient quantities.",
    "Targeted promotions: Bundle frequently associated items as combo offers.",
    "Online recommendation engines: Amazon's 'Frequently Bought Together' feature.",
]:
    story.append(Paragraph(f"• {pt}", bullet_style))

story.append(Paragraph("<b>Key Concepts — Association Rule Mining:</b>", heading_style))
for concept, desc in [
    ("Support", "Fraction of transactions containing the itemset. Support({Bread, Butter}) = Transactions with both / Total transactions. Indicates how frequently the itemset appears."),
    ("Confidence", "Given A is purchased, probability that B is also purchased. Confidence(A→B) = Support(A∪B) / Support(A). Measures rule strength."),
    ("Lift", "Lift(A→B) = Confidence(A→B) / Support(B). Lift &gt; 1 indicates a positive association. Lift = 1 means no relationship."),
]:
    story.append(Paragraph(f"<b>• {concept}:</b> {desc}", bullet_style))

story.append(Paragraph("<b>Apriori Algorithm:</b>", heading_style))
story.append(Paragraph(
    "Apriori uses a level-wise (breadth-first) candidate-generate-and-test approach. It uses the Apriori property: any subset of a frequent itemset must also be frequent (anti-monotonicity). This allows pruning of candidate itemsets that cannot be frequent.",
    sub_style))
for step in [
    "Step 1: Scan database to find all frequent 1-itemsets (items meeting minimum support threshold).",
    "Step 2: Generate candidate 2-itemsets by joining frequent 1-itemsets; scan database to check their support.",
    "Step 3: Repeat — generate k-itemsets from (k-1)-itemsets and prune using Apriori property until no more frequent itemsets found.",
    "Step 4: Generate association rules from frequent itemsets meeting minimum confidence.",
]:
    story.append(Paragraph(f"  {step}", bullet_style))
story.append(Paragraph("<b>Drawback:</b> Multiple database scans (one per level) and large number of candidate itemsets make it slow and memory-intensive for large datasets.", sub_style))

story.append(Paragraph("<b>FP-Growth Algorithm:</b>", heading_style))
story.append(Paragraph(
    "FP-Growth (Frequent Pattern Growth) avoids the costly candidate generation of Apriori. It compresses the database into a compact FP-Tree (Frequent Pattern Tree) data structure using only two database scans.",
    sub_style))
for step in [
    "Step 1: Scan database once to find frequent 1-itemsets and their counts; sort by frequency.",
    "Step 2: Scan database again to build FP-Tree by inserting transactions as paths (shared prefixes are merged).",
    "Step 3: Mine the FP-Tree using divide-and-conquer — for each frequent item, extract conditional pattern base and build a conditional FP-tree; recursively mine.",
]:
    story.append(Paragraph(f"  {step}", bullet_style))
story.append(Paragraph("<b>Advantage:</b> Only 2 database scans; no candidate generation; much faster than Apriori for large datasets.", sub_style))

story.append(Paragraph("<b>Trade-offs Between Apriori and FP-Growth:</b>", heading_style))
tradeoff_data = [
    ["Feature", "Apriori", "FP-Growth"],
    ["Database Scans", "Multiple (k scans for k-itemsets)", "Only 2 scans"],
    ["Candidate Generation", "Yes (costly)", "No"],
    ["Memory Usage", "Lower (no tree structure)", "Higher (FP-Tree can be large)"],
    ["Speed", "Slow on large datasets", "Much faster (5-10x)"],
    ["Scalability", "Poor for large/dense datasets", "Better scalability"],
    ["Implementation", "Simple and easy to understand", "More complex to implement"],
    ["Best For", "Small datasets, educational purposes", "Large-scale retail/enterprise datasets"],
]
tt = Table(tradeoff_data, colWidths=[4*cm, 6.5*cm, 6*cm])
tt.setStyle(TableStyle([
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
story.append(tt)
hr()

# Q9
story.append(Paragraph("Q9: Discuss ethical implications and privacy concerns in deploying data mining on consumer data. Propose methods for responsible data mining. (8 Marks)", q_style))
story.append(Paragraph("<b>Answer:</b>", heading_style))
story.append(Paragraph("<b>Ethical Implications and Privacy Concerns:</b>", heading_style))
for pt in [
    "<b>Informed Consent:</b> Consumers often do not realize the extent to which their data is collected and analyzed. Many 'accept' lengthy terms and conditions without understanding how their data will be mined.",
    "<b>Data Privacy Violations:</b> Mining health records, financial data, or location data without consent is a serious privacy breach. Example: Cambridge Analytica used Facebook user data without explicit consent for political targeting.",
    "<b>Discrimination and Bias:</b> Data mining models trained on biased historical data perpetuate discrimination. Example: Credit scoring algorithms may unfairly penalize applicants from lower-income zip codes, disproportionately affecting minority communities.",
    "<b>Profiling and Manipulation:</b> Detailed consumer profiles built through data mining enable micro-targeted advertising that can manipulate consumer decisions and exploit psychological vulnerabilities.",
    "<b>Data Security Risks:</b> Large consumer datasets stored for mining are attractive targets for hackers. Breaches expose sensitive personal information.",
    "<b>Lack of Transparency (Black Box Models):</b> Complex models (deep neural networks) make decisions that consumers cannot understand or challenge — the right to explanation.",
    "<b>Function Creep:</b> Data collected for one purpose is used for another without consent. Example: Location data collected for navigation apps used to track customer movements for retail analytics.",
    "<b>Re-identification Risk:</b> Even anonymized datasets can often be re-identified by combining with other publicly available data sources.",
]:
    story.append(Paragraph(f"• {pt}", bullet_style))

story.append(Paragraph("<b>Methods for Responsible Data Mining:</b>", heading_style))
for pt in [
    "<b>Privacy by Design:</b> Integrate privacy protections into the data mining system from the ground up — minimize data collection, use anonymization and encryption by default.",
    "<b>Data Anonymization and Pseudonymization:</b> Remove or replace personally identifiable information (PII) before analysis. Use k-anonymity, l-diversity, or t-closeness techniques.",
    "<b>Differential Privacy:</b> Add mathematical noise to query results so individual records cannot be identified while overall statistical patterns remain valid. Used by Apple and Google for collecting usage statistics.",
    "<b>Federated Learning:</b> Train models locally on users' devices without sending raw data to central servers. Only model updates (not personal data) are shared. Preserves privacy while enabling learning.",
    "<b>Transparent and Explainable AI (XAI):</b> Use interpretable models (decision trees, logistic regression) or provide explanations for complex models. Enable users to understand why a decision was made.",
    "<b>Explicit and Granular Consent:</b> Obtain specific consent for each type of data usage. Allow users to opt out of analytics while continuing to use the service.",
    "<b>Regulatory Compliance:</b> Adhere to privacy laws — GDPR (EU), CCPA (California), PDPA (India's Personal Data Protection Bill) — which mandate data minimization, purpose limitation, and right to erasure.",
    "<b>Ethics Review Boards:</b> Establish internal data ethics committees to review data mining projects for potential harms before deployment.",
    "<b>Regular Bias Audits:</b> Audit models for discriminatory patterns; use fairness metrics (demographic parity, equal opportunity) to detect and correct bias.",
]:
    story.append(Paragraph(f"• {pt}", bullet_style))
story.append(Paragraph("<b>Conclusion:</b> Responsible data mining requires a balance between extracting valuable insights and protecting individual privacy and dignity. Organizations must adopt ethical frameworks, comply with regulations, and design systems that respect user rights.", body_style))
hr()

# Q10
story.append(Paragraph("Q10: Web and text mining — discuss challenges unique to unstructured data and techniques for extracting insights from web logs and textual documents. (8 Marks)", q_style))
story.append(Paragraph("<b>Answer:</b>", heading_style))
story.append(Paragraph(
    "Web and text mining extend traditional data mining to handle <b>unstructured and semi-structured data</b> — web pages, social media posts, blog articles, emails, web server logs — which constitute over 80% of all data generated today.",
    body_style))

story.append(Paragraph("<b>Unique Challenges of Unstructured Data:</b>", heading_style))
for pt in [
    "<b>No Fixed Schema:</b> Unlike relational databases, unstructured text has no predefined structure. A text analysis system must discover structure from raw content.",
    "<b>High Dimensionality:</b> A text corpus with thousands of unique words creates an extremely high-dimensional feature space (one dimension per word), leading to the 'curse of dimensionality.'",
    "<b>Ambiguity and Context-Dependency:</b> The same word can have different meanings in different contexts (polysemy). Example: 'bank' means financial institution or river bank. Natural language is inherently ambiguous.",
    "<b>Noise in Web Data:</b> Web pages contain HTML tags, advertisements, navigation menus, and boilerplate content that must be filtered out before meaningful content can be analyzed.",
    "<b>Language Variations:</b> Slang, abbreviations, misspellings, multilingual content, and evolving terminology make text processing difficult. Social media text ('gr8', 'lol', '@mentions') requires special handling.",
    "<b>Dynamic and Evolving Content:</b> Web content changes constantly — links break, pages are updated, new content appears daily. Web crawlers must continuously re-index the web.",
    "<b>Volume and Velocity:</b> The sheer volume of web data (billions of web pages) and the speed at which it is generated challenges both storage and processing systems.",
    "<b>Link Structure Complexity:</b> Web pages are interconnected through hyperlinks, forming a complex graph that must be analyzed for link analysis (PageRank, HITS algorithm).",
]:
    story.append(Paragraph(f"• {pt}", bullet_style))

story.append(Paragraph("<b>Techniques for Web Log Mining:</b>", heading_style))
story.append(Paragraph(
    "Web logs record every HTTP request to a web server — IP address, timestamp, URL requested, HTTP status code, bytes transferred, user agent.",
    sub_style))
for pt in [
    "<b>Data Cleaning:</b> Remove entries for images, CSS, JS files; filter out search engine crawlers; handle missing or corrupted log entries.",
    "<b>Session Identification:</b> Group log entries belonging to the same user visit using IP address + user agent + time-based heuristics.",
    "<b>Path Analysis:</b> Discover common navigation paths through the website to understand user behaviour and optimize site structure.",
    "<b>Clickstream Analysis:</b> Analyze the sequence of pages visited to identify where users drop off in conversion funnels.",
    "<b>Association Rule Mining:</b> Discover which pages are frequently visited together in the same session.",
    "<b>Clustering:</b> Group users with similar browsing patterns for personalization.",
]:
    story.append(Paragraph(f"• {pt}", bullet_style))

story.append(Paragraph("<b>Techniques for Text Mining:</b>", heading_style))
for pt in [
    "<b>Tokenization:</b> Split text into individual words (tokens). Handle punctuation, contractions, and special characters.",
    "<b>Stop Word Removal:</b> Remove common words ('the', 'is', 'at', 'on') that carry little semantic meaning but add noise.",
    "<b>Stemming and Lemmatization:</b> Reduce words to their root form (running → run, better → good). Stemming is faster; lemmatization is more accurate.",
    "<b>TF-IDF (Term Frequency-Inverse Document Frequency):</b> Weights terms by how often they appear in a document relative to how common they are across all documents. Identifies distinctive terms.",
    "<b>Named Entity Recognition (NER):</b> Identifies and classifies named entities — persons, organizations, locations, dates — in text.",
    "<b>Sentiment Analysis:</b> Classifies text as positive, negative, or neutral. Used for social media monitoring, product review analysis, customer feedback.",
    "<b>Topic Modeling (LDA — Latent Dirichlet Allocation):</b> Discovers hidden thematic topics in a large collection of documents without predefined categories.",
    "<b>Word Embeddings (Word2Vec, BERT, GPT):</b> Represent words as dense vectors that capture semantic relationships. 'King' - 'Man' + 'Woman' ≈ 'Queen'. Modern NLP uses transformer-based models (BERT, GPT) for state-of-the-art text understanding.",
    "<b>Text Classification:</b> Categorize documents into predefined categories — spam detection, news categorization, sentiment classification — using Naive Bayes, SVM, or deep learning.",
]:
    story.append(Paragraph(f"• {pt}", bullet_style))
story.append(Paragraph("<b>Conclusion:</b> Web and text mining unlock enormous value from unstructured data. Key to success is robust preprocessing to handle the inherent noise, ambiguity, and heterogeneity of web and text data, followed by appropriate mining techniques tailored to the specific analytical goal.", body_style))

doc.build(story)
print("MCS-221 PDF created successfully.")