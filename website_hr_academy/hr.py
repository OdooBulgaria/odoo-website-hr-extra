# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2015- Vertel AB (<http://www.vertel.se>).
#
#    This progrupdateam is free software: you can redistribute it and/or modify
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

from openerp import models, fields, api, _
import openerp.tools
import xmlrpclib
from openerp.exceptions import Warning
import os, string
import logging
_logger = logging.getLogger(__name__)


class hr(models.Model):
    _inherit = 'hr.employee'

    website_published = fields.Boolean('Available in the website', copy=False, default=False)
    public_info = fields.Text('Public Info')
    chair_nbr = fields.Selection([('01','Stol nr 1'),('02','Stol nr 2'),('03','Stol nr 3'),
                                  ('04','Stol nr 4'),('05','Stol nr 5'),('06','Stol nr 6'),
                                  ('07','Stol nr 7'),('08','Stol nr 8'),('09','Stol nr 9'),
                                  ('10','Stol nr 10'),('11','Stol nr 11'),('12','Stol nr 12'),
                                  ('13','Stol nr 13'),('14','Stol nr 14'),
                                  ('None','None'),('Emeritus','emeritus')],string='Chair')

from openerp import http
from openerp.http import request

class website_hr(http.Controller):

    @http.route(['/academy/chairs'], type='http', auth="public", website=True)
    def chairs(self, **post):
        return request.website.render("website_hr_academy.chair_view", 
            {'employee_ids': request.env['hr.employee'].search([('chair_nbr','not in',['None','emeritus']),('website_published','=',True)],order='chair_nbr')})

    @http.route(['/academy/member/<model("hr.employee"):employee>'], type='http', auth="public", website=True)
    def chairs(self, employee,**post):
        
        return request.website.render("website_hr_academy.employee_view", {'employee': employee})
        

    @http.route(['academy/emeritus'], type='http', auth="public", website=True)
    def emeritus(self, **post):
        return request.website.render("website_hr_academy.emeritus", 
            {'employee_ids': request.env['hr.employee'].search([('chair_nbr','=','emeritus'),('website_published','=',True)],order='name')})
