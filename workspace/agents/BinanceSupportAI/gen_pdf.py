from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, KeepTogether
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
import os

OUTPUT = "binance_futures_guide.pdf"

GOLD = colors.HexColor("#F0B90B")
DARK = colors.HexColor("#1e2329")
BG = colors.HexColor("#0b0e11")
GREEN = colors.HexColor("#0ecb81")
RED = colors.HexColor("#f6465d")
GREY = colors.HexColor("#b7bdc6")
WHITE = colors.white

doc = SimpleDocTemplate(
    OUTPUT, pagesize=A4,
    leftMargin=18*mm, rightMargin=18*mm,
    topMargin=18*mm, bottomMargin=18*mm
)

styles = getSampleStyleSheet()

def S(name, **kw):
    return ParagraphStyle(name, **kw)

title_style = S("Title2", fontSize=22, textColor=WHITE, alignment=TA_CENTER,
                fontName="Helvetica-Bold", spaceAfter=4)
subtitle_style = S("Sub", fontSize=11, textColor=GREY, alignment=TA_CENTER,
                   fontName="Helvetica", spaceAfter=6)
badge_style = S("Badge", fontSize=10, textColor=DARK, alignment=TA_CENTER,
                fontName="Helvetica-Bold", spaceAfter=0)
section_style = S("Sec", fontSize=14, textColor=GOLD, fontName="Helvetica-Bold",
                  spaceAfter=6, spaceBefore=14)
body_style = S("Body2", fontSize=10, textColor=GREY, fontName="Helvetica",
               spaceAfter=4, leading=15)
bold_body = S("BBody", fontSize=10, textColor=WHITE, fontName="Helvetica-Bold",
              spaceAfter=4, leading=15)
bullet_style = S("Bul", fontSize=10, textColor=GREY, fontName="Helvetica",
                 leftIndent=14, spaceAfter=3, leading=14,
                 bulletIndent=4)
warn_style = S("Warn", fontSize=10, textColor=GOLD, fontName="Helvetica",
               spaceAfter=4, leading=14)
tip_style = S("Tip", fontSize=10, textColor=GREEN, fontName="Helvetica",
              spaceAfter=4, leading=14)
danger_style = S("Danger", fontSize=10, textColor=RED, fontName="Helvetica",
                 spaceAfter=4, leading=14)
footer_style = S("Footer", fontSize=9, textColor=GREY, alignment=TA_CENTER,
                 fontName="Helvetica", spaceAfter=2)
footer_link = S("FooterLink", fontSize=9, textColor=GOLD, alignment=TA_CENTER,
                fontName="Helvetica", spaceAfter=2)

def page_bg(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(BG)
    canvas.rect(0, 0, A4[0], A4[1], fill=1, stroke=0)
    canvas.restoreState()

story = []

# ── COVER ──────────────────────────────────────────────────────────────────
story.append(Spacer(1, 20*mm))
story.append(Paragraph("🟡 BINANCE", title_style))
story.append(Paragraph("Futures Trading — Complete Guide", S("T2", fontSize=16, textColor=WHITE,
    alignment=TA_CENTER, fontName="Helvetica-Bold", spaceAfter=6)))
story.append(Paragraph("How to use Binance Futures effectively | Educational Reference", subtitle_style))
story.append(Spacer(1, 4*mm))

badge_data = [["  🟡  Binance Support AI  "]]
badge_tbl = Table(badge_data, hAlign="CENTER")
badge_tbl.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,-1), GOLD),
    ("TEXTCOLOR", (0,0), (-1,-1), DARK),
    ("FONTNAME", (0,0), (-1,-1), "Helvetica-Bold"),
    ("FONTSIZE", (0,0), (-1,-1), 11),
    ("ALIGN", (0,0), (-1,-1), "CENTER"),
    ("ROUNDEDCORNERS", [10,10,10,10]),
    ("TOPPADDING", (0,0), (-1,-1), 6),
    ("BOTTOMPADDING", (0,0), (-1,-1), 6),
    ("LEFTPADDING", (0,0), (-1,-1), 20),
    ("RIGHTPADDING", (0,0), (-1,-1), 20),
]))
story.append(badge_tbl)
story.append(Spacer(1, 6*mm))
story.append(HRFlowable(width="100%", thickness=2, color=GOLD, spaceAfter=10))

