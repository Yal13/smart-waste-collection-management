import streamlit as st
import mysql.connector
import pandas as pd
from login import login_page
import plotly.express as px
import pandas as pd
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.units import inch
from io import BytesIO
st.markdown("""
<style>

/* Don't force the app background */

/* Dashboard Title */
h1{
    text-align:center;
}

/* Metric Cards */
[data-testid="metric-container"]{
    border-radius:15px;
    padding:18px;
    border:2px solid #2ECC71;
}

/* Buttons */
.stButton>button{
    border-radius:10px;
    font-weight:bold;
}

/* Sidebar */
[data-testid="stSidebar"]{
    border-right:2px solid #2ECC71;
}

</style>
""", unsafe_allow_html=True)
def create_pdf(df, title):
    buffer = BytesIO()

    doc = SimpleDocTemplate(
        buffer,
        pagesize=landscape(A4),
        rightMargin=30,
        leftMargin=30,
        topMargin=30,
        bottomMargin=30
    )

    styles = getSampleStyleSheet()
    elements = []

    elements.append(
        Paragraph(
            "Smart Waste Collection Management System",
            styles["Title"]
        )
    )

    elements.append(
        Paragraph(title, styles["Heading2"])
    )

    elements.append(Spacer(1, 15))

    table_data = [list(df.columns)] + df.astype(str).values.tolist()

    table = Table(table_data, repeatRows=1)

    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.green),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1),
         [colors.white, colors.lightgrey]),
        ("FONTSIZE", (0, 0), (-1, -1), 8),
    ]))

    elements.append(table)

    doc.build(elements)

    buffer.seek(0)
    return buffer
# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(page_title="Smart Waste Collection Management", layout="wide")
st.markdown("""
<style>

/* Dashboard Metric Cards */
[data-testid="metric-container"]{
    background: white;
    border: 2px solid #2E7D32;
    padding: 18px;
    border-radius: 15px;
    box-shadow: 3px 3px 12px rgba(0,0,0,0.15);
}

[data-testid="metric-container"]:hover{
    transform: scale(1.03);
    transition: 0.3s;
    border: 2px solid #43A047;
}

/* Metric Labels */
[data-testid="stMetricLabel"]{
    font-size:18px;
    font-weight:bold;
}

/* Metric Values */
[data-testid="stMetricValue"]{
    font-size:30px;
    color:#2E7D32;
}

</style>
""", unsafe_allow_html=True)
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
st.markdown("""
<style>

/* -------------------------
   Sidebar
------------------------- */
[data-testid="stSidebar"]{
    background: linear-gradient(180deg, #1B5E20, #2E7D32);
}

[data-testid="stSidebar"] *{
    color: white !important;
}

/* Sidebar title */
[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3{
    color:white !important;
}

/* Radio button labels */
div[role="radiogroup"] label{
    color:white !important;
    font-weight:600;
}

/* Sidebar buttons */
[data-testid="stSidebar"] .stButton > button{
    width:100%;
    background:#43A047;
    color:white;
    border:none;
    border-radius:10px;
    font-weight:bold;
}

[data-testid="stSidebar"] .stButton > button:hover{
    background:#66BB6A;
    color:white;
}

/* Horizontal line */
hr{
    border:1px solid rgba(255,255,255,0.2);
}

</style>
""", unsafe_allow_html=True)
if not st.session_state.logged_in:
    login_page()
    st.stop()
# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.image(
    "https://img.icons8.com/fluency/96/recycle.png",
    width=80
)
st.image("assets/logo.png", width=150)
st.sidebar.title("Smart Waste")

st.sidebar.success(f"👋 Welcome\n\n{st.session_state.name}")

st.sidebar.info(f"Role: {st.session_state.role}")

st.sidebar.markdown("---")

if st.sidebar.button("🚪 Logout"):
    st.session_state.logged_in = False
    st.session_state.role = ""
    st.session_state.name = ""
    st.rerun()
# -----------------------------
# Database Connection
# -----------------------------
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="yalini@2007",   # Replace with your MySQL password
        database="smart_waste_db"
    )
    cursor = conn.cursor()

except mysql.connector.Error as err:
    st.error(f"Database Connection Failed: {err}")
    st.stop()

# -----------------------------
# Title
# -----------------------------
st.title("🗑️ Smart Waste Collection Management System")
# -----------------------------
# Role Based Navigation
# -----------------------------

