import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo-addons-oca-stock-logistics-reporting",
    description="Meta package for oca-stock-logistics-reporting Odoo addons",
    version=version,
    install_requires=[
        'odoo-addon-delivery_line_sale_line_position>=16.0dev,<16.1dev',
        'odoo-addon-stock_account_valuation_discrepancy_adjust>=16.0dev,<16.1dev',
        'odoo-addon-stock_account_valuation_report>=16.0dev,<16.1dev',
        'odoo-addon-stock_average_daily_sale>=16.0dev,<16.1dev',
        'odoo-addon-stock_card_report>=16.0dev,<16.1dev',
        'odoo-addon-stock_move_value_report>=16.0dev,<16.1dev',
        'odoo-addon-stock_picking_batch_report>=16.0dev,<16.1dev',
        'odoo-addon-stock_picking_operations_multilang>=16.0dev,<16.1dev',
        'odoo-addon-stock_picking_report_custom_description>=16.0dev,<16.1dev',
        'odoo-addon-stock_picking_report_delivery_driver>=16.0dev,<16.1dev',
        'odoo-addon-stock_picking_report_external_note>=16.0dev,<16.1dev',
        'odoo-addon-stock_picking_report_header_repeater>=16.0dev,<16.1dev',
        'odoo-addon-stock_picking_report_incoming_delivery_address>=16.0dev,<16.1dev',
        'odoo-addon-stock_picking_report_internal_delivery_address>=16.0dev,<16.1dev',
        'odoo-addon-stock_picking_report_product_sticker>=16.0dev,<16.1dev',
        'odoo-addon-stock_picking_report_qty_undelivered>=16.0dev,<16.1dev',
        'odoo-addon-stock_picking_report_salesperson>=16.0dev,<16.1dev',
        'odoo-addon-stock_picking_report_summary>=16.0dev,<16.1dev',
        'odoo-addon-stock_picking_report_valued>=16.0dev,<16.1dev',
        'odoo-addon-stock_quantity_history_location>=16.0dev,<16.1dev',
        'odoo-addon-stock_report_quantity_by_location>=16.0dev,<16.1dev',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 16.0',
    ]
)
