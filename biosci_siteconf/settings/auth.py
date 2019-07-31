import ldap
from django_auth_ldap.config import LDAPSearch, LDAPSearchUnion

from .app import *

# UofM Active Directory LDAP

AUTH_LDAP_SERVER_URI = "ldap://ldap.ad.umanitoba.ca"
AUTH_LDAP_BIND_DN = "DN_USERNAME"
AUTH_LDAP_BIND_PASSWORD = "PASSWORD"
AUTH_LDAP_USER_SEARCH = LDAPSearchUnion(
    # allow staff username logins:
    LDAPSearch(
        "dc=ad,dc=umanitoba,dc=ca", ldap.SCOPE_SUBTREE, "(sAMAccountName=%(user)s)"
    ),
    # allow student username logins:
    #     LDAPSearch("dc=ad,dc=umanitoba,dc=ca", ldap.SCOPE_SUBTREE, "(sAMAccountName=%(user)s-INS)"),
    # allow principle logins:
    #     LDAPSearch("dc=ad,dc=umanitoba,dc=ca", ldap.SCOPE_SUBTREE, "(userPrincipalName=%(user)s)"),
)
# AUTH_LDAP_START_TLS = True
AUTH_LDAP_CONNECTION_OPTIONS = {
    ldap.OPT_DEBUG_LEVEL: 0,
    ldap.OPT_REFERRALS: 0,  # Required for AD,
    # source: https://www.djm.org.uk/using-django-auth-ldap-active-directory-ldaps/
    # retrieved 2016-Feb-3
}
AUTH_LDAP_USER_ATTR_MAP = {
    "first_name": "givenName",
    "last_name": "sn",
    "email": "mail",
}
AUTHENTICATION_BACKENDS += ("uofm.auth_backends.ldap.UofMLDAPBackend",)
UOFM_LDAP_CREATE_UNKNOWN_USERS = False

################################################
# Core LDAP Debugging:

# import logging
#
# logger = logging.getLogger('django_auth_ldap')
# logger.addHandler(logging.StreamHandler())
# logger.setLevel(logging.DEBUG)

################################################
