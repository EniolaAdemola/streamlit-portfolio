import streamlit as st


# PAGE SETUP
about_page = st.Page(
    "./views/about_me.py",
    title = "About Me",
    icon = "👩‍💻",
    default = True
)

chatbot_page = st.Page(
    "./views/chatbot.py",
    title = "Chatbot",
    icon = "💬"
)

projects_page = st.Page(
    "./views/projects.py",
    title = "Projects",
    icon = "🚀"
)


# Create our navigation bar
page = st.navigation(
    {
        "Info": [about_page],
        "Projects" : [projects_page, chatbot_page],
    }
)

# Add logos and links to the sidebar
st.logo("./assets/daveworld_logo.png")
st.sidebar.markdown("Made with love by [Daveworld](https://github.com/EniolaAdemola)")

# Run the navigation bar
page.run()