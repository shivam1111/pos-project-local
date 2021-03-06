
from openerp.osv import fields, osv, orm
from openerp.tools.translate import _


class res_partner(osv.Model):
    _inherit = 'res.partner'
    _columns = {
                'sequence':fields.char('Customer Id'),
                }
    _sql_constraints = [
        ('uniq_reference', 'unique(sequence)', "The Customer Id must be unique"),
        ]

    def create(self, cr, uid, vals, context=None):
        if context is None:
            context = {}
        vals['sequence'] = self.pool.get('ir.sequence').get(
            cr, uid, 'res.partner')
        return super(res_partner, self).create(cr, uid, vals, context)

    def copy(self, cr, uid, id, default={}, context=None):
        product = self.read(cr, uid, id, ['sequence'], context=context)
        if product['sequence']:
            default.update({
                'sequence': self.pool.get('ir.sequence').get(
                cr, uid, 'res.partner')
            })

        return super(res_partner, self).copy(cr, uid, id, default, context)
