"""
Authentication module for Entangled with the Word.
Provides login, logout, and session handling functionality using streamlit-authenticator.
"""
import os
import yaml
import streamlit as st
import streamlit_authenticator as stauth
from yaml.loader import SafeLoader


CONFIG_PATH = os.path.join(os.path.dirname(__file__), '..', 'config', 'auth_config.yaml')


def load_auth_config():
    """Load authentication configuration from YAML file or Streamlit secrets."""
    # First, try to load from Streamlit secrets (for production deployment)
    try:
        if hasattr(st, 'secrets') and st.secrets:
            secrets_dict = dict(st.secrets)
            if 'auth' in secrets_dict:
                return dict(st.secrets['auth'])
    except Exception:
        pass  # Secrets not available, fall back to file-based config
    
    # Fall back to local config file (for development)
    if os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, encoding='utf-8') as file:
            return yaml.load(file, Loader=SafeLoader)
    
    # Return default config if nothing else is available
    return {
        'credentials': {
            'usernames': {}
        },
        'cookie': {
            'expiry_days': 30,
            'key': 'entangled_auth_key',
            'name': 'entangled_auth_cookie'
        },
        'pre-authorized': {
            'emails': []
        }
    }


def save_auth_config(config):
    """Save authentication configuration to YAML file."""
    with open(CONFIG_PATH, 'w', encoding='utf-8') as file:
        yaml.dump(config, file, default_flow_style=False)


def get_authenticator():
    """Initialize and return the authenticator instance."""
    config = load_auth_config()
    
    authenticator = stauth.Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days']
    )
    
    return authenticator, config


def render_login():
    """Render the login form and handle authentication."""
    authenticator, config = get_authenticator()
    
    try:
        authenticator.login()
    except Exception as e:
        st.error(f"Authentication error: {e}")
        return None, None
    
    if st.session_state.get("authentication_status"):
        return st.session_state.get("name"), st.session_state.get("username")
    elif st.session_state.get("authentication_status") is False:
        st.error("Username/password is incorrect")
        return None, None
    else:
        st.warning("Please enter your username and password")
        return None, None


def render_logout():
    """Render the logout button in the sidebar."""
    authenticator, _ = get_authenticator()
    authenticator.logout('Logout', 'sidebar')


def is_authenticated():
    """Check if the current user is authenticated."""
    return st.session_state.get("authentication_status", False)


def get_current_user():
    """Get the current authenticated user's information."""
    if is_authenticated():
        return {
            'name': st.session_state.get("name"),
            'username': st.session_state.get("username")
        }
    return None


def require_authentication(admin_only=False):
    """
    Decorator-style function to protect pages that require authentication.
    
    Args:
        admin_only: If True, only allow admin users
    
    Returns:
        True if authenticated, False otherwise
    
    Note:
        To add more admin users, modify the admin check below to use a
        roles field in the config or maintain a list of admin usernames.
    """
    if not is_authenticated():
        st.warning("🔒 Please log in to access this page.")
        render_login()
        return False
    
    if admin_only:
        username = st.session_state.get("username")
        # Currently only 'admin' user has admin privileges
        # To extend, add a 'roles' field to user config in auth_config.yaml
        if username != "admin":
            st.error("🚫 This page requires admin privileges.")
            return False
    
    return True
