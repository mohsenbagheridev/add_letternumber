odoo.define('documents.DocumentsInspector.inherit', function (require) {

"use strict";

  var Docs = require('documents.DocumentsInspector');
  var DocumentsInspector = Docs.include({

    _renderFields: function () {
        const options = { mode: 'edit' };
        const proms = [];
        if (this.records.length > 0) {
            proms.push(this._renderField('letter_number', {
                icon: 'fa fa-envelope o_documents_folder_color',
                readonly: true
            }));
        }
        if (this.records.length === 1) {
            proms.push(this._renderField('name', options));
            if (this.records[0].data.type === 'url') {
                proms.push(this._renderField('url', options));
            }
            proms.push(this._renderField('partner_id', options));
        }
        if (this.records.length > 0) {
            proms.push(this._renderField('owner_id', options));

            proms.push(this._renderField('letter_date', options));
            proms.push(this._renderField('ln', options));
            proms.push(this._renderField('title', options));
            proms.push(this._renderField('folder_id', {
                icon: 'fa fa-folder o_documents_folder_color',
                mode: 'edit'
            }));
        }
        return Promise.all(proms);
    },
  });

});