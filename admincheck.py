from pathlib import Path


def file_exist(name) -> None:
    """
    Create file if it doesn't exist

    :param name: Name of file
    """
    file = Path(name)
    file.touch(exist_ok=True)


def admin_check(ctx) -> bool:
    """
    Check if user has admin priveledges

    :param ctx: The context.

    :return: True if admin, else False.
    """
    file_exist('Admin.txt')
    with open('Admin.txt', 'r') as admin_file:
        for admin in admin_file.readlines():
            if str(ctx.message.author.id) == admin.rstrip("\n"):
                return True
        return False
