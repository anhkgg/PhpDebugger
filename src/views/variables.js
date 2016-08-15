/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

function get_variables_list() {
    $('#variables_treegrid').treegrid('loadData', []);
    RegisteVariablesContextMenu();
    RegistVariablesDbClick();
    
    $.post("variables", {"action":"", "param":""},
        function(data){
            if (data.ret == 1) {
                $('#variables_treegrid').treegrid('loadData', data.data);
            }
    }, "json");
}

function RegistVariablesDbClick() {
    $('#variables_treegrid').treegrid({onDblClickCell:function(field,row){
            if (row){
                if (field == "value" && row.type !="") {
                    show_variable_in_dialog(row.name, row.value);
                }
            }
        }
    });
}

function RegisteVariablesContextMenu() {                 
    $('#variables_treegrid').treegrid({onContextMenu:function(e, row){
            if (row){
                e.preventDefault();
                $(this).treegrid('select', row.id);
                $('#variables_treegrid_contextmenu').menu('show',{
                    left: e.pageX,
                    top: e.pageY
                });                
            }
        }
    });
}

function variables_treegrid_contextmenu_collapse(){
    var node = $('#variables_treegrid').treegrid('getSelected');
    if (node){
        $('#variables_treegrid').treegrid('collapse', node.id);
    }
}

function variables_treegrid_contextmenu_expand(){
    var node = $('#variables_treegrid').treegrid('getSelected');
    if (node){
        $('#variables_treegrid').treegrid('expand', node.id);
    }
}

function show_variable_in_dialog_from_menucontent() {
    var node = $('#variables_treegrid').treegrid('getSelected');
    if (node){
        show_variable_in_dialog(node.name, node.value);
    }
}

function show_variable_in_dialog(name, data) {
    $('#variables_show_json-renderer').empty();
    var options = {
        collapsed: $('#collapsed').is(':checked'),
        withQuotes: $('#with-quotes').is(':checked')
    };
    eval("var theJsonValue = "+ data); 
    $('#variables_show_json-renderer').jsonViewer(theJsonValue, options);
    $('#variables_show').dialog('open').dialog('center').dialog('setTitle',name);
}