if st.session_state.role == "Admin":

    menu = st.sidebar.radio(
        "Navigation",
        [
            "Dashboard",
            "Bins",
            "Workers",
            "Vehicles",
            "Users"
        ]
    )

elif st.session_state.role == "Worker":

    menu = st.sidebar.radio(
        "Navigation",
        [
            "Dashboard",
            "Workers",
            "Vehicles"
        ]
    )

elif st.session_state.role == "User":

    menu = st.sidebar.radio(
        "Navigation",
        [
            "Dashboard",
            "Users"
        ]
    )
# -----------------------------
# Role Permissions
# -----------------------------

is_admin = st.session_state.role == "Admin"
is_worker = st.session_state.role == "Worker"
is_user = st.session_state.role == "User"
# ======================================================
# DASHBOARD
# ======================================================
if menu == "Dashboard":
    
    

    st.markdown(
        """
        <h1 style='text-align:center;color:#2E7D32;'>
            Smart Waste Collection Management System
        </h1>

        <p style='text-align:center;font-size:18px;color:gray;'>
            Efficient • Smart • Sustainable Waste Management
        </p>
        """,
        unsafe_allow_html=True
    )
    st.caption("An Intelligent DBMS Solution for Efficient Waste Monitoring and Management")
    st.success(
        f"👋 {st.session_state.name}**! "
        f"You are logged in as **{st.session_state.role}**."
    )
    from datetime import datetime

    col1, col2 = st.columns(2)

    with col1:
        st.info(f"📅 Date: {datetime.now().strftime('%d %B %Y')}")

    with col2:
        st.info(f"🕒 Time: {datetime.now().strftime('%I:%M %p')}")
        st.markdown("---")
    

    from datetime import datetime

    col1, col2 = st.columns([3,1])

    with col1:
        
        st.write(f"**Role:** {st.session_state.role}")


    st.markdown("---")

    # Database Counts
    cursor.execute("SELECT COUNT(*) FROM bins")
    total_bins = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM workers")
    total_workers = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM vehicles")
    total_vehicles = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM users")
    total_users = cursor.fetchone()[0]

    # Cards
    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric("🗑 Total Bins", total_bins)

    with c2:
        st.metric("👷 Workers", total_workers)

    with c3:
        st.metric("🚛 Vehicles", total_vehicles)

    with c4:
        st.metric("👤 Users", total_users)

    st.markdown("---")

    # Dashboard Charts
    data = pd.DataFrame({
        "Category": ["Bins", "Workers", "Vehicles", "Users"],
        "Count": [
            total_bins,
            total_workers,
            total_vehicles,
            total_users
        ]
    })

    col1, col2 = st.columns(2)

    with col1:
        fig = px.bar(
            data,
            x="Category",
            y="Count",
            title="System Statistics"
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        fig2 = px.pie(
            data,
            names="Category",
            values="Count",
            title="Database Distribution"
        )
        st.plotly_chart(fig2, use_container_width=True)
    st.markdown("""
    <h1>🗑 Smart Waste Collection Management System</h1>
    <h4 style='text-align:center;color:gray;'>
    Efficient • Smart • Sustainable Waste Management
    </h4>
    """, unsafe_allow_html=True)
# ======================================================
# BINS
# ======================================================
elif menu == "Bins":

    if not is_admin:
        st.error("❌ Access Denied! You do not have permission to view this section.")
        st.stop()
    st.header("🗑️ Bins Management")

    tab1, tab2, tab3, tab4 = st.tabs([
        "View Bins",
        "Add Bin",
        "Update Bin",
        "Delete Bin"
    ])

    # ---------------- View Bins ----------------
    with tab1:
        cursor.execute("SELECT * FROM bins")
        rows = cursor.fetchall()

        columns = [
            "Bin ID",
            "Location",
            "Bin Type",
            "Capacity",
            "Fill Level",
            "Status"
        ]

        df = pd.DataFrame(rows, columns=columns)
        st.dataframe(df, use_container_width=True)
        pdf_file = create_pdf(df, "Bin Details")

        st.download_button(
            "📄 Download PDF",
            data=pdf_file,
            file_name="bin_details.pdf",
            mime="application/pdf"
        )
    # ---------------- Add Bin ----------------
    with tab2:

        location = st.text_input("Location")
        bin_type = st.text_input("Bin Type")
        capacity = st.number_input("Capacity", min_value=1)
        fill_level = st.number_input("Fill Level", min_value=0)
        status = st.selectbox(
            "Status",
            ["Available", "Full", "Maintenance"]
        )

        if st.button("Add Bin"):

            cursor.execute(
                """
                INSERT INTO bins
                (location, bin_type, capacity, fill_level, status)
                VALUES (%s,%s,%s,%s,%s)
                """,
                (
                    location,
                    bin_type,
                    capacity,
                    fill_level,
                    status
                )
            )

            conn.commit()

            st.success("✅ Bin Added Successfully!")
    
    # ---------------- Update Bin ----------------
    with tab3:

        st.subheader("Update Bin")

        cursor.execute("SELECT bin_id FROM bins")
        bin_ids = [row[0] for row in cursor.fetchall()]

        if len(bin_ids) == 0:
            st.warning("No bins available to update.")

        else:
            selected_bin = st.selectbox("Select Bin ID", bin_ids)

            cursor.execute(
                """
                SELECT location, bin_type, capacity, fill_level, status
                FROM bins
                WHERE bin_id = %s
                """,
                (selected_bin,)
            )

            record = cursor.fetchone()

            status_options = ["Available", "Full", "Maintenance"]

            location = st.text_input(
                "Location",
                value=record[0],
                key="update_location"
            )

            bin_type = st.text_input(
                "Bin Type",
                value=record[1],
                key="update_type"
            )

            capacity = st.number_input(
                "Capacity",
                min_value=1,
                value=int(record[2]),
                key="update_capacity"
            )

            fill_level = st.number_input(
                "Fill Level",
                min_value=0,
                value=int(record[3]),
                key="update_fill"
            )

            status = st.selectbox(
                "Status",
                status_options,
                index=status_options.index(record[4]) if record[4] in status_options else 0,
                key="update_status"
            )

            if st.button("Update Bin"):

                cursor.execute(
                    """
                    UPDATE bins
                    SET location=%s,
                    bin_type=%s,
                    capacity=%s,
                    fill_level=%s,
                    status=%s
                WHERE bin_id=%s
                """,
                (
                    location,
                    bin_type,
                    capacity,
                    fill_level,
                    status,
                    selected_bin
                )
            )

            conn.commit()
            st.success("✅ Bin updated successfully!")
            st.rerun()
    # ---------------- Delete Bin ----------------
    with tab4:

        st.subheader("🗑 Delete Bin")

        cursor.execute("SELECT bin_id, location FROM bins")
        bins = cursor.fetchall()

        if bins:

            bin_options = {
                f"{row[0]} - {row[1]}": row[0]
                for row in bins
            }

            selected_bin = st.selectbox(
                "Select Bin",
                list(bin_options.keys()),
                key="delete_bin_select"
            )

            if st.button("Delete Bin", key="delete_bin_button"):
                bin_id = bin_options[selected_bin]
                cursor.execute(
                    "DELETE FROM bins WHERE bin_id=%s",
                    (bin_id,)
                )

                conn.commit()

                st.success("✅ Bin deleted successfully!")

                st.rerun()

        else:
            st.info("No bins available to delete.")
# ======================================================
# WORKERS
# ======================================================
elif menu == "Workers":

    if not (is_admin or is_worker):
        st.error("❌ Access Denied! You do not have permission to view this section.")
        st.stop()
    st.header("👷 Workers Management")

    tab1, tab2, tab3, tab4= st.tabs([
        "View Workers",
        "Add Worker",
        "Update Worker",
        "Delete Worker"
    ])

    # ---------------- View Workers ----------------
    with tab1:

        cursor.execute("SELECT * FROM workers")
        rows = cursor.fetchall()

        columns = [
            "Worker ID",
            "Worker Name",
            "Phone",
            "Address",
            "Shift Time"
        ]

        df = pd.DataFrame(rows, columns=columns)
        st.dataframe(df, use_container_width=True)
        pdf_file = create_pdf(df, "Worker Details")

        st.download_button(
            "📄 Download Worker PDF",
            data=pdf_file,
            file_name="worker_details.pdf",
            mime="application/pdf"
        )
    # ---------------- Add Worker ----------------
    with tab2:

        worker_name = st.text_input("worker Name", key="worker_name")
        phone = st.text_input("Phone", key="worker_phone")
        email = st.text_input("Email", key="worker_email")
        address = st.text_input("Address", key="worker_address")
        shift_time = st.text_input("Shift Time", key="worker_shift")
        if st.button("Add Worker"):

            cursor.execute(
                """
                INSERT INTO workers
                (worker_name, phone, address, shift_time)
                VALUES (%s, %s, %s, %s)
                """,
                (worker_name, phone, address, shift_time)
            )

            conn.commit()
            st.success("✅ Worker added successfully!")
            st.rerun()

    # ---------------- Update Worker ----------------
    with tab3:

        cursor.execute("SELECT worker_id FROM workers")
        worker_ids = [row[0] for row in cursor.fetchall()]

        if worker_ids:

            selected_worker = st.selectbox("Select Worker ID", worker_ids)

            cursor.execute(
                """
                SELECT worker_name, phone, address, shift_time
                FROM workers
                WHERE worker_id=%s
                """,
                (selected_worker,)
            )

            record = cursor.fetchone()

            worker_name = st.text_input("Worker Name", value=record[0], key="uw_name")
            phone = st.text_input("Phone", value=record[1], key="uw_phone")
            address = st.text_area("Address", value=record[2], key="uw_address")
            shift_time = st.text_input("Shift Time", value=record[3], key="uw_shift")

            if st.button("Update Worker"):

                cursor.execute(
                    """
                    UPDATE workers
                    SET worker_name=%s,
                        phone=%s,
                        address=%s,
                        shift_time=%s
                    WHERE worker_id=%s
                    """,
                    (
                        worker_name,
                        phone,
                        address,
                        shift_time,
                        selected_worker
                    )
                )

                conn.commit()
                st.success("✅ Worker updated successfully!")
                st.rerun()

        else:
            st.warning("No workers available to update.")
    # ---------------- Delete Worker ----------------
    with tab4:

        st.subheader("🗑 Delete Worker")

        cursor.execute("SELECT worker_id, worker_name FROM workers")
        workers = cursor.fetchall()

        if workers:

            worker_dict = {
                f"{worker[0]} - {worker[1]}": worker[0]
                for worker in workers
            }

            selected_worker = st.selectbox(
                "Select Worker",
                list(worker_dict.keys()),
                key="delete_worker"
            )

            if st.button("Delete Worker"):

                cursor.execute(
                    "DELETE FROM workers WHERE worker_id=%s",
                    (worker_dict[selected_worker],)
                )

                conn.commit()

                st.success("✅ Worker deleted successfully!")
                st.rerun()

        else:
            st.info("No workers available.")
# ======================================================
# VEHICLES
# ======================================================
elif menu == "Vehicles":

    if not (is_admin or is_worker):
        st.error("❌ Access Denied! You do not have permission to view this section.")
        st.stop()
    st.header("🚛 Vehicles Management")

    # Add Vehicle
    with st.expander("➕ Add New Vehicle"):

        vehicle_number = st.text_input("Vehicle Number")
        vehicle_type = st.selectbox("Vehicle Type", ["Mini Truck", "Truck", "Auto", "Van"])
        driver_name = st.text_input("Driver Name")
        capacity = st.number_input("Capacity (kg)", min_value=0)

        if st.button("Add Vehicle"):
            cursor.execute("""
                INSERT INTO vehicles
                (vehicle_number, vehicle_type, driver_name, capacity)
                VALUES (%s, %s, %s, %s)
            """, (
                vehicle_number,
                vehicle_type,
                driver_name,
                capacity
            ))

            conn.commit()
            st.success("✅ Vehicle added successfully!")
            st.rerun()

    st.divider()

    # Show Vehicles
    cursor.execute("SELECT * FROM vehicles")
    rows = cursor.fetchall()

    columns = [
        "Vehicle ID",
        "Vehicle Number",
        "Vehicle Type",
        "Driver Name",
        "Capacity"
    ]

    df = pd.DataFrame(rows, columns=columns)
    st.dataframe(df, use_container_width=True)
    pdf_file = create_pdf(df, "Vehicle Details")

    st.download_button(
        "📄 Download Vehicle PDF",
        data=pdf_file,
        file_name="vehicle_details.pdf",
        mime="application/pdf"
    )
    st.divider()

    # Delete Vehicle
    st.subheader("🗑 Delete Vehicle")

    cursor.execute("SELECT vehicle_id FROM vehicles")
    ids = [row[0] for row in cursor.fetchall()]

    if ids:
        selected_vehicle = st.selectbox("Select Vehicle ID", ids)

        if st.button("Delete Vehicle"):
            cursor.execute(
                "DELETE FROM vehicles WHERE vehicle_id=%s",
                (selected_vehicle,)
            )
            conn.commit()
            st.success("✅ Vehicle deleted successfully!")
            st.rerun()
    else:
        st.info("No vehicles available.")
# ======================================================
# USERS
# ======================================================
elif menu == "Users":

    if not (is_admin or is_user):
        st.error("❌ Access Denied! You do not have permission to view this section.")
        st.stop()
    st.header("👤 Users Management")
    tab1, tab2, tab3, tab4 = st.tabs([
        "View Users",
        "Add User",
        "Update User",
        "Delete User"
    ])

    # ---------------- View Users ----------------
    with tab1:

        cursor.execute("""
            SELECT user_id, name, email, password, phone, role
            FROM users
        """)
        rows = cursor.fetchall()

        columns = [
            "User ID",
            "Name",
            "Email",
            "Password",
            "Phone",
            "Role"
        ]

        df = pd.DataFrame(rows, columns=columns)
        st.dataframe(df, use_container_width=True)
        pdf_file = create_pdf(df, "User Details")

        st.download_button(
            "📄 Download User PDF",
            data=pdf_file,
            file_name="user_details.pdf",
            mime="application/pdf"
        )
    # ---------------- Add User ----------------
    with tab2:

        name = st.text_input("Name", key="user_name")
        email = st.text_input("Email", key="user_email")
        password = st.text_input("Password", type="password", key="user_password")
        phone = st.text_input("Phone", key="user_phone")
        role = st.selectbox("Role", ["Admin", "Worker", "Uuser"])

        if st.button("Add User"):

            cursor.execute("""
                INSERT INTO users
                (name, email, password, phone, role)
                VALUES (%s, %s, %s, %s, %s)
            """, (
                name,
                email,
                password,
                phone,
                role
            ))

            conn.commit()
            st.success("✅ User added successfully!")
            st.rerun()
    # ---------------- Update User ----------------
    with tab3:

        st.subheader("Update User")

        cursor.execute("SELECT user_id, name FROM users")
        user_list = cursor.fetchall()

        if user_list:

            user_dict = {f"{u[0]} - {u[1]}": u[0] for u in user_list}

            selected = st.selectbox(
                "Select User",
                list(user_dict.keys()),
                key="update_user"
            )

            selected_id = user_dict[selected]

            cursor.execute("""
                SELECT name, email, password, phone, role
                FROM users
                WHERE user_id=%s
            """, (selected_id,))

            record = cursor.fetchone()

            name = st.text_input("Name", value=record[0], key="u_name")
            email = st.text_input("Email", value=record[1], key="u_email")
            password = st.text_input("Password", value=record[2], key="u_password")
            phone = st.text_input("Phone", value=record[3], key="u_phone")

            roles = ["Admin", "Worker", "User"]

            role = st.selectbox(
            "Role",
            roles,
            index=roles.index(record[4]),
            key="u_role"
)

            if st.button("Update User"):

                cursor.execute("""
                    UPDATE users
                    SET name=%s,
                        email=%s,
                        password=%s,
                        phone=%s,
                        role=%s
                    WHERE user_id=%s
                """, (
                    name,
                    email,
                    password,
                    phone,
                    role,
                    selected_id
                ))

                conn.commit()
                st.success("✅ User updated successfully!")
                st.rerun()

        else:
            st.info("No users available.")
    # ---------------- Delete User ----------------
    with tab4:

        cursor.execute("SELECT user_id, name FROM users")
        users = cursor.fetchall()

        if users:

            user_dict = {f"{u[0]} - {u[1]}": u[0] for u in users}

            selected = st.selectbox(
                "Select User",
                list(user_dict.keys())
            )

            if st.button("Delete User"):

                cursor.execute(
                    "DELETE FROM users WHERE user_id=%s",
                    (user_dict[selected],)
                )

                conn.commit()
                st.success("✅ User deleted successfully!")
                st.rerun()

        else:
            st.info("No users available.")