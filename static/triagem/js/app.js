const dialog = document.querySelector("#sourceDialog");
const title = document.querySelector("#sourceTitle");
const text = document.querySelector("#sourceText");
const link = document.querySelector("#sourceLink");
const close = document.querySelector(".close");

document.querySelectorAll(".source-button").forEach((button) => {
  button.addEventListener("click", () => {
    title.textContent = button.dataset.sourceTitle;
    text.textContent = button.dataset.sourceText;
    link.href = button.dataset.sourceUrl;
    dialog.showModal();
  });
});

close?.addEventListener("click", () => dialog.close());
dialog?.addEventListener("click", (event) => {
  if (event.target === dialog) dialog.close();
});

const locationForm = document.querySelector("#locationForm");
const locationValue = document.querySelector("#locationValue");
const selectedLocation = document.querySelector("#selectedLocation");
const continueLocation = document.querySelector("#continueLocation");

const labels = {
  rosto: "Rosto / face",
  torax: "Tórax",
  abdome: "Abdome",
  costas: "Costas",
  membro_superior: "Membro superior",
  mao: "Mão",
  membro_inferior: "Membro inferior",
  pe: "Pé",
  regiao_genital: "Região genital",
  gluteo: "Glúteo",
  articulacao: "Sobre ou ao redor de uma articulação",
  outra: "Outro local"
};

function selectLocation(value) {
  if (!locationValue || !selectedLocation || !continueLocation) return;

  locationValue.value = value;
  selectedLocation.textContent = "Região selecionada: " + (labels[value] || value);
  continueLocation.disabled = false;

  document.querySelectorAll(".body-part, .location-option").forEach((element) => {
    element.classList.toggle("selected", element.dataset.value === value || element.dataset.location === value);
  });
}

document.querySelectorAll(".body-part").forEach((part) => {
  part.addEventListener("click", () => selectLocation(part.dataset.value));
});

document.querySelectorAll(".location-option").forEach((option) => {
  option.addEventListener("click", () => selectLocation(option.dataset.location));
});

locationForm?.addEventListener("submit", (event) => {
  if (!locationValue?.value) event.preventDefault();
});
