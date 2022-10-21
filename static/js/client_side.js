$(document).ready(function () {

    $("#prediksi_submit").click(function (e) {
        e.preventDefault();

        // Get File Gambar yg telah diupload pengguna
        var file_data = $('#input_gambar').prop('files')[0];
        var pics_data = new FormData();
        pics_data.append('my_image', file_data);

        // Panggil API dengan timeout 1 detik (1000 ms)
        setTimeout(function () {
            try {
                $.ajax({
                    url: "/api/deteksi",
                    type: "POST",
                    data: pics_data,
                    processData: false,
                    contentType: false,
                    success: function (res) {
                        // Ambil hasil prediksi dan path gambar yang diprediksi dari API
                        res_data_prediksi = res['prediksi']
                        res_gambar_prediksi = res['gambar_prediksi']

                        // Tampilkan hasil prediksi ke halaman web
                        generate_prediksi(res_data_prediksi, res_gambar_prediksi);
                    }
                });
            }
            catch (e) {
                // Jika gagal memanggil API, tampilkan error di console
                console.log("Gagal !");
                console.log(e);
            }
        }, 1000)
    })

    function generate_prediksi(data_prediksi, image_prediksi) {
        var str = "";

        if (image_prediksi == "(none)") {
            str += "<h3>Hasil Prediksi </h3>";
            str += "<br>";
            str += "<h4>Silahkan masukkan file gambar (.jpg)</h4>";
        }
        else {
            str += "<h3>Hasil Prediksi </h3>";
            str += "<br>";
            str += "<img src='" + image_prediksi + "' width=\"200\"></img>"
            str += "<h3>" + data_prediksi + "</h3>";
        }
        $("#hasil_prediksi").html(str);
    }


})