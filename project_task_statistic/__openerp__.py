# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2014 Hugo Santos, Daniel Reis
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
    'name': 'Project Task Statistic',
    'summary': 'Add a new tab Statistics to the task form',
    'version': '1.0',
    'category': 'Project Management',
    'description': """\
Adds a new tab Staticits to the task form, similar to the Issue statistics.
It could be used for information alone, or to use with Automated Actions or
    'author': 'Hugo Santos',
    'depends': [
        'project',
        ],
    'data': [
        'project_task_statistic.xml',
        ],
    'installable': True,
}