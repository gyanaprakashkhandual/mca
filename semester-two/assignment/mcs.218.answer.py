from reportlab.lib.pagesizes import A4 # pyright: ignore[reportMissingModuleSource]
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, Table, TableStyle # pyright: ignore[reportMissingModuleSource]
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle # pyright: ignore[reportMissingModuleSource]
from reportlab.lib.units import cm # pyright: ignore[reportMissingModuleSource]
from reportlab.lib import colors # pyright: ignore[reportMissingModuleSource]
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY # pyright: ignore[reportMissingModuleSource]

doc = SimpleDocTemplate(
    "MCS-218_Answers.pdf",
    pagesize=A4,
    rightMargin=2*cm, leftMargin=2*cm,
    topMargin=2*cm, bottomMargin=2*cm
)

styles = getSampleStyleSheet()

# Custom styles
title_style = ParagraphStyle('Title', parent=styles['Title'], fontSize=16, textColor=colors.HexColor('#1a237e'), spaceAfter=6, alignment=TA_CENTER)
subtitle_style = ParagraphStyle('Subtitle', parent=styles['Normal'], fontSize=11, textColor=colors.HexColor('#1a237e'), spaceAfter=4, alignment=TA_CENTER)
info_style = ParagraphStyle('Info', parent=styles['Normal'], fontSize=10, spaceAfter=3, alignment=TA_CENTER)
q_style = ParagraphStyle('Question', parent=styles['Normal'], fontSize=11, textColor=colors.HexColor('#b71c1c'), spaceBefore=16, spaceAfter=6, fontName='Helvetica-Bold')
body_style = ParagraphStyle('Body', parent=styles['Normal'], fontSize=10.5, spaceAfter=6, leading=16, alignment=TA_JUSTIFY)
sub_style = ParagraphStyle('Sub', parent=styles['Normal'], fontSize=10.5, spaceAfter=4, leading=15, leftIndent=20, alignment=TA_JUSTIFY)
bullet_style = ParagraphStyle('Bullet', parent=styles['Normal'], fontSize=10.5, spaceAfter=3, leading=15, leftIndent=30, bulletIndent=15)
heading_style = ParagraphStyle('Heading', parent=styles['Normal'], fontSize=11, fontName='Helvetica-Bold', spaceAfter=5, spaceBefore=8, textColor=colors.HexColor('#0d47a1'))

story = []

# Header
story.append(Paragraph("INDIRA GANDHI NATIONAL OPEN UNIVERSITY", title_style))
story.append(Paragraph("School of Computer and Information Sciences", subtitle_style))
story.append(Paragraph("Master of Computer Applications (MCA New) — Semester II", info_style))
story.append(HRFlowable(width="100%", thickness=2, color=colors.HexColor('#1a237e'), spaceAfter=8))

