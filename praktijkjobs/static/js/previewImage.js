function previewImage(event) {
    var reader = new FileReader();
    reader.onload = function() {
        var output = document.getElementById('profileImg');
        output.src = reader.result;
    };
    reader.readAsDataURL(event.target.files[0]);
}