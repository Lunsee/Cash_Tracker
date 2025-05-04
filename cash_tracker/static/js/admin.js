$('#id_category').change(function() {
    var category_id = $(this).val();
    $('#id_subcategory').select2('destroy').select2({
        ajax: {
            url: '/subcategory-autocomplete/',
            data: function (params) {
                return {
                    q: params.term,
                    category: category_id  // ID категории
                };
            }
        }
    });
});
