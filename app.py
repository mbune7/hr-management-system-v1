import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Mother Amadea HR System", page_icon="🏥", layout="wide")

# Custom CSS for modern & clean look
st.markdown("""
<style>
    .card {background: white; padding: 20px; border-radius: 16px; box-shadow: 0 6px 16px rgba(0,0,0,0.08); margin: 10px 0;}
    h1, h2, h3 {color: #1e3a8a;}
    .stMetric {background: white; padding: 15px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.08);}
</style>
""", unsafe_allow_html=True)

# ==================== LOGIN ====================
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.title("🏥 Mother Amadea Mission Hospital")
    st.subheader("Human Resource Management System")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("amadea_logo.png", width=240)
        username = st.text_input("Username", "admin")
        password = st.text_input("Password", "12345", type="password")
        if st.button("Login", type="primary", use_container_width=True):
            if username == "admin" and password == "12345":
                st.session_state.logged_in = True
                st.success("✅ Login Successful!")
                st.rerun()
            else:
                st.error("❌ Invalid credentials")
    st.stop()

# ==================== SIDEBAR ====================
st.sidebar.image("amadea_logo.png", width=150)
st.sidebar.title("Mother Amadea")
st.sidebar.subheader("Mission Hospital")
st.sidebar.success(f"Welcome — {datetime.now().strftime('%B %Y')}")

menu = st.sidebar.radio(
    "Navigation",
    ["📊 Dashboard", "👥 Staff Directory", "🏢 Departments", "💰 Payroll",
     "📅 Shift Scheduling", "👥 Staff Scheduling", "⏰ Attendance", 
     "🌴 Leave Management", "📈 KPI Dashboard", "📋 Reports"]
)

if st.sidebar.button("🚪 Logout"):
    st.session_state.logged_in = False
    st.rerun()

# ====================== DASHBOARD ======================
if menu == "📊 Dashboard":
    st.title("📊 Dashboard")
    st.caption(f"Welcome back — {datetime.now().strftime('%B %Y')}")

    c1, c2, c3, c4 = st.columns(4)
    with c1: st.metric("Total Staff", "74", "74 active • 0 on leave")
    with c2: st.metric("Departments", "9")
    with c3: st.metric("Monthly Payroll", "KSH 3,515,002")
    with c4: st.metric("Avg KPI Score", "90.8%")

    col_a, col_b = st.columns(2)
    with col_a: st.info("📅 **5 Leave Requests** Awaiting approval")
    with col_b: st.info("🔄 **0 Shift Swap Requests** Pending review")

    st.subheader("Performance Overview")
    st.progress(0.917, text="Attendance Rate — 91.7%")
    st.progress(0.893, text="Punctuality — 89.3%")
    st.progress(0.905, text="Patient Satisfaction — 90.5%")
    st.progress(0.919, text="Task Completion — 91.9%")

# ====================== STAFF DIRECTORY ======================
elif menu == "👥 Staff Directory":
    st.title("👥 Staff Directory")
    st.caption("74 employees")
    st.text_input("🔍 Search by name, ID or position", "")

    cols = st.columns(4)
    samples = [
        ("Dr. Grace Mwangi", "MAMH-001", "Medical Officer", "OPD"),
        ("Dr. James Okonkwo", "MAMH-002", "Medical Officer", "OPD"),
        ("Jane Atieno", "MAMH-003", "Registered Nurse", "Maternity"),
        ("Peter Kamau", "MAMH-004", "Enrolled Nurse", "CWC"),
    ]
    for i in range(16):
        name, eid, pos, dept = samples[i % 4]
        with cols[i % 4]:
            st.markdown(f"""
            <div class="card" style="text-align:center;">
                <h4>{name}</h4>
                <p>{eid}</p>
                <p><strong>{pos}</strong></p>
                <p style="color:#666;">{dept}</p>
                <span style="background:#10b981;color:white;padding:6px 14px;border-radius:30px;">Active</span>
            </div>
            """, unsafe_allow_html=True)

