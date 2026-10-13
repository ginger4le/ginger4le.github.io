// Shows German or English: ?lang= in the URL first, then the saved choice, else the browser language. The buttons switch and remember it.
(function () {
  var root = document.documentElement;
  var lang = null;
  var asked = /[?&]lang=(de|en)\b/.exec(location.search);
  if (asked) {
    lang = asked[1];
    try { localStorage.setItem("lang", lang); } catch (e) {}
  } else {
    try { lang = localStorage.getItem("lang"); } catch (e) {}
  }
  if (lang !== "de" && lang !== "en") {
    lang = (navigator.language || "de").toLowerCase().indexOf("de") === 0 ? "de" : "en";
  }
  root.setAttribute("data-lang", lang);
  root.setAttribute("lang", lang);
  document.addEventListener("click", function (event) {
    var button = event.target.closest ? event.target.closest("[data-set]") : null;
    if (!button) return;
    var next = button.getAttribute("data-set");
    root.setAttribute("data-lang", next);
    root.setAttribute("lang", next);
    try { localStorage.setItem("lang", next); } catch (e) {}
  });
})();
