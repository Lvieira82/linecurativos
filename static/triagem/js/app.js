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