# Course details table
details = [
    ["Course Code", "MCS-218"],
    ["Course Title", "Data Communication and Computer Networks"],
    ["Assignment No.", "MCA_NEW(II)/218/Assign/2025-26"],
    ["Maximum Marks", "100 (80 Written + 20 Viva Voce)"],
    ["Weightage", "30%"],
    ["Session", "July 2025 & January 2026"],
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

# ============================================================
# Q1
# ============================================================
story.append(Paragraph("Q1: Explain TCP/IP model with layer functionality. Are there any alternative models to TCP/IP? If yes, explain them. (30 Marks)", q_style))

story.append(Paragraph("<b>Answer:</b>", heading_style))
story.append(Paragraph("<b>TCP/IP Model</b>", heading_style))
story.append(Paragraph(
    "The TCP/IP (Transmission Control Protocol / Internet Protocol) model is a concise, practical framework that describes how data is transmitted across the internet and other networks. It was developed by the U.S. Department of Defense (DARPA) and forms the backbone of modern internet communication. The model consists of <b>four layers</b>, each with a specific role:",
    body_style))

layers = [
    ("1. Application Layer (Layer 4)",
     "This is the topmost layer and the one closest to the end user. It defines the protocols that applications use to communicate over the network. It handles high-level protocols, data representation, encoding, and session control.\n\n"
     "Key Protocols: HTTP/HTTPS (web browsing), FTP (file transfer), SMTP/IMAP/POP3 (email), DNS (domain name resolution), DHCP (IP address assignment), Telnet, SSH.\n\n"
     "Functionality: Provides network services directly to user applications, manages data formatting and encryption (e.g., SSL/TLS), and handles user authentication."),
    ("2. Transport Layer (Layer 3)",
     "This layer is responsible for end-to-end communication between the source and destination hosts. It provides reliable or unreliable delivery and error checking.\n\n"
     "Key Protocols: TCP (Transmission Control Protocol) — provides reliable, connection-oriented communication with error detection, flow control, and retransmission of lost packets. UDP (User Datagram Protocol) — provides fast, connectionless, unreliable communication suitable for real-time applications like video streaming, DNS queries.\n\n"
     "Functionality: Segmentation and reassembly of data, port addressing, flow control (sliding window), congestion control, error correction (TCP)."),
    ("3. Internet Layer (Layer 2)",
     "This layer is responsible for logical addressing, routing, and packet forwarding across multiple networks (internetworking).\n\n"
     "Key Protocols: IP (IPv4, IPv6) — provides logical addressing and packet delivery. ICMP — sends error messages and operational information. ARP — maps IP addresses to MAC addresses. OSPF, BGP, RIP — routing protocols.\n\n"
     "Functionality: Assigns IP addresses, determines the best path for data (routing), fragments and reassembles packets across different network types."),
    ("4. Network Access Layer (Layer 1) — also called Link Layer",
     "This is the lowest layer and combines the functions of both the Physical and Data Link layers of the OSI model. It deals with the physical transmission of data over the network medium.\n\n"
     "Key Protocols/Standards: Ethernet, Wi-Fi (IEEE 802.11), PPP, Token Ring, Frame Relay.\n\n"
     "Functionality: Handles physical addressing (MAC addresses), error detection at the frame level, and the actual transmission of bits over the physical medium (copper wire, fiber, wireless).")
]

for title, content in layers:
    story.append(Paragraph(f"<b>{title}</b>", heading_style))
    for para in content.split('\n\n'):
        story.append(Paragraph(para.strip(), sub_style))
    story.append(Spacer(1, 0.2*cm))

story.append(Paragraph("<b>Alternative Models to TCP/IP</b>", heading_style))
story.append(Paragraph("Yes, there are alternative models to TCP/IP. The most important one is the OSI model, but there are others as well:", body_style))

alts = [
    ("1. OSI Model (Open Systems Interconnection)",
     "Developed by ISO (International Organization for Standardization) in 1984, the OSI model is a conceptual 7-layer framework used for understanding and designing network systems.\n\n"
     "The seven layers are: (1) Physical — transmission of raw bits over a physical medium; (2) Data Link — node-to-node data transfer, error detection/correction using MAC addresses; (3) Network — logical addressing and routing (IP); (4) Transport — end-to-end communication, reliability (TCP/UDP); (5) Session — manages sessions between applications; (6) Presentation — data translation, encryption, compression; (7) Application — user-facing protocols like HTTP, FTP.\n\n"
     "Comparison with TCP/IP: OSI is a theoretical/reference model with 7 layers; TCP/IP is a practical/implementation model with 4 layers. OSI separates Session and Presentation layers, while TCP/IP combines them into the Application layer. OSI model is used for teaching/troubleshooting; TCP/IP is used in real-world networking."),
    ("2. IEEE 802 Reference Model",
     "Developed by the Institute of Electrical and Electronics Engineers (IEEE), this model focuses on the lower layers of networking, particularly for LANs. It subdivides the OSI Data Link layer into: Logical Link Control (LLC) sub-layer — manages frame synchronization, flow control, error checking; and Media Access Control (MAC) sub-layer — controls how devices in the network access data and permission to transmit. It is relevant for Ethernet, Wi-Fi, Bluetooth standards."),
    ("3. AppleTalk Protocol Suite",
     "Developed by Apple Inc. in the 1980s for networking Apple computers. It was a proprietary network protocol stack with its own addressing and routing mechanisms. It has been largely discontinued in favor of TCP/IP."),
    ("4. IPX/SPX (Internetwork Packet Exchange/Sequenced Packet Exchange)",
     "A networking protocol suite developed by Novell, used primarily in Novell NetWare systems during the 1980s and 1990s. IPX performs functions similar to IP (addressing, routing), and SPX provides functions similar to TCP (reliable delivery). Largely replaced by TCP/IP in modern networks."),
]
for title, content in alts:
    story.append(Paragraph(f"<b>{title}</b>", heading_style))
    for para in content.split('\n\n'):
        story.append(Paragraph(para.strip(), sub_style))
    story.append(Spacer(1, 0.15*cm))

story.append(Paragraph(
    "<b>Conclusion:</b> While the TCP/IP model is the universal standard for internet communication today, the OSI model remains the most widely used reference framework for teaching and network troubleshooting. Other models like IEEE 802, IPX/SPX, and AppleTalk were historically significant but have largely been superseded by TCP/IP.",
    body_style))

story.append(HRFlowable(width="100%", thickness=0.5, color=colors.grey, spaceBefore=10, spaceAfter=10))

# ============================================================
# Q2
# ============================================================
story.append(Paragraph("Q2: How does Slotted ALOHA improve the performance of the system over Pure ALOHA? (30 Marks)", q_style))
story.append(Paragraph("<b>Answer:</b>", heading_style))

story.append(Paragraph("<b>Introduction to ALOHA Protocols</b>", heading_style))
story.append(Paragraph(
    "ALOHA is a random access protocol developed at the University of Hawaii in the 1970s for wireless packet data networks. It allows multiple stations to share a single communication channel without requiring central coordination. There are two variants: Pure ALOHA and Slotted ALOHA.",
    body_style))

story.append(Paragraph("<b>Pure ALOHA</b>", heading_style))
story.append(Paragraph(
    "In Pure ALOHA, any station can transmit data at any time without checking the channel state. If two or more stations transmit simultaneously, a collision occurs and all frames are corrupted. After a collision, each station waits a random amount of time before retransmitting.",
    body_style))
story.append(Paragraph("Key characteristics:", body_style))
for pt in [
    "Stations transmit frames whenever they have data to send.",
    "No synchronization between stations.",
    "After collision: stations back off for a random time (exponential backoff) and retransmit.",
    "A frame is considered destroyed if any part of it overlaps with another frame's transmission.",
    "Vulnerable period = 2 × frame transmission time (2T). During this entire window, any other transmission causes a collision.",
    "Maximum throughput (efficiency) = 1/(2e) ≈ 18.4% of channel capacity.",
]:
    story.append(Paragraph(f"• {pt}", bullet_style))

story.append(Paragraph(
    "Mathematical Analysis: If G = average number of frames generated per frame time, then the throughput S = G × e^(−2G). The maximum is achieved at G = 0.5, giving S_max = 0.5 × e^(−1) ≈ 0.184 (18.4%).",
    sub_style))

story.append(Paragraph("<b>Slotted ALOHA</b>", heading_style))
story.append(Paragraph(
    "Slotted ALOHA was proposed by Roberts (1972) as an improvement over Pure ALOHA. The key idea is to divide time into discrete slots of equal length (equal to one frame transmission time). Stations are synchronized and can only begin transmission at the start of a time slot. They cannot transmit in the middle of a slot.",
    body_style))
story.append(Paragraph("Key characteristics:", body_style))
for pt in [
    "Time is divided into slots of size T (equal to frame transmission time).",
    "Stations can only begin transmitting at the start of a slot.",
    "All stations are synchronized (e.g., via a clock signal or beacon).",
    "A collision occurs only if two or more stations start transmitting in the same slot.",
    "Vulnerable period = T (only one frame time, not two like Pure ALOHA).",
    "Maximum throughput = 1/e ≈ 36.8% of channel capacity.",
]:
    story.append(Paragraph(f"• {pt}", bullet_style))

story.append(Paragraph(
    "Mathematical Analysis: Throughput S = G × e^(−G). Maximum is achieved at G = 1, giving S_max = e^(−1) ≈ 0.368 (36.8%).",
    sub_style))

story.append(Paragraph("<b>How Slotted ALOHA Improves Performance</b>", heading_style))

improvements = [
    ("1. Reduced Vulnerable Period",
     "In Pure ALOHA, if station A transmits at time t, a collision can occur if any other station transmits between (t−T) and (t+T) — a window of 2T. In Slotted ALOHA, since all transmissions must start at slot boundaries, collision can only occur if another station starts in the exact same slot — a window of only T. This halves the vulnerable period, directly cutting the collision probability."),
    ("2. Doubled Channel Efficiency",
     "By halving the vulnerable period, Slotted ALOHA achieves maximum channel efficiency of approximately 36.8% compared to 18.4% for Pure ALOHA. This means Slotted ALOHA can carry roughly twice as much useful traffic on the same channel."),
    ("3. Less Wasted Bandwidth from Collisions",
     "In Pure ALOHA, partial overlaps (frame partially colliding with another) waste the entire slot. In Slotted ALOHA, since all frames are aligned to slot boundaries, only complete slot-level collisions occur, making the collision outcome more predictable and easier to handle."),
    ("4. Better Performance Under High Load",
     "Under heavy traffic (high G), Slotted ALOHA degrades more gracefully than Pure ALOHA, sustaining higher useful throughput before the channel becomes saturated."),
]
for title, content in improvements:
    story.append(Paragraph(f"<b>{title}</b>", heading_style))
    story.append(Paragraph(content, sub_style))

story.append(Paragraph("<b>Comparison Table: Pure ALOHA vs Slotted ALOHA</b>", heading_style))
comp_data = [
    ["Feature", "Pure ALOHA", "Slotted ALOHA"],
    ["Transmission Time", "Any time", "Start of slot only"],
    ["Synchronization", "Not required", "Required"],
    ["Vulnerable Period", "2T", "T"],
    ["Max Throughput", "18.4% (1/2e)", "36.8% (1/e)"],
    ["Optimal Load (G)", "0.5", "1.0"],
    ["Collision Type", "Full or partial frame", "Full slot only"],
    ["Complexity", "Simple", "Moderate (needs clock sync)"],
]
ct = Table(comp_data, colWidths=[4.5*cm, 6*cm, 6*cm])
ct.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1a237e')),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTNAME', (0,1), (0,-1), 'Helvetica-Bold'),
    ('FONTSIZE', (0,0), (-1,-1), 9.5),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#9fa8da')),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#e8eaf6')]),
    ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('TOPPADDING', (0,0), (-1,-1), 5),
    ('BOTTOMPADDING', (0,0), (-1,-1), 5),
]))
story.append(ct)
story.append(Spacer(1, 0.3*cm))

