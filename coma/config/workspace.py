from frappe import _


def get_data():
    """Return workspace configuration for the COMA module."""

    return [
        {
            "module_name": "COMA",
            "label": _("COMA"),
            "icon": "octicon octicon-briefcase",
            "color": "grey",
            "type": "workspace",
            "link": "Workspace/COMA",
        }
    ]
