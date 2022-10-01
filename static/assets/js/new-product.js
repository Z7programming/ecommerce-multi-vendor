img = document.getElementById("id_image");
img.addEventListener("change", () => {
  document.querySelectorAll(".new_img_inp").forEach((item) => {
    item.remove();
  });
  for (i = 0; i < img.files.length; i++) {
    image = `<img class="img_show" 
                  src="${URL.createObjectURL(img.files[i])}"
               />`;
    document.getElementById("showimage").innerHTML += image;
  }
});