story.append(Paragraph(
    "<b>Conclusion:</b> Slotted ALOHA significantly improves over Pure ALOHA by introducing time synchronization and restricting transmissions to slot boundaries. This simple modification halves the vulnerable period, doubles the maximum channel throughput from 18.4% to 36.8%, and reduces wasted bandwidth from partial collisions. The trade-off is the need for clock synchronization among all stations. Slotted ALOHA forms the basis for more advanced protocols like CSMA/CD used in Ethernet.",
    body_style))

story.append(HRFlowable(width="100%", thickness=0.5, color=colors.grey, spaceBefore=10, spaceAfter=10))

# ============================================================
# Q3
# ============================================================
story.append(Paragraph("Q3: What are various mechanisms for congestion control? (20 Marks)", q_style))
story.append(Paragraph("<b>Answer:</b>", heading_style))

story.append(Paragraph("<b>Introduction to Congestion Control</b>", heading_style))
story.append(Paragraph(
    "Congestion in a network occurs when the demand for network resources (bandwidth, buffer space, processing capacity) exceeds the available supply. This results in packet loss, increased delays, and reduced throughput. Congestion control refers to the mechanisms and techniques used to prevent or alleviate congestion, ensuring fair and efficient use of network resources.",
    body_style))

story.append(Paragraph("<b>Congestion Control Mechanisms</b>", heading_style))

