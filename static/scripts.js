var data = null;
var kur_isim = null;

function onchange_combobox(){ // satir boyama isleminin yapildigi bolum
    isim_select = document.getElementById('select_isim');
    kur_isim = isim_select.value;
    $.ajax({
        url: 'get_data' ,
        success: function(response){
        create_table(data, kur_isim)
        }
    });
}

function get_default_table(){ //sayfa yuklenirken yuklenen default tablo
    $.ajax({
        url: 'get_data',
        success: function(response){
            data = Object.entries(JSON.parse(response)).map(([key, value]) => ({key, value}));
            create_table(data)
        }
    });
}

function change_sort_type(){ // Comboboxtan secilen degere gore siralama
    sort_select = document.getElementById('sort_type');
    sort_type = sort_select.value;
    data.sort(function(a, b){
        return a.value[sort_type] - b.value[sort_type];
    });
    create_table(data, kur_isim)
}

function create_table( table_data, kur_isim="" ){ // tablo olusturma ve innerHtml
    var txt = "";
    var count = 1;
    table_headers = Object.keys(table_data[0].value)
    txt += "<table id='kur-tablosu' class='table table-striped'>"
    txt += "<thead class='thead-dark'><tr style='font-weight:bold'>" + "<td>#</td>"
    table_headers.forEach(function(head) {
        txt += "<td>" + head + "</td>"
    })
    txt += "</tr></thead>";
    txt += "<tbody>";
    Object.values(table_data).forEach(function(key)  {
        if (key.value["Kod"]==kur_isim){
            txt += "<tr style='background-color:#90EE9080'>" + "<td>" + count + "</td>";
            Object.values(key.value).forEach(function(value){
                if ( value == null){
                    txt += "<td>---</td>"
                }else {
                    txt += "<td>" + value + "</td>"
                }
            })
            txt += "</tr>";
        }else{
            txt += "<tr>" + "<td>" + count + "</td>" ;
            Object.values(key.value).forEach(function(value){
                if ( value == null){
                    txt += "<td>---</td>"
                }else {
                    txt += "<td>" + value + "</td>"
                }
            })
            txt += "</tr>";
        }
        count += 1
    });
    txt += "</tbody>"
    txt += "</table>"
    document.getElementById("kur_table").innerHTML = txt;
}