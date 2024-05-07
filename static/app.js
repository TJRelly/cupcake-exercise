// load cupcakes from database
$(document).ready(loadCupcakes);

// update cupcake list
$(".add-cupcake-form").submit(addCupcake);

// delete cupcake
$(".cupcake-ul").on("click", ".del-cupcake", delCupcake);

// function to load cupcakes from database
async function loadCupcakes() {
  const res = await axios.get("/api/cupcakes");
  const cupcakes = res.data.cupcakes;

  for (const cupcake of cupcakes) {
    $(".cupcake-ul").append(
      `<div class="list-item d-flex list-unstyled align-center">
    <img width="40" height="40" src="https://img.icons8.com/color/100/cupcake.png" alt="cupcake"/>
    <li class="cupcake-li">${cupcake.flavor}</li><i class="bi bi-trash text-danger px-2 del-cupcake" data-id=${cupcake.id}></i>
    </div>`
    );
  }
}

// function to load cupcakes from database
async function addCupcake(e) {
  e.preventDefault();

  const flavor = $("#flavor").val() || null;
  const size = $("#size").val();
  const rating = $("#rating").val();
  const imageUrl = $("#image-url").val() || null;

  const form_data = {
    flavor: flavor,
    size: size,
    rating: rating,
    image: imageUrl,
  };

  const res = await axios.post("/api/cupcakes", form_data);

  const cupcake = res.data.new_cupcake;

  $(".cupcake-ul").append(
    `<div class="list-item d-flex list-unstyled align-center">
  <img width="40" height="40" src="https://img.icons8.com/color/100/cupcake.png" alt="cupcake"/>
  <li class="cupcake-li">${cupcake.flavor}</li><i class="bi bi-trash text-danger px-2 del-cupcake" data-id=${cupcake.id}></i>
  </div>`
  );

  $(".add-cupcake-form")[0].reset();
}

// function to delete cupcake

async function delCupcake(e) {
  e.preventDefault();
  let $cupcake = $(e.target).closest("div");
  let cupcakeId = $(e.target).attr("data-id");
  const res = await axios.delete(`/api/cupcakes/${cupcakeId}`);
  console.log(res.data.message)
  $cupcake.remove();
}

// Example starter JavaScript for disabling form submissions if there are invalid fields
(function () {
  "use strict";

  // Fetch all the forms we want to apply custom Bootstrap validation styles to
  var forms = document.querySelectorAll(".needs-validation");

  // Loop over them and prevent submission
  Array.prototype.slice.call(forms).forEach(function (form) {
    form.addEventListener(
      "submit",
      function (event) {
        if (!form.checkValidity()) {
          event.preventDefault();
          event.stopPropagation();
        }

        form.classList.add("was-validated");
      },
      false
    );
  });
})();
