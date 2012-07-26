class ListManager(object):
    """
    Vermonster list manager
    """
    def __init__(self):
        """
        Initialize list manager
        """

    def all(self):
        """
        Get all lists

        Returns
        - A list of cheddar list objects
        """
        pass

    def get(self, id, include_active_tasks=False):
        """
        Get single list

        Parameters

        id: id of the list
        include_active_tasks: True if you would like the returned list to contain active include_active_tasks
                                False if you do not want the returned list to contain any tasks

        Returns
        - A single cheddar list object
        - The list object may contain active tasks if so specified by include_active_tasks parameter
        """
        pass

    def create(self, title):
        """
        Create a new list
        - If the user is not a premium Cheddar user, they can only create a maximum of two lists
        if you try and exceed that calling this method, you will get back an error

        Parameters

        title: title for the new list, eg: 'Foobar #Foobar'

        Returns
        - The list object we just created
        """
        pass

    def reorder(self, list_ids):
        """
        Reorder lists

        Parameters

        list_ids: a list of ids for the users' lists, eg. [34, 56, 78, 89]

        Returns
        - Nothing
        """
        pass