# Disclaimer
warn_data = [[Paragraph(
    "⚠️  <b>Risk Disclaimer:</b> Futures trading involves substantial risk of loss. "
    "Leverage amplifies both gains and losses. This document is for educational purposes only "
    "and does not constitute financial advice. Never trade with funds you cannot afford to lose.",
    warn_style)]]
warn_tbl = Table(warn_data, colWidths=["100%"])
warn_tbl.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,-1), colors.HexColor("#1a1500")),
    ("LINEAFTER", (0,0), (0,-1), 4, GOLD),
    ("LEFTPADDING", (0,0), (-1,-1), 12),
    ("RIGHTPADDING", (0,0), (-1,-1), 12),
    ("TOPPADDING", (0,0), (-1,-1), 10),
    ("BOTTOMPADDING", (0,0), (-1,-1), 10),
]))
story.append(warn_tbl)
story.append(Spacer(1, 6*mm))

# ── SECTION 1: WHAT ARE FUTURES ────────────────────────────────────────────
story.append(Paragraph("📘  1. What Are Binance Futures?", section_style))
story.append(HRFlowable(width="100%", thickness=0.5, color=DARK, spaceAfter=8))

story.append(Paragraph(
    "Binance Futures lets you trade crypto contracts with leverage — controlling a larger "
    "position than your actual capital. Two main types:", body_style))
story.append(Paragraph("• <b>USD-M Futures:</b> Settled in USDT. Most popular. Ideal for USD-based returns.", bullet_style))
story.append(Paragraph("• <b>COIN-M Futures:</b> Settled in the underlying crypto (BTC, ETH...). Better for accumulating crypto.", bullet_style))

# ── SECTION 2: GETTING STARTED ─────────────────────────────────────────────
story.append(Spacer(1, 4*mm))
story.append(Paragraph("⚙️  2. How to Get Started", section_style))
story.append(HRFlowable(width="100%", thickness=0.5, color=DARK, spaceAfter=8))

steps = [
    ("1", "Activate Futures Account",
     ["Go to Binance → Derivatives → USD-M Futures",
      "Accept terms & conditions",
      "Pass the mandatory knowledge quiz"]),
    ("2", "Fund Your Futures Wallet",
     ["Transfer USDT from Spot → Futures wallet",
      "Menu: Wallet → Transfer → Spot → USD-M Futures",
      "Recommended start: $50–$100 minimum"]),
    ("3", "Configure Your Settings",
     ["Margin mode: Isolated (safer) vs Cross (shares whole wallet)",
      "Leverage: Start with 2x–5x when learning",
      "Asset mode: Single-asset recommended for beginners"]),
]

for num, title, bullets in steps:
    header_data = [[
        Paragraph(num, S("N", fontSize=11, textColor=DARK, fontName="Helvetica-Bold",
                         alignment=TA_CENTER)),
        Paragraph(title, S("SH", fontSize=11, textColor=WHITE, fontName="Helvetica-Bold"))
    ]]
    ht = Table(header_data, colWidths=[8*mm, None])
    ht.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (0,0), GOLD),
        ("BACKGROUND", (1,0), (1,0), DARK),
        ("ALIGN", (0,0), (0,0), "CENTER"),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("TOPPADDING", (0,0), (-1,-1), 6),
        ("BOTTOMPADDING", (0,0), (-1,-1), 6),
        ("LEFTPADDING", (1,0), (1,0), 10),
        ("LEFTPADDING", (0,0), (0,0), 2),
        ("RIGHTPADDING", (0,0), (-1,-1), 8),
    ]))
    bul_data = [[Paragraph("• " + b, bullet_style)] for b in bullets]
    bt = Table(bul_data, colWidths=["100%"])
    bt.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), DARK),
        ("LEFTPADDING", (0,0), (-1,-1), 14),
        ("RIGHTPADDING", (0,0), (-1,-1), 10),
        ("TOPPADDING", (0,0), (-1,-1), 4),
        ("BOTTOMPADDING", (0,0), (-1,-1), 4),
    ]))
    story.append(KeepTogether([ht, bt, Spacer(1, 4*mm)]))