mechanisms = [
    ("1. Open-Loop Congestion Control (Prevention)",
     "Open-loop control tries to prevent congestion before it occurs through good design policies. It operates without feedback from the network.\n\n"
     "a) Traffic Shaping: Regulates the rate at which data is injected into the network.\n"
     "   — Leaky Bucket Algorithm: Converts bursty traffic into a steady stream at a fixed rate. Even if packets arrive unevenly, they leave at a constant rate (drip by drip), like water dripping from a leaky bucket.\n"
     "   — Token Bucket Algorithm: Allows controlled bursts. Tokens are added to a bucket at a fixed rate; a packet can only be sent if a token is available. Allows some burstiness up to the bucket size.\n\n"
     "b) Admission Control: Before a new connection is established, the network checks if there are sufficient resources. If not, the connection is rejected to protect existing flows.\n\n"
     "c) Resource Reservation (RSVP): Applications reserve bandwidth, buffer space, and CPU in advance along the path from source to destination."),

    ("2. Closed-Loop Congestion Control (Reaction)",
     "Closed-loop control responds to congestion after it has occurred, using feedback from the network.\n\n"
     "a) Backpressure: A congested node slows down the flow of packets from upstream nodes. The signal propagates backwards hop-by-hop until it reaches the source.\n\n"
     "b) Choke Packets: When a router detects congestion, it sends a special 'choke packet' (warning) back to the source, asking it to reduce its transmission rate. The source reduces traffic, often by half, and slowly increases it again if choke packets stop.\n\n"
     "c) Implicit Signalling: The source infers congestion from observable metrics — increased round-trip time (RTT) or packet loss — without explicit notification from the network.\n\n"
     "d) Explicit Congestion Notification (ECN): Routers mark packets (instead of dropping them) when they detect congestion. The receiver informs the sender via TCP headers, and the sender reduces its rate. Less wasteful than packet-drop-based signalling."),

    ("3. TCP Congestion Control Mechanisms",
     "TCP implements its own end-to-end congestion control through four algorithms:\n\n"
     "a) Slow Start: TCP begins with a small congestion window (cwnd = 1 segment) and doubles it with each acknowledgment (exponential growth) until a threshold (ssthresh) is reached.\n\n"
     "b) Congestion Avoidance: Once cwnd exceeds ssthresh, the growth switches to linear (additive increase) — cwnd grows by 1 MSS per RTT. This is the AIMD (Additive Increase, Multiplicative Decrease) principle.\n\n"
     "c) Fast Retransmit: If the sender receives 3 duplicate ACKs (indicating a single packet was lost, not congestion collapse), it retransmits the missing segment immediately without waiting for a timeout.\n\n"
     "d) Fast Recovery: After fast retransmit, TCP enters fast recovery — it sets ssthresh to half of cwnd, then resumes congestion avoidance (linear increase) rather than restarting slow start from scratch."),

    ("4. Quality of Service (QoS) Based Control",
     "Networks can prioritize traffic using QoS mechanisms to prevent congestion from affecting critical traffic:\n\n"
     "— Weighted Fair Queuing (WFQ): Assigns weights to different traffic classes; higher-priority classes get more bandwidth.\n"
     "— Priority Queuing: High-priority packets are always served before low-priority ones.\n"
     "— Differentiated Services (DiffServ): Packets are marked with service codes (DSCP); routers treat marked packets differently based on predefined policies."),

    ("5. Random Early Detection (RED)",
     "RED is an active queue management (AQM) technique where routers probabilistically drop (or mark) packets before the queue is full, based on average queue size. If the queue is below a minimum threshold: no drops. If between min and max threshold: drop packets with increasing probability. If above max threshold: drop all packets. This prevents synchronization of TCP flows and avoids tail-drop problems."),
]

for title, content in mechanisms:
    story.append(Paragraph(f"<b>{title}</b>", heading_style))
    for para in content.split('\n\n'):
        story.append(Paragraph(para.strip(), sub_style))
    story.append(Spacer(1, 0.15*cm))

story.append(Paragraph(
    "<b>Conclusion:</b> Congestion control is a critical aspect of network management. Open-loop methods like traffic shaping and admission control prevent congestion proactively, while closed-loop methods like backpressure, ECN, and TCP's AIMD mechanism react to congestion dynamically. Modern networks combine multiple mechanisms to achieve efficient, fair, and responsive congestion management.",
    body_style))

# Build
doc.build(story)
print("MCS-218 PDF created successfully.")