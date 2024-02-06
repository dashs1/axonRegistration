import logging

from ldap3 import Server
from ldap3 import Connection
from ldap3 import AUTO_BIND_NO_TLS
from ldap3 import SUBTREE
from ldap3 import ALL_ATTRIBUTES
from ldap3.core.exceptions import LDAPBindError

from django.conf import settings
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User

logger = logging.getLogger(__name__)

class LdapCtlBackend:
    
    
    def authenticate(self, request, username=None, password=None):
        
        c = Connection(Server('ldap.qintra.com', port=1636, use_ssl=True),
                            auto_bind=AUTO_BIND_NO_TLS,
                            read_only=True,
                            check_names=True,
                            user='uid=pinnacle,ou=people,dc=mnet,dc=qintra,dc=com', password='C13xvn2DmdXrVeGhMJrSe27d')
        
        if c is not None:
            
            c.search(search_base='dc=mnet,dc=qintra,dc=com',
                 search_filter='(&(samAccountName=' + username + '))',
                 search_scope=SUBTREE,
                 attributes=ALL_ATTRIBUTES,
                 get_operational_attributes=True)
            
            if len(c.response) == 1:
                
                userdn = c.response[0]['dn']
            
                try:
                    user_c = Connection(Server('ldap.qintra.com', port=1636, use_ssl=True),
                                        auto_bind=AUTO_BIND_NO_TLS,
                                        read_only=True,
                                        check_names=True,
                                        user=userdn, password=password)
                except LDAPBindError:
                    return None

                if user_c is not None:
                    try:
                        user = User.objects.get(username=username)
                    except User.DoesNotExist:
                        # Create a new user. There's no need to set a password
                        # because only the password from settings.py is checked.
                        user = User(username=username)
                        user.is_staff = False
                        user.is_superuser = False
                        user.save()
                    return user
                return None
            
            return None
        
        return None
     
     
    def get_user(self, user_id):
        
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None            
        
    
        
        
        

    
    
    