# ── SECTION 3: KEY CONCEPTS ────────────────────────────────────────────────
story.append(Paragraph("🔑  3. Key Concepts to Master", section_style))
story.append(HRFlowable(width="100%", thickness=0.5, color=DARK, spaceAfter=8))

concepts = [
    ("📊 Long vs Short",
     "Long = bet price goes UP (profit when price rises).\nShort = bet price goes DOWN (profit when price falls)."),
    ("⚡ Leverage",
     "10x leverage = control $1,000 with $100.\nAmplifies profits AND losses equally. Higher leverage = liquidation closer."),
    ("💧 Margin",
     "Initial margin: capital to open position.\nMaintenance margin: minimum to keep it open. Drop below = liquidation."),
    ("💸 Funding Rate",
     "Fee paid between longs/shorts every 8 hours.\nPositive: longs pay shorts. Negative: shorts pay longs."),
    ("📉 Liquidation",
     "Auto-close when margin drops below maintenance level.\nAlways set a Stop-Loss to avoid forced liquidation."),
    ("📋 Order Types",
     "Market: instant execution.\nLimit: execute at your target price.\nStop-Market / Stop-Limit: risk management orders."),
]

half = len(concepts) // 2
rows = []
for i in range(half):
    left_t, left_b = concepts[i]
    right_t, right_b = concepts[i + half]
    cell_l = [Paragraph(left_t, S("CT", fontSize=10, textColor=GOLD, fontName="Helvetica-Bold", spaceAfter=3)),
              Paragraph(left_b, S("CB", fontSize=9, textColor=GREY, fontName="Helvetica", leading=13))]
    cell_r = [Paragraph(right_t, S("CT2", fontSize=10, textColor=GOLD, fontName="Helvetica-Bold", spaceAfter=3)),
              Paragraph(right_b, S("CB2", fontSize=9, textColor=GREY, fontName="Helvetica", leading=13))]
    rows.append([cell_l, cell_r])

concept_tbl = Table(rows, colWidths=["48%", "48%"], hAlign="LEFT",
                    spaceBefore=0, spaceAfter=0, style=TableStyle([
    ("BACKGROUND", (0,0), (-1,-1), DARK),
    ("TOPPADDING", (0,0), (-1,-1), 8),
    ("BOTTOMPADDING", (0,0), (-1,-1), 8),
    ("LEFTPADDING", (0,0), (-1,-1), 10),
    ("RIGHTPADDING", (0,0), (-1,-1), 10),
    ("GRID", (0,0), (-1,-1), 0.5, colors.HexColor("#2b3139")),
    ("VALIGN", (0,0), (-1,-1), "TOP"),
]))
story.append(concept_tbl)

# ── SECTION 4: STRATEGIES ──────────────────────────────────────────────────
story.append(Spacer(1, 4*mm))
story.append(Paragraph("📈  4. Common Trading Approaches", section_style))
story.append(HRFlowable(width="100%", thickness=0.5, color=DARK, spaceAfter=8))

strategies = [
    ("🎯 Trend Following",
     "Trade in the direction of the dominant trend. Use moving averages (MA20, MA50, MA200) to identify direction. "
     "Go long in uptrends, short in downtrends. Best for beginners."),
    ("📊 Support & Resistance",
     "Identify key price levels where market repeatedly reverses. Buy near support, sell/short near resistance. "
     "Confirm with order book depth or volume."),
    ("⚡ Scalping",
     "Many small profits throughout the day using 1m–5m charts. Requires discipline and fast execution. "
     "Use low leverage (3x–5x max) to manage risk."),
    ("🏗️ Swing Trading",
     "Hold positions for days or weeks to capture larger moves. Uses 4h–1D charts. "
     "Less affected by short-term noise. Requires patience."),
]

