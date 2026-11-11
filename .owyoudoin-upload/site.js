// Autoplay the promo only when the viewer hasn't asked for reduced motion.
if (window.matchMedia && matchMedia("(prefers-reduced-motion: reduce)").matches) {
  document.querySelectorAll("video[autoplay]").forEach(function (v) { v.pause(); v.removeAttribute("autoplay"); v.controls = true; });
}
