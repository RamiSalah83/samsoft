$(document).ready(function() {
  $("select.exist-option-only").select2();

  $("select.dynamic-option-create-single").select2({
    tags: true,
  });

  $("select.dynamic-option-create-multiple").select2({
    tags: true,
    multiple: true,
  });

  $("select.dynamic-option-create-createTag").select2({
    tags: true,
    multiple: true,
    createTag: (params) => {
      return {
        id: params.term.length,
        text: params.term,
      };
    }
  });

  $("select.dynamic-option-create-separate-by-comma").select2({
    tags: true,
    tokenSeparators: [','],
  });
})