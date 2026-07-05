import customtkinter as ctks
# -----------------------------
# Personal Information
# -----------------------------
name = "Krutik Hirudkar"
age = 20
nationality = "Indian"
role1 = "Engineer"
role2 = "AI Systems Architect"
vision = "Building self-healing AI systems using logic and math"
philosophy = "Logical architecture is more important than prompt engineering"
music = "Synthwave"
food = "Pizza"

# -----------------------------
# App Setup
# -----------------------------

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Krutik Hirudkar | Architect of Resilience")
app.geometry("1200x750")
app.configure(fg_color="#F5F5F0")

# -----------------------------
# Grid Layout
# -----------------------------

for i in range(6):
    app.grid_columnconfigure(i, weight=1)

for i in range(4):
    app.grid_rowconfigure(i, weight=1)

# -----------------------------
# Hero Card
# -----------------------------
hero = ctk.CTkFrame(
    app,
    corner_radius=30,
    fg_color="#FFFFFF"
)
hero.grid(row=0, column=0, columnspan=4, rowspan=2,
          padx=15, pady=15, sticky="nsew")

ctk.CTkLabel(
    hero,
    text="Human / Engineer / India 🇮🇳",
    font=("Arial", 14)
).pack(anchor="w", padx=25, pady=(20, 5))

ctk.CTkLabel(
    hero,
    text="Krutik\nHirudkar",
    font=("Arial", 42, "bold"),
    justify="left"
).pack(anchor="w", padx=25)

ctk.CTkLabel(
    hero,
    text="Architecting AI-native resilience for the future.\n"
         "Currently bridging logic, mathematics and AI systems.",
    font=("Arial", 16),
    justify="left"
).pack(anchor="w", padx=25, pady=20)

# -----------------------------
# Age Badge
# -----------------------------
age_card = ctk.CTkFrame(
    app,
    corner_radius=30,
    fg_color="#A78BFA"
)
age_card.grid(row=0, column=4, columnspan=2,
              padx=15, pady=15, sticky="nsew")

ctk.CTkLabel(
    age_card,
    text=str(age),
    font=("Arial", 60, "bold"),
    text_color="white"
).pack(expand=True)

ctk.CTkLabel(
    age_card,
    text="Circles of Growth",
    font=("Arial", 16, "bold"),
    text_color="white"
).pack(pady=(0, 20))

# -----------------------------
# Vision Card
# -----------------------------
vision_card = ctk.CTkFrame(
    app,
    corner_radius=25,
    fg_color="#FFFFFF"
)
vision_card.grid(row=2, column=0, columnspan=3,
                 padx=15, pady=15, sticky="nsew")

ctk.CTkLabel(
    vision_card,
    text="VISION 2026",
    font=("Arial", 18, "bold")
).pack(anchor="w", padx=20, pady=(20, 10))

ctk.CTkLabel(
    vision_card,
    text=vision,
    wraplength=400,
    justify="left",
    font=("Arial", 15)
).pack(anchor="w", padx=20, pady=(0, 20))

# -----------------------------
# Philosophy Card
# -----------------------------
philosophy_card = ctk.CTkFrame(
    app,
    corner_radius=25,
    fg_color="#FFFFFF"
)
philosophy_card.grid(row=2, column=3, columnspan=3,
                     padx=15, pady=15, sticky="nsew")

ctk.CTkLabel(
    philosophy_card,
    text="PHILOSOPHY",
    font=("Arial", 18, "bold")
).pack(anchor="w", padx=20, pady=(20, 10))

ctk.CTkLabel(
    philosophy_card,
    text=f'"{philosophy}"',
    wraplength=400,
    justify="left",
    font=("Arial", 15)
).pack(anchor="w", padx=20, pady=(0, 20))

# -----------------------------
# Flow State Card
# -----------------------------
flow_card = ctk.CTkFrame(
    app,
    corner_radius=25,
    fg_color="#FFFFFF"
)
flow_card.grid(row=3, column=0, columnspan=2,
               padx=15, pady=15, sticky="nsew")

ctk.CTkLabel(
    flow_card,
    text="FLOW STATE",
    font=("Arial", 18, "bold")
).pack(anchor="w", padx=20, pady=(20, 10))

ctk.CTkLabel(
    flow_card,
    text=f"🎵 {music}",
    font=("Arial", 20)
).pack(anchor="w", padx=20, pady=(0, 20))

# -----------------------------
# Food Card
# -----------------------------
food_card = ctk.CTkFrame(
    app,
    corner_radius=25,
    fg_color="#FFF4E8"
)
food_card.grid(row=3, column=2, columnspan=2,
               padx=15, pady=15, sticky="nsew")

ctk.CTkLabel(
    food_card,
    text="🍕",
    font=("Arial", 60)
).pack(pady=(15, 5))

ctk.CTkLabel(
    food_card,
    text=food.upper(),
    font=("Arial", 22, "bold")
).pack(pady=(0, 15))

# -----------------------------
# Roles Card
# -----------------------------
roles_card = ctk.CTkFrame(
    app,
    corner_radius=25,
    fg_color="#FFFFFF"
)
roles_card.grid(row=3, column=4, columnspan=2,
                padx=15, pady=15, sticky="nsew")

ctk.CTkLabel(
    roles_card,
    text="ROLES",
    font=("Arial", 18, "bold")
).pack(anchor="w", padx=20, pady=(20, 10))

ctk.CTkLabel(
    roles_card,
    text=f"• {role1}\n• {role2}",
    justify="left",
    font=("Arial", 16)
).pack(anchor="w", padx=20)

# -----------------------------
# Run App
# -----------------------------
app.mainloop()
