import streamlit as st

PARABLES_OF_JESUS = [
    "Parable of the Sower",
    "Parable of the Weeds",
    "Parable of the Mustard Seed",
    "Parable of the Leaven",
    "Parable of the Hidden Treasure",
    "Parable of the Pearl of Great Price",
    "Parable of the Net",
    "Parable of the Lost Sheep",
    "Parable of the Lost Coin",
    "Parable of the Prodigal Son",
    "Parable of the Good Samaritan",
    "Parable of the Unforgiving Servant",
    "Parable of the Workers in the Vineyard",
    "Parable of the Two Sons",
    "Parable of the Wicked Tenants",
    "Parable of the Wedding Banquet",
    "Parable of the Ten Virgins",
    "Parable of the Talents",
    "Parable of the Sheep and the Goats",
    "Parable of the Rich Fool",
    "Parable of the Barren Fig Tree",
    "Parable of the Pharisee and the Tax Collector",
    "Parable of the Shrewd Manager",
    "Parable of the Persistent Widow",
    "Parable of the Friend at Midnight",
    "Parable of the Growing Seed",
    "Parable of the Two Debtors",
    "Parable of the Great Banquet",
    "Parable of the Rich Man and Lazarus",
    "Parable of the Wise and Foolish Builders",
    "Parable of the New Cloth on Old Garment",
    "Parable of the New Wine in Old Wineskins",
    "Parable of the Lamp Under a Basket",
    "Parable of the Tenants",
    "Parable of the Seed Growing Secretly",
    "Parable of the Persistent Friend",
]


def render_parables_list():
    """Display a list of Jesus' parables."""
    st.header("📕 Parables of Jesus")
    for parable in PARABLES_OF_JESUS:
        st.markdown(f"- {parable}")

