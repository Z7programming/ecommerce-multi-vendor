img = document.getElementById("id_image");
img.addEventListener("change", () => {
  document.querySelectorAll(".new_img_inp").forEach((item) => {
    item.remove();
  });
  for (i = 0; i < img.files.length; i++) {
    image = `
    <span class="new_img_inp" style=" width: 100px;  height: 100px;  padding: 2px;
                              border:1px solid blue;  margin: 10px;
                              border-radius: 10px; overflow: hidden " >
      <img  src="${URL.createObjectURL(img.files[i])}"
            style="width: 100px; height: 100px; border-radius: 10px" />
    </span> `;
    document.getElementById("showimage").innerHTML += image;
  }
});