for title, desc in strategies:
    d = [[
        Paragraph(f"<b>{title}</b>", S("ST", fontSize=10, textColor=WHITE, fontName="Helvetica-Bold", spaceAfter=4)),
        Paragraph(desc, S("SD", fontSize=9.5, textColor=GREY, fontName="Helvetica", leading=14))
    ]]
    t = Table(d, colWidths=["100%"])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), DARK),
        ("LEFTPADDING", (0,0), (-1,-1), 12),
        ("RIGHTPADDING", (0,0), (-1,-1), 12),
        ("TOPPADDING", (0,0), (-1,-1), 8),
        ("BOTTOMPADDING", (0,0), (-1,-1), 8),
        ("LINEAFTER", (0,0), (0,-1), 3, GOLD),
    ]))
    story.append(t)
    story.append(Spacer(1, 3*mm))

# ── SECTION 5: RISK MANAGEMENT ─────────────────────────────────────────────
story.append(Paragraph("🛡️  5. Risk Management — The Most Important Section", section_style))
story.append(HRFlowable(width="100%", thickness=0.5, color=DARK, spaceAfter=8))

danger_data = [[Paragraph(
    "❌  Most traders lose money not because of bad strategy, but because of poor risk management.",
    danger_style)]]
danger_tbl = Table(danger_data, colWidths=["100%"])
danger_tbl.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,-1), colors.HexColor("#1a0508")),
    ("LINEBEFORE", (0,0), (0,-1), 4, RED),
    ("LEFTPADDING", (0,0), (-1,-1), 12),
    ("RIGHTPADDING", (0,0), (-1,-1), 12),
    ("TOPPADDING", (0,0), (-1,-1), 8),
    ("BOTTOMPADDING", (0,0), (-1,-1), 8),
]))
story.append(danger_tbl)
story.append(Spacer(1, 4*mm))

risk_headers = ["Rule", "Recommended", "Why"]
risk_data = [
    ["Risk per trade", "1–2% of capital", "Survive a losing streak"],
    ["Leverage", "2x–10x max", "Avoid fast liquidation"],
    ["Stop-Loss", "Always set one", "Limits max loss per trade"],
    ["Take-Profit", "Set before entering", "Lock profits automatically"],
    ["Risk/Reward ratio", "Minimum 1:2", "Profitable even at 40% win rate"],
    ["Daily loss limit", "Max 5–10% per day", "Stop trading when emotionally impaired"],
]

tbl_data = [[Paragraph(h, S("TH", fontSize=10, textColor=DARK, fontName="Helvetica-Bold")) for h in risk_headers]]
for row in risk_data:
    tbl_data.append([Paragraph(row[0], body_style), Paragraph(row[1], tip_style), Paragraph(row[2], body_style)])

risk_tbl = Table(tbl_data, colWidths=["35%", "30%", "35%"])
risk_tbl.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), GOLD),
    ("BACKGROUND", (0,1), (-1,-1), DARK),
    ("ROWBACKGROUNDS", (0,1), (-1,-1), [DARK, colors.HexColor("#161b22")]),
    ("GRID", (0,0), (-1,-1), 0.5, colors.HexColor("#2b3139")),
    ("TOPPADDING", (0,0), (-1,-1), 6),
    ("BOTTOMPADDING", (0,0), (-1,-1), 6),
    ("LEFTPADDING", (0,0), (-1,-1), 10),
    ("RIGHTPADDING", (0,0), (-1,-1), 10),
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
]))
story.append(risk_tbl)
story.append(Spacer(1, 4*mm))

tip_data = [[Paragraph(
    "✅  <b>Golden Rule:</b> Set your Stop-Loss BEFORE opening the position. Never move it further against you.",
    tip_style)]]
tip_tbl = Table(tip_data, colWidths=["100%"])
tip_tbl.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,-1), colors.HexColor("#051a10")),
    ("LINEBEFORE", (0,0), (0,-1), 4, GREEN),
    ("LEFTPADDING", (0,0), (-1,-1), 12),
    ("RIGHTPADDING", (0,0), (-1,-1), 12),
    ("TOPPADDING", (0,0), (-1,-1), 8),
    ("BOTTOMPADDING", (0,0), (-1,-1), 8),
]))
story.append(tip_tbl)

