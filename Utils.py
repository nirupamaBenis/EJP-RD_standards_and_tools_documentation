import chevron

class Utils:

    def get_standards_body(self, standards):
        html_body = ""
        table_body = ""

        for standard in standards:
            name = standard.TITLE
            fair_info = standard.FAIRNESS_INFO
            table_body = table_body + "<br> <br>\n" + self.get_table_body(name, fair_info)

        with open('templates/standards-page.mustache', 'r') as f:
            html_body = chevron.render(f, {'tableContent': table_body})

        return html_body

    def get_table_body(self, standard_name, fairness_info):

        table_body = None

        is_findable = "&nbsp;"
        if fairness_info.IS_FINDABLE:
            is_findable = "X"

        is_accessible = "&nbsp;"
        if fairness_info.IS_ACCESSIBLE:
            is_accessible = "X"

        is_interoperable = "&nbsp;"
        if fairness_info.IS_INTEROPERABLE:
            is_interoperable = "X"

        is_reusable = "&nbsp;"
        if fairness_info.IS_REUSABLE:
            is_reusable = "X"

        is_for_machines = "&nbsp;"
        if fairness_info.IS_FOR_MACHINES:
            is_for_machines = "X"

        is_for_humans = "&nbsp;"
        if fairness_info.IS_FOR_HUMANS:
            is_for_humans = "X"

        is_for_catalogue = "&nbsp;"
        if fairness_info.IS_FOR_CATALOGUE:
            is_for_catalogue = "X"

        is_for_database = "&nbsp;"
        if fairness_info.IS_FOR_DATABASE:
            is_for_database = "X"

        is_for_data_record = "&nbsp;"
        if fairness_info.IS_FOR_DATA_RECORD:
            is_for_data_record = "X"

        with open('templates/table.mustache', 'r') as f:
            table_body = chevron.render(f, {'isFindable': is_findable, 'isAccessible': is_accessible,
                                               'isInteroperable': is_interoperable, 'isReusable': is_reusable,
                                                'isForHuman': is_for_humans, 'isForMachines': is_for_machines,
                                               'isForCatalog': is_for_catalogue, 'isForDatabases': is_for_database,
                                            'isForRecord': is_for_data_record, 'standardName': standard_name})
        return table_body