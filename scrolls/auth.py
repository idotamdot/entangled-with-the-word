"""
Authentication module for Entangled with the Word application.
Provides user login, logout, and role-based access control.
"""

import os
import yaml
import streamlit as st
import streamlit_authenticator as stauth
from typing import Optional, Tuple

# Path to the authentication configuration file
AUTH_CONFIG_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 
                                 "config", "auth_config.yaml")


def load_auth_config() -> dict:
    """
    Load authentication configuration from YAML file.
    
    Returns:
        dict: Authentication configuration dictionary
    """
    if not os.path.exists(AUTH_CONFIG_PATH):
        st.error(f"Authentication config not found at {AUTH_CONFIG_PATH}")
        st.info("Please copy config/auth_config.yaml.example to config/auth_config.yaml and update credentials.")
        return {}
    
    with open(AUTH_CONFIG_PATH, 'r') as file:
        config = yaml.safe_load(file)
    return config


def save_auth_config(config: dict) -> None:
    """
    Save authentication configuration to YAML file.
    
    Args:
        config: Authentication configuration dictionary
    """
    with open(AUTH_CONFIG_PATH, 'w') as file:
        yaml.dump(config, file, default_flow_style=False)


def get_authenticator() -> Optional[stauth.Authenticate]:
    """
    Create and return a Streamlit Authenticator instance.
    
    Returns:
        stauth.Authenticate: Authenticator instance or None if config not found
    """
    config = load_auth_config()
    if not config:
        return None
    
    authenticator = stauth.Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days']
    )
    return authenticator


def get_user_role(username: str) -> str:
    """
    Get the role of a user.
    
    Args:
        username: The username to look up
        
    Returns:
        str: User role ('admin', 'user', etc.) or 'user' if not found
    """
    config = load_auth_config()
    if not config or 'credentials' not in config:
        return 'user'
    
    users = config['credentials'].get('usernames', {})
    user_info = users.get(username, {})
    return user_info.get('role', 'user')


def is_admin(username: str) -> bool:
    """
    Check if a user has admin privileges.
    
    Args:
        username: The username to check
        
    Returns:
        bool: True if user is admin, False otherwise
    """
    return get_user_role(username) == 'admin'


def render_login_form() -> Tuple[Optional[str], bool, Optional[str]]:
    """
    Render the login form in the sidebar.
    
    Returns:
        Tuple containing (name, authentication_status, username)
    """
    authenticator = get_authenticator()
    if authenticator is None:
        return None, False, None
    
    try:
        result = authenticator.login(location='sidebar')
        if result is not None:
            name, authentication_status, username = result
        else:
            name = st.session_state.get("name")
            authentication_status = st.session_state.get("authentication_status")
            username = st.session_state.get("username")
        
        # Store authenticator in session state for logout functionality
        st.session_state['authenticator'] = authenticator
        
        return name, authentication_status, username
    except Exception as e:
        st.sidebar.error(f"Authentication error: {e}")
        return None, False, None


def render_logout_button() -> None:
    """
    Render the logout button in the sidebar.
    """
    authenticator = st.session_state.get('authenticator')
    if authenticator:
        authenticator.logout(button_name='Logout', location='sidebar')


def render_user_info() -> None:
    """
    Display current user information in the sidebar.
    """
    if st.session_state.get("authentication_status"):
        name = st.session_state.get("name", "User")
        username = st.session_state.get("username", "")
        role = get_user_role(username)
        
        st.sidebar.markdown("---")
        st.sidebar.markdown(f"👤 **{name}**")
        st.sidebar.markdown(f"🔑 Role: `{role}`")


def require_auth(page_func):
    """
    Decorator to require authentication for a page.
    
    Args:
        page_func: The page function to wrap
        
    Returns:
        Wrapped function that checks authentication before executing
    """
    def wrapper(*args, **kwargs):
        if not st.session_state.get("authentication_status"):
            st.warning("⚠️ Please log in to access this page.")
            st.info("Use the login form in the sidebar to authenticate.")
            return
        return page_func(*args, **kwargs)
    return wrapper


def require_admin(page_func):
    """
    Decorator to require admin privileges for a page.
    
    Args:
        page_func: The page function to wrap
        
    Returns:
        Wrapped function that checks admin status before executing
    """
    def wrapper(*args, **kwargs):
        if not st.session_state.get("authentication_status"):
            st.warning("⚠️ Please log in to access this page.")
            st.info("Use the login form in the sidebar to authenticate.")
            return
        
        username = st.session_state.get("username", "")
        if not is_admin(username):
            st.error("🚫 Access Denied: Admin privileges required.")
            return
        
        return page_func(*args, **kwargs)
    return wrapper
