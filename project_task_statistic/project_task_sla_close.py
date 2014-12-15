from openerp import models, fields, api
from datetime import datetime, timedelta


class project_task_close_action(models.Model):
    _inherit = "project.task"

    date_closed = fields.Datetime(
        'Date Closed', compute='_close_task_date', store=True)

    @api.one
    @api.depends('stage_id')
    def _close_task_date(self):
        if self.work_ids and self.stage_id.state in ('cancelled','done'):
            #The list is by default already order by desc
            last_line = self.work_ids[0]

            #Get the hours and date
            rec_hours = last_line.hours
            rec_max_date = last_line.date

            #Adding to the max workline date the duration time
            sla_date_close = datetime.strptime(
                rec_max_date, '%Y-%m-%d %H:%M:%S')
            sla_date_close += timedelta(hours=rec_hours)

            #Now finaly update date_closed field
            self.date_closed = sla_date_close
        else:
            self.date_closed = None