# ====================== DEPARTMENTS ======================
elif menu == "🏢 Departments":
    st.title("🏢 Departments")
    st.caption("9 active departments")
    depts = [
        ("ANC", "Antenatal Clinic", "🔴 Active"),
        ("Administration", "Hospital Administration", "🔵 Active"),
        ("CWC", "Child Welfare Clinic", "🔵 Active"),
        ("Lab", "Laboratory Services", "🟠 Active"),
        ("OPD", "Outpatient Department", "🔴 Active"),
        ("Pharmacy", "Pharmacy Department", "🟢 Active"),
        ("Radiology", "Radiology & Imaging", "🔵 Active"),
        ("Theatre 1", "Operating Theatre 1", "🟣 Active"),
        ("Theatre 2", "Operating Theatre 2", "🔴 Active"),
    ]
    cols = st.columns(4)
    for i, (short, full, status) in enumerate(depts):
        with cols[i % 4]:
            st.markdown(f"""
            <div class="card">
                <h3>{short}</h3>
                <p style="color:#666;">{full}</p>
                <p><strong>{status}</strong></p>
            </div>
            """, unsafe_allow_html=True)

# ====================== PAYROLL ======================
elif menu == "💰 Payroll":
    st.title("💰 Payroll Management")
    st.caption("April 2026")
    c1, c2, c3, c4 = st.columns(4)
    with c1: st.metric("Total Gross", "KSH 4,301,202")
    with c2: st.metric("Total Deductions", "KSH 786,200")
    with c3: st.metric("Net Payroll", "KSH 3,515,002")
    with c4: st.metric("Payslips Generated", "74")

    st.subheader("Payroll Records")
    df = pd.DataFrame({
        "Employee": ["Dr. Grace Mwangi", "Dr. James Okonkwo", "Nurse 1 Staff", "Nurse 2 Staff", "Nurse 3 Staff"],
        "ID": ["MAMH-001","MAMH-002","MAMH-003","MAMH-004","MAMH-005"],
        "Department": ["OPD","OPD","OPD","CWC","ANC"],
        "Gross": [211553,217963,52719,50592,51945],
        "Deductions": [40000,40000,7000,7000,7000],
        "Net": [171553,177963,45719,43592,44945],
        "Status": ["Paid","Paid","Paid","Paid","Paid"]
    })
    st.dataframe(df, use_container_width=True, hide_index=True)

# ====================== SHIFT SCHEDULING ======================
elif menu == "📅 Shift Scheduling":
    st.title("📅 Shift Scheduling")
    st.caption("April 2026")
    st.subheader("Shift Legend")
    leg = st.columns(3)
    with leg[0]: st.markdown("**🌅 Morning** (06:00-14:00)")
    with leg[1]: st.markdown("**🌤️ Afternoon** (14:00-22:00)")
    with leg[2]: st.markdown("**🌙 Night** (22:00-06:00)")

    st.markdown("---")
    days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    header = st.columns(7)
    for i, d in enumerate(days):
        with header[i]:
            st.markdown(f"<h4 style='text-align:center'>{d}</h4>", unsafe_allow_html=True)

    weeks = [[1,2,3,4,5,6,7],[8,9,10,11,12,13,14],[15,16,17,18,19,20,21],
             [22,23,24,25,26,27,28],[29,30,0,0,0,0,0]]

    for week in weeks:
        cols = st.columns(7)
        for i, day in enumerate(week):
            with cols[i]:
                if day == 0: continue
                st.markdown(f"<div style='text-align:center;font-weight:bold;margin-bottom:8px;'>{day}</div>", unsafe_allow_html=True)
                shifts = ["N.Staff"]*3 if day % 3 == 0 else ["N.Staff"]*2
                colors = ["#FF9800", "#2196F3", "#9C27B0"]
                for j, s in enumerate(shifts[:3]):
                    st.markdown(f"""
                    <div style="background:{colors[j%3]};color:white;padding:8px;margin:4px 0;border-radius:8px;text-align:center;">
                        {s}
                    </div>""", unsafe_allow_html=True)

# ====================== STAFF SCHEDULING ======================
elif menu == "👥 Staff Scheduling":
    st.title("👥 Staff Scheduling")
    st.caption("April 2026 - Roster & Swap Management")
    df_roster = pd.DataFrame({
        "Staff": ["Dr. Grace Mwangi", "Dr. James Okonkwo", "Nurse 1 Staff", "Nurse 2 Staff", "Nurse 3 Staff"],
        "Department": ["OPD", "OPD", "OPD", "CWC", "ANC"],
        "Total Shifts": [30, 30, 30, 30, 30],
        "Schedule": ["Afternoon, Night, Morning +25"]*5
    })
    st.dataframe(df_roster, use_container_width=True, hide_index=True)