# ── SECTION 6: FEES ────────────────────────────────────────────────────────
story.append(Spacer(1, 4*mm))
story.append(Paragraph("💰  6. Fees on Binance Futures", section_style))
story.append(HRFlowable(width="100%", thickness=0.5, color=DARK, spaceAfter=8))

fee_headers = ["Fee Type", "Rate", "Notes"]
fee_data = [
    ["Maker fee", "0.0200%", "Limit orders that add liquidity"],
    ["Taker fee", "0.0500%", "Market orders / instant fill"],
    ["Funding rate", "Variable (every 8h)", "Check before holding overnight"],
    ["BNB discount", "-10%", "Pay fees in BNB to save"],
]

ftbl_data = [[Paragraph(h, S("FH", fontSize=10, textColor=DARK, fontName="Helvetica-Bold")) for h in fee_headers]]
for row in fee_data:
    ftbl_data.append([Paragraph(r, body_style) for r in row])

fee_tbl = Table(ftbl_data, colWidths=["30%", "30%", "40%"])
fee_tbl.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), GOLD),
    ("BACKGROUND", (0,1), (-1,-1), DARK),
    ("ROWBACKGROUNDS", (0,1), (-1,-1), [DARK, colors.HexColor("#161b22")]),
    ("GRID", (0,0), (-1,-1), 0.5, colors.HexColor("#2b3139")),
    ("TOPPADDING", (0,0), (-1,-1), 6),
    ("BOTTOMPADDING", (0,0), (-1,-1), 6),
    ("LEFTPADDING", (0,0), (-1,-1), 10),
    ("RIGHTPADDING", (0,0), (-1,-1), 10),
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
]))
story.append(fee_tbl)

# ── SECTION 7: CHECKLIST ───────────────────────────────────────────────────
story.append(Spacer(1, 4*mm))
story.append(Paragraph("✅  7. Pre-Trade Checklist", section_style))
story.append(HRFlowable(width="100%", thickness=0.5, color=DARK, spaceAfter=8))

checklist = [
    "☐  Identified the trend (up, down, sideways)?",
    "☐  Checked key support / resistance levels?",
    "☐  Defined entry price?",
    "☐  Set Stop-Loss level (never skip this!)?",
    "☐  Set Take-Profit target?",
    "☐  Calculated risk/reward ratio (min 1:2)?",
    "☐  Checked funding rate (if holding for hours)?",
    "☐  Position size appropriate (max 1–2% risk)?",
    "☐  No major news event upcoming that could spike volatility?",
]

cl_data = [[Paragraph(item, S("CL", fontSize=10, textColor=GREY, fontName="Helvetica", leading=14))] for item in checklist]
cl_tbl = Table(cl_data, colWidths=["100%"])
cl_tbl.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,-1), DARK),
    ("LEFTPADDING", (0,0), (-1,-1), 16),
    ("RIGHTPADDING", (0,0), (-1,-1), 12),
    ("TOPPADDING", (0,0), (-1,-1), 5),
    ("BOTTOMPADDING", (0,0), (-1,-1), 5),
    ("GRID", (0,0), (-1,-1), 0.3, colors.HexColor("#2b3139")),
]))
story.append(cl_tbl)

# ── FOOTER ────────────────────────────────────────────────────────────────
story.append(Spacer(1, 10*mm))
story.append(HRFlowable(width="100%", thickness=1, color=DARK, spaceAfter=6))
story.append(Paragraph("📚 Official Binance Futures Help: https://www.binance.com/en/support/faq/futures", footer_link))
story.append(Paragraph("🔒 Account support: https://www.binance.com/en/chat", footer_link))
story.append(Spacer(1, 2*mm))
story.append(Paragraph("Generated by 🟡 Binance Support AI — For educational purposes only. Not financial advice.", footer_style))

doc.build(story, onFirstPage=page_bg, onLaterPages=page_bg)
print("PDF generated:", OUTPUT)
