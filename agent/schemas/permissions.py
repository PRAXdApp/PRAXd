from enum import Enum

class Permission(str, Enum):
    INSTANCE_READ = "instance:read"
    INSTANCE_WRITE = "instance:write"
    INSTANCE_LOGS = "instance:logs"
    INSTANCE_KILL = "instance:kill"
    ADMIN_ADD_USER = "admin:add_user"
    ADMIN_EDIT_USER = "admin:edit_user"
    ADMIN_SEND_MAIL = "admin:send_mail"