# ====================== ATTENDANCE (Fully Visible) ======================
elif menu == "⏰ Attendance":
    st.title("⏰ Attendance Tracking")
    st.caption("April 2026")

    c1, c2, c3, c4 = st.columns(4)
    with c1: st.metric("Present", "660")
    with c2: st.metric("Absent", "18")
    with c3: st.metric("Late", "62")
    with c4: st.metric("On Leave", "0")

    st.subheader("Attendance Records")
    att_df = pd.DataFrame({
        "Employee": ["Nurse 31 Staff", "Nurse 21 Staff", "Health Records 3 Staff", "Nurse 22 Staff"],
        "Department": ["OPD", "OPD", "Administration", "CWC"],
        "Clock In": ["09:00 AM", "09:05 AM", "08:55 AM", "09:15 AM"],
        "Clock Out": ["05:00 PM", "05:00 PM", "05:00 PM", "04:45 PM"],
        "Hours": ["8.0h", "7.92h", "8.08h", "7.5h"],
        "Status": ["✅ Present", "✅ Present", "✅ Present", "⚠️ Late"]
    })
    st.dataframe(att_df, use_container_width=True, hide_index=True)

# ====================== LEAVE MANAGEMENT (Fully Visible) ======================
elif menu == "🌴 Leave Management":
    st.title("🌴 Leave Management")
    st.caption("2026 • 5 pending requests")

    if st.button("➕ Request Leave", type="primary"):
        st.success("New leave request submitted (demo)")

    st.subheader("Leave Requests")
    leave_df = pd.DataFrame({
        "Employee": ["Nurse 22 Staff", "Nurse 30 Staff", "Nurse 1 Staff", "Nurse 2 Staff", "Cashier 3 Staff"],
        "ID": ["MAMH-024", "MAMH-032", "MAMH-003", "MAMH-004", "MAMH-050"],
        "Type": ["Emergency", "Annual", "Emergency", "Annual", "Sick"],
        "Period": ["Apr 14–18", "Apr 19–23", "Apr 17–21", "Apr 9–13", "Apr 20–21"],
        "Days": [5, 5, 5, 5, 2],
        "Status": ["Pending", "Pending", "Pending", "Pending", "Pending"]
    })
    st.dataframe(leave_df, use_container_width=True, hide_index=True)

# ====================== KPI DASHBOARD (Fully Visible) ======================
elif menu == "📈 KPI Dashboard":
    st.title("📈 KPI Dashboard")
    st.caption("April 2026 Performance")

    c1, c2, c3, c4 = st.columns(4)
    with c1: st.metric("Avg Attendance", "91.7%")
    with c2: st.metric("Avg Punctuality", "89.3%")
    with c3: st.metric("Patient Satisfaction", "90.5%")
    with c4: st.metric("Task Completion", "91.9%")

    st.subheader("Team Averages")
    st.progress(0.917, text="Attendance — 91.7%")
    st.progress(0.893, text="Punctuality — 89.3%")
    st.progress(0.905, text="Patient Satisfaction — 90.5%")
    st.progress(0.919, text="Task Completion — 91.9%")

    st.subheader("Staff KPI Records")
    kpi_df = pd.DataFrame({
        "Employee": ["Procurement Officer", "Nurse 27 Staff", "Nurse 19 Staff", "Radiologist 2 Staff"],
        "Attendance": ["98%", "87%", "97%", "95%"],
        "Punctuality": ["93%", "98%", "96%", "97%"],
        "Satisfaction": ["99%", "98%", "92%", "96%"],
        "Overall": ["95.9%", "95.4%", "95.3%", "95.1%"]
    })
    st.dataframe(kpi_df, use_container_width=True, hide_index=True)

# ====================== REPORTS (Fully Visible) ======================
elif menu == "📋 Reports":
    st.title("📋 Reports")
    st.caption("April 2026 - HR Analytics")

    c1, c2, c3, c4 = st.columns(4)
    with c1: st.metric("Total Staff", "74")
    with c2: st.metric("Departments", "9")
    with c3: st.metric("Net Payroll", "KSH 3,515,002")
    with c4: st.metric("Avg KPI", "90.8%")

    st.subheader("KPI Performance")
    st.progress(0.95, text="Attendance — 95%")
    st.progress(0.92, text="Punctuality — 92%")
    st.progress(0.94, text="Satisfaction — 94%")
    st.progress(0.96, text="Task Completion — 96%")

    st.subheader("Attendance Breakdown")
    st.info("Present: 85% | Absent: 10% | Late: 5%")

    if st.button("📥 Export Report", type="primary"):
        st.success("Report exported successfully!")

# ====================== Fallback ======================
else:
    st.title(menu)
    st.info(f"**{menu}** page is ready.")
