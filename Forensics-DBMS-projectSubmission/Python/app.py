import streamlit as st
from add import add
from read import read
from queries import predef_queries
from queries import query_cmd
from update import update
from delete import delete
from read import add_bg_from_url
from read import sidebar_bg

def main():
    st.title("Forensics Database")  
    add_bg_from_url()
    sidebar_bg()
    menu = ["Add Records", "View Tables", "Update Record", "Delete Records", "Run Predefined Queries", "CMD"]
    choice = st.sidebar.selectbox("Menu", menu)
    if choice == "Add Records":
        add()
    elif choice == "View Tables":
        read()
    elif choice == "Update Record":
        update()
    elif choice == "Delete Records":
        delete()
    elif choice=="Run Predefined Queries":
        predef_queries()
    elif choice=="CMD":
        query_cmd()

if __name__ == '__main__':
 main()