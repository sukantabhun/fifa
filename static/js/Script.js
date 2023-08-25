
function jumpToSection(sectionId) {
    document.getElementById(sectionId).scrollIntoView({ behavior: 'smooth' });
}

document.addEventListener("DOMContentLoaded", function () {
    const animateText = (element) => {
        const text = element.textContent;
        element.textContent = "";

        for (let i = 0; i < text.length; i++) {
            setTimeout(() => {
                element.textContent += text[i];
            }, i * 50);
        }
    };

    const elementsToAnimate = document.querySelectorAll(".fade-in");
    elementsToAnimate.forEach(animateText);
});
document.addEventListener("DOMContentLoaded", function () {
    const animateText = (element) => {
        const text = element.textContent;
        element.textContent = "";

        for (let i = 0; i < text.length; i++) {
            setTimeout(() => {
                element.textContent += text[i];
            }, i * 25); 
        }
    };

    const textToAnimate = document.getElementById("animated-text");
    animateText(textToAnimate);
});
