def get_allowed_columns(org_id: int) -> list[str]:
    """
    Simulates dynamic column config based on org ID.
    This could be replaced by a DB or file lookup in production.
    """
    # Mocked configuration per organization
    org_column_config = {
        1: ["first_name", "last_name", "contact_info", "department", "position", "location", "status"],
        2: ["first_name", "last_name", "department", "position", "location"],
        3: ["first_name", "last_name", "status"]
    }
    # Default fallback if org_id not found
    return org_column_config.get(org_id, ["first_name", "last_name", "department", "position"])

