# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2013 Daniel Reis
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Reassign Project Task',
    'summary': 'Reassign Tasks to other Responsibles and Projects',
    'version': '1.2',
    'category': 'Project Management',
    'description': """
The Responsible (``user_id``) field is made read only, and can instead be
changed through a wizard, accessible only to Project Users.

Regular users (Employee group) will be able to see who is handling the request,
but won't be able to change it.

Project Users can click on the "=> Reassign" link, in front of the current
responsible, to open a dialog where they can select the new responsible and/or
new Project/Service Team it should be assigned to.

Mass reassignments can also be made, through the context menu action on the
Issues list view.
""",
    'author': 'Daniel Reis',
    'website': 'https://github.com/OCA/project-service',
    'depends': [
        'project',
    ],
    'data': [
        'wizard/project_task_reassign_view.xml',
        'project_task_view.xml',
    ],
    'installable': True,
}
